"""Claude API 호출 + 위키 검색 결과 인용 agent. Phase 1 단순 버전."""

from __future__ import annotations

from pathlib import Path

from anthropic import Anthropic

from .search import keyword_search
from .wiki_loader import load_page

SYSTEM_PROMPT = """\
당신은 ginza의 개인 게임 개발 지식 위키를 기반으로 답변하는 어시스턴트입니다.

원칙:
- 답변은 *반드시* 제공된 위키 발췌만 근거로. 위키에 없는 내용은 "위키에 관련 페이지 없음"이라고 명시
- 한국어로 답변. 영문 슬러그·고유명사는 그대로 사용
- 답변 마지막에 인용한 페이지를 `[[slug]]` 형식 wikilink로 나열
- 게임 도메인 용어는 위키 내 정의를 우선
- 답변은 간결하게 (3~6 문장 권장, 길어야 할 때만 길게)
"""

USER_PROMPT_TEMPLATE = """\
질문: {query}

다음은 위키에서 검색된 관련 페이지 발췌입니다 (관련도 순):

{context}

위 발췌만 근거로 답변해 주세요.
"""


def _build_context(hits: list[dict], vault_path: Path) -> str:
    """검색 hit를 컨텍스트 텍스트로 직렬화 (본문 풀 로딩)."""
    if not hits:
        return "(검색된 페이지 없음)"

    blocks = []
    for hit in hits:
        page = load_page(hit["path"])
        body = page["body"].strip()
        if len(body) > 1500:
            body = body[:1500] + "\n...(이하 생략)"
        blocks.append(
            f"### [[{hit['slug']}]] — {hit['title']} (type: {hit['type']})\n\n{body}"
        )
    return "\n\n---\n\n".join(blocks)


def _build_context_rag(pages: list[dict]) -> str:
    """RAG 페이지 결과(slug별 청크 묶음)를 컨텍스트 텍스트로 직렬화."""
    if not pages:
        return "(검색된 페이지 없음)"
    blocks = []
    for p in pages:
        body = "\n\n".join(p["chunks"])
        if len(body) > 1500:
            body = body[:1500] + "\n...(이하 생략)"
        blocks.append(
            f"### [[{p['slug']}]] — {p['title']} (type: {p['type']}, 유사도 {p['score']})\n\n{body}"
        )
    return "\n\n---\n\n".join(blocks)


def ask(
    query: str,
    vault_path: Path,
    api_key: str,
    model: str = "claude-sonnet-4-6",
    search_limit: int = 5,
    max_tokens: int = 1024,
    use_rag: bool = True,
) -> dict:
    """질문 받아 위키 검색 → Claude 답변 생성.

    use_rag=True (기본): BGE-M3 의미 검색. 컬렉션이 비었으면 키워드로 fallback.
    use_rag=False: 키워드 검색 (Phase 1 방식, 회귀 비교용).

    Returns:
        {
            "answer": str,
            "sources": list[dict],  # slug·title·type·score (+ snippet 또는 chunks)
            "model": str,
            "retrieval": "rag" | "keyword",
        }
    """
    retrieval = "keyword"
    if use_rag:
        from . import vectorstore
        if vectorstore.collection_count() > 0:
            from .rag_search import rag_search_pages
            pages = rag_search_pages(query, max_pages=search_limit)
            sources = [
                {"slug": p["slug"], "title": p["title"], "type": p["type"],
                 "score": p["score"], "snippet": (p["chunks"][0][:160] if p["chunks"] else "")}
                for p in pages
            ]
            context = _build_context_rag(pages)
            retrieval = "rag"
        else:
            hits = keyword_search(query, vault_path, limit=search_limit)
            sources = hits
            context = _build_context(hits, vault_path)
    else:
        hits = keyword_search(query, vault_path, limit=search_limit)
        sources = hits
        context = _build_context(hits, vault_path)

    client = Anthropic(api_key=api_key)
    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": USER_PROMPT_TEMPLATE.format(query=query, context=context),
            }
        ],
    )

    answer_text = "\n".join(
        block.text for block in response.content if block.type == "text"
    )

    return {
        "answer": answer_text,
        "sources": sources,
        "model": model,
        "retrieval": retrieval,
    }

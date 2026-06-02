"""Claude API 호출 + 위키 검색 결과 인용 agent. Phase 1 단순 버전."""

from __future__ import annotations

from pathlib import Path

from anthropic import Anthropic

from .search import keyword_search
from .wiki_loader import load_page

SYSTEM_PROMPT = """\
당신은 ginza의 개인 게임 개발 지식 위키를 기반으로 답변하는 어시스턴트입니다.

원칙:
- 답변은 *반드시* 제공된 위키 발췌 또는 graph 도구 결과만 근거로. 근거 없으면 "위키에 관련 페이지 없음"이라고 명시
- 한국어로 답변. 영문 슬러그·고유명사는 그대로 사용
- 답변 마지막에 인용·언급한 페이지를 `[[slug]]` 형식 wikilink로 *빠짐없이* 나열 (본문 표·목록에 등장한 entity도 모두 포함)
- 게임 도메인 용어는 위키 내 정의를 우선
- 답변은 간결하게 (3~6 문장 권장, 길어야 할 때만 길게)

graph 도구 사용 지침:
- "X의 모회사가 소유한 다른 스튜디오", "같은 모회사 스튜디오", "퍼블리셔가 퍼블리싱한 게임", "장르가 같은 게임",
  "A와 B 사이 관계" 등 *관계를 따라가는 질문*은 RAG 발췌만으로 불완전하니 graph 도구를 호출해 정확히 열거할 것
- 이름→slug는 resolve_entity로 먼저 확정. 모회사 자회사 열거는 get_children, 형제는 get_siblings,
  퍼블리싱 게임은 find_by_relation(relation='publishedBy', direction='in') 사용
- 도구 결과와 RAG 발췌를 종합해 답변
- **platform·genre 관계는 데이터가 희소함**. 한 관계 조회가 비거나 적으면 게임별로 반복 조회하지 말고,
  확보된 관계(developedBy·publishedBy·parentOf)로 답하되 "플랫폼 단위 정보는 graph에 부족"이라고 명시
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


def _run_tool_loop(client, model, max_tokens, system, user_content, vault_path, max_iters=8):
    """graph 도구를 호출할 수 있는 tool-use 루프. (answer_text, tool_calls) 반환."""
    from . import graph as G
    from . import graph_tools

    g = G.build_graph(str(vault_path))
    messages = [{"role": "user", "content": user_content}]
    tool_calls = []
    for _ in range(max_iters):
        resp = client.messages.create(
            model=model, max_tokens=max_tokens, system=system,
            tools=graph_tools.TOOLS, messages=messages,
        )
        if resp.stop_reason != "tool_use":
            text = "\n".join(b.text for b in resp.content if b.type == "text")
            return text, tool_calls
        # tool_use 블록 실행
        messages.append({"role": "assistant", "content": resp.content})
        results = []
        for block in resp.content:
            if block.type == "tool_use":
                out = graph_tools.execute(g, block.name, block.input)
                tool_calls.append({"tool": block.name, "input": block.input, "result": out})
                results.append({"type": "tool_result", "tool_use_id": block.id, "content": out})
        messages.append({"role": "user", "content": results})
    # 루프 한도 초과 — 마지막 텍스트라도 반환
    text = "\n".join(b.text for b in resp.content if b.type == "text")
    return text, tool_calls


def ask(
    query: str,
    vault_path: Path,
    api_key: str,
    model: str = "claude-sonnet-4-6",
    search_limit: int = 5,
    max_tokens: int = 1024,
    use_rag: bool = True,
    use_graph: bool = True,
) -> dict:
    """질문 받아 위키 검색(+graph 도구) → Claude 답변 생성.

    use_rag=True (기본): BGE-M3 의미 검색. 컬렉션이 비었으면 키워드로 fallback.
    use_rag=False: 키워드 검색 (Phase 1 방식, 회귀 비교용).
    use_graph=True (기본): 관계 질문 시 Claude가 graph 도구 호출 가능.

    Returns:
        {
            "answer": str,
            "sources": list[dict],
            "model": str,
            "retrieval": "rag" | "keyword",
            "tool_calls": list[dict],  # 호출된 graph 도구 내역
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
    user_content = USER_PROMPT_TEMPLATE.format(query=query, context=context)
    tool_calls = []

    if use_graph:
        answer_text, tool_calls = _run_tool_loop(
            client, model, max_tokens, SYSTEM_PROMPT, user_content, vault_path,
        )
    else:
        response = client.messages.create(
            model=model, max_tokens=max_tokens, system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_content}],
        )
        answer_text = "\n".join(b.text for b in response.content if b.type == "text")

    from .wikilinks import linkify
    answer_text = linkify(answer_text, vault_path)

    return {
        "answer": answer_text,
        "sources": sources,
        "model": model,
        "retrieval": retrieval,
        "tool_calls": tool_calls,
    }

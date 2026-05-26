"""키워드 기반 단순 검색. Phase 2에서 RAG로 대체 예정."""

from __future__ import annotations

import re
from pathlib import Path

from .wiki_loader import iter_wiki_pages, load_page

_TOKEN_RE = re.compile(r"[\w가-힣]+", re.UNICODE)


def _tokenize(text: str) -> list[str]:
    return [t.lower() for t in _TOKEN_RE.findall(text)]


def _score(query_tokens: list[str], page: dict) -> int:
    """제목 매치 가중치 3, 본문 매치 가중치 1."""
    title_tokens = _tokenize(page["title"])
    body_tokens = _tokenize(page["body"])
    score = 0
    for qt in query_tokens:
        score += title_tokens.count(qt) * 3
        score += body_tokens.count(qt)
    return score


def _snippet(body: str, query_tokens: list[str], radius: int = 80) -> str:
    """쿼리 토큰 첫 매치 주변 텍스트 발췌."""
    body_lower = body.lower()
    for qt in query_tokens:
        idx = body_lower.find(qt)
        if idx != -1:
            start = max(0, idx - radius)
            end = min(len(body), idx + len(qt) + radius)
            return ("..." if start > 0 else "") + body[start:end].strip() + ("..." if end < len(body) else "")
    return body[: 2 * radius].strip()


def keyword_search(query: str, vault_path: Path, limit: int = 5) -> list[dict]:
    """쿼리에 가장 잘 매치되는 위키 페이지 top N 반환.

    Returns: [{slug, title, type, score, snippet, path}, ...]
    """
    query_tokens = _tokenize(query)
    if not query_tokens:
        return []

    scored = []
    for md_path in iter_wiki_pages(Path(vault_path)):
        page = load_page(md_path)
        s = _score(query_tokens, page)
        if s > 0:
            scored.append({
                "slug": page["slug"],
                "title": page["title"],
                "type": page["type"],
                "score": s,
                "snippet": _snippet(page["body"], query_tokens),
                "path": page["path"],
            })

    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:limit]

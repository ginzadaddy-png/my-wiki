"""의미 검색 — 쿼리 임베딩 → Chroma top-k 청크. 키워드 검색의 RAG 대체.

같은 페이지(slug)에서 여러 청크가 나오면 점수(거리) 좋은 것 기준으로 묶어
페이지 단위 결과도 제공 (agent 컨텍스트 조립용).
"""

from __future__ import annotations

from .embedder import embed_query
from . import vectorstore


def rag_search(query: str, top_k: int = 8) -> list[dict]:
    """쿼리에 의미적으로 가까운 청크 top-k 반환.

    Returns: [{id, slug, title, type, heading, text, distance, score}, ...]
        score = 1 - distance (cosine) — 높을수록 유사.
    """
    qvec = embed_query(query)
    hits = vectorstore.query(qvec, top_k=top_k)
    for h in hits:
        h["score"] = round(1.0 - h["distance"], 4)
    return hits


def rag_search_pages(query: str, top_k_chunks: int = 12, max_pages: int = 5) -> list[dict]:
    """청크 검색 후 페이지(slug) 단위로 묶어 반환.

    각 페이지의 best 청크 점수로 랭킹. agent 컨텍스트용.

    Returns: [{slug, title, type, score, chunks: [text...]}, ...]
    """
    hits = rag_search(query, top_k=top_k_chunks)
    by_slug: dict[str, dict] = {}
    for h in hits:
        slug = h["slug"]
        if slug not in by_slug:
            by_slug[slug] = {
                "slug": slug,
                "title": h["title"],
                "type": h["type"],
                "score": h["score"],
                "chunks": [],
            }
        by_slug[slug]["chunks"].append(h["text"])
        by_slug[slug]["score"] = max(by_slug[slug]["score"], h["score"])

    pages = sorted(by_slug.values(), key=lambda p: p["score"], reverse=True)
    return pages[:max_pages]

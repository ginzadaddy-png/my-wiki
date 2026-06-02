"""벡터 스토어 — numpy 기반 in-memory 코사인 검색.

chromadb의 영속 HNSW 인덱스가 재기동 시 'Error finding id'로 간헐 실패하는
문제(버전·세그먼트 reload 불안정)를 피하기 위해, 임베딩을 portable 파일
(embeddings.npy + meta.json)로 저장하고 numpy brute-force로 검색한다.
- 규모: ~1,400벡터 × 1024차원 → 내적 1회로 1ms 미만. HNSW 불필요.
- 빌드 임베딩은 BGE-M3에서 L2 정규화되므로 코사인 = 내적.
- 영속/버전/세그먼트 의존성 0 → 로컬·Space 어디서나 동일하게 동작.

인터페이스(query / collection_count)는 chromadb 시절과 동일하게 유지.
"""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

INDEX_DIR = Path(__file__).resolve().parent.parent / "index"
EMB_PATH = INDEX_DIR / "embeddings.npy"
META_PATH = INDEX_DIR / "meta.json"


def save_index(chunks: list[dict], embeddings: list[list[float]]) -> int:
    """청크 메타 + 임베딩을 portable 파일로 저장. Returns: 저장 개수."""
    import numpy as np

    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    arr = np.asarray(embeddings, dtype="float32")
    np.save(EMB_PATH, arr)
    meta = [
        {
            "id": c["id"],
            "slug": c["slug"],
            "title": c["title"],
            "type": c["type"],
            "heading": c["heading"],
            "text": c["text"],
        }
        for c in chunks
    ]
    META_PATH.write_text(json.dumps(meta, ensure_ascii=False), encoding="utf-8")
    _load.cache_clear()
    return len(meta)


@lru_cache(maxsize=1)
def _load():
    """임베딩 행렬 + 메타를 로드 (lazy singleton). 없으면 (None, [])."""
    import numpy as np

    if not EMB_PATH.exists() or not META_PATH.exists():
        return None, []
    emb = np.load(EMB_PATH)  # N×D, 빌드 시 L2 정규화됨
    meta = json.loads(META_PATH.read_text(encoding="utf-8"))
    return emb, meta


def collection_count() -> int:
    _, meta = _load()
    return len(meta)


def query(query_embedding: list[float], top_k: int = 5) -> list[dict]:
    """쿼리 임베딩으로 top-k 청크 검색 (코사인).

    Returns: [{id, slug, title, type, heading, text, distance}, ...]
        distance = 1 - cosine (작을수록 유사) — rag_search가 score=1-distance로 환산.
    """
    import numpy as np

    emb, meta = _load()
    if emb is None or not meta:
        return []
    q = np.asarray(query_embedding, dtype="float32")
    n = np.linalg.norm(q)
    if n > 0:
        q = q / n  # embed_query가 이미 정규화하지만 방어적으로
    sims = emb @ q  # emb 정규화됨 → 내적 = 코사인 유사도
    k = min(top_k, len(meta))
    top = np.argpartition(-sims, k - 1)[:k]
    top = top[np.argsort(-sims[top])]  # 유사도 내림차순
    hits = []
    for i in top:
        i = int(i)
        m = meta[i]
        hits.append({
            "id": m["id"],
            "slug": m["slug"],
            "title": m["title"],
            "type": m["type"],
            "heading": m.get("heading", ""),
            "text": m["text"],
            "distance": float(1.0 - sims[i]),
        })
    return hits

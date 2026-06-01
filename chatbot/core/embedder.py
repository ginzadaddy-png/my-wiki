"""BGE-M3 임베딩 래퍼. 로컬 모델 — API 비용 0, 한국어·교차언어 강함.

최초 import 시 모델(~2.3GB)을 다운로드/로드하므로 lazy singleton으로 관리.
"""

from __future__ import annotations

from functools import lru_cache

MODEL_NAME = "BAAI/bge-m3"


@lru_cache(maxsize=1)
def _get_model():
    """모델을 한 번만 로드 (lazy singleton)."""
    from sentence_transformers import SentenceTransformer

    return SentenceTransformer(MODEL_NAME)


def is_warm() -> bool:
    """BGE-M3 모델이 이미 이 프로세스에 로드됐는지 (콜드스타트 감지용)."""
    return _get_model.cache_info().currsize > 0


def embed_texts(texts: list[str], batch_size: int = 16) -> list[list[float]]:
    """문서 청크 임베딩 (정규화 → cosine 유사도용)."""
    model = _get_model()
    vecs = model.encode(
        texts,
        batch_size=batch_size,
        normalize_embeddings=True,
        show_progress_bar=len(texts) > 50,
    )
    return [v.tolist() for v in vecs]


def embed_query(query: str) -> list[float]:
    """단일 쿼리 임베딩."""
    model = _get_model()
    vec = model.encode([query], normalize_embeddings=True)[0]
    return vec.tolist()

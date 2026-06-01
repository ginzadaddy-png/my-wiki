"""Chroma 영속 벡터 스토어 래퍼. chatbot/chroma_db/ 에 SQLite 기반 저장."""

from __future__ import annotations

from pathlib import Path

CHROMA_DIR = Path(__file__).resolve().parent.parent / "chroma_db"
COLLECTION = "wiki_chunks"


def _client():
    import chromadb

    return chromadb.PersistentClient(path=str(CHROMA_DIR))


def get_collection(reset: bool = False):
    """컬렉션 핸들 반환. reset=True면 기존 삭제 후 재생성.

    임베딩은 외부(embedder)에서 주입하므로 embedding_function 없음.
    """
    client = _client()
    if reset:
        try:
            client.delete_collection(COLLECTION)
        except Exception:
            pass
    return client.get_or_create_collection(
        name=COLLECTION,
        metadata={"hnsw:space": "cosine"},
    )


def upsert_chunks(chunks: list[dict], embeddings: list[list[float]], reset: bool = True) -> int:
    """청크 + 임베딩을 컬렉션에 적재. reset=True면 전체 재색인.

    Returns: 적재된 청크 수.
    """
    col = get_collection(reset=reset)
    col.add(
        ids=[c["id"] for c in chunks],
        embeddings=embeddings,
        documents=[c["text"] for c in chunks],
        metadatas=[
            {
                "slug": c["slug"],
                "title": c["title"],
                "type": c["type"],
                "heading": c["heading"],
            }
            for c in chunks
        ],
    )
    return col.count()


def query(query_embedding: list[float], top_k: int = 5) -> list[dict]:
    """쿼리 임베딩으로 top-k 청크 검색.

    Returns: [{id, slug, title, type, heading, text, distance}, ...]
    """
    col = get_collection()
    res = col.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )
    hits = []
    ids = res["ids"][0]
    docs = res["documents"][0]
    metas = res["metadatas"][0]
    dists = res["distances"][0]
    for i in range(len(ids)):
        m = metas[i]
        hits.append({
            "id": ids[i],
            "slug": m["slug"],
            "title": m["title"],
            "type": m["type"],
            "heading": m.get("heading", ""),
            "text": docs[i],
            "distance": dists[i],
        })
    return hits


def collection_count() -> int:
    try:
        return get_collection().count()
    except Exception:
        return 0

"""위키 전체를 청크화 → BGE-M3 임베딩 → Chroma 재색인.

ingest 사이클 끝에 실행. (Phase 4에서 자동화 워크플로우로 연결 예정)

사용:
    python build_index.py
"""

from __future__ import annotations

import os
import time
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(override=True)

from core.chunker import chunk_vault  # noqa: E402
from core.embedder import embed_texts  # noqa: E402
from core import vectorstore  # noqa: E402


def main() -> None:
    vault = Path(os.getenv("VAULT_PATH", r"C:\Vault\Ginza\my-wiki"))

    print(f"[1/3] 청크화: {vault}")
    t0 = time.perf_counter()
    chunks = chunk_vault(vault)
    print(f"      {len(chunks)}개 청크 ({time.perf_counter()-t0:.1f}s)")

    print("[2/3] BGE-M3 임베딩 (최초 실행 시 모델 다운로드 ~2.3GB)")
    t0 = time.perf_counter()
    embeddings = embed_texts([c["embed_text"] for c in chunks])
    print(f"      {len(embeddings)}개 벡터, dim={len(embeddings[0])} ({time.perf_counter()-t0:.1f}s)")

    print("[3/3] Chroma 재색인 (reset)")
    t0 = time.perf_counter()
    count = vectorstore.upsert_chunks(chunks, embeddings, reset=True)
    print(f"      컬렉션 총 {count}개 ({time.perf_counter()-t0:.1f}s)")
    print(f"\n완료. 저장 위치: {vectorstore.CHROMA_DIR}")


if __name__ == "__main__":
    main()

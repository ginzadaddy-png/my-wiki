"""Phase 1 평가 쿼리 8개 배치 실행. 결과를 콘솔 + JSON으로 출력."""

from __future__ import annotations

import json
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(override=True)

from core import ask  # noqa: E402

QUERIES = [
    ("1", "Astro Bot은 어느 스튜디오가 만들었어?"),
    ("2", "MDA 프레임워크가 뭐야?"),
    ("3", "Sekiro의 전투 디자인 특징은?"),
    ("4", "retention 관련 인사이트는?"),
    ("5", "Sony가 모회사인 스튜디오 중 PS5 독점작을 만든 곳은?"),
    ("6", "Nintendo Switch 2 출시일은?"),
    ("7", "FromSoftware와 Team Asobi의 개발 방식 차이는?"),
    ("8", "AAA 스튜디오들의 스케일링 전략 비교는?"),
]


def main() -> None:
    key = os.getenv("ANTHROPIC_API_KEY")
    model = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6")
    vault = Path(os.getenv("VAULT_PATH", r"C:\Vault\Ginza\my-wiki"))

    results = []
    total_in = total_out = 0
    for qid, q in QUERIES:
        res = ask(q, vault, key, model=model)
        top3 = [f"{h['slug']}({h['score']})" for h in res["sources"][:3]]
        results.append({
            "id": qid,
            "query": q,
            "top3": top3,
            "answer": res["answer"],
        })
        print(f"\n{'='*70}\n[Q{qid}] {q}")
        print(f"top-3: {', '.join(top3) if top3 else '(검색 결과 없음)'}")
        print(f"답변:\n{res['answer']}")

    out_path = Path(__file__).parent / "eval-results.json"
    out_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n\n결과 JSON 저장: {out_path}")


if __name__ == "__main__":
    main()

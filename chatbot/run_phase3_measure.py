"""Phase 3(graph) 진입 측정. 진짜 다중 hop 관계 쿼리 5개를 RAG로 실행.

로드맵 v2 조건: RAG가 5개 중 3개 이상 못 풀면 Phase 3(graph) 진입.
각 쿼리는 entity 관계를 2-hop 이상 따라가야 정확한 답이 나옴.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(override=True)

from core import ask  # noqa: E402

# 각 쿼리: (id, 질문, 정답 핵심, 필요 hop 설명)
QUERIES = [
    ("M1",
     "Astro Bot을 만든 스튜디오의 모회사가 소유한 다른 스튜디오들은?",
     "Team Asobi→Sony→Sony Santa Monica·Naughty Dog·Sucker Punch·Insomniac 등",
     "game→studio→parent→sibling studios (2-hop)"),
    ("M2",
     "God of War(2018)를 만든 스튜디오와 같은 모회사를 가진 스튜디오들을 나열해줘.",
     "Sony Santa Monica→Sony→다른 Sony 퍼스트파티",
     "game→studio→parent→siblings (2-hop)"),
    ("M3",
     "Sucker Punch와 Naughty Dog의 공통 모회사는 어디고, 그 모회사의 다른 자회사는?",
     "공통=Sony, 다른 자회사 나열",
     "두 studio→공통 parent→other children (join)"),
    ("M4",
     "FromSoftware와 같은 소울라이크 장르를 만드는 다른 스튜디오·게임은?",
     "FromSoftware soulslike(다크소울·엘든링·세키로)→같은 장르 다른 작품",
     "studio→genre→other games of genre (genre hop)"),
    ("M5",
     "Ghost of Tsushima를 만든 스튜디오의 모회사가 퍼블리싱한 PS5 독점작들은?",
     "Sucker Punch→Sony→Sony 퍼블리싱 PS5 독점작",
     "game→studio→parent→published exclusives (2-hop)"),
]


def main() -> None:
    key = os.getenv("ANTHROPIC_API_KEY")
    model = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6")
    vault = Path(os.getenv("VAULT_PATH", r"C:\Vault\Ginza\my-wiki"))

    results = []
    for qid, q, expected, hop in QUERIES:
        res = ask(q, vault, key, model=model, use_rag=True)
        top3 = [f"{h['slug']}({h['score']})" for h in res["sources"][:3]]
        results.append({"id": qid, "query": q, "expected": expected,
                        "hop": hop, "top3": top3, "answer": res["answer"]})
        print(f"\n{'='*72}\n[{qid}] {q}")
        print(f"  필요 추론: {hop}")
        print(f"  정답 핵심: {expected}")
        print(f"  검색 top-3: {', '.join(top3)}")
        print(f"  답변:\n{res['answer']}")

    out = Path(__file__).parent / "eval-phase3-measure.json"
    out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n\n저장: {out}")


if __name__ == "__main__":
    main()

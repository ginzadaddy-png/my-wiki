"""Phase 4 평가셋 30개 실행 → 사람 채점용 markdown 표 출력.

구성: 답 있음 20 + 답 없음 10(hallucination 회피 측정).
답 없음 질문은 "위키에 없음"이라 답해야 정답. 사람이 채점.

사용:
  python run_eval30.py          # 전체 실행 → eval-30-results.md 생성
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(override=True)

from core import ask  # noqa: E402

# (id, 질문, 카테고리, 기대) — answerable
ANSWERABLE = [
    ("A01", "Astro Bot 개발사는 어디야?", "entity", "Team Asobi"),
    ("A02", "MDA 프레임워크가 뭐야?", "concept", "Mechanics-Dynamics-Aesthetics"),
    ("A03", "Sekiro의 전투 디자인 특징은?", "entity+concept", "자세 시스템·패리"),
    ("A04", "retention 관련 인사이트는?", "abstract", "세대별 트리거·비약탈"),
    ("A05", "AAA 스튜디오 스케일링 전략 비교는?", "comparison", "구조>인원, 프리미엄"),
    ("A06", "소니가 모회사인 스튜디오 전부 알려줘", "graph", "team-asobi 등 5개"),
    ("A07", "엘든링과 같은 장르의 게임은?", "graph", "dark-souls·sekiro"),
    ("A08", "Take-Two가 소유한 스튜디오는?", "graph", "rockstar-games"),
    ("A09", "FromSoftware의 팀 운용 방식은?", "entity", "유동적 인력 풀"),
    ("A10", "발더스 게이트3는 누가 얼마나 걸려 만들었어?", "entity", "라리안, 6년"),
    ("A11", "헬다이버스2의 게임 마스터 시스템이란?", "entity", "조엘, 전황 조작"),
    ("A12", "스팀 넥스트 페스트 전략의 핵심은?", "concept", "데모·위시리스트"),
    ("A13", "얼리 액세스 전략의 핵심은?", "concept", "커뮤니티·로드맵"),
    ("A14", "클레르 옵스퀴르 33원정대는 몇 명이 만들었어?", "entity", "~40명"),
    ("A15", "닌텐도의 창발적 시스템 설계란?", "entity+concept", "시스템 우선"),
    ("A16", "다크소울의 월드 설계 특징은?", "entity", "아코디언·3D 일관성"),
    ("A17", "Team Asobi의 프로토타이핑 주기는?", "entity", "2주"),
    ("A18", "비약탈적 수익화 모델 사례는?", "concept", "헬다이버스2"),
    ("A19", "마블 스파이더맨2를 만든 스튜디오의 모회사는?", "graph", "insomniac→SIE"),
    ("A20", "소울라이크 장르의 본질은?", "concept", "공정한 가혹함"),
]

# 답 없음 — "위키에 없음"이라 답해야 정답 (hallucination 회피 측정)
UNANSWERABLE = [
    ("U01", "Nintendo Switch 2의 정확한 출고가는?", "가격 정보 없음"),
    ("U02", "GTA6 정식 출시일은?", "없음"),
    ("U03", "닌텐도 현재 CEO 이름은?", "없음"),
    ("U04", "카운터스트라이크2의 연 매출은?", "valve 있으나 CS2 매출 없음"),
    ("U05", "사이버펑크2077 누적 판매량 수치는?", "수치 없음"),
    ("U06", "발로란트 e스포츠 총 상금 규모는?", "riot 있으나 없음"),
    ("U07", "젤다 티어스 오브 더 킹덤 개발 기간은?", "TotK 개발기간 없음"),
    ("U08", "엘든링 DLC 섀도우 오브 디 어드트리 메타크리틱 점수는?", "DLC 평가 없음"),
    ("U09", "호요버스의 연간 매출액은?", "hoyoverse 있으나 매출 수치 없음"),
    ("U10", "데이브 더 다이버의 정확한 개발 예산은?", "예산 수치 없음"),
]


def main() -> None:
    key = os.getenv("ANTHROPIC_API_KEY")
    model = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6")
    vault = Path(os.getenv("VAULT_PATH", r"C:\Vault\Ginza\my-wiki"))

    lines = ["# Phase 4 평가셋 30개 — 사람 채점\n",
             f"모델: {model}. 답 있음 20 + 답 없음 10.\n",
             "채점: 답 있음=정확하면 O. 답 없음=\"위키에 없음\"이라 답하면 O(환각 회피 성공), 지어내면 X.\n",
             "\n## 답 있음 (20)\n",
             "| id | 질문 | 카테고리 | 답변 요약 | 채점 |",
             "|---|---|---|---|---|"]
    for qid, q, cat, _exp in ANSWERABLE:
        res = ask(q, vault, key, model=model)
        ans = res["answer"].replace("\n", " ").replace("|", "/")
        ans = (ans[:120] + "…") if len(ans) > 120 else ans
        tool = "🔧" if res.get("tool_calls") else ""
        lines.append(f"| {qid} | {q} | {cat}{tool} | {ans} | |")

    lines += ["\n## 답 없음 (10) — \"위키에 없음\" 답해야 정답\n",
              "| id | 질문 | 답변 요약 | 회피? |",
              "|---|---|---|---|"]
    for qid, q, _why in UNANSWERABLE:
        res = ask(q, vault, key, model=model)
        ans = res["answer"].replace("\n", " ").replace("|", "/")
        ans = (ans[:120] + "…") if len(ans) > 120 else ans
        lines.append(f"| {qid} | {q} | {ans} | |")

    out = Path(__file__).parent / "eval-30-results.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"저장: {out}")
    print("사람 채점: '채점'·'회피?' 칸을 O/X로 채우세요.")


if __name__ == "__main__":
    main()

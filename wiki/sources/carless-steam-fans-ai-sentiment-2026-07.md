---
title: "GameDiscoverCo — Steam 팬은 게임 속 AI를 어떻게 보나 (설문, Carless)"
type: source-summary
source_url: "https://newsletter.gamediscover.co/p/what-do-steam-fans-really-think-about"
source_author: "Simon Carless (GameDiscoverCo)"
source_published: 2026-07-07
sources: []
related: ["[[ai-disclosure-player-sentiment|AI 디스클로저 플레이어 정서]]", "[[ai-gamedev|게임 개발에서의 생성형 AI]]", "[[audience-discovery-systems|오디언스 발견 시스템]]", "[[valve|Valve]]"]
created: 2026-07-13
updated: 2026-08-03
confidence: high
---

**원문**: [newsletter.gamediscover.co](https://newsletter.gamediscover.co/p/what-do-steam-fans-really-think-about) — Simon Carless (GameDiscoverCo), 2026-07-07

GameDiscoverCo의 *Steam Fan Snapshot*(경품 기반 모집, 6/25–7/2 필드, 전체 ~1.6만 중 AI 문항 ~3,800명 응답)에서 뽑은 **소비자 측 AI 정서** 데이터. 표본은 평균보다 참여도 높은 "코어 Steam 팬"이라는 점을 저자가 명시.

## AI 공개(disclosure) 게임 구매 태도

| 태도 | 비율 |
|------|------|
| 무관심 (구매에 문제 없음) | **43%** |
| 중립 | 26% |
| 부정 | **31%** (그중 구매 거부 8%) |

- **디스클로저 열람**: 상세히 읽음 44% · 대충 봄 45% · 무시 11%
- **개발자 신뢰**: AV(오디오·비주얼) AI 사용을 *완전 공개*한다고 믿는 유저 **17%뿐** (35%는 "일부만 공개된다"고 의심) — 투명성 회의 큼

## 용도별 수용도 (2,100 응답 텍스트 분석)

- **조건부 수용 51%** — 특정 용도에 한해 허용
- 언급 빈도: 코딩/프로그래밍 헬퍼 **239** · 프로토타입·플레이스홀더 에셋 119 · 반복 작업 101
- **코딩 툴 공개 여부**: "Claude Code 같은 AI 코딩 툴도 공개돼야" **56% vs 반대 8%**

## Steam MAU 신규 추정 (덤)

EU DSA 공시(H2 2025 EU **3,110만** MAU) + 대역폭 분포 외삽 → **글로벌 ≈1.98억 MAU** (2025 말, 연말 2.1억까지 성장 가능성).

> ⚠️ 모순 (2026-08-03 **해소**): 기존 [[valve|Valve]] 페이지의 **~1.4억**과 Carless의 **~1.98억** 격차를 재조사한 결과, *대등한 두 추정의 대립이 아니라 한쪽의 기준선 오류*로 판명됐다. 1.4억은 Valve의 **2021년 공식 수치(1.32억 MAU·6,900만 DAU)를 최신치로 오표기한 애그리게이터 계보**에 +11%를 얹은 파생값이다. Carless 쪽은 Valve의 **DSA 법정 공시(H2 2025 EU 3,110만)** 라는 최신 공식 숫자에서 대역폭 분포로 역산한 값이고, 2021 MAU:피크CCU 비율(4.8배)을 2026-01 피크 CCU 4,204만에 대입한 독립 검증(약 2.02억)과도 일치한다. → **위키는 Carless 추정(약 2억, 추정 병기)을 채택**하고 1.4억은 사용하지 않는다. 상세 계보 표는 [[valve|Valve]] "MAU 규모 — 수치 계보와 채택 기준" 절.

> 💡 **핵심 인사이트:** 개발자 정서([[ai-gamedev]])는 2026년 부정 52%로 격앙됐지만, *구매자* 정서는 무관심 43% > 부정 31%로 온도차가 크다. 소비자 저항은 "AI 자체"보다 **불투명한 공개**에 집중 — 신뢰 17%가 이를 방증. 즉 AI 사용 시 리스크를 낮추는 레버는 *숨기기*가 아니라 *명확한 디스클로저*이며, 코딩·프로토타입 같은 비-플레이어페이싱 용도는 이미 폭넓게 용인된다.

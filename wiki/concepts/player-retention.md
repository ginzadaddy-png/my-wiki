---
title: "플레이어 리텐션"
type: concept
sources: []
related: ["[[engagement-loop|인게이지먼트 루프]]", "[[live-service-design|라이브 서비스 설계]]", "[[mobile-gamedev|모바일 게임 개발]]", "[[launch-metrics|흥행 예측 지표]]", "[[data-driven-development|데이터 기반 개발]]", "[[early-access-strategy|얼리 액세스 전략]]"]
created: 2026-06-22
updated: 2026-06-22
confidence: medium
---

획득(acquisition) *이후* 플레이어를 얼마나 유지·재방문시키는지 측정·관리하는 지표 체계. 설계 측면은 [[engagement-loop|인게이지먼트 루프]], 운영 측면은 [[live-service-design|라이브 서비스 설계]]와 짝을 이룬다.

## 핵심 지표

- **D1 / D7 / D30 리텐션** — 첫 플레이 후 N일째 복귀율. 곡선 아래 면적이 평균 라이프타임의 프록시.
- **churn** = 1 − retention.
- **DAU/MAU (stickiness)** — 월간 유저 중 매일 돌아오는 비율. **0.2(20%)가 합격선, 0.3+(30%)가 world-class**. 7% 미만은 심각한 참여 문제. (캔디크러시류 캐주얼 25–30%, 소셜카지노 35%+)
- **LTV** ≈ ARPDAU × 평균 라이프타임 → D1·D7이 곡선 적합의 앵커.

> ⚠️ 정정: 핸드오프 스캐폴드의 "DAU/MAU 우수 0.5+"는 과장. 실제 world-class는 **30%+**이며 0.5(50%)는 비현실적. (출처: udonis·clevertap stickiness 벤치마크 2024–25)

## classic vs rolling retention

- **classic** — 정확히 N일째에 복귀한 비율.
- **rolling** — N일째 *이후 언제라도* 복귀한 비율 → 항상 classic보다 높음.
- 두 정의를 섞으면 5–10%p 차이가 그대로 오차가 된다. 벤치마크 비교 시 **정의 일치 필수**. (출처: devtodev)

## 벤치마크 — 단일 숫자 인용 금지

GameAnalytics **Q1 2024 실측 중앙값**(10,000+ 프로젝트, 27억 MAU):

| 지표 | 전체 중앙값 | iOS 상위 25% |
|---|---|---|
| D1 | 22.91% | 31–33% |
| D7 | 4.2% | 7–8% |
| D28 | 0.85% | ~3% 미만이 75% |

> ⚠️ 정정: 스캐폴드가 "통용치"로 적은 D1 30–35% / D7 8–12% / D30 3–5%는 **중앙값이 아니라 상위권(iOS top-25%)에 가깝다**. 위키·보고서 인용 시 *중앙값 vs 상위 분위*를 반드시 구분. (출처: [GameAnalytics Q1 2024 Mobile Gaming Benchmarks](https://www.gameanalytics.com/reports/mobile-games-benchmarks-q1-2024))

**분석사 편차**: GameAnalytics·Adjust·AppsFlyer 간 정의·표본·측정 윈도우 차로 5–10%p 편차가 정상. 단일 출처 단정 금지. 콘솔/PC 프리미엄은 표준 벤치마크가 희소해 완주율·주간 활성·Steam playtime이 프록시.

**장르 경향**(방향성, 검증된 절대치 아님): 하이퍼캐주얼은 D1 높고 D30 급락 / 퍼즐·캐주얼은 D30 견고 / RPG·미드코어는 D1 낮으나 ARPU·라이프타임 길다 / 소셜카지노 최상위.

## 실무 적용

- **코호트 분석** — 설치 코호트별 리텐션 커브 비교.
- **FTUE 퍼널 drop-off** — D1은 사실상 첫인상(온보딩) 품질 지표.
- **예측 churn 세그먼트 → win-back** — 이탈 신호 기반 복귀 캠페인.

> 💡 **핵심 인사이트:** 리텐션 숫자는 *정의·표본·분위*가 붙어야 의미가 산다. "D1 35%"는 출처와 정의 없이는 정보가 아니라 노이즈다. 그리고 리텐션은 결과 지표일 뿐, 그 *원인*은 [[engagement-loop|루프 설계]]와 [[player-trust-design|플레이어 신뢰]]에 있다.

---

*세대별 복귀 트리거(Gen X·M·Z) 모델은 [[live-service-design|라이브 서비스 설계]]의 "Players → Residents" 섹션 참조. 본 페이지 수치는 deep-research로 1차 출처 검증(2026-06)했으며, 분석사 추정·벤치마크는 연도·정의가 바뀌면 갱신 대상.*

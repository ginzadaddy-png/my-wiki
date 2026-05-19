---
title: "ZR Consulting Steam Revenue Forecaster — 인디 런치 예측 모델"
type: source-summary
sources: []
related: ["[[steam-revenue-forecasting|Steam 매출 예측 모델]]", "[[publisher-deal-structures|퍼블리셔 딜 구조]]", "[[launch-metrics|흥행 예측 지표]]", "[[game-pricing-strategy|게임 가격 전략]]", "[[marketing-strategy|마케팅 전략]]", "[[indie-business-strategy|인디 비즈니스 전략]]", "[[zukowski-next-fest-strategy|Zukowski Next Fest 분석]]", "[[steam-next-fest-2026-analysis]]"]
created: 2026-05-18
updated: 2026-05-18
confidence: medium-high
source_url: "https://zrconsulting.de/steam-forecaster/"
source_author: "Zoran Roso (ZR Consulting, Munich)"
source_published: 2026-05
---

**원문**: [zrconsulting.de/steam-forecaster](https://zrconsulting.de/steam-forecaster/) — ZR Consulting, Munich, 2026 업데이트

독일 뮌헨의 게임 산업 컨설팅 ZR Consulting(대표 Zoran Roso, 25년 경력)이 공개한 **무료 Steam 매출 예측 계산기 + 방법론 문서**. 인디·중소 스튜디오의 *런치 매출 예측* 및 *퍼블리셔 딜 stress test*에 사용. 모든 multiplier·시간 분포·계산 순서가 100% 공개되어 있어 재현 가능.

> 💡 **핵심 인사이트:** Steam에서 흥행을 좌우하는 변수는 무한하지만 *영향력 큰 8개 driver*로 압축 가능. 위시리스트 수, 사전 buzz, 리뷰 tier 세 가지가 Year-1 매출 변동의 70%+ 설명. *서브장르별로 conversion rate가 10× 차이 나므로* "Steam 평균 15%" 같은 일반론은 의사결정에 쓸모없다 — 자신의 sub-genre 기준이 필요하다.

## 핵심 정량 — 위시리스트 conversion 모델

[GameDiscoverCo 2025-10 연구](https://newsletter.gamediscover.co/p/the-state-of-steam-wishlist-conversions)(Simon Carless) 데이터를 기반으로:

- **Week-1 median conversion: 0.15×** (15% of wishlists)
- **가격 $10 초과 시: 0.10×** (33% 감소) — *가격이 가장 직접적인 conversion 영향 요인*
- 분산: median에서 ±10× 변동 가능
- 42개 sub-genre × 12 parent family 별도 벤치마크

## 서브장르별 conversion 상위·하위 (Zukowski 2024 success rate)

| 위치 | 장르 | 1,000 review 달성률 |
|---|---|---|
| 상위 | Open World Survival Craft | **24.5%** |
| 상위 | Farming Sim (cozy) | **20.8%** |
| 상위 | Horror | 절대 hit 볼륨 1위 |
| 상위 | Idle / Incremental, Job Sim | 상위 tier |
| 하위 | Match-3 | single digit % |
| 하위 | 2D Platformer | single digit % |
| 하위 | Traditional Visual Novel | single digit % |

**Co-op horror 폭발 사례** (median의 7~29×):
- PEAK: **29×** median
- Mage Arena: 8.7×
- R.E.P.O.: 7.5×

## Review tier multipliers (discoverability gate)

| Tier | Multiplier | 의미 |
|---|---|---|
| Negative | 0.25× | 거의 절멸 |
| Mixed | 0.55× | 매출 반토막 |
| Mostly Positive | **1.0×** | baseline |
| Very Positive | 1.15× | |
| Overwhelmingly Positive | **1.4×** | 알고리즘 push |

*"한 tier drop으로 1년 매출이 반토막날 수 있다"* — Steam discoverability algorithm이 review를 강하게 gating.

## Pre-launch buzz multipliers

| Tier | Multiplier | 대표 사례 |
|---|---|---|
| None | 1.0× | quiet release |
| Some | 1.15× | |
| Building | 1.4× | |
| Strong | 1.8× | |
| **Phenomenon** | **2.5×** | Hades · Vampire Survivors · Balatro · Lethal Company |

Phenom tier는 *연 1회 수준*. 의도된 희소성: "part craft, part timing, part luck."

## Launch context lifts (런치 컨텍스트)

- **Demo at launch**: +8% conversion
- **Next Fest 참여**: +4% conversion + 런치월 매출 비중 증가 효과
- 둘 다 *상호 독립적·곱셈 작용* — 같이 가능하면 둘 다 적용. *가장 cheap한 revenue boost*

## Time distribution (Year 1)

- **런치월: ~38%** (Year-1 매출 중)
- 월 3·6 Steam-wide sale 시점에 lift
- Year 2 add-on: Year 1의 **+35%**
- Healthy launches: 50~200% 추가 위시리스트가 Year 1 동안 발생, **0.7× conversion**으로 환산

## 가격·환불·플랫폼 cut

- **Regional pricing haircut**: 글로벌 20-30% / US·EU 중심 5-15%
- **Refund rate**: 평균 7% (단편 10-15%, 장편 3-7%)
- **Steam cut**: 30% (≤$10M), 25% ($10-50M), 20% (>$50M) — 인디는 사실상 30%만 해당

## 8 Drivers — Sensitivity Ranking

ZR Forecaster의 가장 큰 가치는 *어디에 시간·돈을 쓸지* 우선순위가 명확하다는 점. Tornado chart로 변동성 크기에 따라 정렬:

1. **Wishlists at launch** — 가장 통제 가능. demo·Next Fest·creator outreach·paid acquisition·store page·capsule iteration으로 lift
2. **Post-launch wishlists** — 패치·sale·creator outreach·community management
3. **Pre-launch buzz** — capsule 후크·streamer outreach·festival submission·Discord
4. **Review score** — 크래시 0·첫 시간 polish·리뷰 응답·빠른 패치·스토어 페이지 기대치 관리
5. **Price** — 장르 평균 벤치마크·플레이타임·콘텐츠·polish로 정당화
6. **Refund rate** — 강한 1시간 오프닝·크래시 0·길이 투명 공개·데모 self-select
7. **Organic** — 태그·patch·sale 참여·바이럴·스트리머
8. **Seasonal/Launch discount** — 의도적 trade-off. 0% = 자신감 신호, 10% = 표준, 20%+ = 알고리즘에 약세 신호

## Publisher Deal Stress Test — 4가지 구조

ZR이 *DACH + Central Europe 인디 publishing 협상* 경험으로 모델링한 4종:

| 구조 | 메커니즘 | 위험 |
|---|---|---|
| **Self-published** | 100% post-Steam (= 70% gross) | 마케팅·PR·store ops 자체 부담 |
| **Standard rev share (30%)** | 70/30 split post-Steam | 표준 |
| **Aggressive rev share (50%)** | 50/50 split | 퍼블리셔 기여 높아야 정당화 |
| **Recoup-first** | 100% to publisher until recouped | 매출 부진 시 dev 0 |
| **MG against royalty** | Upfront MG → 이후 royalty로 recoup | dev cashflow 가장 안전 |
| **Marketing fee** | Fixed fee off top + rev share | 저매출 시 fee가 매출 잠식 |

## Calibrated estimates — ZR 자체 추정 (medium confidence)

다음은 1차 데이터가 아닌 ZR 보정값. 신뢰도 유의:
- Buzz tier multipliers
- Demo +8% / Next Fest +4% lift
- Post-launch 0.7× ratio
- Year-1 launch month 38%
- Year-2 +35%
- Organic 5-50%
- Community growth 5/15/35% bands
- Playtest → review/refund mapping

## 한계·주의

- ZR 본인 명시: *"30-50% 편차 가능. 예측이 아닌 계획 도구"*
- 1차 데이터(Carless·Zukowski·Valve)는 high confidence, 자체 calibration은 medium
- Specific game이 model 밖으로 30-50% 벗어날 수 있는 요인: press cycle·viral moment·genre saturation·competitor launch·marketing 실행
- ZR Consulting 자체는 비교적 무명. 신뢰도는 *인용 출처*에 의존

## 위키 연결

- [[steam-revenue-forecasting|Steam 매출 예측 모델]] — 본 자료가 만든 신규 concept (모델·매트릭스·sensitivity 정량 정리)
- [[publisher-deal-structures|퍼블리셔 딜 구조]] — 본 자료가 만든 신규 concept (4종 구조·stress test)
- [[launch-metrics|흥행 예측 지표]] — 가짜 신호 vs 행동 기반 + ZR conversion·refund·time distribution 보강
- [[game-pricing-strategy|게임 가격 전략]] — $10 threshold drop · regional haircut 정량 보강
- [[marketing-strategy|마케팅 전략]] — Demo·Next Fest lift · 8-driver sensitivity 보강
- [[indie-business-strategy|인디 비즈니스 전략]] — break-even · publisher deal stress test 보강
- [[zukowski-next-fest-strategy|Zukowski Next Fest 분석]] — 같은 데이터 소스 (Chris Zukowski 2024 success rate)
- [[steam-next-fest-2026-analysis]] — Next Fest 정량 lift 비교
- [[early-access-strategy|얼리 액세스 전략]] — playtest cohort → review tier · refund 매핑 메커니즘
- [[peak|PEAK]] — co-op horror 29× outlier 사례 (PEAK·Mage Arena·R.E.P.O.)

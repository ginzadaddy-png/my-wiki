---
title: "Steam 매출 예측 모델 (Steam Revenue Forecasting)"
type: concept
sources: ["[[carless-wishlist-conversions-2025-10]]", "[[carless-genres-ruled-steam-2025-06]]", "[[zukowski-2025-year-review]]", "[[zukowski-bad-launch-recovery-2024]]", "[[zrconsulting-steam-forecaster-2026]]", "[[zukowski-next-fest-strategy]]", "[[steam-next-fest-2026-analysis]]", "[[steam-next-fest-wishlist-benchmarks-2025]]"]
related: ["[[launch-metrics|흥행 예측 지표]]", "[[marketing-strategy|마케팅 전략]]", "[[game-pricing-strategy|게임 가격 전략]]", "[[indie-business-strategy|인디 비즈니스 전략]]", "[[publisher-deal-structures|퍼블리셔 딜 구조]]", "[[early-access-strategy|얼리 액세스 전략]]", "[[valve|Valve]]", "[[forecasting-vs-launch-metrics|예측 vs 측정 비교]]"]
created: 2026-05-18
updated: 2026-05-18
confidence: medium-high
---

**Steam 매출 예측 모델**은 인디·중소 스튜디오가 *런치 전*에 Year-1 매출 범위를 추정하고, 어떤 변수가 결과를 가장 크게 좌우하는지 파악해 자원 배분 우선순위를 결정하는 정량 프레임워크다. 위시리스트 수·서브장르·리뷰 tier·사전 buzz·런치 컨텍스트가 핵심 입력. ZR Consulting의 *Steam Revenue Forecaster* (2026)와 GameDiscoverCo·Chris Zukowski의 정량 데이터를 기반으로 한다.

> 💡 **핵심 인사이트:** "Steam 위시리스트 conversion 평균 15%"라는 일반론은 의사결정에 *쓸모없다*. 동일 카테고리 게임이 median에서 *10-20× 차이*로 분포 (GameDiscoverCo Carless 2025-10 원전). PEAK 같은 co-op viral은 *266×* median outperform, 전통적 visual novel은 한 자릿수 %. *자신의 sub-genre 벤치마크 + 분포 상한·하한*을 함께 보아야 한다. 더불어 8개 driver 중 상위 3개(wishlist count · pre-launch buzz · review tier)가 Year-1 매출 변동의 70%+를 설명한다.

## 핵심 공식 ([[zrconsulting-steam-forecaster-2026]])

```
Year-1 net = Wishlists × SubGenre_conv × Review_mult × Buzz_mult
           × (1 + post_launch_ratio × 0.7)
           × ARPU_effective
           × (1 - refund_rate)
           × (1 - steam_cut_30%)
           + Organic_sales
```

각 변수의 정량 범위와 통제 방법은 다음 절에서.

## 1) Wishlist conversion 정량 ([[carless-wishlist-conversions-2025-10]] 1차)

GameDiscoverCo Simon Carless 2025-10 데이터 (>25k wishlist 게임, 2024-09~2025-09 기간):

| 필터 | Week-1 median conversion |
|---|---|
| All games (>25k wishlists) | **0.15×** |
| Adult 게임 제외 | 0.14× |
| **>$10 가격 게임만** | **0.10×** |

**Variance**: 게임마다 *10-20×* 차이 (median의 10% ~ 10× 사이 분포). 가장 중요한 단일 caveat — *median 단일 숫자로 자기 게임 예측 시도 자체가 near-fatally flawed*.

> ⚠️ ZR Forecaster (2026-05)는 위 0.15·0.10× 수치는 동일 인용하지만 *variance를 10×로 축소*해 표기. 실제 Carless 원전은 **10-20× variance**. 더 큰 불확실성을 전제로 계획해야 함.

## 2) 서브장르별 1,000-review 달성률 ([[zukowski-2025-year-review]] · [[zukowski-bad-launch-recovery-2024]] 1차)

> ⚠️ **연도 명시 필수.** ZR Forecaster (2026-05)가 OWSC 24.5% / Farming 20.8%로 인용한 수치는 *2024 데이터*. 2025년에는 OWSC 20.8% (-4pp), **Farming 8.3% (-12pp, 60% 감소)** — 연도마다 변동이 크다.

### 2025 출시 게임 분석 (Zukowski 2026-01, n=20,282)

| 장르 | 2024 % | **2025 %** | 변화 |
|---|---|---|---|
| Open World Survival Craft | 24.5% | **20.8%** | ⬇ -4pp |
| Farming Sim (cozy) | 20.8% | **8.3%** | ⬇⬇ **-12pp** |
| Roguelike Deckbuilder | 6.71% | 5.1% | ⬇ |
| Simulation (Job Sim 등) | 3.76% | **4.1%** | ⬆ |
| Management | 5.43% | 3.4% | ⬇ |
| Horror | 1.81% | **3.2%** | ⬆ |
| Idle / Incremental | 3.05% | 2.79% | ⬇ |
| RPG | 1.46% | **2.4%** | ⬆ |
| Tower Defense | 1.44% | 1.76% | ⬆ |
| Racing | 1.34% | 2.1% | ⬆ |
| Automation | 1.57% | 1.19% | ⬇ |
| Sexual Content | 1.26% | 1.1% | ⬇ |
| Souls-like | 0.83% | 0.8% | ➡ |
| RTS | 0.82% | 0.9% | ⬆ |
| Metroidvania | 2.21% | 1.1% | ⬇⬇ |
| Colony Sim | 0.63% | 1.0% | ⬆ |
| City Builder | 2.70% | **0.5%** | ⬇⬇ |
| VR | 0.43% | 0.27% | ⬇ |
| Puzzle | 0.36% | 0.34% | ➡ |
| 2D Platformer | 0.25% | 0.18% | ⬇ |
| Point & Click | 0.13% | 0.18% | ⬆ |
| 3D Platformer | 0.72% | **0.05%** | ⬇⬇⬇ |

전체 시장: 20,282 출시 게임 중 1,000+ review 달성 **608개 (2.99%)** — 역대 최고 ([[zukowski-2025-year-review]] 골든 에이지 분석).

### Top 10 (1000+ review 절대 수)

```
2025: Narrative(51) · Simulation(43) · Horror(39) · RPG(28) · Idle(27)
      Roguelike(22) · Sexual(21) · Multi-Shooter(21) · Shooter(21) · Management(19)
2024: Horror(47) · Narrative(30) · Simulation(27) · Shooter(27) · OWSC(23)
      Sexual(20) · Idle(20) · Management(19) · RPG(17) · Roguelike(16)
2023: Horror(28) · OWSC(23) · Simulation(21) · Narrative(20) · Multi-Shooter(20)
2022: Horror(29) · Shooter(23) · Sexual(20) · RPG(19) · Simulation(17)
```

→ **장르 메타는 4-5년 단위로 매우 안정** (Top 10 중 9개가 전년과 동일). Narrative 부상은 *중국 FMV 게임* (Revenge on Gold Diggers 등) 영향.

## 3) Co-op viral outliers ([[carless-wishlist-conversions-2025-10]] 1차)

Carless 2025-10 원전 데이터 (Top 20 best-seller 분석):

| 게임 | Carless multiplier | ZR 인용 | 차이 |
|---|---|---|---|
| **[[peak|PEAK]]** (co-op mountaineering) | **266×** | 29× | 한 자릿수 |
| **Mage Arena** (PvP magic arena) | **78×** | 8.7× | 한 자릿수 |
| **R.E.P.O.** (co-op horror) | **68×** | 7.5× | 한 자릿수 |
| **WEBFISHING** (chill social) | 67× | — | — |
| **Revenge On Gold Diggers** (Chinese FMV) | **539×** | — | — |
| **The Cabin Factory** (horror, social video) | 16× | — | — |
| **A Game About Digging A Hole** | 13× | — | — |
| FlyKnight (co-op friendly) | 18× | — | — |
| **InZOI** (life sim, AAA pre-order 포함) | 3.2× (Top 20 minimum) | — | — |

> ⚠️ **ZR Forecaster의 outlier 수치는 한 자릿수 축소되어 인용되었음.** PEAK 29× vs Carless 266×, Mage Arena 8.7× vs 78×, R.E.P.O. 7.5× vs 68×. 위키 사용 시 *Carless 원전 우선* 인용. ZR이 다른 시점·다른 시그널 정의를 썼을 가능성 있음.

**공통 패턴**: 모두 *online co-op 중심 crewlike*. 한 컨텐츠 크리에이터 발견이 전파의 시작점 (예: BRUTALISTICK VR의 Bucky 41-video 시리즈 → [[zukowski-bad-launch-recovery-2024]] 참조).

## 2) Review tier multiplier

| Tier | Multiplier | 알고리즘 영향 |
|---|---|---|
| Negative | 0.25× | 거의 절멸 |
| Mixed | 0.55× | 매출 반토막 |
| **Mostly Positive** | **1.0×** | baseline·인플렉션 포인트 |
| Very Positive | 1.15× | |
| Overwhelmingly Positive | **1.4×** | 알고리즘 push |

> ⚠️ Mostly Positive 70%가 *알고리즘 게이트*. 그 아래면 wishlist conversion·discovery 동시 침체. 첫 시간 polish·크래시 0·early review 응답이 *비대칭적 ROI*.

## 3) Pre-launch buzz multiplier

[[marketing-strategy|마케팅 전략]]의 정량 모델:

| Tier | Multiplier | 사례 |
|---|---|---|
| None | 1.0× | quiet release |
| Some | 1.15× | small streamer coverage |
| Building | 1.4× | meaningful press · festival |
| Strong | 1.8× | TGA 노미네이션 수준 |
| **Phenomenon** | **2.5×** | Hades · Vampire Survivors · [[balatro|Balatro]] · Lethal Company |

Phenom tier는 *연 1회* 발생. 의도된 희소성. *part craft, part timing, part luck.*

## 4) Launch context lifts

- **Demo at launch**: +8% conversion
- **Next Fest 참여**: +4% conversion + 런치월 비중 ↑
- 두 효과 *독립적·곱셈*

→ 자세한 페스트 알고리즘·CL2 vs HMD 비교는 [[steam-next-fest-2026-analysis]] · [[zukowski-next-fest-strategy]] 참조.

## 5) Time distribution (Year 1·2)

```
Month  1: ~38%  ← 런치월
Month  2: ~12%
Month  3: lift (첫 Steam-wide sale)
Month  6: lift (Summer Sale 등)
Month 12: cumulative 100% of Year 1
Year   2: +35% of Year 1 total
```

Year 2 +35% 추정은 healthy launch + 지속적 가시성(sale 참여·content update) 전제. cold-launched 타이틀은 그보다 낮음.

## 6) Post-launch wishlists

- 발매 후 추가되는 wishlist는 *사전 wishlist의 0.7× conversion*
- Healthy launches: launch-day 카운트의 50~200% 추가 발생
- Sleeper hit은 그보다 훨씬 많음 (BG3·Hades 같은 경우)

→ [[catalog-economics|카탈로그 이코노믹스]]와 자연스럽게 연결 — 사후 wishlist는 cross-sell·patch·sale·creator 활동의 누적 결과

## 7) Effective ARPU

```
ARPU = list_price × (1 - regional_haircut) × (1 - blended_discount)
where blended_discount = launch_discount × 0.38 + seasonal_discount × 0.62
```

- **Regional haircut**: 글로벌 20-30% / US·EU 중심 5-15% → [[game-pricing-strategy|게임 가격 전략]] 참고
- **Blended discount**: 런치월(38%)과 그 외(62%) 가중평균
- 런치 10% discount = 표준. 20%+ = 알고리즘에 약세 신호. 0% = 자신감 신호

## 8) 8 Drivers — Sensitivity Ranking (Tornado)

매출 변동성 크기 순. 위에 있을수록 *집중 투자* 가치 큼:

```
[████████████████████]  1. Wishlists at launch        (±40%)
[██████████████]        2. Pre-launch buzz             (1.0~2.5×)
[█████████████]         3. Review score                (0.25~1.4×)
[██████████]            4. Post-launch wishlists       (0.7× sub-rate)
[████████]              5. Price                       (±$5)
[██████]                6. Refund rate                 (5-15%)
[█████]                 7. Organic / non-wishlist      (5-50%)
[████]                  8. Seasonal · launch discount  (±5pp)
[██]                    9. Regional pricing            (5-30%)
[██]                    10. Demo + Next Fest           (+12% 합산)
```

> ⚠️ 위 ranking은 *전형적* 게임 기준. 게임마다 다름:
> - 단편 narrative game → refund rate가 위로
> - 화제성 강한 IP/디렉터 → buzz가 위로
> - 코어 audience 작은 장르 → wishlist count가 결정적

## 9) Calibrated estimates — 신뢰도 분리

다음 항목은 1차 데이터가 아닌 *ZR Consulting 보정값*. 신뢰도 medium:
- Buzz tier multipliers (1.0~2.5×)
- Demo +8% / Next Fest +4% lift
- Post-launch 0.7× ratio
- Year-1 launch month 38%
- Year-2 +35%
- Organic 5-50% range
- Community growth 5/15/35% bands
- Playtest cohort → review/refund mapping

1차 데이터 high confidence:
- Sub-genre conversion (GameDiscoverCo 2025-10)
- Genre success rate (Zukowski 2024)
- Steam cut 30%/25%/20% (Valve 공식)
- Refund 5-10% (Valve 발언)
- Regional pricing haircut (Steam 권장 matrix)

## 10) Self-diagnosis 체크리스트 (예측 정밀도 사전 점검)

다음을 알면 예측이 정확해진다:
1. Sub-genre 매트릭스에서 자신의 정확한 위치 식별 (parent family + sub-genre)
2. 위시리스트 trajectory 90일 (30일 net add ÷ 30 × days_to_launch)
3. Demo 또는 closed playtest 데이터 (downloads · review % · completion rate)
4. Wishlist 출처 분포 (paid 비중 vs organic — paid >40% 시 risk)
5. Community 30일 성장률 (Discord/newsletter, *절대 사이즈보다 성장률*)
6. 동일 스튜디오 prior game 매출 (있으면 *가장 강력한 comp*)

## 한계 및 적용 주의

- **30-50% 편차 가능**: ZR이 명시한 model 한계
- **모델로 못 잡는 요인**: press cycle, viral moment, genre saturation, competitor launch, marketing execution 디테일
- **소규모 cohort 신호**: playtest <20명 응답은 *directional only*
- **Paid wishlist quality**: 유료 광고로 산 wishlist는 organic 대비 conversion 낮음. paid 비중 >40% 시 forecast downside

## 추가 조사 주제
- 한국 인디 스튜디오 sub-genre 매트릭스 매핑 — 위 ZR 매트릭스가 글로벌 indie. 한국 인디(예: [[balatro|Balatro]]식 single hit) sub-genre 위치 검증
- 일본·아시아 시장에서의 Steam vs 콘솔 conversion 격차 (forecaster는 글로벌 가정)
- AA·미드 프라이스 게임에서 forecaster 적용 가능성 — 인디 모델 기반이라 [[clair-obscur-expedition-33|클레르 옵스퀴르]] 같은 600만 hits에 적용 시 보정 필요
- Co-op viral outlier (PEAK 29×) 메커니즘 분석 — 모델이 *못 잡는* 영역

---
title: "GameDiscoverCo — Steam Wishlist Conversions 2024-2025 (Carless 2025-10)"
type: source-summary
sources: []
related: ["[[steam-revenue-forecasting|Steam 매출 예측 모델]]", "[[launch-metrics|흥행 예측 지표]]", "[[game-pricing-strategy|게임 가격 전략]]", "[[zrconsulting-steam-forecaster-2026]]", "[[zukowski-next-fest-strategy|Zukowski Next Fest 분석]]", "[[peak|PEAK]]"]
created: 2026-05-18
updated: 2026-05-18
confidence: high
source_url: "https://newsletter.gamediscover.co/p/the-state-of-steam-wishlist-conversions"
source_author: "Simon Carless (GameDiscoverCo)"
source_published: 2025-10-17
---

**원문**: [newsletter.gamediscover.co](https://newsletter.gamediscover.co/p/the-state-of-steam-wishlist-conversions) — Simon Carless, GameDiscoverCo, 2025-10-17

GameDiscoverCo의 창업자 Simon Carless가 *GDCo Pro의 외부 추정 데이터*를 처음 macro-analysis로 공개. ZR Consulting Steam Forecaster가 인용한 wishlist conversion median 0.15× / >$10 0.10× / 10-20× variance 수치의 **1차 데이터 source**.

> 💡 **핵심 인사이트:** "Wishlist conversion 평균 X%"라는 단일 숫자는 *의미가 거의 없다*. 동일 카테고리 게임이 *10-20배 차이*로 분포한다. 의사결정에 쓰려면 *median + 분산*을 함께 보아야 하고, 자신의 게임이 분포 어디에 들어갈지는 *서브장르·co-op 여부·NSFW 여부·가격·content creator 활동* 등 multi-factor로 결정된다.

## 핵심 정량 (1차 데이터)

### Conversion median (2024-09 ~ 2025-09, >25k wishlist 게임)
| 필터 | Median conversion |
|---|---|
| All games (>25k wishlists) | **0.15×** |
| Adult 제외 | 0.14× |
| **>$10 게임만** | **0.10×** |

100,000 launch wishlist 게임 → median 10,000 Week-1 sales

### Variance
- 게임마다 **10-20× 차이** (10-20%가 아닌 *10-20배*)
- Top 20 best-seller는 모두 median (0.11× 기준) 상회
- Lowest top 20 outperformer: **InZOI 3.2×**
- Highest: **Revenge On Gold Diggers 539×** (Chinese FMV)
- **PEAK 266×** (co-op mountaineering)

### "Slipping over time" 가설 — 부정
- 2022년부터 'reviews in Week 1 vs Hype score' 추적
- 슬리핑 아님 — *경쟁 게임 수 증가*로 wishlist 자체 모으기가 어려워졌을 뿐

## Top Converters (6×+ median outperform)

가장 명확한 패턴: **online co-op crewlike**

| 게임 | Multiplier | 카테고리 |
|---|---|---|
| **PEAK** | **266×** | co-op mountaineering (viral) |
| **Mage Arena** | 78× | magic arena PvP |
| **R.E.P.O.** | 68× | high-retention co-op horror |
| **WEBFISHING** | 67× | chill, 작은 wishlist 시작 |
| **FlyKnight** | 18× | co-op friendly |
| **The Cabin Factory** | 16× | 호러, 소셜 비디오 발견 |
| **A Game About Digging A Hole** | 13× | 단순 hook + YouTube/Twitch |

추가 카테고리:
- **PC 스포츠 (NBA 2K26, EA Sports FC 25)**: 'casual'이 wishlist 없이 사러 옴
- **Single player social video 폭발**: 한 컨텐츠 크리에이터 발견이 시작점

## Under Converters (0.07× 부근부터)

평균 패턴 분석:
| 지표 | Under converter median | Top 20 select |
|---|---|---|
| Player review score (7 day) | **67% Mixed** | 91% Very Positive |
| Days on Steam before launch | **411 days** | 214 days |

함의:
- **Review score gating**: Mixed 67% = 매출 반토막 (Steam algorithm)
- **Stale wishlist**: 오래된 coming soon page는 organic wishlist rate 낮음 → 매수 의도 약화
- **Sequel 함정**: 큰 기대치 + 원작 deep discount = 신작 conversion 감소
- **"Boutique indie" 함정**: 'oh interesting' WL은 매수로 전환 안 됨

## ZR Forecaster 수치와의 차이 정정

| 항목 | ZR Forecaster (2026-05) 표기 | Carless 원전 (2025-10) |
|---|---|---|
| Median Week-1 conversion | 0.15× | **0.15×** ✓ |
| >$10 conversion | 0.10× | **0.10×** ✓ |
| Variance | 10× | **10-20×** (더 큼) |
| PEAK multiplier | 29× | **266×** (한 자릿수 차이!) |
| Mage Arena | 8.7× | **78×** |
| R.E.P.O. | 7.5× | **68×** |

> ⚠️ ZR Forecaster의 일부 outlier multiplier가 Carless 원전과 *한 자릿수* 차이. ZR이 다른 베이스라인 또는 시점 데이터를 인용했을 가능성. [[steam-revenue-forecasting]]·[[publisher-deal-structures]] 수치 *재검토 필요*.

## 데이터 caveat (Carless 본인 명시)

- "Wishlist conversion as some kind of reliable metric is **near-fatally flawed**"
- "We don't know. You don't know. If we did, we wouldn't be doing this for a living, etc."
- "Here's data to torture yourselves over in the meantime, while you ponder the ineffable complexity of it all"

## 위키 연결

- [[steam-revenue-forecasting|Steam 매출 예측 모델]] — 핵심 정량의 1차 source citation 승격
- [[launch-metrics|흥행 예측 지표]] — Under converter 패턴 (review score gating·411 days stale wishlist)
- [[game-pricing-strategy|게임 가격 전략]] — $10 threshold 1차 데이터
- [[zrconsulting-steam-forecaster-2026]] — 보조 layer (Carless가 원전, ZR이 인용·재구성)
- [[peak|PEAK]] — 266× outlier 사례 (29× 정정)
- [[zukowski-next-fest-strategy]] — 같은 산업 분석 사이클의 다른 source

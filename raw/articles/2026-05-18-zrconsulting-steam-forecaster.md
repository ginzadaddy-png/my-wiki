---
title: "Steam Revenue Forecaster — ZR Consulting"
source: "https://zrconsulting.de/steam-forecaster/"
author: "Zoran Roso (ZR Consulting, Munich)"
published: 2026-05
fetched: 2026-05-18
type: interactive-tool + methodology-doc
---

# Steam Revenue Forecaster — ZR Consulting

Forecast indie launch revenue · stress-test publisher offers. Free planning tool.
2026 benchmarks · European indie market focus · "Built for studios negotiating with publishers"

## 핵심 정량 모델

### 1) Wishlist conversion by sub-genre
- **Week-1 median: 0.15×** (15%) of wishlists convert to sales
- **Week-1 for games >$10: 0.10×** (33% drop)
- Variance ~10× from median in either direction
- 42 sub-genres × 12 parent families benchmarked separately
- Top breakouts (co-op horror): PEAK 29×, Mage Arena 8.7×, R.E.P.O. 7.5×
- Top genres by success rate (Zukowski 2024):
  - Open World Survival Craft 24.5%
  - Farming Sim 20.8%
  - Horror (leads absolute volume)
  - Idle/Incremental, Job Sims (top tier)
- Bottom: Match-3, 2D Platformer, traditional Visual Novel (single digits)

### 2) Review tier multipliers
| Tier | Multiplier |
|---|---|
| Negative | 0.25× |
| Mixed | 0.55× |
| Mostly Positive | 1.0× (baseline) |
| Very Positive | 1.15× |
| Overwhelmingly Positive | 1.4× |

Gates Steam discoverability at algorithm level. One-tier drop can halve year-1.

### 3) Pre-launch buzz multipliers
| Tier | Multiplier | Examples |
|---|---|---|
| None | 1.0× | quiet release |
| Some | 1.15× | |
| Building | 1.4× | |
| Strong | 1.8× | |
| Phenomenon | 2.5× | Hades · Vampire Survivors · Balatro (once-per-year) |

Compounds with both wishlist conversion *and* organic discovery (multiplicative).

### 4) Launch context lifts
- Demo at launch: +8% conversion
- Next Fest participation: +4% conversion + shifts more revenue into launch month
- Both compound with each other and with wishlist count

### 5) Organic / non-wishlist sales
- Range: 5-50% of wishlist sales (20% default)
- Compounds with buzz multiplier

### 6) Effective ARPU calculation
```
ARPU = list_price × (1 - regional_haircut) × (1 - blended_discount)
where blended_discount = launch_discount × 0.38 + seasonal_discount × 0.62
```

### 7) Regional pricing haircut
- Steam recommended matrix: $19.99 USD → ~$14 BR / ~$12 TR / ~$10 IN / ~$8 some SEA
- Blended haircut:
  - Globally-appealing games: 20-30%
  - US/EU-focused: 5-15%

### 8) Refund rate
- Steam average: 5-10% (7% default)
- Short games: 10-15%
- Long games: 3-7%

### 9) Steam revenue cut
- 30% up to $10M lifetime
- 25% $10M-$50M
- 20% above $50M
- Only 30% tier relevant for indies

### 10) Time distribution (Year 1)
- Launch month: ~38%
- Major lift at months 3 and 6 (Steam-wide sales)
- Year 2 add-on: +35% of Year 1 total

### 11) Post-launch wishlist conversion
- 0.7× of pre-launch rate (post-launch wishlist holders had weaker purchase intent at sign-up)
- Healthy launches add 50-200% of launch-day wishlist count over Year 1

## 8 Drivers — Sensitivity Ranking (Tornado Chart)

순서: 게임마다 다르지만 보통 다음 순서로 영향력 높음
1. **Wishlists at launch** — 가장 통제 가능한 단일 lever (±40% 범위)
2. **Post-launch wishlists** — 발매 후 추가, 0.7× conversion
3. **Pre-launch buzz** — 멀티플리커, 1.0×~2.5×
4. **Review score** — discoverability gate, 한 tier drop = 매출 반토막
5. **Price** — 더 비싸게 받기 vs conversion 감소 trade-off
6. **Refund rate** — short games에서 특히 critical
7. **Organic / non-wishlist** — store discovery, sale events
8. **Seasonal discounts** — sale 참여 vs ARPU 보존 trade-off
9. **Launch discount** — 10% standard, 20%+ = 약세 신호 (algorithmically)
10. **Regional pricing** — 거의 inherited
11. **Demo + Next Fest** — 가장 cheap한 revenue boost

## Publisher Deal Structures (Stress Test)

### 1. Self-published (baseline)
- 100% post-Steam to studio (= 70% gross)
- Studio handles marketing, PR, store ops

### 2. Standard rev share (30%)
- 70/30 split post-Steam
- Publisher provides marketing + ops support

### 3. Aggressive rev share (50%)
- 50/50 split post-Steam
- Higher publisher contribution expected

### 4. Recoup-first
- 100% to publisher until defined amount recouped
- After recoup: split kicks in
- Risk: never recoup = 0 to dev

### 5. MG against royalty
- Upfront Minimum Guarantee paid to dev
- Publisher recoups from royalties before paying further
- Dev keeps MG regardless → safest for dev cashflow

### 6. Marketing fee deal
- Fixed marketing fee off top
- Then rev share kicks in
- Risk: low-sale game = fee eats majority

## Sources cited (1차 데이터)
1. **GameDiscoverCo 2025-10 wishlist study** (Simon Carless) — newsletter.gamediscover.co
2. **Chris Zukowski annual indie success breakdowns** — howtomarketagame.com
3. **GameDiscoverCo June 2025 single-tag taxonomy** — Steam games >$1M revenue
4. **VG Insights · Gamalytic** — public estimates cross-check
5. **Valve official revenue share tier table** — partner.steamgames.com
6. **Steam refund policy** — store.steampowered.com/steam_refunds
7. **Steam regional pricing matrix** — partner.steamgames.com pricing/currencies

## Calibrated estimates (ZR 자체 추정 — high → medium confidence)

다음은 ZR이 publicly available data + own modeling으로 *보정한* 값. 1차 데이터셋이 아님:
- Buzz tier multipliers (1.0×~2.5×)
- Demo conversion lift (+8%)
- Next Fest lift (+4%)
- Post-launch wishlist conversion ratio (0.7)
- Year-1 launch month share (38%)
- Year-2 add-on (+35%)
- Organic / non-wishlist range (5-50%)
- Community growth bands (5/15/35% per month)
- Reach grade bands (trailer/creator/press weights)
- Playtest → review tier · refund mapping

## Calibration → Forecaster mapping

각 입력 신호가 forecaster 어느 input으로 매핑되는지:
- **Buzz tier** ← max of (trajectory velocity, demo conv+uplift, community growth, combined reach)
- **Review tier** ← avg of (demo review %, playtest reception)
- **Wishlists at launch** ← trajectory projection (preferred) or demo wishlist-after fallback
- **Post-launch wishlists** ← max of (trajectory monthly velocity × 3-12 months) or (demo delta × 0.5-4×)
- **Refund rate** ← playtest completion tier mapping (15% / 10% / 7% / 5%)

## ZR Consulting 정보
- 위치: Munich, Germany (Christophstr. 5, 80538 München)
- 대표: Zoran Roso (Geschäftsführer)
- 경력: 25년 게임 산업 (Publishing · Marketing · Business development)
- 포커스: DACH + Central Europe 인디 publishing 협상

## Methodology disclaimers
- "Calibration grades and forecast suggestions are planning estimates derived from publicly-available indie launch benchmarks"
- "Treat as a decision-support tool, not a prediction"
- "Specific games can deviate 30-50% from these projections due to factors no model can capture (press cycle, viral moments, genre saturation, marketing execution)"

## 위키 연결 가능 페이지
- launch-metrics (sub-genre conversion·refund·buzz·time distribution)
- game-pricing-strategy ($10 threshold, regional haircut)
- marketing-strategy (demo·Next Fest lift, 8-driver sensitivity)
- indie-business-strategy (break-even, publisher deal stress test)
- zukowski-next-fest-strategy (같은 데이터 소스, 정량 모델 추가)
- steam-next-fest-2026-analysis
- early-access-strategy (playtest cohort → review/refund prediction)
- peak (PEAK 29× co-op horror outlier 사례)

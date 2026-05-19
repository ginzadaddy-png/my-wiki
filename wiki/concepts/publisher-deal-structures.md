---
title: "퍼블리셔 딜 구조 (Publisher Deal Structures)"
type: concept
sources: ["[[zrconsulting-steam-forecaster-2026]]", "[[vincke-bg3-ea]]", "[[kasavin-hades-ea]]"]
related: ["[[indie-business-strategy|인디 비즈니스 전략]]", "[[steam-revenue-forecasting|Steam 매출 예측 모델]]", "[[early-access-strategy|얼리 액세스 전략]]", "[[marketing-strategy|마케팅 전략]]"]
created: 2026-05-18
updated: 2026-05-18
confidence: medium
---

**퍼블리셔 딜 구조**는 인디·중소 스튜디오가 퍼블리셔와 협상할 때 마주치는 *5가지 표준 구조*와 각 구조가 cashflow·리스크·EV에 미치는 영향을 다룬다. 어느 구조가 "좋은 deal"인지는 *프로젝트 매출 분포·dev 캐시 여력·퍼블리셔 기여도*에 따라 다르다. ZR Consulting이 DACH·Central Europe 인디 publishing 협상 경험에서 정리한 4종 + self-publish baseline 모델을 기반으로 한다.

> 💡 **핵심 인사이트:** 동일한 퍼블리셔 제안이 *기대 매출 분포*에 따라 정반대 의미가 된다. 매출이 base case에 가깝게 분포한 게임에 *Recoup-first*는 dev에게 매우 불리하지만, downside 시나리오가 두꺼운 게임에 *MG against royalty*는 가장 안전한 옵션이다. 단순 % 비교가 아니라 *각 구조를 자신의 [[steam-revenue-forecasting|예측 모델]] downside/base/upside 시나리오에 stress-test* 해야 한다.

## 5가지 표준 구조

### 1. Self-published (baseline)
- **메커니즘**: Steam 30% cut만 떼고 100% dev. dev = 70% gross
- **dev 부담**: 마케팅·PR·store ops·QA·로컬라이제이션·플랫폼 출시·CS 전부
- **Cash flow**: 출시 후 1~2주 단위로 Steam → dev (대형 cashflow positive 가능)
- **언제 적합**: 마케팅 capacity 보유 + 충분한 런웨이 + 자체 IP

### 2. Standard rev share (30%)
- **메커니즘**: post-Steam 70/30 split (퍼블리셔 30%) → dev 49% gross
- **퍼블리셔 기여**: 마케팅 예산·PR·store 운영·creator outreach·플랫폼 관계
- **언제 적합**: dev 마케팅 capacity 부족 + 퍼블리셔의 audience reach가 명확한 가치
- **딜의 함정**: rev share %가 *유일한 비용*인 것처럼 보이지만 marketing fee·platform expense를 별도 청구할 수 있음

### 3. Aggressive rev share (50%)
- **메커니즘**: post-Steam 50/50 split → dev 35% gross
- **퍼블리셔 기여 요구**: 단순 마케팅이 아닌 *큰 비중의 capacity* — 개발 자금 일부, 글로벌 로컬라이제이션, console porting, 콘솔 퍼블리싱
- **언제 적합**: dev가 개발 자금·콘솔 publish capacity 부족 + 퍼블리셔가 *실질적 위험*을 분담
- **위험**: rev share %만 보면 dev는 매출 1/3만 가져가는 셈

### 4. Recoup-first
- **메커니즘**: 모든 post-Steam 매출이 *퍼블리셔에 먼저* 흘러감 → 약속된 recoup 금액 도달 후 split 발동
- **퍼블리셔 기여**: 개발 자금 직접 투자 + 마케팅·PR
- **위험 ① — dev**: 게임 매출이 recoup 금액 미달 시 dev가 받는 게 0 또는 미미. *런치 매출 분포 downside 시나리오를 명시적으로 점검* 필요
- **위험 ② — 퍼블리셔**: 매출 부진 시 자체 손실. 퍼블리셔도 자기 베팅 모델
- **언제 적합**: dev가 개발 자금이 없고 게임 매출 가능성이 매우 높을 때

### 5. MG against royalty (Minimum Guarantee)
- **메커니즘**: 계약 즉시 dev에 정해진 MG 지급 → 이후 royalty가 발생할 때마다 퍼블리셔가 *MG를 recoup* → recoup 끝나면 split 발동
- **핵심 차이**: dev는 *MG를 무조건 keep* (게임이 실패해도 반환 없음)
- **dev cashflow 가장 안전**: upfront cash + downside protection
- **퍼블리셔 위험**: dev가 MG만 챙기고 매출 부진 시 그 손실은 퍼블리셔
- **언제 적합**: dev cashflow 보강이 우선 순위일 때, 매출 불확실성이 클 때

### 6. Marketing fee deal
- **메커니즘**: 매출 발생 시 *고정 marketing fee를 먼저 떼고* 나머지에 rev share 적용
- **위험**: 저매출 시 marketing fee가 매출의 큰 비중 차지. 매출이 적게 나오면 dev 0
- **언제 적합**: 매출 base case가 충분히 큰 게임 + 퍼블리셔의 마케팅 capacity가 압도적 가치를 줄 때

## 4종 stress test 비교 ([[zrconsulting-steam-forecaster-2026]] 모델)

ZR Forecaster의 stress test는 각 구조를 *base case·downside·upside* 시나리오에 적용하여 dev 측 Year-1 net을 비교한다.

| 구조 | Downside 시나리오 | Base case | Upside 시나리오 |
|---|---|---|---|
| Self-published | 매출 작아도 70% gross 유지 | 표준 | 가장 큰 upside (100% post-Steam 모두 dev) |
| Standard 30% | 49% gross — 안정적 | 평균 | upside 일부 sacrifice |
| Aggressive 50% | 35% gross — dev 위험 | 평균 | upside 절반 sacrifice |
| Recoup-first | **0에 가까움 (위험 최대)** | recoup 후 split | recoup 빠르면 적정 split |
| MG against royalty | **MG = dev floor (보호됨)** | MG 후 split | MG가 작아 보임 |
| Marketing fee | **fee가 매출 잠식 (위험)** | 평균 | fee 비중 작아짐 |

> ⚠️ Recoup-first vs MG against royalty는 *외형은 비슷*하지만 dev 입장에서 정반대. Recoup-first는 *dev가 0부터 시작해 recoup 후 split*, MG는 *dev가 MG로 시작해 publisher가 recoup*. Cashflow·downside protection 차이가 결정적.

## 협상 시 점검 항목

[[zrconsulting-steam-forecaster-2026|ZR Forecaster]] 에서 명시한 dev 측 자가 진단:

1. **매출 분포 추정**: [[steam-revenue-forecasting|예측 모델]]의 downside·base·upside 3 시나리오에 각 deal 적용
2. **Break-even 시점**: production budget을 dev share로 회수하기까지 몇 카피 필요한가
3. **퍼블리셔 기여의 *실질* 가치**: 마케팅 capacity·플랫폼 관계·로컬라이제이션·콘솔 publish — 어느 것이 *dev에게 정말 부족한 것*인가
4. **자금 압박 상황**: dev cashflow가 *지금* 필요한가 vs 1~2년 후 매출이면 충분한가 → MG vs Recoup vs Self-publish 갈림
5. **창의적 통제권**: 일부 deal은 콘텐츠·출시일·플랫폼 결정권을 퍼블리셔에 양도

## Self-publish 모델 사례

성공한 self-publish 사례는 매출 분포에 대한 확신 + 자체 마케팅 capacity가 있는 경우:
- **[[balatro|Balatro]]** — Playstack 퍼블리셔이지만 LocalThunk 단독 개발 + 단순 marketing fee 구조
- **[[fromsoftware|FromSoftware]]** — Bandai Namco를 퍼블리싱 파트너로 두지만 대규모 IP 자산 보유로 협상력 우위
- **[[supergiant-games|Supergiant Games]]** — *완전 self-publish*. Pyre·Hades·Hades 2 자체 출시. 노 크런치·이직률 0% 유지 가능한 사이즈
- **[[hazelight-studios|Hazelight Studios]]** — EA 퍼블리셔이지만 *Friend Pass* 같은 자체 비즈니스 모델 통합

## EA 기반 점진 매출 — 별도 분기

[[early-access-strategy|얼리 액세스 전략]]은 publisher deal과 직교하는 매출 구조. EA로 매출 검증 후 1.0 출시 시 협상력이 달라짐:
- **[[larian-studios|Larian]]** BG3: 3년 EA로 250만 카피 + 시장 검증 → 1.0 자체 출시 협상력
- **[[supergiant-games|Supergiant]]** Hades: EA "파일럿 에피소드" 모델로 매월 캐릭터·관계 학습 → 1.0 정식 출시 시 publisher 없이 가능
- **[[iron-gate-studio|Iron Gate]]** Valheim: EA 단계로 5인 팀이 ~1,500만 카피 → publisher 협상력 압도

EA 매출이 있는 상태에서의 publisher 협상은 *recoup-first*나 *MG*보다 *standard rev share* 또는 *marketing fee* 쪽으로 기우는 것이 일반적.

## 위키 연결

- [[indie-business-strategy|인디 비즈니스 전략]] — 인디 창업·생존·자금조달 맥락
- [[steam-revenue-forecasting|Steam 매출 예측 모델]] — stress test의 input
- [[early-access-strategy|얼리 액세스 전략]] — EA가 협상력에 미치는 영향
- [[marketing-strategy|마케팅 전략]] — 퍼블리셔 기여의 실질 가치 평가

## 한계 및 적용 주의

- ZR Forecaster의 stress test는 *Year-1 매출* 기준. 장기 ([[catalog-economics|카탈로그 이코노믹스]]) 관점 별도
- 동일 구조라도 *세부 조항*(territory·platform·콘텐츠 통제·기간·옵션·sequel 권리)에 따라 deal value 변동 큼
- DACH·Central Europe 시장 기준. 일본·한국 publisher 시장은 별도 분석 필요

## 추가 조사 주제
- 한국·일본 인디 퍼블리싱 시장의 deal 구조 — Nexon·NetEase·Kakao Games 등 vs DACH 시장 비교
- Console publish 권리만 분리한 hybrid deal (PC self-publish + console partner)
- IP·sequel 권리 조항이 dev에 미치는 장기 가치
- 신규 EA·F2P 게임의 publisher 의존도 변화 — [[helldivers-2|Helldivers 2]] (Sony) vs [[arc-raiders|Arc Raiders]] (Nexon 자회사)

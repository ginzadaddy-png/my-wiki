---
title: "Valve"
type: entity
sources: ["[[zrconsulting-steam-forecaster-2026]]", "[[carless-wishlist-conversions-2025-10]]", "[[gdc25-steam-new-rules]]", "[[steam-next-fest-2026-analysis]]", "[[gdc24-steam-secrets]]", "[[carless-steam-fans-ai-sentiment-2026-07]]"]
related: ["[[steam-revenue-forecasting|스팀 매출 예측]]", "[[steam-next-fest|Steam Next Fest]]", "[[marketing-strategy|마케팅 전략]]", "[[launch-metrics|런치 메트릭]]", "[[publisher-deal-structures|퍼블리셔 딜 구조]]", "[[game-pricing-strategy|가격 전략]]", "[[game-market-trends|시장 구조 변화]]"]
created: 2026-05-26
updated: 2026-08-03
confidence: high
---

미국 워싱턴 벨뷰 기반의 비공개 게임·소프트웨어 회사. **Steam**(2003~) 운영자이자 PC 게임 유통의 사실상 표준을 만든 사업체. 게임 개발사로도 활동(Half-Life·Portal·Counter-Strike·Dota 2·Half-Life: Alyx) 하지만, 위키에서 다루는 비중은 *플랫폼 사업자* 측면이 압도적.

## 기본 정보

- **설립**: 1996년 (Gabe Newell, Mike Harrington — 마이크로소프트 출신)
- **본사**: 미국 워싱턴 벨뷰
- **사업**: Steam 플랫폼 운영, Source / Source 2 엔진, 자체 게임 개발, Steam Deck 하드웨어
- **수수료 구조**: 매출 기준 30% (~\$10M 이상 25%, \$50M 이상 20%) — [[publisher-deal-structures|퍼블리셔 딜 구조]]에서 self-publish 시 인디에게 가장 중요한 변수
- **비공개 기업**: IPO 없음, 외부 보고 의무 없음 → 위키 분석은 *외부 관찰·1차 source 분석*에 의존
- **동시접속자(CCU)**: 2025년 처음 4,000만 명 돌파 → 2026-01-11 4,204만 최고 기록, 이후 4,230만 (2020년 대비 ~2배)
- **시장 배경**: PC·콘솔 매출 +13%·다운로드 +6% 성장 — 다운로드 감소·매출 +1%대 정체인 모바일과 대조 (*AB180 'Game UA 2026' 세미나, 2026-06*)

### MAU 규모 — 수치 계보와 채택 기준

Valve는 비공개 기업이라 **헤드라인 MAU를 2021년 이후 공표하지 않았다.** 위키에서 쓰는 숫자는 반드시 계보를 밝혀야 한다.

| 수치 | 성격 | 시점 | 출처·산출 |
|---|---|---|---|
| **1.32억 MAU** (DAU 6,900만, 피크 CCU 2,740만) | **Valve 공식** | **2021** | Steam Year in Review 2021 — *마지막 공식 헤드라인 수치* |
| **3,110만 EU MAU** | **Valve 공식(법적 의무 공시)** | **H2 2025** | EU 디지털서비스법(DSA) 이용자 수 공시 — *현존하는 유일한 최신 공식 숫자* |
| **약 1.98억 글로벌 MAU** → 2026 상반기 2억+ | 1차 추정 | H2 2025 → H1 2026 | [[carless-steam-fans-ai-sentiment-2026-07]] — DSA 3,110만 × Steam 공개 대역폭 분포로 유럽 비중 역산, 2021 기준선 성장률 대입으로 교차 확인 |
| 약 1.4억 (+11%) | **채택 철회** | "2025"로 유통 | 통계 애그리게이터 계보 — Valve의 **2021년 1.32억을 최신치로 오표기한 뒤 성장률을 얹은 값** |

> 💡 **핵심 인사이트 — 1.4억은 왜 틀렸나:** 이 수치를 싣는 애그리게이터들은 DAU를 *6,900만*으로 함께 적는데, 이는 Valve의 **2021년 Year in Review 수치 그대로다.** 즉 1.32억 → "2024년치"로 오표기 → +11% → "2025년 1.4~1.47억"이라는 한 갈래에서 나온 파생값이며, *2025년에 측정된 값이 아니다.* AB180 세미나 인용도 이 계보 위에 있다.

**독립 검증 (CCU 비율)**: 2021년 MAU 1.32억 ÷ 피크 CCU 2,740만 = **4.8배**. 이 비율을 2026-01 피크 CCU 4,204만에 대입하면 **약 2.02억** — Carless 추정과 일치하고, 1.4억(비율 3.3배로 급락해야 성립)과는 맞지 않는다.

> **위키 채택 기준**: ① 하드 숫자가 필요하면 **3,110만 EU MAU (H2 2025, 공식)** 를 쓴다. ② 글로벌 규모는 **약 2억 (2026 상반기, Carless 추정)** 으로 쓰되 *추정임을 반드시 병기*한다. ③ 1.4억은 사용하지 않는다.

**규모 비교 기준점**: 소니 공식 PSN MAU **1.25억** (2026-03 기준, Q1 실적) → Steam이 PSN 대비 약 **60% 크다**. [[game-market-trends|시장 구조]]에서 "PC 우위 전환"을 말할 때의 정량 근거.

## 위키에서 Valve를 다루는 4개 축

### 1. 플랫폼 알고리즘 ([[launch-metrics]] · [[steam-next-fest]])

- **2024-10 ML 알고리즘 전환**: 머신러닝 기반 가시성 알고리즘 도입. 이후 "낭비된 노출" 정밀화 — Crashlands 2 (2024-06, 624만 노출 → 15,987 위시리스트) vs How Many Dudes? (2026-02, 64만 노출 → 14,740 위시리스트). *노출 1/10이지만 위시리스트는 거의 같음*
- **"no black marks" 공식 입장**: 과거 부진을 처벌하지 않음, 매출만 본다. 다만 [[zukowski-bad-launch-recovery-2024|Zukowski 분석]]은 회복률 0.156%로 *실질적 처벌 효과*를 측정

### 2. Steam Next Fest 운영자 ([[steam-next-fest]])

분기별 무료 데모 페스티벌. 인디·중소 스튜디오 출시 마케팅 캘린더의 *피크 이벤트*. 2024-10 "open to everyone" 알고리즘 도입 → 게임 3,000개 폭증으로 *전 등급 동반 하락* → 2025-02 재보정으로 상위 등급 회복.

### 3. 매출 데이터 1차 출처 ([[steam-revenue-forecasting]])

[[carless-wishlist-conversions-2025-10|Carless wishlist conversions]]·[[zukowski-2025-year-review|Zukowski 2025 retro]] 등 1차 분석이 Valve 공개 데이터·SteamDB·GameDiscoverCo crawl에 의존. 위키 매출 분석의 *원천*이자 *접근 제한 데이터*의 게이트키퍼.

### 4. 가격 정책 인프라 ([[game-pricing-strategy]])

지역 가격 가이드라인, 세일 캘린더, \$10 단절선(0.15× → 0.10× conversion), regional haircut — 모두 Valve의 플랫폼 룰이 인디 비즈니스 의사결정의 *바운더리 컨디션*을 정의.

## 게임 개발사로서의 Valve (현재 위키 비중 낮음)

Half-Life 시리즈·Portal·Counter-Strike(원작자 인수)·Team Fortress·Dota 2·Left 4 Dead·Half-Life: Alyx(VR)·Deadlock(2024 클로즈 베타). 자체 게임 개발은 *불규칙적*이며 *사내 평면 조직 구조*로 알려져 있음 — 직원 자율 프로젝트 선택. 위키는 *플랫폼 측면* 우선 다루며, 게임 개발 케이스는 향후 보강 대상.

> 💡 **핵심 인사이트:** Valve는 위키 내 *플랫폼 단일 게이트키퍼*. 인디 비즈니스 분석의 거의 모든 *바운더리 컨디션*(수수료·가시성·세일·지역 가격·refund) 출처가 Valve로 수렴. 그래서 동등한 비중의 entity가 없음 — Epic Games Store·GOG 페이지가 신규 생성되면 *비교 페이지* 가능.

## 추가 조사 주제

- Valve 사내 *평면 조직* 모델 — [[dev-org-structure|개발 조직 구조]]에서 다른 모델과 비교
- Steam Deck 하드웨어 전략이 PC 게임 시장 구조에 미치는 영향
- 2024-10 ML 알고리즘 전환의 *알고리즘 reverse engineering* 시도 — [[zukowski-next-fest-strategy|Zukowski Next Fest 전략]] 등이 부분 추론

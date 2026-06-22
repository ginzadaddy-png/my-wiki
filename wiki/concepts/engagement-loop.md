---
title: "인게이지먼트 루프"
type: concept
sources: []
related: ["[[player-retention|플레이어 리텐션]]", "[[live-service-design|라이브 서비스 설계]]", "[[player-trust-design|플레이어 신뢰 설계]]", "[[mda-framework|MDA 프레임워크]]", "[[game-balance|게임 밸런싱]]", "[[mobile-gamedev|모바일 게임 개발]]"]
created: 2026-06-22
updated: 2026-06-22
confidence: medium
---

플레이어가 행동→피드백→재동기 부여를 반복하며 계속 플레이하게 만드는 순환 구조. 지표 측면은 [[player-retention|플레이어 리텐션]], 운영 케이던스는 [[live-service-design|라이브 서비스 설계]]와 짝을 이룬다.

## 루프의 이론적 토대

**Daniel Cook "Loops and Arcs"(2012)** — 루프는 *정신모델(mental model) → 행동(action) → 게임 시스템 → 피드백 → 정신모델 갱신*의 순환(스킬 아톰, skill atom)이며, **프랙탈(fractal)**하게 여러 빈도·레벨에서 중첩된다. 일회성으로 소비되는 **아크(arc)**(내러티브·컷신)와 대비된다. (출처: [lostgarden.com](https://lostgarden.com/2012/04/30/loops-and-arcs/))

> ⚠️ 단, "루프=리텐션 / 아크=소진"식 강한 인과 단정은 적대 검증에서 기각(0-3)됨. 루프·아크는 *분석 렌즈*이지 리텐션 결정론이 아니다 — 내러티브 중심 게임도 재플레이를 유발한다.

## 3계층 네스팅

| 계층 | 시간축 | 예 | 역할 |
|---|---|---|---|
| core | 초·분 | 조준→사격→재장전 | 재미(순간) |
| mid | 세션 | 미션·스테이지 | 세션 완결감 |
| meta | 다세션 | 레벨업·시즌패스·컬렉션 | 지속성(재방문) |

짧은 루프의 출력이 긴 루프의 입력이 된다. core가 재미를, meta가 지속성을 담당.

## 행동심리학 기제

- **John Hopson "Behavioral Game Design"(2001)** — Skinner 강화 스케줄을 게임에 적용한 토대 문헌. 'contingency' = 보상이 주어지는 시점을 규율하는 규칙. (출처: [gamedeveloper.com](https://www.gamedeveloper.com/design/behavioral-game-design))
- **변동비율(variable ratio)** 강화는 가장 높은 전반적 활동률을 산출하고 고정 스케줄의 "보상 후 멈춤"이 적다 → 가챠·루트박스의 행동학적 근거. *단 Hopson 본인이 "가장 높은 율 ≠ 최선의 디자인"이라 단서를 달았고, 비율이 커지면 멈춤도 증가한다.*
- **Nir Eyal Hook 모델**(*Hooked*, 2014) — 트리거(외부/내부)→행동→가변보상→투자(매몰비용)의 4단계 순환으로 습관 형성. (출처: [nirandfar.com](https://www.nirandfar.com/how-to-manufacture-desire/)). 보상 예측·갈망의 신경과학 근거는 Schultz의 보상 예측 오차(reward prediction error)로 인용되나, "도파민=쾌락 화학물질" 등식은 과잉단순화.

## 라이브서비스 케이던스

- **배틀패스 기원**: Valve **Dota 2 Compendium(2013, The International)** → Epic **Fortnite 배틀패스(Season 2, 2017-12 출시 · 2018 대중화)**로 표준화. (출처: [Wikipedia·PC Gamer](https://en.wikipedia.org/wiki/Battle_pass)) — 스캐폴드의 "Fortnite 시즌2(2018)"는 출시 시점 2017-12로 정정.
- 레이어: 일일 로그인 → 주간 미션 → 한정 이벤트(LTE) → 시즌(통상 분기) → 연례 tentpole. 예측 가능한 리듬(습관) + 한정성(스파이크) 병행. (※ "표준 시즌 9–13주"는 본 검증 라운드 미확인 — 추정)

## 윤리적 vs 약탈적 — 경계선

- **게임 다크패턴 3분류** (Zagal·Björk·Lewis, FDG 2013): **시간형(Temporal) / 금전형(Monetary) / 사회적 자본형(Social Capital-Based)**. ⚠️ 스캐폴드의 "심리형"은 오기 — 원 논문 세 번째 범주는 *사회적 자본형*(데일리 로그인 강요·소셜 피라미드). '심리형'은 후속 문헌(Karlsen 2019 등)이 추가한 차원.
- **규제 사례** — FTC가 Epic Games에 총 **$520M**($275M COPPA 벌금 + $245M 다크패턴 환불, 2022-12) 부과, "dark patterns"를 공식 명시. ([FTC 보도자료](https://www.ftc.gov/news-events/news/press-releases/2022/12/fortnite-video-game-maker-epic-games-pay-more-half-billion-dollars-over-ftc-allegations))
- **루트박스 규제 분기**(양측 병기): **벨기에(2018)** — 신법이 아니라 기존 도박법 *재해석*, 실효성 낮음(상위 iPhone 게임 82.0%가 여전히 운영, Xiao 2023). **영국 DCMS** — 도박 *불분류* 유지(자율규제, 조건부).
- **WHO ICD-11 게이밍 장애(6C51**, 2022-01-01 발효) = 통제력 손상·우선순위 증가·부정적 결과에도 지속의 *행동* 기준(시간량 아님) ↔ **Aarseth et al.(2017, 33인)** 반론: 근거 부족·정상 게이머 위양성·낙인·도덕적 공황 → 학계 미해결. WHO 채택 입장과 반론을 *병기*해야 함.

## 비약탈적 모범

[[helldivers-2|헬다이버스 2]] Warbond — 기간 만료 없음 + 프리미엄 재화 인게임 획득 가능. [[player-trust-design|플레이어 신뢰]]를 소비하지 않는 루프 설계의 사례축. ([[live-service-design|라이브 서비스 설계]]의 "비약탈적 모델의 기준" 참조)

> 💡 **핵심 인사이트:** 좋은 루프는 매 회전마다 새 패턴을 *학습*시킨다(Koster). 학습이 멈추면 재미가 죽고 **컴펄전(강박)만** 남는다 — 이 지점이 *윤리적 인게이지먼트(내재 동기)* vs *약탈적 컴펄전(보상 스케줄 착취)*의 경계선이다.

---

*본 페이지 이론·인용·규제 수치는 deep-research로 1차 출처 검증(2026-06). 분석사 추정·규제 현황은 변동 시 갱신 대상.*

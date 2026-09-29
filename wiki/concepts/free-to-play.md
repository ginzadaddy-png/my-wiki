---
title: "F2P·부분유료 모델"
type: concept
sources: ["[[missing-middle-paradigm-shift-2026]]", "[[gdc26-arc-raiders-reset]]", "[[ign-generations-in-play-2026]]", "[[newzoo-pc-console-2026]]", "[[gi-newzoo-ggmr-2026-release-2026-09]]", "[[gdc26-rules-of-the-game]]", "[[alinea-steam-dlc-attach-rates-2026-05]]", "[[roblox-retention-algorithm-tradeoff-2026-08]]", "[[bain-gaming-report-2026]]"]
related: ["[[live-service-design|라이브 서비스 설계]]", "[[game-pricing-strategy|게임 가격 전략]]", "[[mid-price-sweet-spot|중가 프리미엄 스위트스폿]]", "[[player-trust-design|플레이어 신뢰 설계]]", "[[engagement-loop|인게이지먼트 루프]]", "[[webshop-direct-monetization|웹샵·D2C 직접 수익화]]", "[[subscription-economy-gaming|구독 경제]]", "[[mmorpg|MMO·MMORPG]]", "[[arc-raiders|아크 레이더스]]", "[[marathon|Marathon]]", "[[fortnite|Fortnite]]", "[[genshin-impact|원신]]"]
created: 2026-09-29
updated: 2026-09-29
confidence: medium
---

**F2P(부분유료)**는 게임 자체는 무료로 열고, 게임 안에서 파는 것 — 배틀패스·가챠·외형·재화 — 으로 돈을 버는 모델이다. 위키 46개 파일이 이 말을 쓰는데 정작 모델 자체를 다루는 페이지가 없어, 흩어진 언급을 여기로 모은다.

> 💡 **핵심 인사이트 — 위키의 F2P 근거는 한쪽으로 기울어 있다.** 가장 자세한 서술은 *F2P를 떠난 사례*(아크 레이더스·마라톤)와 *F2P가 쌓은 불신*이다. F2P를 운영해 크게 성공한 쪽(포트나이트·원신·LoL·Apex)은 엔티티 프로필과 외부 추정 매출로만 남아 있다. 그래서 이 페이지는 "F2P를 어떻게 설계하나"보다 **"프리미엄 개발사가 F2P를 고를 때 무엇을 따져야 하나"**에 가깝다.

## 무엇을 파는가

| 장치 | 위키 사례 | 페이지 |
|---|---|---|
| 배틀패스 | Dota 2 Compendium(2013)에서 시작해 포트나이트(2017-12)가 표준으로 만듦 | [[engagement-loop]] · [[fortnite]] |
| 가챠 | 원신 — 90연 천장·50/50, 과금은 캐릭터·무기로 한정하고 메인 스토리는 전부 무료 | [[genshin-impact]] |
| 외형·재화 | 포트나이트 V-Bucks, Apex 팩(외형 가챠), LoL 스킨 | [[apex-legends]] · [[league-of-legends]] |
| 웹샵 직판 | 모바일 D2C 약 \$17B — 모바일 인앱 결제의 약 15% | [[webshop-direct-monetization]] |

가챠·루트박스가 잘 먹히는 행동학적 근거로는 *변동비율 강화*(보상이 언제 나올지 모를 때 활동률이 가장 높다)가 인용된다. 다만 이 개념을 게임 설계에 적용한 Hopson 본인이 *"가장 높은 활동률이 최선의 디자인은 아니다"*라고 단서를 달았다 ([[engagement-loop|인게이지먼트 루프]]).

**운영하는 쪽의 네 가지 모양** — 위키 엔티티 페이지들이 서로 비교해 둔 것이다.

- [[epic-games|Epic]] 포트나이트 — F2P 배틀로얄 + 플랫폼(UEFN). 2018년 매출 \$5.4B
- [[hoyoverse|HoYoverse]] 원신 — 가챠 + 크로스플랫폼
- [[riot-games|Riot]] LoL — F2P MOBA + 트랜스미디어
- [[respawn-entertainment|Respawn]] Apex — F2P 배틀로얄 + 싱글플레이 AAA를 한 스튜디오에서 함께 운영
- 한국 MMO(넥슨·엔씨)의 아이템 과금은 [[mmorpg|MMO·MMORPG]]에서 따로 다룬다

## 떠나는 쪽 — 프리미엄으로 돌아선 두 사례

**[[arc-raiders|아크 레이더스]]**는 F2P 코옵 슈터로 기획했다가 \$40 프리미엄으로 바꿨다. 이유는 설계였다 — *"F2P 구조에서는 크래프팅 타이머와 노가다가 불가피하다. 유저의 시간을 기만하는 것이다"*(디자인 디렉터 Virgil Watkins). 결과는 1,400만 장·동접 96만이었고, 이후 매달 약 30%씩 빠져 4월에는 최고점 대비 −80%가 됐다 ([[live-service-design|라이브 서비스 설계]]).

**[[marathon|Marathon]]**도 F2P 계획을 접고 \$39.99로 냈다. 여기에는 드문 숫자가 남았다 — 무료 테스트(Server Slam) 최고 동접 **143,621명**, 유료 출시 후 최고 동접 **88,337명**. 돈을 받기 시작하자 최고 동접이 약 39% 낮아졌다.

> 💡 두 사례가 말하는 것 — **과금 모델은 가격표가 아니라 설계 제약이다.** F2P는 팔 자리를 만들기 위해 루프에 일부러 마찰(대기·반복)을 넣게 만든다. 프리미엄으로 바꾸면 그 마찰을 지울 수 있지만, 대신 *들어오는 문*에 문턱이 생긴다. 아크 레이더스는 마찰을 지운 쪽의 편익을, 마라톤은 문턱의 비용을 보여준다. 어느 쪽이 더 큰지는 장르와 관객이 정한다.

## 불신 — 장르 전체가 진 빚

- **레이블 자체가 신뢰 적자**다. F2P라는 말만으로 같은 장르의 다른 게임이 쌓아 온 불신을 물려받는다 ([[player-trust-design|플레이어 신뢰 설계]] · [[gdc26-rules-of-the-game]])
- **반대 방향으로도 번진다.** Ravenswatch: Merlin은 프리미엄 게임에, 이미 외형 DLC를 팔던 위에, *플레이 가능한 캐릭터*를 유료로 얹었다. 오디언스는 이를 *"F2P에 맞는 모델"*로 읽었고, DLC 부속 판매율은 9%로 비교군 아래쪽이었다 ([[alinea-steam-dlc-attach-rates-2026-05]])
- **피로의 원인**으로 위키가 꼽는 것은 기간 한정 배틀패스(FOMO)·인위적 대기 시간·기계적인 이벤트 달력이다 ([[live-service-design]])
- **약탈하지 않는 쪽의 비용**: Roblox가 추천 기준을 *시간당 매출*에서 *장기 잔존*으로 바꾸자 수익화가 가이던스보다 2% 모자랐고, 다음 분기 부킹 전망은 전년 대비 14–18% 감소로 잡혔다. 편익은 오래 걸려 오고 비용은 분기 단위로 먼저 온다 ([[roblox-retention-algorithm-tradeoff-2026-08]])

## 누가 F2P로 들어오나 — 세대

| 접근 방식 | Gen X | Millennials | Gen Z |
|---|---|---|---|
| F2P | 30% | 32% | **46%** |
| 구독 | 33% | 29% | 21% |
| 정가 구매 | 42% | 38% | **20%** |

IGN 조사는 이 차이를 *의지의 신호*로 읽는다 — 정가 구매는 "이 게임에 전념한다", 구독은 "한번 해 본다", F2P는 "선택지로 열어 둔다" ([[ign-generations-in-play-2026]]). Gen Z를 노리는 라이브 게임은 F2P + UGC·소셜 기능 + 오래 머무는 진행 구조가 기본 조합이 된다는 것이 [[live-service-design|라이브 서비스 설계]]의 결론이다.

## 시장 신호 — 서구에서는 약세

- **서구 6개 시장 디지털 매출이 줄었다.** Newzoo의 진단은 *"F2P와 매년 나오는 프리미엄 시리즈의 약세가 잘 된 신작을 상쇄했다"* ([[gi-newzoo-ggmr-2026-release-2026-09]])
- **콘솔 F2P의 효율이 떨어진다.** 플레이 시간당 F2P 매출은 PC가 전년 대비 ▲10%로 PS의 약 2배·Xbox의 3배다. 콘솔에서는 매출이 플레이 시간보다 빨리 빠진다. Xbox 프리미엄 성장(▲3.6%)이 F2P와 CoD 손실을 메우지 못한 것도 같은 흐름이다 ([[newzoo-pc-console-2026]])
- **중가 프리미엄의 반사 이익**: \$30–50 밴드가 자라는 이유 중 하나로 *F2P 과금 피로를 피하는 자리*가 꼽힌다 ([[mid-price-sweet-spot]]) — 해석이지 측정은 아니다
- **지출 집중**: Bain 조사에서 상위 20%가 지출의 73%를 낸다. 같은 보고서에서 개인화 오퍼로 바꾼 한 대형 F2P사는 라이브 운영 캠페인의 플레이어당 매출이 50% 넘게 올랐다 ([[bain-gaming-report-2026]])

## 약점과 한계 (비판적 읽기)

- **운영사 1차 자료가 없다.** 포트나이트 \$5.4B·누적 \$20B+, Apex \$3B+는 외부 추정이다. 결제 전환율·결제자 비율·이용자당 일 매출 같은 F2P의 핵심 지표가 위키에 하나도 없다
- **떠난 사례에 기울어 있다.** F2P → 프리미엄 전환은 두 건이 자세하지만, 반대 방향(프리미엄 → F2P) 전환이나 *F2P로 남아서 성공한 신작*의 설계 기록은 없다
- **지역 편향이 크다.** Newzoo의 결론은 전부 서구 6개국(한국·중국·일본 제외) 기준이다. F2P 비중이 큰 아시아 모바일·MMO에 그대로 옮기면 과대 일반화다
- **"F2P 약세"는 한 문장짜리 진단이다.** Newzoo 보도에 폭·종 수·분류 기준 같은 정량이 없다
- **Bain 수치는 자기신고 설문이다.** "상위 20%가 73%"는 실거래가 아니고, Bain 스스로도 지출 집중을 *F2P에서는 10년 된 상식*이라고 적었다
- **마라톤의 −39%는 조건이 다른 두 시점이다.** 무료 테스트는 기간 한정 이벤트였고 유료 출시는 상시 판매다. 유료화의 순수한 효과로 읽으면 안 된다

## 관련 페이지

- [[live-service-design|라이브 서비스 설계]] · [[engagement-loop|인게이지먼트 루프]] · [[player-trust-design|플레이어 신뢰 설계]]
- [[game-pricing-strategy|게임 가격 전략]] · [[mid-price-sweet-spot|중가 프리미엄 스위트스폿]] · [[subscription-economy-gaming|구독 경제]]
- [[webshop-direct-monetization|웹샵·D2C 직접 수익화]] · [[mmorpg|MMO·MMORPG]]
- [[arc-raiders|아크 레이더스]] · [[marathon|Marathon]] — F2P를 떠난 두 사례
- [[fortnite|Fortnite]] · [[genshin-impact|원신]] · [[apex-legends|Apex Legends]] · [[league-of-legends|League of Legends]] — F2P를 운영하는 쪽

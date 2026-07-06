---
title: "전투·조력 AI 동반자 설계"
type: concept
sources: ["[[gdc14-tlou-buddy-ai]]", "[[gdc14-elizabeth-ai-postmortem]]", "[[gdc06-fear-goap]]", "[[gdc05-halo2-ai-complexity]]", "[[escort-mission-design-bycer]]", "[[miyazaki-elden-ring-spirit-ashes]]"]
related: ["[[companion-design|동반자(Companion) 설계]]", "[[companion-philosophy|RPG 동반자 설계 철학 비교]]", "[[combat-design|전투 디자인]]", "[[game-feel|게임 필]]", "[[ai-navigation|AI 내비게이션]]", "[[game-balance|게임 밸런싱]]", "[[soulslike|소울라이크]]"]
created: 2026-07-06
updated: 2026-07-06
confidence: medium
---

*전투·게임플레이 시스템*으로서의 AI 동반자·조력자·소환물을 설계하는 방법론. [[companion-design|내러티브 동반자 설계]]가 승인·로맨스·감정 유대(스토리텔링 축)를 다룬다면, 이 페이지는 **"곁에 있는 AI를 어떻게 플레이어의 짐이 아닌 자산으로 만드는가"**라는 시스템 축을 다룬다.

> 💡 **핵심 인사이트:** 전투 AI 동반자의 성공은 *얼마나 똑똑한가*가 아니라 *플레이어의 판타지를 방해하지 않으면서 유용해 보이는가*로 결정된다. 무적·투명화·어그로 분산·자원 공급·지능 착시는 모두 *플레이어 경험을 위해 AI의 자율성/현실성을 의도적으로 희생*하는 기법이다.

## 1. 제1 과제 — 호위 미션의 저주 피하기

전투 동반자 설계의 출발점은 [[escort-mission-design-bycer|호위 미션]]이 왜 미움받는지를 뒤집는 것이다.

| 실패 원인 | 정형 해법 |
|--|--|
| 코어 메카닉과 불일치 | 동반자를 코어 루프 안에 통합 (전투 자산화) |
| 플레이어 페이싱 통제권 상실 | 플레이어가 속도·명령을 쥐게 함 |
| 취약·수동적 escortee | 다운 상태(즉사 대신 부활), 회복력 부여 |
| 무능한 AI 파트너 | 탱킹(어그로 리다이렉트)·자원 공급으로 역할 부여 |

## 2. "짐이 되지 않는" 설계 — Elizabeth 모델

[[gdc14-elizabeth-ai-postmortem|BioShock Infinite의 Elizabeth]]는 호위 대상의 정의를 역전시켰다:
- **적이 그녀를 공격·타겟팅하지 않음** → 보호 부담 제거
- 전투 중 **탄약·체력·소금·돈을 플레이어에게 던져줌**, Tear로 엄폐물 소환 → 호위 *대상*이 아니라 전투 *자산*
- 항상 **플레이어와 다음 목표 사이**에 배치, 연극 기법(마커·시선 추적)으로 생명감 부여

## 3. 몰입을 위한 의도적 비현실 — 투명화와 어그로 분산

- [[gdc14-tlou-buddy-ai|The Last of Us의 엘리]]: **비전투 스텔스 중 적에게 아예 감지되지 않는다** — 동료가 실수로 잠입을 망치는 것을 원천 차단. 단 너무 안전하면 "동료 없는 느낌" → 유용성(투척·엄호)으로 존재감 확보. AI가 "속임수(cheating)"를 쓰지 않는 진정성도 함께 지킴
- [[miyazaki-elden-ring-spirit-ashes|엘든 링의 Spirit Ashes]]: 소환물의 본질은 **어그로 분산·탱킹** — 적 주의를 나눠 받아 플레이어에게 여유를 준다. 미야자키는 이를 필수 밸런스가 아닌 *난이도 자기조절 옵션(접근성 도구)*으로 규정

> ⚠️ 모순: 투명화·무적은 [[gdc05-halo2-ai-complexity|Halo]]식 "속을 수 있는 AI"가 주는 리얼리즘과 상충한다. [[escort-mission-design-bycer|Bycer]]도 무적화가 "왜 얘가 나를 호위 안 하지?"라는 몰입 붕괴를 낳는다고 지적. → 정답은 게임 톤에 따라 다르다 (몰입형 리얼리즘 vs 스트레스 없는 조력).

## 4. 지능 착시(illusion of intelligence)

적대 AI에서 정립된 "똑똑해 보이는" 기법은 동반자 AI에도 그대로 적용된다.

- [[gdc06-fear-goap|F.E.A.R.의 GOAP]]: 실제 지능감은 알고리즘이 아니라 *올바른 타이밍에 재생되는 애니메이션 + 무전 대사(bark)*에서 나온다 — "측면 잡아!"를 들려주는 것이 측면포위 계산보다 중요할 수 있다
- [[gdc05-halo2-ai-complexity|Halo 2의 지식 모델]]: AI 지식을 실제 월드와 분리(perception filter)해 *AI가 틀린 것을 믿고, 속고, 놀랄 수 있게* — 지능감은 AI를 더 똑똑하게가 아니라 *지식을 제한*해서 만든다

## 5. 내비게이션 전제

전투 동반자는 [[ai-navigation|AI 내비게이션]] 품질에 종속된다. follow region·동적 엄폐 선택([[gdc14-tlou-buddy-ai|TLOU]]의 raycast cover pack)이 무너지면 곧바로 호위 미션의 "끼임" 문제로 회귀한다. 동반자 이동 자유도의 상한은 AI의 지형 이해도가 정한다.

## 연결 개념
- [[companion-design|내러티브 동반자 설계]] — 감정·승인·로맨스 축 (이 페이지의 자매 개념)
- [[companion-philosophy|RPG 동반자 설계 철학 비교]] — 에이전시-감정 trade-off
- [[combat-design|전투 디자인]] — 동반자가 개입하는 전투 판타지·밸런스
- [[game-balance|게임 밸런싱]] — 어그로 분산·난이도 자기조절 레버
- [[game-feel|게임 필]] — 조력의 즉각 피드백·존재감

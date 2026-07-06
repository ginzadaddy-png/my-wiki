---
title: "Bringing BioShock Infinite's Elizabeth to Life: An AI Development Postmortem (John Abercrombie / Irrational)"
type: source-summary
sources: []
related: ["[[combat-companion-ai|전투·조력 AI 동반자 설계]]"]
source_url: "https://www.gdcvault.com/play/1020831/Bringing-BioShock-Infinite-s"
source_author: "John Abercrombie (Irrational Games)"
source_published: 2014-03
created: 2026-07-06
updated: 2026-07-06
confidence: high
---

**원문**: [Bringing BioShock Infinite's Elizabeth to Life (GDC Vault)](https://www.gdcvault.com/play/1020831/Bringing-BioShock-Infinite-s) — GDC 2014, John Abercrombie(Irrational Games, lead programmer). 보조: [Game Developer 리뷰](https://www.gamedeveloper.com/design/video-how-irrational-gave-life-to-i-bioshock-infinite-i-s-elizabeth)

BioShock Infinite의 Elizabeth를 "AI 로봇이 아닌 사람처럼" 느끼게 만든 AI postmortem. Elizabeth는 리더이자 팔로워, 동적이자 스크립트, 즐겁게 하는 자이자 즐거워하는 자라는 **모순된 요구**를 동시에 만족해야 했다.

## "짐이 되지 않는 동반자"
- **적이 Elizabeth를 공격·타겟팅하지 않는다** → 플레이어는 그녀를 보호할 필요가 전혀 없음 (호위 미션의 최대 스트레스 제거)
- 전투 중 **탄약·체력·소금(salts)·돈을 플레이어에게 던져줌**, Tear로 엄폐물·터렛 등 유용한 구조물 소환 → 호위 *대상*이 아니라 전투 *자산*으로 역전

## 생명감(life-like) 기법 — 연극 기법 차용
- 게임 관습보다 **연극(theater) 기법**을 적용
- 월드에 **마커(marker)**를 배치해 호기심을 표현, 눈이 오브젝트를 추적(eye tracking)
- 항상 **플레이어와 다음 목표 사이**에 위치시켜 길잡이 역할 + 화면에서 자연스럽게 존재

> 💡 **핵심 인사이트:** "무적 + 자원 공급 + 목표 사이 배치"의 조합으로 *호위 미션의 정의를 뒤집었다* — 지켜야 할 부담이 아니라 곁에 두고 싶은 파트너로.

→ 관련: [[combat-companion-ai|전투·조력 AI 동반자 설계]]

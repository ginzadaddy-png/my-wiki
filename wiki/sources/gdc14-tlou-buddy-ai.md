---
title: "Endure and Survive: The AI of The Last of Us (Max Dyckhoff / Naughty Dog)"
type: source-summary
sources: []
related: ["[[combat-companion-ai|전투·조력 AI 동반자 설계]]", "[[the-last-of-us|The Last of Us]]"]
source_url: "https://www.gamedeveloper.com/design/endure-and-survive-the-ai-of-the-last-of-us"
source_author: "Max Dyckhoff (Naughty Dog)"
source_published: 2014-08
created: 2026-07-06
updated: 2026-07-06
confidence: high
---

**원문**: [Endure and Survive: the AI of The Last of Us](https://www.gamedeveloper.com/design/endure-and-survive-the-ai-of-the-last-of-us) — Game Developer, Max Dyckhoff(Naughty Dog)의 GDC 2014 강연 정리, 2014

The Last of Us의 **버디 AI(Buddy AI)** 설계 postmortem. 핵심 과제는 엘리를 *짜증나는 호위 대상이 아니라 진짜 동료*로 만드는 것.

## 투명화(Invisibility) 설계
- 엘리는 **비전투 스텔스 중 Hunter·Infected에게 아예 감지되지 않는다** — 엘리가 실수로 엄폐물 밖으로 나가 플레이어의 잠입을 망치는 사고를 원천 차단
- 밸런스 함정: 너무 안전하면 "동료가 없는 느낌" → 유용성(적에게 벽돌·병 투척, 위험 시 총 사용)으로 존재감 확보

## 포지셔닝·비-부정행위(non-cheating)
- 플레이어 뒤 **follow region** 유지, 80개 raycast로 동적 "cover action pack" 평가해 인접 엄폐 선택
- 조엘이 엄폐 중 엘리를 몸으로 가려주는 전용 애니메이션 → 정서적 유대 강화
- 물리 아이템 없이 벽돌 투척, 플레이어가 재잠입하면 엘리도 스텔스 복귀
- AI가 "속임수(cheating)"를 쓰지 않게 해 경험의 진정성 유지

## 개발 현실
- 동반자 AI 시스템을 **출시 5개월 전 폐기 후 6주 만에 재구축** — 결국 게임의 정체성이 된 기능의 반복 난이도를 방증

> 💡 **핵심 인사이트:** 동료를 "안 보이게" 만드는 것은 리얼리즘의 포기가 아니라 *플레이어의 스텔스 판타지를 지키기 위한 의도적 선택*이다.

→ 관련: [[combat-companion-ai|전투·조력 AI 동반자 설계]]

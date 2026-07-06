---
title: "Three States and a Plan: The AI of F.E.A.R. (Jeff Orkin / Monolith)"
type: source-summary
sources: []
related: ["[[combat-companion-ai|전투·조력 AI 동반자 설계]]"]
source_url: "https://www.gamedeveloper.com/design/building-the-ai-of-f-e-a-r-with-goal-oriented-action-planning"
source_author: "Jeff Orkin (Monolith Productions)"
source_published: 2006-03
created: 2026-07-06
updated: 2026-07-06
confidence: high
---

**원문**: [Building the AI of F.E.A.R. with Goal Oriented Action Planning](https://www.gamedeveloper.com/design/building-the-ai-of-f-e-a-r-with-goal-oriented-action-planning) — Game Developer, Jeff Orkin(Monolith)의 GDC 2006 강연 "Three States and a Plan" 정리. 원논문: [Semantic Scholar](https://www.semanticscholar.org/paper/012ef03d0f951092b8645b69aebdbce900ac03e4)

F.E.A.R.의 적 AI는 **GOAP(Goal-Oriented Action Planning)** — STRIPS 유사 실시간 플래너로, 스크립트가 아니라 *스스로 행동 계획을 세워* 측면포위·후퇴·재집결·압박을 만든다.

## 구조
- **3-state FSM**: GoTo(이동)·Animate(사격·재장전 등)·Use Smart Object(환경 상호작용)
- 약 **70개 goal + 120개 action** 인코딩, 플래너가 짧은(보통 1~2 액션) 시퀀스를 동적 생성

## 지능 착시(illusion of intelligence)
- 실제로 하는 일은 "적절한 상황에서 애니메이션을 재생하는 것" — **"올바른 위치·타이밍에 재생될 때 똑똑해 보인다"**
- 적끼리 서로의 존재를 몰라도 시퀀스가 조율돼 협동처럼 보임
- (준1차 통설) 무전 대사(bark)로 "측면 잡아!" 등을 외쳐 *플레이어에게 의도를 들려주는* 것이 지능감의 큰 몫 — 강연 자체는 애니메이션 타이밍을 강조

> 💡 **핵심 인사이트:** 지능감은 알고리즘 정교함이 아니라 *플레이어가 읽어낼 수 있는 신호(타이밍·대사)*에서 나온다 — 동반자 AI에도 그대로 적용되는 원리.

→ 관련: [[combat-companion-ai|전투·조력 AI 동반자 설계]]

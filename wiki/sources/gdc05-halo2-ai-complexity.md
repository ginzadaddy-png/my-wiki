---
title: "Handling Complexity in the Halo 2 AI (Damian Isla / Bungie)"
type: source-summary
sources: []
related: ["[[combat-companion-ai|전투·조력 AI 동반자 설계]]"]
source_url: "https://www.gamedeveloper.com/programming/gdc-2005-proceeding-handling-complexity-in-the-i-halo-2-i-ai"
source_author: "Damian Isla (Bungie)"
source_published: 2005-03
created: 2026-07-06
updated: 2026-07-06
confidence: high
---

**원문**: [GDC 2005 Proceeding: Handling Complexity in the Halo 2 AI](https://www.gamedeveloper.com/programming/gdc-2005-proceeding-handling-complexity-in-the-i-halo-2-i-ai) — Game Developer, Damian Isla(Bungie)의 GDC 2005 강연 proceeding

Halo 2 AI가 복잡성을 다룬 방식. 복잡성을 무작정 늘리면 런타임 저하·확장성 악화·연출 통제 불가, 그리고 **"AI가 의도적이 아니라 무작위로 행동하는 것처럼 보이는"** 최악의 대가를 치른다.

## 지식 모델(prop / perception filter)
- **prop 표현**이 AI 지식 모델의 핵심 — 위치·방향·경로 등 상태 정보를 *실제 월드 상태와 분리*하고 액터의 **지각 필터(perception filter)**로 게이팅
- 두 표현이 갈라질 수 있으므로 **AI는 사실이 아닌 것을 믿을 수 있다** → 속고(tricked)·혼란스러워하고·놀라고·실망하는 AI 가능

> 💡 **핵심 인사이트:** "의도적으로 행동하는" 인상은 AI를 *더 똑똑하게* 만드는 게 아니라 *지식을 제한*해서 만든다 — 지능 착시의 반대 축. 플레이어가 AI를 속일 여지를 남기는 것이 오히려 살아있는 상대라는 감각을 준다.

→ 관련: [[combat-companion-ai|전투·조력 AI 동반자 설계]], [[gdc06-fear-goap|F.E.A.R. GOAP]]

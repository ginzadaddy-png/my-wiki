---
title: "Epic — The Road to Unreal Engine 6 (UE5·UEFN 통합·Blueprint 폐기 예고)"
type: source-summary
source_url: "https://www.unrealengine.com/news/the-road-to-ue-6"
source_author: "Epic Games (Marcus Wassmer 설명)"
source_published: 2026-06-17
sources: []
related: ["[[unreal-engine-5|Unreal Engine 5]]", "[[proprietary-engine-vs-ue5|자체 엔진 vs UE5 의사결정 매트릭스]]", "[[designer-empowerment|디자이너 도구화]]", "[[game-market-trends|게임 시장 트렌드]]"]
created: 2026-06-23
updated: 2026-06-23
confidence: high
---

**원문**: [Epic 공식 — The road to Unreal Engine 6](https://www.unrealengine.com/news/the-road-to-ue-6) — Epic Games (Marcus Wassmer), 2026-06-17. *Epic 원문은 자동 fetch 403 → [gamedeveloper.com](https://www.gamedeveloper.com/programming/unreal-engine-6-will-merge-ue5-and-uefn-into-a-single-unified-engine-) (Bryant Francis, 2026-06-17) 미러로 검증.*

Epic이 **UE5와 UEFN(Unreal Editor for Fortnite)을 단일 통합 엔진 UE6로 합치겠다**고 발표. Wassmer: *"UE6는 우리가 그것들을 어떻게 ship·operate하는지를 진화시키는 것"*.

**핵심 방향**
- **언어 전환**: C++ → **Verse**를 primary 스크립트로. 대규모 멀티플레이 시뮬레이션·크로스게임 로직·지속 경제 처리 목적, 접근성 확대 표방.
- **Blueprint·Actors 점진 폐기**: 신 프레임워크가 *"충분히 성숙"*하면 deprecate. 초기 UE6엔 유지되고, 이후 *변환 툴* 제공 — 즉시 제거 아님.
- **Roblox식 생태계**: 콘텐츠·코드·경제가 게임·엔진 간 이식·상호운용(오픈 표준), Fortnite 코스메틱 크로스게임부터 시작.
- **AI 통합**: Claude·Gemini를 에디터에 내장 — *"창의성·생산성 multiplier"*로 포지셔닝.
- **타임라인**: **2027년 말 Early Access**, 정식 출시는 그 12~18개월 후.

> ⚠️ **산업 시그널·쟁점:** [[clair-obscur-expedition-33|33원정대]]의 *Blueprint 95%* 모델([[designer-empowerment|디자이너 도구화]]의 기술 토대)이 장기적으로 폐기 대상이 됨 → 소규모 팀의 비주얼 스크립팅 접근성 경로 재편 우려로 백래시. [[unreal-engine-5]] "한계와 우려"에 적힌 *Epic 의존성*이 더 심화되는 방향.

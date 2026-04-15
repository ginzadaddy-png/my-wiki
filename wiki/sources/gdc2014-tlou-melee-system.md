---
title: "Unsynced: The Last of Us Melee System (GDC 2014)"
type: source-summary
sources: ["raw/articles/2026-04-15T122900+0900-Unsynced The Last of Us Melee System.md"]
related: ["[[전투 디자인]]"]
created: 2026-04-15
updated: 2026-04-15
confidence: high
---

GDC 2014. Naughty Dog, Anthony Newman. TLOU 근접 전투 시스템 — "비동기화(Unsynced)" 애니메이션 설계 철학.

## 핵심 요약

**Unsynced(비동기화)란**: 전통적 근접 전투는 공격자와 피격자 애니메이션을 동기화(잠금). TLOU는 이를 **분리(decouple)** — 각 캐릭터가 독립적으로 반응.

**설계 이유**:
- 동기화 방식은 "영화적"이지만 컨트롤 박탈감 → 리얼리즘과 반응성의 충돌
- Unsynced: 공격 도중에도 방향 전환·타겟 변경 가능 → 전투 유동성 증가
- TLOU의 그루티(grounded) 전투 느낌과 일치

**기술적 구현**:
- 피격 반응 애니메이션 독립 실행 → 여러 적 동시 처리 가능
- 충돌 판정과 애니메이션 타이밍 분리 → 공격 판정이 시각보다 선행 가능

**무기 내구도 시스템**:
- 무기가 부서진다 → 전투 중 임기응변 강조
- 희소성과 결합: 근접 전투가 무거운 선택

> **핵심 인사이트:** "동기화를 깨면 더 자연스러워진다." 애니메이션 잠금을 제거하면 전투가 덜 영화적으로 보이지만, 플레이어는 더 강한 주체감을 느낀다.

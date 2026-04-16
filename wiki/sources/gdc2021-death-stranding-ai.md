---
title: "'Death Stranding': An AI Postmortem (GDC 2021)"
type: source-summary
sources: ["raw/articles/2026-04-15T122811+0900-'Death Stranding' An AI Postmortem.md"]
related: ["[[ai-navigation|AI 내비게이션]]", "[[kojima-productions|코지마 프로덕션]]"]
created: 2026-04-15
updated: 2026-04-15
confidence: high
---

GDC 2021 AI Summit. Kojima Productions, Eric Johnson (AI 프로그래머). 데스 스트랜딩의 복잡한 자연 지형 위 AI 내비게이션 기술 포스트모템.

## 핵심 요약

**지형이 적인 게임**: 플레이어가 지형을 극복하는 게임 → NPC도 동일한 어려움을 겪어야 함. 내비메시가 복잡해지는 근본 원인.

**핵심 솔루션**:
1. **이벤트 기반 재경로**: 타이머 기반 리패스 제거 → 5가지 조건 감지 시에만 재경로 계산
2. **경로 직선화**: 래스트 개선법(raycast shortcutting)으로 꺾인 경로 최적화
3. **진입 비용 분리**: 고비용 지형(바위·강)에 통과 비용과 진입 비용을 별도 설정 → 들어가면 계속 가고, 밖에서는 회피
4. **하이브리드 내비**: AI 도로망 + 내비메시 합산 → 수 킬로미터 이동 가능

**동적 지형 지원**:
- 사다리·다리: 플레이어 설치 시 자동으로 내비메시 링크 생성 → NPC가 즉시 활용
- Strand 오브젝트(BT 조우): 빌딩 위 점프 링크 동적 생성

**공간 쿼리 트릭**: 델타 비용(경로 비용 - 경로 길이)으로 강을 건너가야 하는 위치 지양 → 자연스러운 지형 회피

> **핵심 인사이트:** 플레이어의 이동 자유도를 그대로 NPC에 부여하려면, 내비 시스템이 플레이어의 물리 엔진만큼 지형을 이해해야 한다.

---
title: "MDA 프레임워크"
type: concept
sources: ["[[gmtk-mda-framework]]", "[[skyrim-not-perfect-mda]]"]
related: ["[[combat-design|전투 디자인]]", "[[game-balance|게임 밸런싱]]", "[[player-guidance-design|플레이어 유도 설계]]", "[[open-world-design|오픈월드 설계]]"]
created: 2026-04-20
updated: 2026-04-20
confidence: high
---

2004년 Hunicke, LeBlanc, Zubek이 제안한 게임 분석·설계 프레임워크. 게임 디자이너가 왜 특정 메카닉이 특정 감정을 만드는지 이해하는 도구.

## 3단계 구조

| 계층 | 정의 | 예시 |
|------|------|------|
| **Mechanics** | 규칙·시스템·버튼·수치 | 탄약 최대치 = 50 |
| **Dynamics** | 플레이어의 반응 행동 | 탄약 넉넉 → 무모하게 발사 |
| **Aesthetics** | 플레이어의 감정 경험 | 강력함·무적감 |

- 코드 → 행동 → 감정의 **인과 연쇄**
- 디자이너는 감정에 직접 접근 불가 → **코드를 바꿔 연쇄를 유발**

## 분석 방향 vs 설계 방향

- **분석 시**: Aesthetics(느낌) → Dynamics(행동) → Mechanics(코드) 역방향 추적
- **설계 시**: 목표 Aesthetics 정의 → 그걸 만드는 Dynamics 구상 → 구현할 Mechanics 결정

## 실전 적용

**Alien: Isolation 세이브 시스템** ([[gmtk-mda-framework]]):
- 자동 저장(Mechanics) → 죽어도 몇 분만 잃으니 태평 (Dynamics) → 공포감 없음 (Aesthetics)
- 수동 저장기(Mechanics) → 신중하게 이동 (Dynamics) → 극도의 긴장감 (Aesthetics)

**스카이림** ([[skyrim-not-perfect-mda]]):
- 버그 투성이 메카닉에도 불구하고 "경이로움(Wonder)"과 "여정(Journey)"의 미학이 결함을 압도
- **올바른 Aesthetics 목표가 메카닉 완성도보다 중요**

## Aesthetics 8가지 (원 논문)

Sensation·Fantasy·Narrative·Challenge·Fellowship·Discovery·Expression·Submission

> **핵심 인사이트:** "올바른 메카닉"은 없다 — 목표하는 감정(Aesthetics)에 맞는 메카닉이 올바른 것이다. 다른 게임의 메카닉을 복사할 때는 그 게임이 어떤 감정을 목표로 했는지 먼저 이해해야 한다.

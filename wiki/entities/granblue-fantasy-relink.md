---
title: "GRANBLUE FANTASY: Relink (그랑블루 판타지 리링크)"
type: entity
sources: ["[[cedec2026-granblue-relink-battle|CEDEC 2026 Relink 배틀 제작]]"]
related: ["[[cygames|Cygames]]", "[[combat-companion-ai|전투·조력 AI 동반자 설계]]", "[[combat-design|전투 디자인]]", "[[ip-adaptation-design|IP 적응 설계]]"]
created: 2026-07-30
updated: 2026-07-30
confidence: medium
relations:
  developedBy: [cygames]
  publishedBy: [cygames]
  platform: [ps5, ps4, pc]
---

**GRANBLUE FANTASY: Relink**는 [[cygames|Cygames]]가 개발·퍼블리싱한 4인 협동 액션 RPG. 모바일 IP 그랑블루 판타지의 콘솔·PC 확장작이며, 2026년 대형 확장 **Endless Ragnarok**으로 이어졌다.

> 💡 **핵심 의의 — 접근성과 동료 AI가 같은 구조:** 어시스트 모드(이동+공격 / 이동만)가 동료 AI와 **동일 아키텍처**를 쓴다. "AI가 캐릭터를 대신 조작하는 방식"을 잘 만들면 그것이 곧 접근성 기능이 되고, 동시에 자동 플레이 QA 도구가 된다 — 하나의 구조로 세 문제를 푸는 설계.

## 배틀 설계 ([[cedec2026-granblue-relink-battle]])

- **28캐릭터 × 3 마스터 스타일 = 84 플레이 스타일.** 공통 요소는 표준 데이터 포맷, 고유 메카닉은 조작 타입별 분류 → 신규 캐릭터는 파라미터 조정으로 대응
- **동료 AI 2계층**: Character AI(비헤이비어 트리+FSM으로 플레이어 입력 모사) + Meta AI(포지셔닝·체인 어택·게이지 계산으로 풀 콤보 보장)
- **의도적 제약**: "자세 잡고 걷기" 정지 상태로 AI가 플레이어보다 먼저 적을 정리하는 것을 방지
- 회피는 예측이 아니라 **피격 후 무효화**로 구현 — 비용을 아끼면서 결과만 맞추는 지능 착시

## 관련 위키 페이지

- [[cygames|Cygames]] — 개발·퍼블리싱
- [[combat-companion-ai|전투·조력 AI 동반자 설계]] — 플레이어 판타지를 방해하지 않는 조력 AI
- [[ip-adaptation-design|IP 적응 설계]] — 액션 초심자인 IP 팬을 위한 어시스트 설계

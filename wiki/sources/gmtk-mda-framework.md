---
title: "게임 디자이너처럼 생각하는 법 (MDA 프레임워크)"
type: source-summary
sources: ["How To Think Like A Game Designer"]
related: ["[[mda-framework|MDA 프레임워크]]", "[[combat-design|전투 디자인]]", "[[game-market-trends|게임 시장 트렌드]]"]
created: 2026-04-20
updated: 2026-04-20
confidence: high
---

Mark Brown / Game Maker's Toolkit (2023-02-18). Alien: Isolation 세이브 시스템 사례로 시작.

## MDA 프레임워크

- **Mechanics**: 게임의 규칙·시스템·버튼·수치
- **Dynamics**: 플레이어가 그 메카닉에 반응해 취하는 행동
- **Aesthetics**: 플레이어가 그 행동 속에서 느끼는 감정 (그래픽·아트 스타일이 아님)

코드(Mechanics) → 플레이어 행동(Dynamics) → 플레이어 감정(Aesthetics)의 인과 연쇄.  
디자이너는 감정에 직접 접근할 수 없다 — **코드를 바꿔서 연쇄를 유발**해야 한다.

## 핵심 교훈: 메카닉은 맥락 없이 복사하면 안 된다

- Alien: Isolation 초기 자동 저장 → "죽어도 몇 분만 잃으니 태평하게 돌아다님" → 공포게임에서 역효과
- "다른 게임에서 메카닉이 왜 작동하는지 이해한 뒤에 복사하라"
- 탄약 제한 예시: 탄약 무한 → 무모한 전투 → 강력함·무적감 / 탄약 희소 → 신중한 전투 → 긴장·생존감

> **핵심 인사이트:** MDA는 메카닉이 왜 특정 감정을 만드는지 역추적하는 도구다. 게임을 분석할 때는 Aesthetics(느낌)에서 Mechanics(코드)로 거슬러 올라가고, 게임을 만들 때는 Mechanics에서 Aesthetics로 내려온다.

---
title: "Asobo Studio"
type: entity
sources: ["[[gdc2023-asobo-how-to-make-aaa-small-team]]"]
related: ["[[a-plague-tale-requiem|A Plague Tale: Requiem]]", "[[small-team-development|소규모 팀 전략]]", "[[proprietary-engine-strategy|독자 엔진 전략]]"]
created: 2026-04-28
updated: 2026-04-28
confidence: high
---

프랑스 보르도 기반 독립 스튜디오. A Plague Tale 시리즈와 Microsoft Flight Simulator로 알려진 소규모 팀의 AAA 도전 사례. 2002년 설립, 자체 인하우스 엔진 보유.

## 기본 정보

- **설립**: 2002년 (프랑스 보르도)
- **대표작**: A Plague Tale: Innocence(2019) · A Plague Tale: Requiem(2022) · Microsoft Flight Simulator(2020)
- **엔진**: 인하우스 엔진 (2002년 창립 이래 자체 개발·유지, Flight Simulator 제외)
- **아트팀 규모**: Requiem 기준 약 20명 아티스트

## 핵심 철학: "Focus on What Matters"

Asobo 전체 레이토모티프. A Plague Tale 1·2와 Flight Simulator를 모두 소규모 팀으로 완성한 근거:

- **Quixel Megascans** 보조 에셋 활용 → 아티스트 시간을 영웅 에셋에 집중
- **Midpoly 메시 전략**: 신세대 콘솔에서 무거운 지오메트리 지원 → 제작 속도↑, 반복 유연성↑
- **Displacement Map → Blend Map 재활용**: 별도 텍스처 공수 절감

## 비주얼 방법론 (Requiem 기준)

[[gdc2023-asobo-how-to-make-aaa-small-team]]

**One Time Period, One Place, One Style**
- 중세 14세기 프랑스 / 남부 프랑스·북부 이탈리아 한정
- 클로드 로랭(Claude Lorrain) 회화를 마스터 비주얼 레퍼런스로 사용
- 제약이 팀 공통 언어 역할 → 방향 논쟁 없이 빠른 의사결정

**Fast Level Building**
- Day 1 블록아웃 → Day 2 러프 에셋 배치 → 1~2주 폴리시
- 방향성을 먼저 검증하고 완성도는 나중에

**Get Rid of the 3D Feeling**
- 메시·블렌드·데칼·프로젝션으로 패턴 반복 제거
- "We build our vistas like illustrations or paintings. Composition is vital."

## 인하우스 엔진

언론에 Unreal Engine으로 오보된 사례가 많지만, Asobo는 창립 이래 자체 엔진을 유지한다.

- 계층형(Hierarchy-based) 에디터 + 커스텀 기능·단축키
- Requiem 개발 중 추가된 기능: **Decals · Ocean · Volumetric Fog · POM**
- Flight Simulator는 예외 (Microsoft 플랫폼 엔진 사용)

> 💡 **핵심 인사이트:** Asobo는 [[small-team-development|소규모 팀 전략]]과 [[proprietary-engine-strategy|독자 엔진]] 둘 다를 결합한 보기 드문 사례다. "Focus on what matters"는 단순 슬로건이 아니라 에셋 전략·레벨 빌딩·엔진 투자 모든 의사결정의 필터로 작동한다.

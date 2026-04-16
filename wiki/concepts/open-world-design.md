---
title: "오픈월드 설계"
type: concept
sources: [
  "[[open-world-linearization-gta5]]",
  "[[skyrim-not-perfect-mda]]",
  "[[zelda-vs-ubisoft-open-world]]",
  "[[botw-eldenring-visual-guidance]]",
  "[[gmtk-world-design-elden-ring]]",
  "[[gmtk-world-design-dark-souls]]",
  "[[dark-souls-world-hides-lore]]",
  "[[dark-souls-lordran-layout]]",
  "[[gdc2024-skyrim-starfield-design-collab]]",
  "[[gdc2024-valheim-early-access]]"
]
related: ["[[level-design-principles|레벨 디자인 원칙]]", "[[emergent-systems-design|창발적 시스템 설계]]"]
created: 2026-04-15
updated: 2026-04-15
confidence: high
---

오픈월드는 자유와 방향 사이의 긴장이다. 플레이어가 어디든 갈 수 있지만, 어디로 가야 할지 알아야 한다.

## 자유의 역설: 선형화

**GTA5의 선택적 제약** ([[open-world-linearization-gta5]]):
- 오픈월드도 미션 안에서는 선형화 — NPC 따라가기, 경로 차단, 공간적 깔때기
- "자유를 보존하면서 내러티브 순간을 연출하는" 기술이 오픈월드 설계의 핵심

**SDT 이론으로 본 젤다 vs 유비식** ([[zelda-vs-ubisoft-open-world]]):
- 자기결정이론(SDT): 자율성·유능감·관계성이 모두 충족될 때 재미
- 유비식: 지도 UI가 자율성을 대체 → 유능감 박탈
- BotW: "인력(Attraction)"으로 자연스럽게 끌어당김 → 자율성 유지

## 시각적 유도: 필드 삼각형 법칙

**대형→중형→소형 랜드마크 계층** ([[botw-eldenring-visual-guidance]]):
1. 대형 랜드마크 (산, 탑): 전체 방향 설정
2. 중형 랜드마크 (폐허, 나무): 중간 목표
3. 소형 랜드마크 (빛, 연기): 즉각적 관심

단계적 노출: 랜드마크를 처음엔 흘끗, 가까워질수록 자세히 — 탐험 욕구를 계속 갱신.

## 세계 구조 패턴

**엘든 링: 레거시 던전 + 오픈 필드** ([[gmtk-world-design-elden-ring]]):
- 레거시 던전(성): 선형·집중·내러티브 밀도
- 오픈 필드: 비선형·탐험·자유
- 두 층위가 번갈아 나타나며 리듬 형성

**다크소울: 아코디언 구조** ([[gmtk-world-design-dark-souls]]):
- 선형→개방→선형→개방→선형의 반복
- 3D 메트로이드바니아: 지름길 해금이 공간 이해를 강화

**공간 = 내러티브** ([[dark-souls-world-hides-lore]]):
- 환경 자체가 스토리를 암시 — 직접 설명 없이 공간이 역사를 품음
- "연결된 느낌"의 비밀: 3D 공간적 일관성 ([[dark-souls-lordran-layout]])

## 오픈월드의 심리학

**MDA 프레임워크로 본 스카이림** ([[skyrim-not-perfect-mda]]):
- 버그 투성이지만 "경이로움(Wonder)"과 "여정(Journey)"의 미학이 결함을 압도
- 완벽한 메카닉 < 올바른 미학적 목표

**Bethesda 협업 발전** ([[gdc2024-skyrim-starfield-design-collab]]):
- 오픈월드가 클수록 레벨↔퀘스트 팀 간 의사소통 비용 급증
- 스카이림→스타필드: 전문화와 협업 구조화가 필수

> **핵심 인사이트:** 오픈월드의 자유는 무한한 선택지가 아니라 **"어디로든 갈 수 있다는 느낌"을 유지하면서 플레이어를 자연스럽게 흥미로운 곳으로 이끄는 것**이다.

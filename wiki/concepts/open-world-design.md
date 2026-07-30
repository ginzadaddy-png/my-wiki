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
  "[[gdc2024-valheim-early-access]]",
  "[[gdc24-spiderman2-open-world]]",
  "[[ex-rockstar-ben-hinchliffe-interview]]",
  "[[cedec2026-crimson-desert-world-first]]"
]
related: ["[[level-design-principles|레벨 디자인 원칙]]", "[[emergent-systems-design|창발적 시스템 설계]]", "[[open-world-guidance|오픈월드 유도 비교]]", "[[marvel-spiderman-2|마블 스파이더맨 2]]", "[[death-stranding|데스 스트랜딩]]", "[[red-dead-redemption-2|레드 데드 리뎀션 2]]", "[[crimson-desert|붉은사막]]", "[[pearl-abyss|펄어비스]]", "[[designer-empowerment|디자이너 도구화]]"]
created: 2026-04-15
updated: 2026-07-30
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

## 록스타식 오픈월드 밀도 설계

**Ben Hinchliffe (前 록스타 디자이너)** ([[ex-rockstar-ben-hinchliffe-interview]]):
- 맵 전체에서 콘텐츠 공백 없도록 **메티큘러스하게 배치 계획**
- 플레이어가 지시를 따르지 않아도 세계는 살아있어야 함 → "What-if" 레이어
  - RDR2 moonshine 미션: 다리 습격 안 하면 마차가 강도 캠프까지 이동, 완전한 씬 구현
  - "99%가 못 보는 콘텐츠지만 존재한다"
- **90% 규칙**: 미션 개발의 90%는 플레이어의 예상 밖 행동을 수용하거나 막는 작업
- 좋은 오픈월드 = 막지 않고 수용하되 여전히 작동하는 게임

## 월드 퍼스트 — 퀘스트보다 세계가 먼저 ([[crimson-desert|붉은사막]])

[[pearl-abyss|펄어비스]]가 약 200명·7년으로 만든 [[cedec2026-crimson-desert-world-first|붉은사막]]은 제작 *순서*를 뒤집었다. 퀘스트 사양이 세계를 규정하는 대신, 세계가 먼저 존재하고 퀘스트가 그 위에 얹힌다.

**3층 병렬 구조**: 환경 층(지형·식생·야생동물·랜드마크) / 콘텐츠 층(아이템·NPC·스케줄·캠프·퍼즐) / 메타게임 층(교역소·세력 거점·전략 시스템). 각 층이 독립 진행되되 의미 있게 겹친다.

- 효과: *"퀘스트 안내 없이도 단서만으로 플레이 가능"* — 탐험이 스토리의 보조가 아니라 1차 게임플레이가 된다. 위 록스타의 *"플레이어가 지시를 따르지 않아도 세계는 살아있어야 한다"*와 같은 목표를 **제작 순서**로 달성한 사례
- **페이즈 스위칭**: 안정적인 「베이스 레벨」(지형)과 변화하는 「게임플레이 레벨」(건물·적·퍼즐)을 분리 → 맵 복제 없이 같은 장소를 다른 상태로 전환
- 배치는 대규모 구조물 Houdini + 지역·지형 데이터 기반 절차적 분포, 기억에 남을 순간만 수작업 → [[art-pipeline-design|아트 파이프라인]]의 90:10 도구화와 같은 비율

> ⚠️ 모순: 베데스다 사례([[gdc2024-skyrim-starfield-design-collab]])는 오픈월드가 커질수록 *레벨↔퀘스트 팀 소통 비용*이 급증한다고 진단했다. 붉은사막은 그 비용을 **팀 간 의존을 없애는 방향**(월드 퍼스트 + XML 공통 언어)으로 풀었지만, 대가로 **메인 스토리의 존재감이 약해졌다**고 발표자들이 직접 인정했다 — "물리적 세계의 제약이 내러티브를 규정했고, 그 역이 아니었다". 즉 소통 비용을 없애면 내러티브 통제력을 잃는 trade-off가 존재한다.

> 💡 **핵심 인사이트:** 오픈월드의 자유는 무한한 선택지가 아니라 **"어디로든 갈 수 있다는 느낌"을 유지하면서 플레이어를 자연스럽게 흥미로운 곳으로 이끄는 것**이다. 록스타는 여기서 한 발 더 나아가 — 플레이어가 어디로 가든 세계가 이미 그곳에서 살아있도록 만든다.

---
title: "[GDC26] Game Character Pipelines at Embark: Freedom Through Structure (Östsjö & Arvidsson)"
type: source-summary
sources: []
related: ["[[embark-studios|엠바크 스튜디오]]", "[[art-pipeline-design|아트 파이프라인 설계]]", "[[arc-raiders|아크 레이더스]]", "[[multi-project-development|멀티 프로젝트 개발]]", "[[small-team-development|소규모 팀 개발]]", "[[innersource|이너소스]]", "[[proprietary-engine-strategy|독자 엔진 전략]]"]
source_url: "https://www.youtube.com/watch?v=UFeC-VBbO90"
source_author: "Erik Östsjö (Technical Artist), Björn Arvidsson (Senior Character Artist) — Embark Studios"
source_published: 2026-04-08
created: 2026-05-18
updated: 2026-05-18
confidence: high
---

**원문**: [Game Character Pipelines at Embark — GDC 2026 (YouTube)](https://www.youtube.com/watch?v=UFeC-VBbO90) — Erik Östsjö & Björn Arvidsson (Embark Studios), GDC 2026, SideFX 후원

[[embark-studios|엠바크]]의 캐릭터 파이프라인 발표. The Finals(2023)·[[arc-raiders|Arc Raiders]](2025-10-30 출시) 두 게임이 *같은 파이프라인을 공유*하는 메커니즘과 그 설계 원칙. [[small-team-development|적은 인원으로 많이 만들기]]의 기술적 실체 — 도구화가 [[dev-talent-pipeline|인재 파이프라인]]·[[multi-project-development|멀티 프로젝트]]를 어떻게 가능하게 하는지의 케이스 스터디.

## 5가지 미션 선언 (Mission Statements)

발표자들이 명시한 파이프라인 설계 5원칙:

1. **Kit-bash 마인드** — 캐릭터를 "여러 조각의 조립체"로 다룬다 (단일 모놀리식 X)
2. **피드백 분리** — *게임 피드백*과 *asset 피드백*을 분리. 한쪽 변화가 다른 쪽을 깨지 않도록
3. **Late lock-down** — 절대 필요할 때까지 lock하지 않는다. Delayed decision making
4. **No blockers** — 사람이 안 본 단계가 있으면 procedural이 그 자리를 메꾼다
5. **90/10 도구화** — 도구가 지루하고 반복적인 일을 90%까지 처리, 아티스트는 "아티스트답게" 10%에 집중

## Tech Stack 핵심

**Houdini (절차적 코어)**
- 노드 기반 인터페이스 + 강력한 geometry processing + 커스터마이즈 가능
- "Houdini는 무섭다"는 평판 회피: 자체 UI 레이어로 아티스트를 점진적으로 끌어들임 → 지금은 모든 캐릭터 아티스트가 Houdini에서 작업
- 자체 launcher가 Houdini + 모든 dependencies + templates 자동 설치 (버전 관리 통합)

**USD (Universal Scene Description)**
- 발표자 비유: **"3D의 PSD"** — JPEG → PSD가 OBJ → USD에 대응
- **Single source of truth**: 한 process가 자기가 신경 쓰는 것만 저장 (예: 색깔만). geometry 업데이트 여부 의심 불필요
- **Layer composition** — 한 layer 변경이 다른 layer 영향 안 줌. helmet 예시: box → block out → 실제 helmet 거치는 동안 hierarchy 유지
- **Unified Python API** — 통합 필요 시 직접 빌드 가능

**외부 DCC 통합**
- ZBrush · Marvelous · Blender · Substance Painter · Maya 모두 Houdini와 연결
- "한 도구가 모든 걸 해결할 수 없다 — 기존 specialized 도구·워크플로우를 버리지 말자"

## Origins Node — 외부 DCC 통합 메커니즘

> 💡 **핵심 인사이트:** Origins node가 Houdini와 외부 DCC 간 *live link*를 구현한다. ZBrush 노드 클릭 → 자동 dependencies·templates·software 업데이트 sync → 작업 후 다시 sync. **모든 software가 같은 "truth"를 본다**. 한 software에서 메시 업데이트 시 Substance Painter import가 자동 트리거.

- 각 connected software에 custom plugin 탑재 (cleanup, USD outliner, import/export)
- ZBrush 내부에 Houdini의 scene graph를 확장 → 아티스트가 ZBrush 안에서 asset 구조 설정 가능
- 결과: "everything is a layer" — 불필요한 export/import 반복 제거

## 진화 — 두 번의 실패에서 배운 것

**Phase 1: Black-box procedural (초기)**
- ZBrush high poly → procedural 직통 → 게임 asset
- 작동할 때는 surprisingly well, but 안 될 때 *아티스트가 refine 못 함*
- 교훈: 완전 black box는 위험 — 아티스트가 개입할 수 있는 손잡이 필요

**Phase 2: Box-of-boxes (모듈러 분할)**
- "box → boxes 컬렉션"으로 분할 + 캐릭터를 kit-bashy 조각으로 분할
- 각 piece에 best fit하는 box sequence 할당
- 자체 Python 앱 빌드 — **but** "less people로 more하기" 원칙과 충돌 (앱 개발이 풀타임 + 정상 업무)

**Phase 3: Houdini Solaris (현재)**
- 자체 앱 포기, Houdini Solaris(USD 기반) 발표 타이밍이 맞아 통합
- "Houdini는 절차주의의 고향" — 자기 자리를 찾음

## Procedural UV Layout — PDG 병렬 처리 사례

UV layout 노드 분석 (Solaris + PDG + SOPS 결합 예시):

- **Solaris 선택**: hierarchy 기반 선택 (single face index 아닌). 토폴로지 변경에 강건. `prim patterns`로 일반화된 선택 가능
- **PDG (Procedural Dependency Graph) 병렬화**: native loop는 한 asset 변경 시 모두 재처리. PDG는 변경된 것만 parallel 재처리
- **Custom validation**: 색깔 변경 같은 topology/UV 무관 변화는 *재실행 안 함* — "가장 빠른 방법은 안 하는 것"
- 각 asset = dot, color = status, warning indicator 명확

## Substance Painter 통합

- **Auto-matching**: high poly ↔ low poly 자동 페어링 (world space 기반 best fit 추정). 수동 override는 viewer state로
- 한 번 노드 실행 → Painter 자동 bake → 다음 단계로
- Manual refine 시 *유일한 수동 작업*: "이 piece들이 Unreal에서 같은 material이다" 지정 (그게 전부)
- Painter에서 텍스처 저장 → 네트워크 변경 감지 → 필요한 노드만 cook → Unreal로 자동 push (notify chain)

## Edit-in-Place — 충돌 해결 패턴

Kit bash collision 발생 시 *source asset을 건드리지 않는다*:
- 충돌 지점에 새 node 추가 → high/low poly 정렬 유지
- node를 disconnect하면 원상복구 (안전)
- node 내부에 일반 SOP 사용 가능 (Houdini sculpt = ZBrush 흉내)
- 모든 manual 변경을 *deformer*로 처리 → topology 변경·transform에 강건

## Wrapping — Body Type 적응 (Finals 사례)

- The Finals 시즌 6: 6개 body type 옷 자동 적응 필요
- 새 노드 만들고 일부 프로젝트에 slot in → 다른 파이프라인 영향 없음 (격리)
- 노드 mature되면 모든 creator가 사용 가능. 새 프로젝트는 templates 몇 개만 추가

## Batching — Cross-project 일괄 처리

- 시즌 6에서 body type 추가 요청 → batching tool로 *모든 프로젝트*에서 wrap + Unreal export 일괄 재실행
- UI: 각 dot = 프로젝트, color = state
- **부가 효과**: 그동안 노드들도 개선되어 있어서 모든 body type이 *무료로 quality boost*

## Cross-Project 공유 — Arc Raiders ↔ The Finals

> 💡 **핵심 인사이트:** Arc Raiders와 The Finals는 *같은 파이프라인을 공유*한다. 차이는 *project-specific 노드 몇 개* + wrap system + customization뿐. Engine(Unreal)도 공유. 이게 [[embark-studios|엠바크]] "360명으로 4개 게임 포트폴리오" 목표의 *기술적 실체*.

Q&A: "두 게임이 얼마나 비슷한가?" → "It's a lot. 같은 파이프라인. 개별 노드만 다름."

## Delayed Decision Making

- texture resolution, UV packing, piece 조합 같은 *최종 in-game asset 결정*을 마지막 단계에서
- 같은 캐릭터를 in-game cutscene용으로 upscale → 다시 downscale해서 in-game asset으로 export
- 핵심 원칙: **"가능한 한 오래 fluid·flexible 유지"**

## Onboarding & Rigging 통합

- **별도 onboarding 프로그램 없음** — "collective" 문화. 한 노드씩 점진 학습
- Rigging: 초기엔 Maya 풀 파이프라인 → Origin 노드로 sync → 지금은 Houdini-only로 점진 이동 (custom 절차적 cloth·joint 노드 개발 중)
- 시사: 파이프라인 통합이 *5년 점진 마이그레이션*이지 한 번에 결정한 게 아님

## 자매 위키 페이지

- [[embark-studios|엠바크 스튜디오]] — 본 발표가 부연하는 엠바크 철학·360명·4 game 포트폴리오의 기술적 실체
- [[art-pipeline-design|아트 파이프라인 설계]] — 본 발표를 일반화한 concept
- [[gdc2023-asobo-how-to-make-aaa-small-team]] — 비교 사례: Asobo 20명 아티스트의 도구화 (포토그래메트리·절차적 지형)
- [[gdc26-expedition33-programmers]] — 비교 사례: Sandfall 프로그래머 4명의 Blueprint 95% 활용
- [[multi-project-development|멀티 프로젝트 개발]] — 파이프라인 공유 = 멀티 프로젝트의 실제 동작 메커니즘
- [[innersource|이너소스]] — Embark Rust 오픈소스화 + 본 발표의 internal pipeline 공유 모델

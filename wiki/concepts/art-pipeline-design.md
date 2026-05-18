---
title: "아트 파이프라인 설계 (Art Pipeline Design)"
type: concept
sources: ["[[gdc2026-embark-character-pipeline]]", "[[gdc2023-asobo-how-to-make-aaa-small-team]]", "[[gdc26-expedition33-programmers]]"]
related: ["[[embark-studios|엠바크 스튜디오]]", "[[asobo-studio|Asobo]]", "[[small-team-development|소규모 팀 개발]]", "[[multi-project-development|멀티 프로젝트 개발]]", "[[dev-talent-pipeline|개발 인재 파이프라인]]", "[[proprietary-engine-strategy|독자 엔진 전략]]", "[[innersource|이너소스]]", "[[designer-empowerment|디자이너 도구화]]"]
created: 2026-05-18
updated: 2026-05-18
confidence: high
---

**아트 파이프라인 설계**는 캐릭터·환경·이펙트 같은 아트 자산을 *데이터·도구·자동화의 조합*으로 다루는 인프라 설계. AAA 규모를 *인원 추가가 아닌 도구로* 달성하려는 스튜디오들이 5~10년에 걸쳐 누적한 패턴. [[dev-talent-pipeline|인재 파이프라인]]을 *기술 측면*에서 지탱하는 토대 — 도구가 90%를 처리하면 적은 인원으로 많이 만들 수 있고, 그게 곧 *정리해고 없는 개발 사이클*의 전제가 된다.

> 💡 **핵심 인사이트:** [[embark-studios|엠바크]]의 Erik Östsjö·Björn Arvidsson은 *5원칙*을 제시했다 — kit-bash 마인드 / 게임·asset 피드백 분리 / late lock-down / no blockers (procedural이 빈 자리 메꿈) / 90/10 도구화. 이 원칙이 실제 360명으로 The Finals + Arc Raiders + 후속 2개 게임을 *같은 파이프라인*으로 만드는 메커니즘이다.

## 4가지 핵심 원칙

### 1. Kit-bash 모듈러 (vs 모놀리식)

- 캐릭터·환경을 *재조합 가능한 조각의 집합*으로 다룸
- 한 조각 변경이 다른 조각을 깨지 않음 (격리)
- 다른 프로젝트의 조각을 가져와 새 조합 가능 → cross-project 자산 재활용
- Embark: 한 outfit을 backpack·glove·body 등으로 분할

### 2. 피드백 분리 (Game vs Asset)

- *게임 피드백* (밸런스, 게임플레이) ↔ *asset 피드백* (퀄리티, 모델링)을 분리
- 한쪽 변경이 다른 쪽 작업을 깨지 않음
- 결과: 게임 디렉터의 결정과 아트 디렉터의 결정이 *독립 사이클*로 굴러감

### 3. Late Lock-down (Delayed Decision Making)

- texture resolution, UV packing, 최종 piece 조합 같은 결정을 *가능한 한 늦게*
- 같은 asset이 in-game cutscene용 high-res와 in-game용 low-res로 *말기에* 분기
- 원칙: "가능한 한 오래 fluid·flexible 유지"
- 반대 패턴: 초기에 lock-down → 변경 시 재작업 폭주

### 4. 90/10 도구화 (Tools handle 90%, artist 10%)

- 도구가 지루하고 반복적인 부분을 90%까지 처리 (예: 자동 UV layout, auto-matching, batch 재실행)
- 아티스트는 "아티스트답게" — 창의적·심미적 결정에 집중
- 도구가 lock-out하지 않음 — 항상 manual override 경로 (예: viewer state)

## 기술 패턴

### Single Source of Truth (USD layer composition)

- USD = "3D의 PSD" — layer 합성으로 single source 유지
- 한 process가 자기가 신경 쓰는 것만 저장 (예: 색깔만)
- "이 mesh가 업데이트된 거 맞나" 같은 의심 제거
- 한 software에서 변경 → 다른 software가 *자동으로 같은 truth*를 봄 (live link)

### 외부 DCC 통합 (vs 일원화)

- ZBrush·Marvelous·Blender·Substance Painter·Maya 모두 통합
- "한 도구가 모든 걸 해결할 수 없다 — specialized 도구를 버리지 말자"
- 각 DCC에 custom plugin (cleanup, import/export, USD hierarchy 확장)

### PDG 병렬 + Custom Validation

- 변경된 것만 재처리 (native loop는 모두 재처리)
- "가장 빠른 방법은 안 하는 것" — 색깔 변경은 UV 재계산 트리거 안 함
- 각 asset = dot, color = status, warning indicator 명확

### Edit-in-Place

- kit bash 충돌·refine 필요 시 *source asset을 안 건드리고* 그 자리에 node 추가
- 충돌 지점 격리 → disconnect로 원상복구
- 모든 manual 변경을 *deformer*로 처리 → topology·transform에 강건

### Batching (Cross-project 일괄 재처리)

- 새 body type 추가 같은 cross-cutting 변경을 *모든 프로젝트*에 일괄 적용
- 그동안 노드들이 개선되어 있으면 *모든 자산이 무료 quality boost*

## 적용 사례 비교

| 스튜디오 | 도구 | 핵심 메커니즘 | 결과 |
|---|---|---|---|
| [[embark-studios\|Embark]] | Houdini + USD + 외부 DCC | Origins node · USD layer · kit-bash · batching | The Finals + Arc Raiders 같은 파이프라인 공유, 360명 4 게임 목표 |
| [[asobo-studio\|Asobo]] | 포토그래메트리 · 절차적 지형 | 자동화로 인원 부족 보강 | A Plague Tale Requiem AAA 비주얼을 20명 아티스트로 |
| [[sandfall-interactive\|Sandfall]] | UE5 Blueprint | 도구가 코드 작성 대체 | Expedition 33 프로그래머 4명 (Blueprint 95% 사용) |

## 인재 파이프라인과의 관계

- 아트 파이프라인이 [[dev-talent-pipeline|인재 파이프라인]]을 *가능하게* 한다 (필요조건)
- 도구가 90%를 처리하면 → 적은 인원으로 많이 만들 수 있고 → 인원 추가 없이 멀티 프로젝트 가능 → 정리해고 사이클 회피
- 반대: 도구화 없는 멀티 프로젝트 시도는 [[risks-multi-game-development|Double Fine]] 패턴 (6+ 동시, 인력 분산, 생산성 하락)

## 멀티 프로젝트와의 관계

- 같은 파이프라인을 여러 게임이 공유 = [[multi-project-development|멀티 프로젝트]]의 *기술적 실체*
- Embark: Arc Raiders + Finals 차이 = "individual nodes 몇 개"뿐
- cross-project batching으로 *시즌 추가*·*body type 확장* 같은 변경을 동시 적용
- 자원 잠식 위험 감소: 전문가가 한 프로젝트에 묶이지 않고 *파이프라인*에 묶임

## 도구화의 매몰 비용 논리

- 인원 추가 = *매번 새 비용* (퇴직 시 사라짐)
- 도구화 = *매몰 비용* (지금 만들면 다음 프로젝트도 빨라짐)
- Embark Söderlund: "신작마다 인원을 늘리는 회사는 결국 정리해고로 끝난다"
- Asobo·Embark·Sandfall이 다른 길로 도구화를 선택한 공통 이유

## 도입 단계 (Embark의 5년 경험)

1. **Phase 1: Black-box procedural** — 작동할 땐 좋지만 실패 시 refine 불가. 교훈: 손잡이 필요
2. **Phase 2: Box-of-boxes 모듈러** — 자체 Python 앱. 정상 업무와 충돌. 교훈: 도구 자체가 인력 분산 유발
3. **Phase 3: Houdini Solaris (USD 기반)** — 자체 앱 포기, mature한 외부 도구 위에 build. 결과: 안정화

> ⚠️ **단기 도입 시 위험:** 도구 자체가 *full-time 인력*을 요구해서 본업과 충돌. Embark가 자체 앱을 포기한 것처럼, *외부 mature 도구* 위에 build하는 게 도구화 인력 부담을 줄이는 패턴.

## 한국·중소 스튜디오 적용 한계

- Houdini·USD·복수 DCC 통합은 *기술적 학습 비용*이 큼 (5년 누적이 필요)
- 그러나 [[asobo-studio|Asobo]]처럼 *한 가지 자동화* (예: 포토그래메트리)만 도입해도 효과 큼
- [[sandfall-interactive|Sandfall]]처럼 *Blueprint 95%* 같은 단일 도구 전환도 유효
- 핵심: *어떤 도구를 도입할지*가 아니라 *5축 원칙*을 어디든 적용

## 추가 조사 주제

- 도구화 ROI 정량 측정 (도구 개발 시간 vs 향후 절약 시간)
- 한국 게임사 아트 파이프라인 표준화 사례 (넥슨·엔씨·스마일게이트 등)
- USD 한국 도입 현황 — Pixar USD가 게임 업계에서 표준화 진행 중인지
- AI 생성 도구가 아트 파이프라인을 어떻게 변화시킬지 ([[ai-gamedev]]와의 결합)

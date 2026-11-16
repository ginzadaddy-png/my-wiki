---
title: "엠바크 스튜디오 (Embark Studios)"
type: entity
sources: ["[[gdc26-arc-raiders-reset]]", "[[embark-soderlund-quarter-budget]]", "[[multiproject-innersource-report]]", "[[gdc2026-embark-character-pipeline]]", "[[nexon-ir-2q26]]", "[[nexon-ir-3q26]]"]
related: ["[[arc-raiders|아크 레이더스]]", "[[data-driven-development|데이터 기반 개발]]", "[[small-team-development|소규모 팀 개발]]", "[[multi-project-development|멀티 프로젝트 개발]]", "[[art-pipeline-design|아트 파이프라인 설계]]"]
created: 2026-04-13
updated: 2026-11-11
confidence: high
---

스웨덴 스톡홀름 소재 게임 스튜디오. [[nexon|넥슨]] 자회사. DICE(배틀필드 시리즈) 출신 패트릭 수더룬드가 2018년 설립.

| 항목 | 내용 |
|------|------|
| 설립 | 2018년 |
| 위치 | 스웨덴 스톡홀름 |
| 모회사 | [[nexon|넥슨]] |
| 전체 인원 | 약 360명 (2026년 기준) |
| 대표 게임 | [[arc-raiders]], The Finals |
| 주요 장르 | 익스트랙션 슈터 / FPS |
| 누적 판매 | 아크 레이더스 1,700만 장 돌파 (2026년 11월 발표) · 누적 매출 880억엔+ (2026년 6월 말, 이후 미갱신) |

## 개발 철학

**리셋 경험 (2023)**: [[arc-raiders|아크 레이더스]] 개발 중 팀을 120명에서 25명으로 축소하는 극단적 결정을 내림. 기술적으로 완성됐지만 재미없는 게임을 살리기 위한 선택.

**기둥(Pillar) 기반 소통**: 지시 대신 의도와 기둥을 공유 → 팀원이 스스로 해결책을 찾도록 설계. [[vision-statement|비전 선언문]]과 유사하지만 문제 해결 프레임워크로 더 적극 활용.

**데이터 통합**: 데이터 팀을 기능 팀 내부에 통합. 3일 버스트 사이클과 우선순위 바구니 시스템으로 주관적 논쟁을 데이터로 대체. → [[data-driven-development|데이터 기반 개발]] 참고

**AAA 효율화 전략**: "AAA는 규모가 아니라 퀄리티". AAA 예산의 1/4 수준으로 경쟁. 핵심은 AI 도입이 아닌 **파이프라인 재설계** (포토그래메트리, 절차적 지형 생성, 구식 워크플로우 교체). CEO 수더룬드: "600~800명이 될 이유가 없다. 우리가 스튜디오를 시작한 이유를 잊지 않겠다." → [[multi-project-development|멀티 프로젝트 개발]] 참고

**향후 목표**: 4개 게임 포트폴리오(현재 2개). 인원 대폭 증가 없이 달성 목표.

**모회사 전략 언어로 승격** ([[nexon-ir-2q26|넥슨 2Q26 IR]]): 넥슨이 [[arc-raiders|아크 레이더스]]의 성과를 "서구 시장을 여는 재현 가능한 전략의 실증"으로, 엠바크의 소수 인원·신기술 개발 전략을 "넥슨 글로벌 전개의 돌파구"로 공식 규정. [[embark-soderlund-quarter-budget|AAA 예산 4분의 1 전략]]이 자회사 실험에서 그룹 공식 전략으로 올라섰다. THE FINALS도 출시 30개월 이후 시즌 운영으로 매출이 전년보다 증가.

**3분기에는 표현이 한 단계 낮아졌다** ([[nexon-ir-3q26|넥슨 3Q26 IR]]): "재현 가능한 전략"이라는 말은 다시 나오지 않고, Frozen Trail이 "장기 인게이지먼트를 중시하는 엠바크 전략의 유효성을 뒷받침했다"는 평가만 남았다. 배경은 숫자다 — 아크 레이더스 매출이 줄면서 넥슨 북미·유럽 비중이 21% → 10%로 돌아갔고, 3분기 성장은 전부 메이플·FC에서 나왔다. THE FINALS는 Q3 소폭 감소, Q4는 시즌 12로 전년 수준 전망. 한편 넥슨이 전사 인원을 묶는 중에도 유럽 지역 인원은 323 → 384명(+19%)으로 늘었다(유럽 인원이 곧 엠바크라는 설명은 자료에 없다). 이 모델이 재현되는지는 엠바크의 다음 타이틀이 나와야 판정할 수 있다.

**아트 파이프라인 공유 (Houdini + USD)** — [[gdc2026-embark-character-pipeline|GDC26 발표 (Östsjö & Arvidsson)]]:
- **Arc Raiders와 The Finals가 *같은 파이프라인*을 공유**. 차이는 project-specific 노드 몇 개 + wrap system + customization뿐. Unreal engine도 공유
- Houdini Solaris(USD 기반)가 절차적 코어. ZBrush·Marvelous·Blender·Substance Painter·Maya 모두 Origins node로 live link
- USD = "3D의 PSD" — single source of truth, layer 합성으로 한 software 변경이 모두에 자동 전파
- *Kit-bash 마인드*: 캐릭터를 재조합 가능한 조각으로 분할 → cross-project 자산 재활용
- *Batching*: 시즌 6 body type 추가 같은 cross-cutting 변경을 모든 프로젝트에 일괄 적용. 그동안 개선된 노드로 모든 자산이 *무료 quality boost*
- 5년 진화: Black-box procedural → Box-of-boxes 자체 앱 → Houdini Solaris (현재). 자체 앱 포기 이유: "less people로 more" 원칙과 충돌
- 이게 "360명 4 게임 포트폴리오" 목표의 *기술적 실체* → [[art-pipeline-design|아트 파이프라인 설계]] 참고

**오픈소스 우선 철학**: 핵심 언어로 C++ 대신 Rust 채택 (메모리 안전성, 레이스 컨디션 원천 차단). 자체 코어 기술 GitHub 공개 → 외부 커뮤니티 기여 유도. "AAA를 만들기 위해 반드시 수천 명의 인력이 필요하지 않다." → [[innersource|이너소스]] 참고

---
title: "Unreal Engine 5"
type: concept
sources: ["[[expedition33-ue5-interview]]", "[[missing-middle-paradigm-shift-2026]]", "[[gdc26-expedition33-programmers]]", "[[gdc26-hogwarts-evolving-aaa]]", "[[gdc26-newzoo-market-analysis]]", "[[capcom-fy26-ir]]"]
related: ["[[proprietary-engine-strategy|독자 엔진 전략]]", "[[sandfall-interactive|샌드폴 인터랙티브]]", "[[clair-obscur-expedition-33|클레르 옵스퀴르: 33원정대]]", "[[small-team-development|소규모 팀 개발]]", "[[designer-empowerment|디자이너 도구화]]", "[[avalanche-software|Avalanche Software]]", "[[hogwarts-legacy|호그와트 레거시]]", "[[game-market-trends|게임 시장 트렌드]]", "[[proprietary-engine-vs-ue5|자체 엔진 vs UE5 의사결정 매트릭스]]"]
created: 2026-05-18
updated: 2026-05-18
confidence: high
---

**Unreal Engine 5 (UE5)**는 Epic Games가 2022년 공개한 차세대 게임 엔진. *Nanite·Lumen·MetaHuman·Niagara·World Partition*으로 대표되는 고수준 시스템과 *Blueprint 비주얼 스크립팅*이 결합되어 *소규모 팀의 AAA급 비주얼*을 현실 가능하게 만든 *2020년대 중반 게임 산업의 표준 인프라*. 독자 엔진과의 ROI 분기점을 재정의했고, [[game-market-trends|미싱 미들]] 부상의 기술적 토대.

> 💡 **핵심 인사이트:** UE5의 진짜 변화는 *기능*이 아니라 *접근성*이다. *400명 크레딧·30~40명 코어*의 [[clair-obscur-expedition-33|33원정대]]가 *95% Blueprint*로 AAA 비주얼을 만든 사건은 *엔진 진입장벽*이 *팀 규모와 무관*해진 시점의 신호. 동시에 *독자 엔진 ROI 분기점*을 *300명+*로 끌어올린 변수이기도 함.

## 핵심 기술 스택

| 기술 | 영역 | 주요 활용 사례 |
|---|---|---|
| **Nanite** | 가상화된 지오메트리 (수십억 폴리곤 즉시 렌더링) | [[clair-obscur-expedition-33|Expedition 33]] 환경, [[hogwarts-legacy|Hogwarts Legacy]] 건축 |
| **Lumen** | 실시간 전역 조명 (다이내믹 GI·반사) | Expedition 33 시네마틱·동굴, 미싱 미들 게임 비주얼 표준 |
| **MetaHuman** | 사실적 캐릭터·페이셜 애니메이션 | Expedition 33 페이셜 캡처, 시네마틱 인물 |
| **Niagara** | VFX·파티클·시뮬레이션 | Expedition 33 전투 이펙트, 환경 파티클 |
| **World Partition + HLOD** | 오픈월드 스트리밍·LOD 자동 관리 | 광역 오픈월드 게임의 기본 인프라 |
| **Chaos** | 물리·파괴·차량 | (활용 사례 추가 조사 필요) |
| **Blueprint** | 비주얼 스크립팅 | Expedition 33 *게임 로직 95%* |

## [[clair-obscur-expedition-33|클레르 옵스퀴르 33원정대]] — Blueprint 95% 사례

[[expedition33-ue5-interview]]·[[gdc26-expedition33-programmers]]의 핵심 데이터:

- **팀 규모**: 코어 30~40명, 크레딧 400명 (아웃소싱 포함)
- **프로그래머 4명**으로 운영 — *Blueprint 95% + C++ 5%*
- **인터랙티브 뮤직 시스템**: Blueprint 기반. 탐험/전투/시네마틱/메뉴별 자동 음악 전환, 플레이리스트 간 부드러운 크로스페이드
- **페이셜 애니메이션**: MetaHuman Animator + 전신 캡처 + VFX 통합 시네마틱
- **World Partition + HLOD**: 넓은 오픈 월드 최적화, 스트리밍 경계 부드러운 전환
- **성과**: $1,000만 미만 예산, $50 가격, 출시 33일에 330만장, 연말 600만장, TGA 9관왕

> 💡 *"UE5의 고수준 기술들이 소규모 팀에도 접근 가능한 이유는 에픽의 공개 생태계(소스코드·UDN·커뮤니티) 덕분"* — Tom Guillermin

## [[avalanche-software|아발란체]] — [[hogwarts-legacy|호그와트 레거시]] AAA 사례 ([[gdc26-hogwarts-evolving-aaa]])

- *400+명 멀티 스튜디오 협업*에서 UE4→UE5 전환
- Nanite로 *호그와트 성 자체*를 단일 LOD로 표현
- World Partition으로 *전체 오픈월드 동시 협업*
- *팬 IP 게임*에서 UE5는 *환경의 충실도*를 결정하는 핵심 변수

## 서드파티 엔진 ROI 재정의 — [[proprietary-engine-strategy]]와의 관계

UE5 등장으로 *독자 엔진 ROI 분기점*이 위로 이동:

| 스튜디오 규모 | UE5 이전 권장 | UE5 이후 권장 |
|---|---|---|
| ~50명 단일 IP | 서드파티 (Unity 등) | UE5 무수정 (샌드폴 모델) |
| 50~300명 멀티 IP | 트레이드오프 | UE5 + 사내 plug-in 레이어 |
| 300명+ 시리즈 IP | 독자 엔진 (캡콤 RE ENGINE) | 독자 엔진 유지 (캡콤·록스타 RAGE·CDPR REDengine) |
| 차세대 GTA 급 | 독자 엔진 필수 | 독자 엔진 필수 |

> ⚠️ *Asobo Studio 예외*: ~300명이지만 *장르 정체성(중세 사실주의 조명)*이 엔진 인프라가 되어 독자 엔진 유지 ([[gdc2023-asobo-how-to-make-aaa-small-team]]). 규모만으로 결정되지 않는 변수가 있음.

## "엔진 무수정 원칙" — 샌드폴 모델

[[sandfall-interactive|샌드폴]]가 정립한 *UE5 활용 원칙*:
- **버전 업 비용 방지** — Epic이 매년 발표하는 신규 기능을 *추가 작업 없이* 흡수
- **버그 수정 자동** — Epic의 패치가 자동 적용
- **마켓플레이스·서드파티 플러그인 적극** — 개발 속도 확보
- **에픽 소스코드 적극 활용** — *읽기는 하되 수정하지 않기* — 디버깅·이해 자산

[[expedition33-ue5-interview]] 권장: UDN(언리얼 개발자 네트워크), 에픽 소스코드, 커뮤니티 포럼 *적극 활용*.

## Blueprint와 [[designer-empowerment|디자이너 도구화]]

UE5 Blueprint는 [[designer-empowerment]]의 *기술적 인프라*:
- 디자이너가 *프로그래머 없이* 게임 로직 작성 가능
- 프로그래머는 *Blueprint 노드를 C++로 확장*하는 *플랫폼 제공자* 역할
- 33원정대: 4명 프로그래머가 *Blueprint 노드 라이브러리*만 만들면, 30+명 디자이너·아티스트가 *직접 콘텐츠 생산*
- 결과: 소규모 팀 생산성이 *콘텐츠 양*과 분리됨

## 시장 점유 — [[game-market-trends|시장 트렌드]] 변수

[[gdc26-newzoo-market-analysis]]·[[matthew-ball-2026-report]] 추정:
- 2025 기준 *Steam 신규 출시 게임 중 UE5 비중*은 *Unity와 1:1 수준*까지 도달
- AAA 영역에서 UE5 비중 증가 (Avalanche·Sandfall·다수의 미싱 미들 사례)
- 동시에 *Unity가 모바일·인디 우위* 유지 — 분기점은 *그래픽 충실도*

## 한계와 우려

> ⚠️ **공통 함정:**
> 1. *Stutter 문제* — UE5는 셰이더 컴파일 stutter로 출시 게임이 *기술적 평판*에서 깎이는 사례 다수
> 2. *Nanite·Lumen 오용* — 모든 환경을 Nanite로 처리하면 *VRAM 폭증*. 결과: 미들엔드 GPU에서 성능 저하
> 3. *Blueprint 95%의 함정* — 33원정대는 *프로파일링·최적화* 능력으로 Blueprint 비용을 통제. *팀 역량 없이 Blueprint만으로* 만들면 *프레임 드롭*이 출시 후 패치 부담으로
> 4. *Epic 의존성* — Epic 정책 변화·라이선스 변경 시 *대안 없음*. CDPR이 *Witcher 4*를 UE5로 결정한 이후의 산업 결정은 *Epic 의존도*를 더 끌어올림

## 사례 비교

| 게임 | 스튜디오 규모 | UE5 활용 패턴 |
|---|---|---|
| [[clair-obscur-expedition-33|Expedition 33]] | 30~40명 | Blueprint 95% + 무수정 |
| [[hogwarts-legacy]] | 400+명 | UE4→UE5 마이그레이션 + Nanite 적극 |
| [[arc-raiders]] | ~100명 | UE5 + 자체 네트워크 레이어 |
| Black Myth: Wukong | ~140명 | UE5 + 중국 시장 특화 |
| Witcher 4 (개발 중) | CDPR 1,000+명 | REDengine 포기, UE5 채택 결정 — 산업 시그널 |

## 추가 조사 주제

- UE5 Stutter·셰이더 컴파일 문제 — 출시 후 patch로 해결한 케이스 정량 분석
- *Nanite + Lumen* VRAM 부하 — 미들엔드 GPU에서 미싱 미들 게임 frame drop 사례
- *Epic 라이선스* — Unreal Engine 5.x 사용료 정책 변경 이력
- Unity vs UE5 결정 분기 — 인디·중소 스튜디오의 *실제 선택 기준* 인터뷰 수집
- CDPR REDengine 포기 사례 — 독자 엔진 *유지 비용* vs UE5 *전환 비용*의 ROI 비교

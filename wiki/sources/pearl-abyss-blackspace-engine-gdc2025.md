---
title: "펄어비스 블랙스페이스 엔진 GDC 2025 공개 — 인벤 보도"
type: source-summary
source_url: "https://www.inven.co.kr/webzine/news/?news=304278&site=angelstone"
source_author: "이두현 (Inven)"
source_published: 2025-03-24
sources: []
related: ["[[pearl-abyss|펄어비스]]", "[[proprietary-engine-strategy|독자 엔진 전략]]", "[[proprietary-engine-vs-ue5|자체 엔진 vs UE5 의사결정 매트릭스]]", "[[unreal-engine-5|Unreal Engine 5]]", "[[open-world-design|오픈월드 설계]]"]
created: 2026-05-29
updated: 2026-05-29
confidence: high
---

**원문**: [펄어비스 붉은사막의 심장, '블랙스페이스 엔진'](https://www.inven.co.kr/webzine/news/?news=304278&site=angelstone) — 인벤 이두현 기자, 2025-03-24

펄어비스가 GDC 2025에서 차세대 자체 엔진 *블랙스페이스 엔진(Blackspace Engine)*을 미디어에 *최초 공개*. 검은사막 엔진의 후속 *2세대* 엔진으로, *룩앤필·기술 통제·멀티플랫폼 지원* 3대 핵심 가치 아래 개발. *붉은사막*이 첫 상용 검증 사례.

> 💡 **핵심 인사이트:** *상용 엔진이 범용성을 위해 표준화된 틀을 제공*하는 데 반해, 블랙스페이스 엔진은 *펄어비스가 원하는 독특한 스타일과 디테일*을 위한 *맞춤 제작 도구*. *"창작의 자유에 제한을 두지 않도록"*이 설계 방향. *Nanite·Lumen 같은 UE5 표준 기능에 대응되는 자체 솔루션을 다층으로 보유* — 거리 기반 렌더링·심리스 로딩·GPU 물리·FFT 해양·레이 트레이싱·통합 대기 산란까지. 한국 게임사 중 *AAA UE5 표준에 정면 대응하는 자체 엔진*은 거의 유일.

## 3대 핵심 가치

| 가치 | 의미 |
|---|---|
| **룩앤필 (Look & Feel)** | 펄어비스만의 시각적 정체성 |
| **기술에 대한 완전한 통제 (Control of Technology)** | 엔진의 모든 레이어를 자사 통제 — 외부 엔진 라이선스 의존도 zero |
| **멀티플랫폼 지원 (Multi-Platform Support)** | PC·콘솔 cross-platform 동일 베이스 |

## 핵심 기술 스택

| 기술 | 영역 |
|---|---|
| **거리 기반 렌더링 (Distance Rendering)** | draw distance 최적화, 원경 LOD 적용 — "원경 나무도 실제 오브젝트" |
| **심리스 로딩 (Seamless Loading)** | 끊김 없는 광역 오픈월드 |
| **다이내믹 물리 효과** | 충격 세기에 따라 파편 수 변동, 실시간 물리 연산 |
| **GPU 기반 물리 연산** | 머리카락·말 갈기·바람·천 (빨랫줄) 시뮬레이션 |
| **FFT Ocean Simulation** | 파도·조수 사실 표현 |
| **Shallow Water Simulation** | 얕은 수심 — 바위에 부딪히는 잔물 흐름 |
| **Fluid + Froxel Raymarching** | 안개·유체 동적 효과 |
| **레이 트레이싱 (Ray Tracing)** | 창문·등불·난로·날씨 광원 실시간 계산 |
| **Real-time Light Calculation** | 불꽃 일렁임 + 파티클 연동 |
| **Unified Atmospheric Scattering with Volumetric Cloud** | 대기 산란 + 볼륨형 구름 실시간 |
| **Shape Variation** | 나무 형상 변화 — 반복 패턴 방지 |
| **임포스터 → 3D 모델 LOD 전환** | 성능·품질 균형 |

## 시연 핵심 장면

- **파이웰 대륙 스카이다이빙** — 산꼭대기에서 하강, draw distance 최적화로 부드러운 전환 + 원경 디테일
- **전투 물리 효과** — 클리프 공격 → 충격 세기로 파편 수 변동, 방벽 부딪힘 실시간 계산
- **문 파괴** — 나무 조각 패턴이 *애니메이션이 아닌 실시간 물리 연산*
- **머리카락·말 갈기** — GPU 기반 동적 시뮬레이션
- **물·옷 젖음** — 들어갔다 나온 옷의 *젖음 → 마름* 시간 변화 표현
- **레이 트레이싱 광원** — 창문 틈새, 등불, 난로, 불꽃 일렁임에 따른 그림자 실시간

## 검은사막 엔진 → 블랙스페이스 엔진 진화

- *검은사막 엔진(1세대, 2014~)*: MMORPG cross-platform 베이스, PC·모바일·콘솔 동일 적용
- *블랙스페이스 엔진(2세대, 2025-03 GDC 최초 공개)*: 차세대 그래픽 충실도 대응, Nanite·Lumen급 표준 + 펄어비스 자체 솔루션
- "거의 새로 만든 수준" — 2019 지스타 붉은사막 영상 대비 "부끄럽다"고 평가할 정도의 기술적 진화
- 첫 상용 검증 = *붉은사막* — 이후 *도깨비(DokeV)* 등 다른 장르 게임에 적용 예정

## [[unreal-engine-5|UE5]] 표준과의 대응

블랙스페이스 엔진의 기술 스택은 *UE5 Nanite·Lumen·Niagara·World Partition 등 표준 기능에 정면 대응*하는 *자체 솔루션* 구조. 한국 게임사 중 *AAA UE5 표준에 자체 대안을 갖춘 회사*는 *드문 사례* — 대부분 *UE5 라이선스 베이스 + 일부 커스텀*([[nexon|넥슨]] 퍼스트 디센던트·Krafton PUBG·Shift Up 스텔라 블레이드)인 반면, 펄어비스는 *전 layer 자체 통제* 모델.

> ⚠️ **검증 한계:** 본 기사는 *2025-03 GDC 시연 시점*의 정보. *실제 상용 검증*은 *붉은사막 출시 (2026-03 예정)* 이후. 시연 영상의 *충실도가 출시 빌드에 100% 반영*될지는 별개 검증 필요. 펄어비스 *2019 지스타 영상 → 2025 영상*의 *7년 진화*를 보면 *지속 갱신 중 엔진*임이 분명.

## 시사점 — [[proprietary-engine-strategy|자체 엔진 전략]] 관점

1. **5번째 ROI 정당화 모델 검증** — *MMORPG cross-platform + 자체 IP + 자체 엔진* 모델이 *AAA 오픈월드 액션 어드벤처(붉은사막)*로 확장 가능함을 보임. [[catalog-economics|카탈로그]] 측면에서 *검은사막 IP carry + 신규 IP 확장*의 *공통 엔진 인프라*
2. **UE5 시장 점유에 자체 엔진으로 도전** — *Witcher 4 CDPR UE5 전환*과 정반대 시그널. *주권형 자체 엔진* 진영의 *한국 representative*
3. **3대 핵심 가치 (Look&Feel·Tech Control·Multi-Platform)** — *장르 정체성*(Asobo·Remedy)과 *다장르 공유*(캡콤) 사이의 *제3의 정당화 방식*. *"펄어비스 색깔"* 자체를 엔진에 박는 것이 핵심

## 추가 조사 권장

- *2026-03 붉은사막 출시 후* 시연 영상 대비 실제 게임 빌드 충실도 검증
- *DokeV·검은사막 차세대* 적용 시점·구체 차이
- *블랙스페이스 엔진의 모바일 지원* — 검은사막 모바일과 같은 cross-platform 적용 여부
- *GDC 2025 세션 정확한 제목·발표자 명* (인벤 기사는 펄어비스 관계자만 인용)
- *공식 펄어비스 IR·기술 블로그*에 *블랙스페이스 엔진 추가 자료* 확인

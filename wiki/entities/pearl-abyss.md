---
title: "펄어비스 (Pearl Abyss)"
type: entity
sources: ["[[pearl-abyss-blackspace-engine-gdc2025]]"]
related: ["[[proprietary-engine-strategy|독자 엔진 전략]]", "[[proprietary-engine-vs-ue5|자체 엔진 vs UE5 의사결정 매트릭스]]", "[[unreal-engine-5|Unreal Engine 5]]", "[[live-service-design|라이브 서비스 설계]]", "[[catalog-economics|카탈로그 이코노믹스]]", "[[multi-project-development|멀티 프로젝트 개발]]", "[[mobile-gamedev|모바일 게임 개발]]", "[[dev-talent-pipeline|개발 인재 파이프라인]]", "[[game-market-trends|게임 시장 트렌드]]"]
created: 2026-05-29
updated: 2026-05-29
confidence: medium-high
relations:
  parentOf: []
---

**펄어비스 (Pearl Abyss)**는 2010 한국 안양 본사 설립, 창업자 김대일(Daeil Kim). 2017 KOSDAQ 상장(263750). [[proprietary-engine-strategy|독자 엔진 전략]]의 *한국 케이스이자 MMORPG 진영의 정점 사례* — *Black Desert Engine* 자체 개발, *PC·모바일·콘솔 cross-platform*에 동일 엔진 적용. CCP Games 인수(2018, $425M)로 *EVE Online IP 확보*, *멀티 IP 포트폴리오* 진입.

> 💡 **핵심 포지셔닝:** *MMORPG 자체 엔진 + cross-platform 적용*의 검증 사례. [[capcom|캡콤]]·[[fromsoftware|프롬소프트]]·[[remedy-entertainment|Remedy]]의 *AAA 자체 엔진* 모델과 달리 *MMORPG 라이브 서비스 + 자체 엔진*이라는 *제5의 카테고리*. *검은사막 엔진(Black Desert Engine)*은 *2014 출시 시점에 한국 MMO에서 드물게 콘솔급 비주얼*을 보였고, *모바일·콘솔 포팅*에서도 *동일 엔진 베이스*를 유지. 차세대 *블랙스페이스 엔진(Blackspace Engine)*은 2025-03 GDC 2025에서 미디어 최초 공개, *룩앤필·기술 통제·멀티플랫폼 지원* 3대 핵심 가치 아래 *붉은사막* 첫 상용 검증, 이후 *DokeV* 등 적용 예정.

## 핵심 데이터

| 항목 | 수치 |
|---|---|
| 설립 | 2010 (한국 안양) |
| 창업자 | 김대일 (Daeil Kim) |
| 상장 | KOSDAQ 2017 (263750) |
| 직원 수 | 약 1,500명+ (2024 기준 외부 추정) |
| 주력 IP | 검은사막 (Black Desert) — PC·모바일·콘솔 멀티 플랫폼 |
| 자회사 | CCP Games (2018-09 인수, $425M) — EVE Online |
| 검은사막 PC 누적 (한국) | 2,800만+ 등록 계정 (2023 추정) |
| 검은사막 글로벌 누적 매출 (외부 추정) | $2B+ (시리즈 전체) |

## 주요 작품

| 게임 | 출시 | 플랫폼 | 비고 |
|---|---|---|---|
| **검은사막 PC** | 2014-12 (한국) / 2016-03 (글로벌) | PC | MMORPG, 한국 외 100+ 국가 서비스 |
| 검은사막 모바일 | 2018-02 | iOS·Android | 모바일 동일 엔진 포팅 |
| 검은사막 콘솔 | 2019 (PS4·XB1) / 2025 (PS5·XSX) | 콘솔 | cross-platform 동일 베이스 |
| Shadow Arena | 2020 | PC | BR 모드, 2022 종료 |
| EVE Online (CCP) | 2003 운영 | PC | 2018 인수 |
| **붉은사막 (Crimson Desert)** | 2026-03 예정 | PC·콘솔 | *블랙스페이스 엔진* 첫 상용 검증, 오픈월드 액션 어드벤처 |
| **DokeV (도깨비)** | 미정 | PC·콘솔 | 오픈월드 어드벤처 |
| 검은사막 후속 (가칭 BD2) | 미정 | TBA | 차세대 IP |

## 자체 엔진 전략 — 검은사막 엔진 → 블랙스페이스 엔진

[[proprietary-engine-strategy|독자 엔진 전략]] 페이지의 *한국 MMORPG 케이스*:

### 검은사막 엔진 (Black Desert Engine, 1세대, 2014~)
- *C++ 기반 in-house 엔진* — 2010~2014 4년 R&D
- *액션 MMORPG에 최적화* — 논타겟팅 전투·캐릭터 모델 충실도·캐릭터 커스터마이징(*세계 최고 수준*으로 평가받음)
- *PC·모바일·콘솔 동일 베이스* — 2018 모바일·2019 콘솔 포팅 시 *동일 엔진 base + 플랫폼 layer 분리* 모델
- *MMO 서버 인프라 통합* — 클라이언트 엔진 + 서버 인프라가 *동일 R&D 조직*에서 통합 개발
- *10년 라이브 서비스* 동안 *지속 엔진 갱신* — 신규 지역·캐릭터·클래스가 *엔진 능력 확장*에 직결

### 블랙스페이스 엔진 (Blackspace Engine, 2세대, 2025-03 GDC 최초 공개) — [[pearl-abyss-blackspace-engine-gdc2025|인벤 보도]]

**3대 핵심 가치:**
- **룩앤필 (Look & Feel)** — 펄어비스만의 시각적 정체성
- **기술에 대한 완전한 통제 (Control of Technology)** — 엔진 전 layer 자사 통제
- **멀티플랫폼 지원 (Multi-Platform Support)** — PC·콘솔 cross-platform 동일 베이스

**핵심 기술 스택 (UE5 Nanite·Lumen 표준에 정면 대응):**

| 기술 | 영역 |
|---|---|
| 거리 기반 렌더링 (Distance Rendering) | draw distance 최적화 + 원경 LOD — "원경 나무도 실제 오브젝트" |
| 심리스 로딩 (Seamless Loading) | 끊김 없는 광역 오픈월드 |
| 다이내믹 물리 효과 | 충격 세기에 따라 파편 수 변동, 실시간 물리 연산 |
| GPU 기반 물리 연산 | 머리카락·말 갈기·바람·천 시뮬레이션 |
| FFT Ocean Simulation | 파도·조수 사실 표현 |
| Shallow Water Simulation | 얕은 수심·잔물 흐름 |
| Fluid + Froxel Raymarching | 안개·유체 동적 효과 |
| 레이 트레이싱 (Ray Tracing) | 창문·등불·난로·날씨 광원 실시간 |
| Real-time Light Calculation | 불꽃 일렁임 + 파티클 연동 |
| Unified Atmospheric Scattering + Volumetric Cloud | 대기 산란·볼륨형 구름 실시간 |
| Shape Variation | 나무 형상 변화 — 반복 패턴 방지 |
| 임포스터 → 3D 모델 LOD 전환 | 성능·품질 균형 |

**검증 시점:**
- 2025-03 GDC 2025에서 *미디어 최초 공개* — 펄어비스가 엔진 성능을 미디어에 직접 공개한 첫 사례
- *붉은사막*이 *첫 상용 검증* 사례, 출시 2026-03 예정
- 이후 *DokeV* 등 다른 장르 게임에 적용 예정
- "2019 지스타 붉은사막 영상을 *부끄럽다*고 평가할 정도" — *7년 기술 진화*

**[[unreal-engine-5|UE5]]와의 관계:** UE5 Nanite·Lumen·Niagara·World Partition 등 표준 기능에 *정면 대응하는 자체 솔루션*. 한국 게임사 중 *AAA UE5 표준에 자체 대안을 갖춘 회사*는 드문 사례. [[capcom|캡콤]] RE Framework→RE ENGINE 전환과 *2세대 엔진 전환 패턴* 유사.

## MMORPG 라이브 서비스 + 자체 엔진 결합 ROI

[[live-service-design|라이브 서비스 설계]]·[[catalog-economics|카탈로그 이코노믹스]] 관점에서 *MMORPG catalog 모델*의 자체 엔진 ROI 정당화:

1. **10년+ 라이브 서비스** — *catalog economics 진입 조건*인 *long product life 5년+* 충족
2. **글로벌 100+ 국가 서비스** — *지역별 서버·번역·결제 인프라*가 *자체 엔진 통제*로 통합 운영
3. **PC·모바일·콘솔 동일 자산** — *cross-platform 자산 재활용*이 *자체 엔진 마진 극대화*의 기반
4. **MMO 서버 인프라 동시 통제** — *클라이언트 + 서버*가 *동일 엔진 generation*에서 통합 개발 → *외부 엔진(UE5 등) 도입 시 서버 인프라와 분리* 어려움
5. **catalog 매출 모델** — 검은사막 단일 IP가 *10년+ 매출 carry*, 자체 엔진 R&D 비용을 *시간축*으로 회수

> ⚠️ **다른 catalog 4모델과의 분기**: [[catalog-economics-3-publishers|캡콤·닌텐도·Take-Two 3사 비교]]에서 *MMO recurrent 모델은 별개 5번째 모델*로 분류 권장됨. 펄어비스 검은사막이 그 표본 — *PC·모바일·콘솔 cross-platform 라이브 서비스 + 자체 엔진 + 단일 IP carry* 결합 모델.

## CCP Games 인수 (2018) — 멀티 IP 진입

- 2018-09 *$425M 전액 현금 인수* — *아이슬란드 CCP Games (EVE Online 운영)*
- *목적*: ① EVE Online IP 확보 ② SF MMO 노하우 ③ 글로벌 운영 인프라
- *결과*: EVE Online 서비스 지속 + 펄어비스의 *멀티 IP 포트폴리오* 진입 ([[multi-project-development|멀티 프로젝트 개발]] 모델)
- *Cash 흐름 risk*: 인수 후 *현금 자산 감소*, 2018~2020 *주가 변동성 큼*
- *시너지 한계*: EVE Online과 검은사막의 *플레이어 base·운영 모델 분리* — *공통 인프라 활용 어려움*

## 시그니처 차별점

1. **세계 최고 수준 캐릭터 커스터마이징** — 검은사막 출시 시점부터 *얼굴 슬라이더·체형 조각*이 *2014 기준 산업 최고*. 12년 후에도 *벤치마크 위치 유지*
2. **논타겟팅 액션 MMORPG** — 클릭형 한국 MMO 전통과 차별화, *콘솔·모바일 cross-platform 호환성*의 기반
3. **자체 엔진 자체 IP 자체 운영** — *3축 수직 통합*이 한국 게임사 중 *드문 패턴* (NCSoft 리니지·넥슨 메이플 등도 자체 엔진이나 *AAA 콘솔 cross-platform*는 약함)
4. **PC·모바일·콘솔 동시 IP 운영** — *모바일 + 콘솔 cross-platform*은 *원신 (HoYoverse)*과 *한국 진영 비교 짝* 가능

## risk

> ⚠️ **risk:**
> 1. *블랙스페이스 엔진 상용 검증 미완* — 2025-03 GDC 시연 영상은 공개됐으나 *실제 상용 빌드 충실도*는 *2026-03 붉은사막 출시 후* 검증. 시연 영상 대비 출시 빌드 *충실도 다운그레이드* risk
> 2. *붉은사막 다년 지연* — 2019 첫 공개 후 *6년 누적 지연*. *cash flow 부담* (검은사막 매출에 전적 의존)
> 3. *MMORPG 시장 성숙기* — 한국 MMO 시장이 *원신·로블록스·신규 장르*에 점유 잠식. *검은사막 매출 정체* 가능성
> 4. *CCP Games 시너지 미흡* — 인수 6년차에도 *공통 인프라 활용 사례 부재*. *인수 ROI 검증 어려움*
> 5. *EU·미국 규제* — 한국 MMO의 *확률형 아이템 규제* 강화 시 *글로벌 매출 충격*

## 비교 — 자체 엔진 진영 사례별

| 스튜디오 | 엔진 | 규모 | 핵심 ROI 정당화 |
|---|---|---|---|
| [[capcom\|캡콤]] | RE ENGINE | 2,500명+ | 다장르 IP 공유 |
| [[remedy-entertainment\|Remedy]] | Northlight | ~380명 | 장르 정체성 인프라 |
| [[asobo-studio\|Asobo]] | 인하우스 | ~300명 | 장르 정체성 인프라 |
| [[rockstar-games\|Rockstar]] | RAGE | 2,000명+ | 오픈월드 스케일 |
| **Pearl Abyss** | **검은사막 엔진 → 블랙스페이스 엔진** | **~1,500명** | **MMORPG cross-platform + 라이브 서비스 + 자체 IP** |
| [[fromsoftware\|FromSoftware]] | 자체 엔진 | ~300명 | 소울 시리즈 통일 게임 필감 |

펄어비스는 *MMORPG 라이브 서비스* 카테고리의 *유일한 자체 엔진 representative*. *AAA 콘솔 진영*과 다른 *5번째 ROI 정당화 모델*.

## 한국 게임사 비교 — 자체 엔진 보유 측면

| 회사 | 자체 엔진 | cross-platform 적용 |
|---|---|---|
| **펄어비스** | 검은사막 엔진 · 블랙스페이스 엔진 | PC·모바일·콘솔 동일 베이스 |
| NCSoft | 혼용 | 리니지·TL·아이온 각각 분기, *통합 엔진 약함* |
| [[nexon\|넥슨]] | 자회사별 혼용 | [[embark-studios\|엠바크]] UE5, [[mint-rocket\|민트로켓]] Unity, 퍼스트 디센던트 UE5 |
| Krafton | UE 베이스 | PUBG UE4·UE5 |
| Shift Up | UE 베이스 | 스텔라 블레이드 UE4 |

펄어비스는 *한국 메이저 중 가장 일관된 자체 엔진 cross-platform 전략* — *NCSoft가 IP별 분리 혼용*, *Krafton/Shift Up이 UE 베이스*인 환경에서 *수직 통합 자체 엔진 모델*을 *유지*.

## 관련 위키 페이지

- [[proprietary-engine-strategy|독자 엔진 전략]] — 자체 엔진 ROI 정당화 모델
- [[proprietary-engine-vs-ue5|자체 엔진 vs UE5 의사결정 매트릭스]] — Pearl Abyss는 *MMORPG 라이브 서비스 + 자체 엔진* 카테고리
- [[multi-project-development|멀티 프로젝트 개발]] — CCP 인수 + 붉은사막·DokeV·검은사막 멀티 IP
- [[catalog-economics|카탈로그 이코노믹스]] — MMO recurrent 5번째 모델
- [[live-service-design|라이브 서비스 설계]] — 검은사막 10년+ 운영
- [[mobile-gamedev|모바일 게임 개발]] — 모바일·콘솔 cross-platform 모델

## 추가 조사

- *블랙스페이스 엔진 모바일 지원 여부* — 검은사막 모바일 후속작이 *블랙스페이스 엔진 기반*인지 검은사막 엔진 유지인지
- *붉은사막 출시 후 블랙스페이스 엔진 상용 빌드 충실도* — GDC 2025 시연 영상 대비 출시 빌드 (2026-03 이후 검증)
- *DokeV (도깨비)* 출시 시점·블랙스페이스 엔진 적용 디테일
- *검은사막 한국 외 매출 분포* (북미·유럽·일본·동남아) — 펄어비스 IR 분기 보고
- *CCP Games 인수 6년차 ROI* 정량 분석 (EVE Online 매출 추이·시너지)
- *NCSoft·넥슨·Krafton과의 한국 MMO 엔진 전략 비교* — 별도 비교 페이지 가치
- *GDC 2025 펄어비스 발표 세션 정확한 제목·발표자 명* — 인벤 기사는 펄어비스 관계자만 인용, 공식 GDC vault 자료 확인 권장

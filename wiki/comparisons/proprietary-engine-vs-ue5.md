---
title: "자체 엔진 vs UE5 — 의사결정 매트릭스"
type: comparison
sources: ["[[capcom-ir2021-dev-strategy]]", "[[capcom-fy26-ir]]", "[[re2023-re-engine-philosophy]]", "[[expedition33-ue5-interview]]", "[[gdc26-expedition33-programmers]]", "[[gdc26-hogwarts-evolving-aaa]]", "[[gdc2023-asobo-how-to-make-aaa-small-team]]", "[[pearl-abyss-blackspace-engine-gdc2025]]"]
related: ["[[proprietary-engine-strategy|자체 엔진 전략]]", "[[unreal-engine-5|Unreal Engine 5]]", "[[capcom|캡콤]]", "[[sandfall-interactive|샌드폴 인터랙티브]]", "[[asobo-studio|Asobo Studio]]", "[[remedy-entertainment|Remedy Entertainment]]", "[[avalanche-software|Avalanche Software]]", "[[pearl-abyss|펄어비스]]", "[[small-team-development|소규모 팀 개발]]", "[[multi-project-development|멀티 프로젝트 개발]]"]
created: 2026-05-29
updated: 2026-05-29
confidence: high
---

자체 엔진과 UE5 양 진영의 트레이드오프를 *스튜디오 규모·타이틀 다양성·장르 정체성* 세 축으로 정리한 의사결정 매트릭스. [[proprietary-engine-strategy|독자 엔진 전략]]과 [[unreal-engine-5|UE5]] 두 개념의 *시간축 짝* — UE5 등장 이후 ROI 분기점이 어떻게 이동했는가가 핵심 변화.

> 💡 **핵심 인사이트:** 엔진 선택은 *기술 우열* 문제가 아니라 *ROI 분기점* 문제다. UE5 이전엔 50명도 자체 엔진을 만지작거렸지만, 2025년 기준 *300명 + 시리즈 IP*가 자체 엔진 ROI의 새 임계선. 그 이하는 UE5 무수정이 합리적이고, 그 이상에서도 *장르 정체성 인프라*가 아니면 전환 압력이 커진다. CDPR의 [[unreal-engine-5|REDengine → UE5]] 결정이 산업 시그널.

## 핵심 비교 표

| 변수 | 자체 엔진 | UE5 무수정 (샌드폴 모델) |
|---|---|---|
| **초기 투자** | 수년 R&D ([[capcom|캡콤]] RE ENGINE: RE7까지 다년) | 즉시 가동, 라이선스 + 5% 로열티 |
| **유지 비용** | 플랫폼 변화·렌더링 트렌드마다 자체 갱신 | Epic이 자동 갱신, 버전업 흡수 |
| **하드웨어 최적화** | 플랫폼별 극대화 가능 (MH Rise 끊김 없는 협동) | Nanite·Lumen 최적화는 Epic이 담당 |
| **장르 통합성** | 시리즈 IP·다장르 공유 ([[capcom\|캡콤]] RE·MH·SF) | 마켓플레이스·플러그인 활용 |
| **인재 의존도** | 엔진 인력 영구 필요 ([[capcom\|캡콤]] R&D 기반기술부) | 일반 UE5 개발자 채용 가능 |
| **버그·셰이더 stutter** | 자체 책임, 수정 가능 | Epic 패치 대기, *공통 stutter 함정* |
| **시장 시그널·평판** | "기술 회사" 포지셔닝 (Rockstar RAGE·Remedy Northlight) | "콘텐츠 회사" 포지셔닝 |
| **출시 후 갱신 비용** | 자체 인력으로 무한 갱신 ([[capcom\|캡콤]] 카탈로그 9년 곡선 가능) | Epic 의존, 라이선스 변경 시 *대안 없음* |
| **장르 정체성 구현** | 가능 ([[asobo-studio\|Asobo]] 중세 사실주의·[[remedy-entertainment\|Remedy]] 심리 호러) | *고수준 추상화*가 정체성을 흐릴 수 있음 |
| **디자이너 도구화** | 자체 에디터 ([[asobo-studio\|Asobo]] 계층형 에디터) | Blueprint ([[clair-obscur-expedition-33\|33원정대]] 95%) |

## ROI 분기점 — UE5 이전 vs 이후

| 스튜디오 규모 | UE5 이전 권장 | UE5 이후 권장 |
|---|---|---|
| **~50명 단일 IP** | 서드파티 (Unity 등) | **UE5 무수정** ([[sandfall-interactive\|샌드폴]] 모델) |
| **50~300명 멀티 IP** | 트레이드오프 영역 | **UE5 + 사내 plug-in 레이어** |
| **300명+ 시리즈 IP** | 자체 엔진 ([[capcom\|캡콤]] RE ENGINE) | *자체 엔진 유지* — 단 *전환 압력 증가* |
| **차세대 GTA·Witcher 급** | 자체 엔진 필수 | *Rockstar는 RAGE 유지, [[cd-projekt-red\|CDPR]]는 UE5 전환* |

UE5 등장의 핵심 결과: **분기점이 위로 이동**. ~50명에서 *자체 엔진 시도 자체가 사라지고*, 300명+에서도 *전환 압력이 형성*된다.

## 자체 엔진 진영 — 사례별 위치

| 스튜디오 | 엔진 | 핵심 ROI 정당화 |
|---|---|---|
| [[capcom\|캡콤]] (2,500명+) | RE ENGINE | *다장르 공유* — RE·MH·SF·DMC 한 엔진으로 통합. [[capcom-fy26-ir\|FY26·3]] 카탈로그 83.7% 매출 |
| [[remedy-entertainment\|Remedy]] (~380명) | Northlight | *장르 정체성* — 심리 호러·꿈의 논리·초자연적 조명을 엔진이 인프라화 |
| [[asobo-studio\|Asobo]] (~300명) | 인하우스 | *장르 정체성* — 중세 사실주의 조명·환경. Decals·Volumetric Fog·POM 자체 추가 |
| Rockstar | RAGE | *오픈월드 스케일* — GTA·RDR 동시 가능한 단일 인프라 |
| 코지마 ([[kojima-productions\|KojiPro]]) | Decima (Guerrilla 공유) | *Decima 공유 모델* — 자체 엔진의 *셰어드* 변형 |
| [[fromsoftware\|프롬소프트]] | 자체 엔진 | *소울 시리즈* 통일된 게임 필감 — 엔진과 디자인 분리 어려움 |
| [[pearl-abyss\|펄어비스]] (~1,500명) | **검은사막 엔진 → 블랙스페이스 엔진** (2025-03 GDC 공개) | ***MMORPG cross-platform 라이브 서비스 + 자체 IP*** — PC·모바일·콘솔 동일 베이스, MMO 서버 인프라 통합 통제. 검은사막 10년 catalog로 R&D 회수. 블랙스페이스 엔진은 *Nanite·Lumen 표준에 정면 대응* (거리 기반 렌더링·FFT 해양·레이 트레이싱·통합 대기 산란 등). [[pearl-abyss-blackspace-engine-gdc2025\|GDC 2025 시연]] |

## UE5 진영 — 사례별 위치

| 스튜디오·게임 | 팀 규모 | UE5 활용 패턴 |
|---|---|---|
| [[sandfall-interactive\|샌드폴]] / [[clair-obscur-expedition-33\|Expedition 33]] | 30~40명 | *Blueprint 95% + 무수정* — $1,000만 미만 예산, $50 가격, TGA 9관왕 |
| [[avalanche-software\|아발란체]] / [[hogwarts-legacy\|호그와트 레거시]] | 400+명 | *UE4→UE5 마이그레이션* — Nanite로 호그와트 성 단일 LOD |
| [[embark-studios\|엠바크]] / [[arc-raiders\|아크 레이더스]] | ~100명 | *UE5 + 자체 네트워크 레이어* — 익스트랙션 슈터 인프라 |
| Game Science / Black Myth: Wukong | ~140명 | *UE5 + 중국 시장 특화 * |
| [[cd-projekt-red\|CDPR]] / Witcher 4 (개발 중) | 1,000+명 | *REDengine 포기, UE5 채택 결정* — 산업 시그널 |

## 세 가지 *예외 변수* — 규모 단독으로 결정되지 않는 케이스

### 1. 장르 정체성이 엔진을 결정할 때 ([[asobo-studio|Asobo]]·[[remedy-entertainment|Remedy]])
중간 규모(~300~400명)지만 자체 엔진 유지. *장르 정체성(중세 사실주의·심리 호러)이 엔진 인프라*가 될 때 ROI 산식이 달라진다. Asobo 인하우스 엔진은 "[[a-plague-tale-requiem|A Plague Tale]] 등불·중세 환경"의 *시각적 정체성 도구*. Remedy Northlight은 "[[alan-wake-2|Alan Wake 2]] 꿈의 논리"의 *연출 인프라*.

### 2. 멀티 IP·시리즈 IP 카탈로그 ([[capcom|캡콤]])
자체 엔진 ROI는 *카탈로그 곡선*과 연동. 캡콤 RE ENGINE은 RE7(2017)~MH Wilds(2025) 9년에 걸쳐 *다장르 IP*를 통합 갱신. *카탈로그 매출 83.7%* 모델이 *엔진 유지 비용*을 정당화. [[catalog-economics|카탈로그 이코노믹스]]와 직결.

### 3. *Epic 의존성* — UE5의 숨은 비용
UE5 라이선스·정책 변화 시 *대안 없음*. CDPR이 [[cd-projekt-red|REDengine 포기 + UE5 채택]]을 결정한 후 *산업 전체의 Epic 의존도*가 상승. 자체 엔진 진영은 *주권* 측면에서 *전략적 자산*으로 평가받기 시작.

### 4. *MMORPG 라이브 서비스 + 서버 인프라* 통제 ([[pearl-abyss|펄어비스]])
*5번째 ROI 정당화 카테고리*. *MMO 서버 인프라*는 *클라이언트 엔진과 분리 불가능*한 영역 — *외부 엔진(UE5 등) 도입 시 서버 인프라 호환성 문제*가 *자체 엔진 유지를 정당화*. [[pearl-abyss|펄어비스]] 검은사막 엔진(1세대)·블랙스페이스 엔진(2세대, [[pearl-abyss-blackspace-engine-gdc2025|2025-03 GDC 공개]])은 *PC·모바일·콘솔 동일 베이스 cross-platform + MMO 서버 통합 운영* 결합. *NCSoft·넥슨이 IP별 엔진 분리·플랫폼 분리 운영*인 한국 환경에서 *드문 수직 통합 모델*.

## 의사결정 흐름도

```
신규 프로젝트
   ↓
스튜디오 규모?
   ├─ ~50명 → UE5 무수정 (또는 Unity)
   ├─ 50~300명 → UE5 + 부분 수정 (필요시 plug-in)
   └─ 300명+ ↓
        MMORPG·라이브 서비스 + 자체 서버 인프라인가?
           ├─ YES (펄어비스) → 자체 엔진 유지 (서버 인프라 통합 통제)
           └─ NO ↓
                장르 정체성이 엔진 인프라가 필요한가?
                   ├─ YES (Remedy·Asobo) → 자체 엔진 유지
                   └─ NO ↓
                        멀티 IP·카탈로그 모델인가?
                           ├─ YES (캡콤) → 자체 엔진 유지
                           └─ NO (단일 IP) → UE5 전환 검토 (CDPR 시그널)
```

## 공통 함정 — 양 진영에 적용

| 함정 | 자체 엔진 진영 | UE5 진영 |
|---|---|---|
| **유지 비용 과소평가** | 플랫폼 변화·렌더링 트렌드마다 자체 갱신 | Epic 라이선스 변경·정책 리스크 |
| **인재 의존성** | 엔진 인력 이탈 시 *대체 어려움* | Blueprint 95% 함정 — *프로파일링·최적화 능력* 필수 |
| **셰이더 stutter** | 자체 책임 | UE5 공통 stutter, *출시 후 patch 부담* |
| **비주얼 통일성 vs 일반화** | 장르 정체성 강하지만 *다른 장르 어려움* | Lumen·Nanite 활용 표준화 시 *비주얼 차별화 압력* |

## 시사점

엔진 결정은 *세 축*의 교차점이다:

1. **규모** — *50명·300명·1,000명*에서 ROI 산식이 다름
2. **타이틀 다양성** — *단일 IP·시리즈 IP·멀티 IP*에서 카탈로그 곡선이 다름
3. **장르 정체성** — *엔진이 정체성 인프라인가, 게임 콘텐츠 도구인가*

세 축이 모두 *자체 엔진* 방향을 가리킬 때만 *자체 엔진 ROI*가 정당화. 그 외엔 UE5 무수정이 *기본값*. 한국 인디·중견 스튜디오는 *50~300명 구간*에 다수 위치 — *UE5 + 부분 수정*이 default 권장.

### 한국 메이저 — 자체 엔진 vs UE5 분기

| 회사 | 엔진 전략 | 정당화 |
|---|---|---|
| [[pearl-abyss\|펄어비스]] | **자체 엔진 (검은사막·블랙스페이스)** | MMORPG cross-platform + 서버 인프라 통합, 2025-03 GDC에서 블랙스페이스 엔진 공개 |
| NCSoft | 혼용 | 리니지·TL·아이온 각각 분기, *통합 엔진 약함* |
| [[nexon\|넥슨]] | 자회사별 혼용 | [[embark-studios\|엠바크]] UE5, [[mint-rocket\|민트로켓]] Unity, 퍼스트 디센던트 UE5 |
| Krafton | UE 베이스 | PUBG UE4·UE5 |
| Shift Up | UE 베이스 | 스텔라 블레이드 UE4 |

펄어비스는 한국 메이저 중 *가장 일관된 자체 엔진 수직 통합 모델*. NCSoft·넥슨이 *IP·자회사별 분리 운영*인 환경에서 *예외 사례*.

## 관련 분석

- [[proprietary-engine-strategy|독자 엔진 전략]] — 자체 엔진 진영의 상세 ROI 분석
- [[unreal-engine-5|Unreal Engine 5]] — UE5 기술 스택과 활용 패턴
- [[catalog-economics|카탈로그 이코노믹스]] — *카탈로그 매출 모델*이 자체 엔진 ROI를 정당화하는 메커니즘
- [[multi-project-development|멀티 프로젝트 개발]] — *엔진 공유*가 멀티 프로젝트의 *기술 인프라*가 되는 방식

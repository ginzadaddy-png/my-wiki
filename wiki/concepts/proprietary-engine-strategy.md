---
title: "독자 엔진 전략"
type: concept
sources: ["[[capcom-ir2021-dev-strategy]]", "[[re2023-re-engine-philosophy]]", "[[expedition33-ue5-interview]]", "[[gdc2023-asobo-how-to-make-aaa-small-team]]", "[[pearl-abyss-blackspace-engine-gdc2025]]"]
related: ["[[capcom|캡콤]]", "[[sandfall-interactive|샌드폴 인터랙티브]]", "[[asobo-studio|Asobo Studio]]", "[[remedy-entertainment|Remedy Entertainment]]", "[[pearl-abyss|펄어비스]]", "[[small-team-development|소규모 팀 개발]]", "[[proprietary-engine-vs-ue5|자체 엔진 vs UE5 의사결정 매트릭스]]"]
created: 2026-04-14
updated: 2026-04-14
confidence: high
---

자체 게임 엔진을 개발·유지하는 전략. 개발 비용 절감과 품질 통제 사이의 트레이드오프를 중심으로, 스튜디오 규모에 따라 전혀 다른 결론에 도달한다.

## 독자 엔진의 이점 (캡콤 RE ENGINE 모델)

- **하드웨어 최적화**: 플랫폼별 성능 극대화 가능 (MH라이즈의 끊김 없는 협동 플레이)
- **기술 공유**: 레지던트 이블(공포), 몬스터 헌터(협동 액션), 스트리트 파이터(격투) 등 완전히 다른 장르에 같은 엔진 적용 → 기술 인력이 타이틀 경계를 넘어 협업
- **집중 환경**: 엔진 문제가 아닌 게임 내용에 집중할 수 있는 환경 제공
- **지속적 진화**: 게임 팀의 피드백이 엔진 개선으로 직접 연결

**조직 구조**: 캡콤은 R&D 기반기술부(엔진팀)와 타이틀 개발팀을 분리. 관리 유닛이 인터페이스로 중간에서 조율 → 엔진 팀이 특정 타이틀에 종속되지 않고 장기 발전 가능

## 독자 엔진의 비용과 한계

- **초기 투자**: RE ENGINE도 RE7까지 수년의 개발 기간 필요
- **유지 비용**: 플랫폼 변화마다 엔진도 업데이트해야 함
- **규모 필요**: 소규모 스튜디오에는 현실적으로 불가능

## 서드파티 엔진 활용 (샌드폴 모델 — 대안)

[[sandfall-interactive|샌드폴 인터랙티브]] (~40명)는 반대 전략을 택했다:
- UE5를 수정하지 않고 그대로 사용 → 버전 업 비용 방지, 최신 버그 수정 자동 획득
- "엔진에 손대지 않기"가 원칙 → 루멘·나나이트 등 UE5 고수준 기능을 한계까지 활용
- 마켓플레이스·서드파티 플러그인 적극 활용으로 개발 속도 확보

> ⚠️ **트레이드오프**: 캡콤(독자 엔진)과 샌드폴(서드파티 엔진 무수정)은 정반대 전략이지만 둘 다 성공했다. 결정 요인은 **스튜디오 규모**와 **타이틀 다양성**. 300명+ 멀티타이틀 스튜디오는 독자 엔진이 ROI가 나오지만, 40명 단일 타이틀 스튜디오는 서드파티 무수정이 더 효율적.

## 중간 규모 독자 엔진 — Asobo Studio

[[asobo-studio|Asobo Studio]]는 캡콤(2,500명)보다 훨씬 작지만 자체 엔진을 2002년부터 유지한다. [[a-plague-tale-requiem|A Plague Tale: Requiem]] 개발 시:

- 언론은 Unreal Engine으로 오보했지만 실제는 Asobo 인하우스 엔진
- 계층형 에디터 + 커스텀 기능·단축키로 소규모 팀 생산성 최적화
- 게임 개발 중 필요한 기능을 직접 추가: Decals · Ocean · Volumetric Fog · POM
- 장르 정체성(중세 사실주의 조명·환경)에 최적화된 렌더링 파이프라인

Asobo 모델의 시사점: 독자 엔진이 꼭 대형 스튜디오만의 선택지는 아니다. 엔진이 게임의 **장르 정체성 구현 도구**가 될 때, 투자 대비 효과가 규모를 넘어설 수 있다.

> 💡 **핵심 인사이트:** 엔진 전략의 핵심 질문은 "우리가 엔진을 통제할 것인가, 엔진이 우리를 도울 것인가"가 아니다. "이 투자가 우리 규모와 목표에 ROI가 나오는가"다. Asobo는 여기에 하나를 더한다: **엔진이 장르 정체성의 인프라가 될 때** 소규모라도 독자 엔진이 합리적이다.

## 중간 규모 독자 엔진 — Remedy Northlight

[[remedy-entertainment|Remedy Entertainment]] (~380명)도 자체 엔진 Northlight를 장기간 유지하는 사례. [[alan-wake-2|Alan Wake 2]] 개발에서 Northlight는 단순 기술 자산이 아니라 *Remedy의 장르 정체성*(심리 호러·꿈의 논리·초자연적 조명·영상미)을 구현하는 **인프라**로 기능한다. Asobo와 같이 *중간 규모 + 장르 정체성* 케이스 — 캡콤 모델(2,500명 멀티 타이틀)과 샌드폴 모델(40명 단일 타이틀) 사이의 *세 번째 길*.

## MMORPG 라이브 서비스 자체 엔진 — 펄어비스 케이스

[[pearl-abyss|펄어비스]] (~1,500명, 한국 안양)는 *MMORPG 라이브 서비스 + 자체 엔진* 카테고리의 *유일한 representative*. 캡콤·Remedy·Asobo의 *AAA 콘솔 자체 엔진* 모델과 다른 *5번째 ROI 정당화*:

- **검은사막 엔진 (Black Desert Engine, 1세대, 2014~)** — *C++ 기반 in-house*, 2010~2014 4년 R&D. 검은사막 PC(2014)·모바일(2018)·콘솔(2019/2025) *동일 베이스 cross-platform* 적용
- **블랙스페이스 엔진 (Blackspace Engine, 2세대, 2025-03 GDC 최초 공개)** — *룩앤필·기술 통제·멀티플랫폼 지원* 3대 핵심 가치. 거리 기반 렌더링·심리스 로딩·GPU 물리·FFT 해양·레이 트레이싱·통합 대기 산란 등 *UE5 Nanite·Lumen 표준에 정면 대응하는 자체 솔루션*. *붉은사막* 첫 상용 검증, 이후 *DokeV* 등 적용 예정 ([[pearl-abyss-blackspace-engine-gdc2025|인벤 보도]])
- *MMO 서버 인프라 + 클라이언트 엔진* 동시 통제 — *외부 엔진(UE5 등) 도입 시 서버 인프라 분리 어려움*이 자체 엔진 유지의 *추가 정당화*
- *10년+ 라이브 서비스 catalog 모델* — 검은사막 단일 IP가 *시간축 매출 carry*, 자체 엔진 R&D 비용을 *catalog로 회수*

> 💡 **5번째 ROI 정당화 모델**: 캡콤(다장르 IP 공유)·Asobo·Remedy(장르 정체성)·Rockstar(오픈월드 스케일)·FromSoftware(시리즈 게임 필감)에 *MMORPG cross-platform 라이브 서비스 + 자체 IP*가 추가. *NCSoft 리니지·넥슨 메이플*은 *PC·모바일 분리 운영* 측면에서 *펄어비스의 cross-platform 동일 베이스 모델과 분기*.

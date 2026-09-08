---
title: "Unity 엔진"
type: concept
sources: ["[[cedec2026-ratatan-small-team-console]]", "[[indiebi-game-pricing-strategy]]", "[[ai-asset-pipeline-tech-landscape-2026]]", "[[tencent-light-ai-pipeline-2026]]"]
related: ["[[unreal-engine-5|Unreal Engine 5]]", "[[proprietary-engine-strategy|자체 엔진 전략]]", "[[proprietary-engine-vs-ue5|자체 엔진 vs UE5]]", "[[small-team-development|소규모 팀 개발 전략]]", "[[ai-asset-pipeline|AI 게임 에셋 산업화 파이프라인]]", "[[art-pipeline-design|아트 파이프라인 설계]]", "[[hoyoverse|호요버스]]", "[[ratatan|Ratatan]]", "[[mint-rocket|민트로켓]]"]
created: 2026-09-08
updated: 2026-09-08
confidence: low
---

**Unity**는 위키의 엔진 논의에서 [[unreal-engine-5|UE5]]와 [[proprietary-engine-strategy|자체 엔진]] 사이에 놓이는 세 번째 선택지다. 지금까지 개별 사례의 *부속 정보*로만 등장했는데(어느 스튜디오가 무엇으로 만들었나), 그 언급들을 모으면 **UE5와 다른 종류의 선택 논리**가 보인다.

> ⚠️ **커버리지 경계**: 이 페이지는 Unity를 다룬 1차 자료를 ingest해서 쓴 것이 아니라, 다른 주제의 소스에 부속으로 등장한 Unity 언급 11건을 모은 것이다. **엔진 자체의 기술 평가·로드맵·라이선스 정책은 위키 커버리지 밖**이고, 따라서 여기서 "Unity가 낫다·못하다"류의 판단은 하지 않는다. confidence: low.

## 위키가 실제로 관측한 것 — 세 가지 사용 패턴

| 패턴 | 사례 | 쓰이는 이유 |
|---|---|---|
| **개량해서 자기 엔진으로** | [[hoyoverse]] — Unity 기반 자체 개량 엔진 | *Tech Otakus* DNA. 엔진 통제가 IP 통제로 직결. 모바일·크로스플랫폼이 주전장 |
| **하이브리드 — Unity + 자사 엔진** | [[ratatan]] — Unity + 자사 「Theory Engine」 단일 코드베이스 | 멀티 플랫폼 이식을 *최대공약수 방식*으로. Switch 2 약 4개월, PS5·Xbox 각 약 3개월 |
| **소규모 팀의 기본값** | [[mint-rocket]] (넥슨 자회사 중 Unity 축) | 팀 규모·장르가 UE5의 비용을 정당화하지 않는 구간 |

> 💡 **핵심 인사이트:** 위키가 모은 Unity 사례는 전부 **"엔진을 그대로 쓰지 않는다"**는 공통점이 있다. 호요버스는 개량해서 자기 것으로 만들었고, Ratatan은 자사 엔진과 붙여 단일 코드베이스로 굴린다. 반면 [[unreal-engine-5|UE5]] 쪽 대표 사례([[sandfall-interactive|샌드폴]])의 핵심은 **"무수정"**이었다. 같은 서드파티 엔진인데 위키 안에서 정반대 운용 철학의 표본으로 인용되고 있다 — 이 대비 자체가 아직 검증되지 않은 관찰이다.

## 결정 분기에서의 위치

[[proprietary-engine-vs-ue5|자체 엔진 vs UE5]] 비교가 세운 규모별 분기에서 Unity는 *~50명 단일 IP* 구간의 대안으로 표기된다.

```
~50명 단일 IP  →  UE5 무수정 (또는 Unity)
```

즉 위키의 현재 자료에서 Unity와 UE5는 **같은 칸을 공유하는 대체재**로 취급되고 있고, 둘을 가르는 기준은 아직 수집되지 않았다. [[unreal-engine-5]] 페이지도 *"Unity vs UE5 결정 분기 — 인디·중소 스튜디오의 실제 선택 기준 인터뷰 수집"*을 남은 갭으로 적어 뒀다. **이 페이지는 그 갭을 메운 것이 아니라 갭의 위치를 명확히 한 것이다.**

## 파이프라인 층에서의 Unity

엔진 선택과 별개로, Unity는 위키의 [[ai-asset-pipeline|AI 에셋 파이프라인]] 논의에서 **출력 포맷의 기본값**으로 반복 등장한다.

- **Unity 6 네이티브 USD 지원** — 신규 패키지 `com.unity.importer.usd`·`com.unity.exporter.usd`·`com.unity.usd.core`. 레거시 `com.unity.formats.usd`는 폐기 대상 ([[ai-asset-pipeline-tech-landscape-2026]])
- 텐센트 LIGHT 파이프라인의 자연어 의도 예시가 *"이펙트를 Unity 프리팹으로 내보내줘"* ([[tencent-light-ai-pipeline-2026]]) — AI 파이프라인이 상정하는 도착지가 Unity라는 뜻
- OpenUSD가 공용 원장으로 안착하면서 **엔진 선택과 에셋 파이프라인이 분리되는 방향** — [[art-pipeline-design]]의 논지와 연결

## 가격 전략 자료로서

[[indiebi-game-pricing-strategy|IndieBI × Unity]] 가격 책정 보고서는 위키의 [[game-pricing-strategy|가격 전략]] 축에서 인용되는 소스다. 이 경우 Unity는 엔진이 아니라 **데이터 발행 주체**로 등장한다 — 엔진사가 자사 생태계 데이터를 근거로 시장 가이드를 내는 형태.

## 남은 갭

- Unity vs UE5의 **실제 선택 기준** — 라이선스 비용, 팀의 기존 숙련도, 타깃 플랫폼 중 무엇이 결정적인지 1차 인터뷰 없음
- 2023년 런타임 요금 사태 이후의 **신뢰 회복 여부** — 위키에 자료 전무. [[player-trust-design|신뢰 설계]]를 개발사↔플랫폼 관계에 적용해 볼 만한 케이스이나 근거 미수집
- Unity Technologies(회사)의 재무·전략 — 커버리지 밖

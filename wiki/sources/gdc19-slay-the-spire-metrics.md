---
title: "[GDC19] Slay the Spire: Metrics Driven Design and Balance"
type: source-summary
source_url: "https://www.gdcvault.com/play/1025731"
source_author: "Anthony Giovannetti (Mega Crit Games)"
source_published: 2019-03
sources: ["raw/articles/2026-06-16-gemini-deepresearch-roguelike.md"]
related: ["[[roguelike|로그라이크]]", "[[data-driven-development|데이터 기반 개발]]", "[[game-balance|게임 밸런싱]]", "[[early-access-strategy|얼리 액세스 전략]]"]
created: 2026-06-16
updated: 2026-06-16
confidence: medium
---

**원문**: [gdcvault.com/play/1025731](https://www.gdcvault.com/play/1025731) — Anthony Giovannetti (Mega Crit Games), GDC 2019
> 출처 주의: 본 요약은 Gemini Enterprise Deep Research 보고서(raw/articles/2026-06-16-gemini-deepresearch-roguelike.md, 2026-06-16)가 인용·정리한 내용을 옮긴 것으로, GDC Vault 1차 강연을 직접 확인하지 않았다. 인용 수치·표현은 1차 재검증 권장 (confidence medium).

덱빌딩 로그라이크 [[balatro|발라트로]]·하데스 이전에 장르 메트릭 밸런싱의 원형을 제시한 메가 크리트의 강연. 얼리 액세스 기간 동안 축적한 플레이어 텔레메트리로 카드·유물을 조율한 방법론.

## 핵심 포인트

- **수집 메트릭 3종**: ① 제시 시 다른 카드 대비 선택률(Pick Rate) ② 최종 3·4막 승리 덱 내 포함 여부(Win Rate in Deck) ③ 특정 적 조우 시 절약/손실 평균 체력. 초기 3개 대시보드 → 정식 출시 시 **90여 개 실시간 필터 그래프**로 확장.
- **'평균적 밸런싱' 거부**: 모든 요소의 파워를 평탄화하면 실험 욕구·도파민이 급감. 대신 강력한 시너지를 *허용하되* 동시 정합 확률을 수학적으로 격리해 **출현 희소성**을 제어.
- **유기적 제약 사례 (Wraith Form)**: 픽률·승률이 기형적 아웃라이어인 카드를 메커니즘 제거가 아니라 *사용 시 민첩 점진 감소*라는 상황적 페널티로 재정립해 *상황적 유효성(Situational Viability)*을 보강.
- **승천(Ascension) 난이도 사다리**: 수평 다양성을 훼손하지 않으며 숙련자에게 점진 제약(엘리트 빈도·저주 카드·물가·이중 보스) 부과.

> 💡 **핵심 인사이트:** 로그라이크 밸런싱의 목표는 *완벽한 수학적 균형*이 아니라, 플레이어가 불완전한 부품을 가치 있게 조합하는 *마스터리의 재미* 보존이다. 사기 빌드를 없애는 대신 재현 확률을 낮추고, 메트릭으로 아웃라이어를 유기적으로 다듬는다. [[data-driven-development|데이터 기반 개발]]의 장르 적용 정석.

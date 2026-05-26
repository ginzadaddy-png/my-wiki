---
title: "예측 vs 측정 — Steam 매출 예측 모델과 흥행 메트릭"
type: comparison
sources: ["[[zrconsulting-steam-forecaster-2026]]", "[[carless-wishlist-conversions-2025-10]]", "[[zukowski-bad-launch-recovery-2024]]", "[[firstlook-signals-of-success]]", "[[steam-next-fest-wishlist-benchmarks-2025]]"]
related: ["[[steam-revenue-forecasting|Steam 매출 예측 모델]]", "[[launch-metrics|흥행 예측 지표]]", "[[marketing-strategy|마케팅 전략]]", "[[indie-business-strategy|인디 비즈니스 전략]]", "[[publisher-deal-structures|퍼블리셔 딜 구조]]"]
created: 2026-05-26
updated: 2026-05-26
confidence: high
---

[[steam-revenue-forecasting|Steam 매출 예측 모델]]과 [[launch-metrics|흥행 예측 지표]]는 **같은 질문을 다른 시점에서** 푼다. 전자는 *런치 전*에 위시리스트·서브장르·리뷰 tier·buzz multiplier를 입력으로 Year-1 매출 범위를 추정하는 *forward-looking 정량 프레임*. 후자는 *런치 전후 시점에서 실제 행동 데이터*(플레이 시간·재플레이·1·7일 유지율·디스코드 적극 참여)를 보고 *진짜 신호와 가짜 신호를 구별*하는 *measurement 프레임*. 둘은 경쟁하지 않고 *시간축의 짝*으로 함께 사용된다.

## 한 페이지 비교

| 차원 | [[steam-revenue-forecasting\|매출 예측 모델]] | [[launch-metrics\|흥행 메트릭]] |
|---|---|---|
| 시점 | 런치 전 (6~12개월) | 런치 전후 (데모 + 런치 첫 달) |
| 출력 | Year-1 매출 범위 ($) | 흥행 신호 진위 판단 |
| 핵심 입력 | 위시리스트 수, 서브장르 conversion, review tier, pre-launch buzz, 8 driver | 플레이 시간·재플레이·1·7일 유지율·디스코드 active |
| 변동성 | ZR 명시: 30~50% 편차 | First Look: AAA·AA 93%가 예측 실패 경험 |
| 의사결정 용도 | 자원 배분·publisher deal 협상·break-even 계산 | 마케팅 push·post-launch patch·시리즈 IP 투자 |
| 주요 위험 | "위시리스트 평균 15%" 같은 *median 일반론*에 의존 | *조회수·인지도 같은 가짜 신호*에 의존 |

## 같은 데이터 1차 source, 다른 사용처

두 개념 모두 [[carless-wishlist-conversions-2025-10|Carless wishlist conversions]]·[[zukowski-bad-launch-recovery-2024|Zukowski 회복률 분석]]·[[firstlook-signals-of-success|First Look 흥행 신호]] 같은 1차 정량 source를 기반으로 한다. 차이는 *어떤 컬럼을 읽는가*:

- **forecasting**은 *median × multiplier* 컬럼을 사용해 *수익을 예측* (예: PEAK 266× outlier가 *내 게임 conversion 상한선* 추정 근거)
- **launch-metrics**는 *median × distribution* 컬럼을 사용해 *내 게임이 어디에 위치하는지 측정* (예: Zukowski 28/18,239 회복률 0.156%가 *기준선 대비 위치* 진단 근거)

## 의사결정 흐름 — 짝으로 사용하는 방법

```
[6~12개월 전]   forecasting → break-even 계산 + publisher deal stress test
                                ↓
[3~6개월 전]   첫 buzz → forecasting multiplier 재calibration
                                ↓
[데모/Next Fest] launch-metrics → conversion·playtime·discord 측정
                                ↓
[런치 첫 주]    launch-metrics → forecasting 가정 검증·반론
                                ↓
[런치 첫 달]    launch-metrics → 회복률 위치 진단 + 시리즈 IP 결정
```

핵심: forecasting은 *가정*을 만들고, launch-metrics는 *가정을 검증*한다. 둘 중 하나만 쓰면 *과신*(예측만) 또는 *사후약방문*(측정만)으로 끝난다.

## 함께 쓰일 때의 함정

> ⚠️ **circular reasoning 위험:** forecasting의 buzz multiplier를 *위시리스트 증가율*로 보정하면 launch-metrics의 *위시리스트는 가짜 신호*라는 결론과 충돌. ZR Forecaster도 위시리스트를 *알고리즘 가치(Valve 달러)* 입력으로만 사용하지 *직접 매출 입력*으로는 사용 안 함 — 이 분리를 *반드시* 유지해야 두 프레임이 충돌 없이 작동.

## 사례 적용

- **[[balatro]]**: forecasting 8 driver 중 *pre-launch buzz multiplier* 상한 (Hades·Balatro = 2.5×)이 이 게임을 어떻게 예측했을지 vs launch-metrics의 *플레이 시간 1위 41%* 같은 행동 신호가 어떻게 검증했을지 비교 가능 케이스
- **[[arc-raiders]]**: forecasting은 *F2P→프리미엄 전환*을 어떻게 계산했나 vs launch-metrics는 *2개월 유지율 91% → -80%* 하락을 어떻게 측정했나
- **[[dave-the-diver]]**: forecasting median 예측 vs launch-metrics 디스코드 적극 참여·민트로켓 답변 정책의 *행동 신호*

## 추가 조사 주제

- *Recovery* 시나리오: launch-metrics가 "회복 가능"이라 판단했을 때 forecasting을 *어떻게 재calibration*하는지
- forecasting의 8 driver 중 *어떤 driver가 launch-metrics의 어떤 행동 지표와 1:1 매핑*되는지 정렬표
- 한국 인디 사례에서 두 프레임의 적용 — 한국어 source 부족, 향후 조사 대상

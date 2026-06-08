---
title: "플랫폼 수수료 vs 직접 판매 (D2C)"
type: comparison
sources: ["[[xsolla-webshop-ecosystem]]", "[[zrconsulting-steam-forecaster-2026]]"]
related: ["[[webshop-direct-monetization|웹샵·D2C 직접 수익화]]", "[[publisher-deal-structures|퍼블리셔 딜 구조]]", "[[xsolla|엑솔라]]", "[[valve|Valve]]", "[[game-pricing-strategy|게임 가격 전략]]", "[[live-service-design|라이브 서비스 설계]]"]
created: 2026-06-08
updated: 2026-06-08
confidence: medium
---

게임사가 매출을 올리는 *유통 채널*을 수수료·역할·통제권 관점에서 비교한다. 플랫폼 스토어(모바일 구글·애플, PC [[valve|Steam]])의 **30% 수수료 모델**과, 자체 웹샵을 통한 **D2C(직접 판매)** 모델은 대립이 아니라 *역할이 다른 두 채널*이며, 2026년 현재 둘을 병행하는 [[webshop-direct-monetization|하이브리드 구조]]가 표준이 되고 있다.

> 💡 **핵심 인사이트:** 채널 선택은 단순 "수수료 몇 %"가 아니라 *발견(신규 유입) vs 락인(진성 유저 심화)* 기능의 분담 문제다. 플랫폼은 발견을, D2C는 관계·데이터 내재화를 담당한다. 단일 채널 올인은 양쪽 모두에서 비효율적.

## 채널별 비교

| 축 | [[valve]] (PC) | 모바일 스토어 | 직접 판매(D2C) |
|---|---|---|---|
| 수수료 | 30% (10M$↑ 25%·50M$↑ 20%) | 구글·애플 30% | 결제 솔루션 수수료(<30%) + 운영비 |
| 1차 역할 | 발견·유통 인프라 | 발견·첫 결제(백화점) | 진성 유저 락인(VIP 샵) |
| 마케팅 자유도 | 알고리즘·룰 종속 | 정책 종속 | 게임사 자유 설계 |
| 유저 데이터 | 플랫폼 보유 | 플랫폼 보유 | 게임사 직접 보유 |
| 세무·컴플라이언스 | 플랫폼 처리 | 플랫폼 처리 | merchant of record 대행([[xsolla]]) |
| 규제 방향 | 안정 | 외부결제 점진 허용 | 주도권 확대 중 |

## 세 가지 채널 논리

### 1. 모바일 30% — 발견의 비용

구글·애플 인앱 결제는 *신규 유저 발견과 첫 결제*에 강하지만 30% 수수료·획일적 결제·유저 데이터 비보유가 한계. 반독점 규제 완화로 인앱 외부 링크가 허용되며 *독점 균열* 진행 중.

### 2. PC self-publish 30% — 단일 변수의 명료함

[[valve|Steam]] 30%는 [[publisher-deal-structures|퍼블리셔 딜 구조]]에서 self-publish 시 *유일하게 명료한 비용*. PC 패키지·인디는 D2C보다 이 단일 변수와 [[game-pricing-strategy|가격·세일 전략]]이 더 직접적인 의사결정축.

### 3. D2C 웹샵 — 락인과 데이터 내재화

자체 웹샵은 수수료 절감을 *넘어* 진성 유저와 직접 관계를 맺고 결제 데이터를 내재화하는 채널. [[live-service-design|라이브 서비스]] 게임에서 신규 유입비 폭등에 대응하는 *장기 수익 사령탑*. 단 merchant of record·APM·라이브옵스 운영 부담이 따름.

## 의사결정 가이드

- **모바일 F2P·라이브 서비스**: 스토어(발견) + 웹샵(락인) 하이브리드. 출시와 *동시* 웹샵 도입이 인지도 효율 우위.
- **PC 패키지·인디**: [[valve|Steam]] 30% + [[publisher-deal-structures|퍼블리셔 딜]] 최적화가 우선. D2C는 부차적.
- **해외 진출 중소사**: 국가별 결제·세무 장벽이 가장 큰 비용 → merchant of record(예: [[xsolla]]) 모델이 진입 장벽 자체를 제거.

> ⚠️ D2C 매출·전환 수치 상당수가 결제 솔루션사 자체/익명 데이터. 수수료 절감분도 솔루션 수수료·운영비 차감 후 *실질 순익*으로 따져야 함.

## 위키 연결

- [[webshop-direct-monetization|웹샵·D2C 직접 수익화]] — D2C 운영 3단계·기술 인프라
- [[publisher-deal-structures|퍼블리셔 딜 구조]] — self-publish 30% baseline 맥락
- [[game-pricing-strategy|게임 가격 전략]] — 플랫폼 가격·세일 룰
- [[live-service-design|라이브 서비스 설계]] — D2C가 결합되는 운영 모델

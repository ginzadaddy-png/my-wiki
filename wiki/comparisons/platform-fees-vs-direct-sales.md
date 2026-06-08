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

## 플랫폼 약관상 적용 가능성

각 플랫폼 약관·정책을 직접 확인한 결과, "웹샵/D2C가 가능한가"는 플랫폼마다 의미가 다르다.

- **[[valve|Steam]] (PC)** — 구독자 약관은 *소비자용*이라 개발사 웹샵 규칙(별도 Steam Distribution Agreement 소관)은 담고 있지 않다. 다만 §1에서 Steam 내 거래·Steam Wallet 결제는 *Valve가 판매자*(→ 30% 영역)임을 명시하고, §2 E·F(Retail Purchase / Authorized Resellers)는 **Product Key·CD-Key를 리테일·공식 리셀러를 통해 Steam 밖에서 판매·활성화하는 것을 허용**한다. 즉 PC는 "키 외부 판매" 경로가 약관에 명시돼 있고, F2P 인게임 재화도 PC 개방성상 자체 웹 결제가 가능하다.
- **PlayStation** — 이용약관이 가장 명확히 잠근다. §14.2.1은 "PS Store와 게임 내 스토어(in-game store)의 거래를 포함한 모든 구매는 회원과 SIE 간 거래"로 규정하고, §14.10.2는 "**게임·앱·PS Store 외부에서 가상 아이템을 얻으려는 시도 금지**"로 규정한다 → 콘솔 게임 재화의 외부 웹샵 판매를 직접 차단.
- **Xbox** — 마이크로소프트는 자체 *Gaming Web Purchase Service*(웹 구매 서비스)를 운영한다. 약관상 MS가 판매자/마켓플레이스 facilitator로서 디지털 상품을 웹에서 직접 팔며(자사·파트너 모바일 타이틀 포함, MS 계정 불필요), 즉 *플랫폼 홀더 본인이 1st-party 웹 D2C 채널*을 차린 형태다. 제3자 개발사가 콘솔에서 외부결제 webshop을 여는 프레임워크는 아니며, 약관에 "수수료 회피 목적의 우회 금지"가 명시돼 있다.

> 💡 **핵심:** 모바일 D2C가 활발한 건 강제 인앱결제 독점이 규제로 깨졌기 때문. 콘솔은 (PSN 약관이 소비자의 외부 구매를 잠그고) + (아래 크로스플랫폼 정책이 파트너 매출 누수를 클로백)하는 이중 구조라 모바일식 우회가 성립하지 않는다.

1차 출처: [Steam Subscriber Agreement](https://store.steampowered.com/subscriber_agreement/) · [PlayStation Network 이용약관 (한국)](https://www.playstation.com/ko-kr/legal/psn-terms-of-service/) · [Microsoft Gaming Web Purchase Service Terms (US)](https://www.xbox.com/en-US/legal/web-purchase)

## 콘솔 크로스플랫폼 커머스 — 패리티·도매가 상한

게임이 PlayStation과 다른 플랫폼(PC·모바일·타 콘솔)에 동시 출시되어 *크로스커머스*(플랫폼 간 인게임 구매 콘텐츠 공유)를 운영하는 경우, Sony는 이를 허용하되 파트너 정책으로 *PlayStation 귀속분*을 보호한다. 콘솔에서 웹샵/D2C 자체를 막기보다, 결제가 어디서 일어나든 경제적 형평을 맞추는 장치다.

- **패리티 의무**: 비-PlayStation 플랫폼에서 실거래로 판매하는 모든 콘텐츠는 *PS Store에도 동시에* 제공해야 한다. 유료 가상화폐로 얻는 혜택·콘텐츠를 *다른 채널에서 더 싸게 실거래로 팔 수 없다*. 게임과 무관한 외부 스토어에서 구매한 콘텐츠의 PS 전송은 미지원 → 웹샵 전용 특가·독점으로 PS 유저를 빼돌리는 구도를 차단.
- **도매가 상한**: 파트너가 소매가를 통제하면, PS Store에 공급하는 도매가를 *비-PlayStation 플랫폼 소매가에 연동해 상한*을 둔다 — 플랫폼이 표준 수준(~30%)의 마진을 유지하도록. 즉 외부 채널에서 더 싸게 팔아도 PS 기준 도매가가 그에 묶여, 가격 차익만으로 PS 매출을 잠식하기 어렵다.

> ⚠️ 이 항목은 플랫폼 홀더의 *파트너 대상 비공개 정책*에 근거한다. 실제 적용 시 해당 플랫폼과 직접 계약·확인이 필요하다.

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

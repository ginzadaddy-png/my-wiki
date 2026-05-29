---
title: "miHoYo / HoYoverse"
type: entity
sources: []
related: ["[[live-service-design|라이브 서비스 설계]]", "[[mobile-gamedev|모바일 게임 개발]]", "[[game-market-trends|게임 시장 트렌드]]", "[[ip-adaptation-design|IP 적응 설계]]", "[[catalog-economics|카탈로그 이코노믹스]]", "[[multi-project-development|멀티 프로젝트 개발]]"]
created: 2026-05-29
updated: 2026-05-29
confidence: medium
relations:
  parentOf: []
---

**miHoYo**(米哈游, 2012 상하이 설립)은 중국 상하이 본사의 게임 개발·퍼블리셔. 창업자 Cai Haoyu(蔡浩宇)·Liu Wei(刘伟)·Luo Yuhao(罗宇皓) 3인은 상하이교통대학 동기. 글로벌 브랜드는 **HoYoverse**(2022~), 글로벌 운영 법인은 **Cognosphere LLC**(싱가포르·미국). [[mobile-gamedev|모바일 게임 개발]]과 [[game-market-trends|게임 시장 트렌드]] 양쪽에서 *2020년대 원신 쇼크*의 진원지로 인용된다.

> 💡 **핵심 포지셔닝:** *F2P 가챠 모바일 + AAA 비주얼*의 결합 모델. *"Tech Otakus Save the World"* 비전 아래 *애니메이션 스타일 + 광역 오픈월드 + 가챠*를 *글로벌 cross-platform*(모바일·PC·PS·Xbox)으로 통합. *모바일 출신 회사가 콘솔·PC 시장을 위협*하는 첫 케이스로 *모바일 4대 벽 돌파* 사례로 분석됨.

## 주요 작품

| 게임 | 출시 | 플랫폼 | 누적 매출 (외부 추정) |
|---|---|---|---|
| Honkai Impact 3rd | 2014 (CN) / 2017 (글로벌) | 모바일·PC | ~$1B+ |
| 원신 (Genshin Impact) | 2020-09-28 | 모바일·PC·PS·Xbox(2024) | **$6~8B+** (2024 기준 외부 추정) |
| Honkai: Star Rail | 2023-04-26 | 모바일·PC·PS5 | ~$2B+ (출시 1년) |
| Zenless Zone Zero | 2024-07-04 | 모바일·PC·PS5 | ~$500M+ (출시 6개월) |
| Genshin Concert·애니 (2026 예정) | TBA | 미디어 cross | - |

## 핵심 성공 요인

1. **F2P + 가챠 + AAA 비주얼 결합** — 모바일 가챠 모델 ARPU + PC·콘솔급 비주얼 충실도. 산업 표준을 *모바일 기대치 위로* 끌어올림
2. **글로벌 cross-platform** — 모바일·PC·PS·Xbox cross-play·cross-save 표준화. 플랫폼별 모객을 *한 IP에 통합*
3. **6주 update 사이클** — 정기 *Version update* (1.0·1.1·1.2…) 모델. 매 사이클마다 신규 캐릭터·지역·이벤트로 *retention 가속*
4. **자체 엔진 + 자체 IP** — Unity 기반 자체 개량 엔진. *Tech Otakus* DNA가 엔진 통제·IP 통제로 직결
5. **중국 본토 ↔ 글로벌 이중 운영** — Cognosphere(글로벌)·miHoYo(중국)을 *법인 분리*해 *중국 규제*와 *글로벌 마케팅* 동시 대응

## 라이브 서비스 모델 분석

[[live-service-design|라이브 서비스 설계]] 관점에서 HoYoverse 모델은 *비약탈적 + 가챠 + 광역 콘텐츠*의 균형:

- **무료 콘텐츠가 풍부** — 메인 스토리·맵·캐릭터 일부는 *완전 무료*로 플레이 가능
- **가챠 ARPU는 *고래 의존*이지만 진입장벽 낮음** — *천장(pity) 시스템*으로 *극단적 P2W 회피*
- ***Battle Pass 외 시즌 콘텐츠* 다층화** — 일일·주간·월간·버전별 이벤트 4단 구조
- **글로벌 동시 운영의 어려움**: 시간대·결제·번역·문화 콘텐츠 검열 등 *동시 launch ops* 복잡도가 *경쟁 진입장벽*

## 글로벌 시장 영향 — *원신 쇼크*

[[game-market-trends|게임 시장 트렌드]] 페이지에서 인용되는 *원신 쇼크*의 핵심:
- *모바일 가챠 게임이 콘솔·PC 시장을 위협* — 일본·한국 모바일 RPG 시장 dominance, 글로벌 진입
- 한국 NCSoft·넥슨·Krafton 등이 *F2P MMO 모델에서 cross-platform RPG 모델로 pivot* 압력
- *AAA 콘솔 개발사*가 *F2P 모바일 비주얼 기준*에 압박 — Sony·MS도 자체 라이브 서비스 도전

## risk

> ⚠️ **모델 risk:**
> 1. *가챠 의존* — 한국·일본 규제·글로벌 컴플라이언스 변화 시 *매출 충격*
> 2. *6주 사이클 burnout* — *내부 개발 인력 cycle 부담*. [[dev-talent-pipeline|개발 인재 파이프라인]] 측면 risk
> 3. *복수 IP 동시 운영* — 원신·Star Rail·ZZZ가 *서로 자기잠식*. [[multi-project-development|멀티 프로젝트 개발]]의 *자원 잠식* 사례
> 4. *중국 규제·게임 판호* — 본토 신작 출시 지연이 *현금 흐름*에 영향

## 비교 — 라이브 서비스 4사

| 항목 | miHoYo | [[epic-games\|Epic]] | [[riot-games\|Riot]] | [[respawn-entertainment\|Respawn]] |
|---|---|---|---|---|
| 본사 | 상하이 | 노스캐롤라이나 케리 | LA | LA |
| 모회사 | 비상장 (중국) | 텐센트 40% | 텐센트 100% | EA 산하 |
| 시그니처 모델 | F2P 가챠 + cross-platform | F2P BR + 플랫폼 | F2P MOBA + transmedia | F2P BR + 싱글 듀얼 |
| 주력 IP | 원신·Star Rail·ZZZ | Fortnite | LoL·Valorant | Apex·Star Wars Jedi |
| 엔진 | Unity 개량 | Unreal (자사) | 자체 | UE/Source |

## 관련 위키 페이지

- [[genshin-impact|원신 (Genshin Impact)]] — 주력 IP
- [[honkai-star-rail|Honkai: Star Rail]] — 차세대 IP (페이지 미생성, 추후)
- [[mobile-gamedev|모바일 게임 개발]] — 원신 쇼크의 역설 인용
- [[live-service-design|라이브 서비스 설계]] — 비약탈적 가챠 모델
- [[catalog-economics|카탈로그 이코노믹스]] — 라이브 서비스 변형으로의 catalog 모델

## 추가 조사

- 원신·Star Rail·ZZZ의 *자기잠식 vs 동반 성장* 정량 (Sensor Tower·Niko Partners)
- *중국 법인 vs Cognosphere* 매출 분리 정확 수치
- *Genshin 콘솔 cross-save* 도입(2024) 후 *매출 곡선* 변화
- *2024 Cai Haoyu 일선 후퇴* 발표 후 *조직 변화*

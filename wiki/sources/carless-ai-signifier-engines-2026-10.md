---
title: "Carless — Next Fest의 숨은 AI 신호, 엔진 점유율 (2026-10)"
type: source-summary
source_url: "https://newsletter.gamediscover.co/p/the-hidden-ai-signifier-in-next-fest"
source_author: "Simon Carless (GameDiscoverCo)"
source_published: 2026-10-30
sources: []
related: ["[[ai-disclosure-player-sentiment|AI 공시와 플레이어 정서]]", "[[unity-engine|Unity 엔진]]", "[[unreal-engine-5|Unreal Engine 5]]", "[[ai-gamedev|게임 개발에서의 생성형 AI]]", "[[steam-next-fest|Steam Next Fest]]", "[[game-market-trends|게임 시장 트렌드]]", "[[carless-next-fest-october-2026-results]]", "[[zukowski-next-fest-october-2026]]", "[[roblox|Roblox]]"]
created: 2026-11-02
updated: 2026-11-02
confidence: medium
---

**원문**: [The hidden AI signifier in Next Fest - and why it's so complex...](https://newsletter.gamediscover.co/p/the-hidden-ai-signifier-in-next-fest) — GameDiscoverCo, Simon Carless, 2026-10-30. **일부 유료** — 무료 구간(메인 에세이)까지만 반영

Steam의 공식 AI 공시만으로는 AI 사용을 다 셀 수 없으니, **데모가 쓴 엔진의 변화**를 두 번째 신호로 보자는 글이다.

## 1. 공식 AI 공시 — 세 회차 추이

| Next Fest 회차 | AI 공시 데모 | 비율 |
|---|---|---|
| 2026-02 | 750 | 21.2% |
| 2026-06 | 1,163 | 26.5% |
| **2026-10** | **2,517** | **34.4%** |

- 공시 내용: 비주얼 아트 **약 70%**(대부분 아이콘·스토어 아트이지 게임 아트 전체가 아님) · 현지화 28% · 마케팅·스토어 페이지 26% · 음악 19% · 게임 내 텍스트 17% · 효과음 15.5%
- AI 공시작은 저CCU 구간에 몰린다. CCU 100을 넘긴 공시작 52개는 대부분 *핵심이 아닌 요소*에 AI를 썼다고 공시했다
- 공시는 **AI 코드 도우미 사용을 포함하지 않는다** — 저자가 공시를 "더해서 읽으면 안 된다"고 하는 이유

## 2. 엔진 점유율 — 인기 순위에 따라 갈린다

| 엔진 | 전체 데모 (직전 → 이번) | 피크 CCU 상위 100 | 피크 CCU 상위 1,000 |
|---|---|---|---|
| Unity | **약 46%** (1위 유지) | **53%** | — |
| 엔진 미탐지 | 12.9% → **17.7%** (2위) | 7% | 14% |
| Godot | 12.6% → **17.4%** (3위) | 6% | 12% |
| Unreal | **12.3%** (4위로 하락) | **28%** | — |

- 방법: GDCo가 거의 모든 데모의 파일 매니페스트를 스캔
- **미탐지 증가 가설**: 바이브 코딩 게임이 Three.js 같은 프레임워크를 써서 탐지 도구에 안 잡힌다. Godot은 오픈소스이고 MCP 연동이 있어 바이브 코딩에 인기다
- CCU 1짜리 "엔진 없음" 게임을 직접 보면 대부분 2D 불릿 헤븐·불릿 헬·퍼즐이다

> 💡 **핵심 인사이트 — 엔진 점유율은 "누가 많이 만드나"와 "누가 많이 플레이되나"가 다르다.** Unreal은 전체 데모의 12.3%뿐이지만 피크 CCU 상위 100에서는 28%로 두 배 넘게 뛴다. 반대로 미탐지·Godot은 아래로 갈수록 비중이 커진다. 즉 *데모 공급 폭증분*은 주로 저CCU 구간의 미탐지·Godot에서 나오고, 상위권은 여전히 Unity·Unreal이 나눠 갖는다. 저자 결론도 같다 — 바이브 코딩 게임이 차트를 위협하지는 않고, **진짜 경쟁자는 AI 코드 도움을 "메스처럼" 쓰는 숙련된 1인·초소형 팀**이다.

## 3. Steam 출시 수

- 2026-09 **2,875개(+76% YoY)** · 2026-10 현재까지 **3,114개(+53%)** — SteamDB 기준
- 연환산 전망 **2027년 약 3.5만 개** (2025년 약 2.1만, 2026년 현재까지 약 2.3만)

## 4. 뉴스 라운드업에서 쓸 만한 것

- **Roblox Q3**: 평균 DAU 1.38억(−9% YoY) · 부킹 \$1.70B(−12%) · 매출 \$1.57B(+16%) · 개발자 지급 \$403M(−6%)
- Xbox FY27 Q1 콘텐츠·서비스 −2% \$5.4B, 하드웨어 −14%
- Twitch 7일 시청 시간(최근 3개월 출시작) 2위 Phantom Blade Zero — [[phantom-blade-zero|Phantom Blade Zero]] 출시 주 화제성

## 약점과 한계 (비판적 읽기)

- **유료 구간이 빠졌다.** "This week on Steam" 절(Phantom Blade·Probably Stolen 등) 본문은 반영하지 못했다
- **엔진 탐지 방법이 공개되지 않았다.** "자체 도구로 매니페스트 스캔"뿐이라 오탐·미탐 비율을 알 수 없다. 미탐지 증가를 바이브 코딩으로 설명하는 것은 *가설*이고, 커스텀 엔진·웹 프레임워크·탐지 도구의 한계도 같은 결과를 낼 수 있다
- **Unity·Unreal의 직전 회차 값이 본문에 없다.** "Unreal 4위로 하락"은 순위 변화만 있고 몇 %p 줄었는지는 차트 이미지에만 있다
- **CCU 상위 집단에서 Unreal 비중이 높은 이유를 분리하지 않았다.** 엔진 자체보다 *팀 규모·예산*이 CCU를 결정할 가능성이 크다 — Unreal을 쓰는 팀이 원래 더 크고 마케팅 예산이 많을 수 있다
- 공시 분류는 저자가 **Claude로 요약**한 결과다. 분류 기준·검수 방법은 밝히지 않았다
- 2027년 3.5만 개 전망은 두 달치 증가율을 연환산한 단순 외삽이다

## 기존 위키 연결

- [[ai-disclosure-player-sentiment|AI 공시와 플레이어 정서]] — 공급 쪽 공시율 세 회차 시계열과 공시 내용 분류
- [[unity-engine|Unity 엔진]] · [[unreal-engine-5|Unreal Engine 5]] — 인디 데모 기준 엔진 점유율과 인기 구간별 차이
- [[ai-gamedev|게임 개발에서의 생성형 AI]] — 바이브 코딩이 엔진 선택(Godot·웹 프레임워크)까지 바꾸는 흐름
- [[game-market-trends|게임 시장 트렌드]] — Steam 연간 출시 수 전망
- [[carless-next-fest-october-2026-results]] — 같은 저자의 사흘 전 결산

---
source: "https://newsletter.gamediscover.co/p/the-hidden-ai-signifier-in-next-fest"
author: "Simon Carless (GameDiscoverCo)"
published: 2026-10-30
title: "The hidden AI signifier in Next Fest - and why it's so complex... (GameDiscoverCo)"
---

> 2026-10-30 발행분. 2026-11-02 source radar 후보로 발굴 → 사용자 지정 ingest.
> 저작권 보호를 위해 본문 전문 대신 **구조화 발췌**(수치·논지 요약, WebFetch 추출)로 보존. 스폰서·홍보 문구 제외.
> **유료 구간 있음** — 무료 부분(디스커버리 뉴스 + 메인 에세이)만 발췌. "This week on Steam: wow, Phantom Blade, Probably Stolen…" 절 본문은 유료라 미열람.
> 카테고리·엔진 추세·CCU 차트는 이미지라 텍스트에 적힌 수치만 옮김.

## 디스커버리 뉴스 (요지)
- Twitch 7일 시청 시간(최근 3개월 출시작): 1 축구 · 2 Phantom Blade Zero · 3 Wardogs. 이어서 Moon Sweepers(약 70k CCU) 등
- Footprints.gg 전통 매체 언급(10-21~28): GTA 6 · CoD MW4 · Cyberpunk 2077 · Phantom Blade Zero
- Xbox FY27 Q1: 콘텐츠·서비스 -2% $5.4B, 하드웨어 -14%
- Talos Principle 2 기본가 $30 → $40
- **Roblox Q3**: 평균 DAU 1.38억(-9% YoY), 부킹 $1.70B(-12%), 매출 $1.57B(+16%), 개발자 지급 $403M(-6%)

## 메인 — Steam AI 공시
- Next Fest 공식 AI 공시: **2026-02 750개(21.2%) → 06 1,163개(26.5%) → 10 2,517개(34.4%)**
  - (비율로 역산한 분모: 약 3,540 / 4,390 / 7,320 — 발췌자 계산)
- 공시 내용 분류(저자가 Claude로 요약): 비주얼 아트 **약 70%**(대부분 아이콘·스토어 아트이지 "전체 아트"가 아님) · 현지화 28% · 마케팅·스토어 페이지 26% · 음악 19% · 게임 내 텍스트·대사 17% · 효과음 15.5% · 나머지는 그 이하
- CCU 분포: AI 공시작은 저CCU 구간에 몰림(차트). CCU 100 초과 공시작 52개 — 대부분 핵심이 아닌 요소에 AI 사용 공시. 고CCU 공시작 중 BORE는 CCU 고점이 의심스럽고 No Mortal Space는 아시아 우선 출시
- 한계: 공시는 **"AI 코드 도우미" 사용을 포함하지 않음**. 미공시 사용은 집계 불가(Valve는 노골적 AI 아트에 대해 시스템·수동 검사)

## 메인 — 엔진 점유율 (숨은 AI 신호)
- 방법: 거의 모든 데모의 파일 매니페스트를 스캔(GDCo 자체 도구)
- 10월 Next Fest 데모 7k+ — 예상 약 5k보다 약 40% 많음
- 점유율(전체 데모): **Unity 약 46%(1위 유지) · 엔진 미탐지 12.9% → 17.7%(2위) · Godot 12.6% → 17.4%(3위, 예상보다 2%p가량 빠름) · Unreal 12.3%(4위로 하락)**
- **피크 CCU 상위 100**: Unity 53% · Unreal 28% · Godot 6% · 미탐지 7%
- **피크 CCU 상위 1,000**: 미탐지 14% · Godot 12% — 인기 순위 아래로 갈수록 미탐지·Godot 비중 상승
- 미탐지 증가 가설: 바이브 코딩 게임이 Three.js 같은 프레임워크를 써서 탐지 도구에 안 잡힘. Godot은 오픈소스이고 MCP 인터페이스(godot-mcp)가 있어 바이브 코딩에 인기
- 1-CCU "엔진 없음" 게임 육안 확인(Slime Glutton·Calibration Sequence·Ribbit Robber·Anomaly Grid·Song of Larithea 등): 대부분 2D 불릿 헤븐·불릿 헬·퍼즐. Godot 쪽은 장르가 더 다양

## 저자 논지
- 공개 AI 공시를 그냥 더하면 안 된다 — 공시는 실사용을 과소 집계하므로 **엔진 탐지 추세가 두 번째 신호**
- AI가 일부 장르의 진입점을 낮춤. 1-CCU 데모는 프롬프트만으로 거의 100% 만들 수 있다
- 바이브 코딩 게임이 차트를 위협할 가능성은 낮고, AI 우선 게임이 곧 Next Fest 상위에 오르지도 않을 것
- 진짜 위협은 **AI 코드 도움을 "메스처럼" 쓰는 숙련된 1인·초소형 팀**
- 5k 대 7k 공황은 "의아하다"

## Steam 출시 수 (SteamDB, Lucien Parsons 경유)
- 2026-09 **2,875개(+76% YoY)** · 2026-10 현재까지 **3,114개(+53%)**
- 연환산 전망: **2027년 약 3.5만 개** ← 2025년 약 2.1만, 2026년 현재까지 약 2.3만

## 기타
- 막판 뉴스: Claude에 "특정 기존 게임의 재현물을 만들지 말 것" 규칙 추가

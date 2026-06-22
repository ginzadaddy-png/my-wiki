# 플레이어 리텐션·인게이지먼트 루프 — Claude Code CLI 재실행 핸드오프

> ✅ **완료 (2026-06-22, archived)** — 이 핸드오프는 Claude Code에서 `deep-research`(28소스·107주장·25 적대검증)로 ③ 출처를 검증해 **`wiki/concepts/player-retention`·`engagement-loop` 두 페이지로 반영 완료**됨. 정정 6건(다크패턴 3분류 = 사회적 자본형, 리텐션 벤치마크 분위 표기, DAU/MAU 30%+, Genshin ~$3.7B, Hades 2020-09-20, Fortnite 배틀패스 Season 2 2017-12·CoC ~$6B)과 인과 단정 기각 결과는 [[log]] 및 두 위키 페이지에 반영됨. 아래 스캐폴드(②~⑤)는 **검증 전 학습지식 초안**이므로 더 이상 truth source 아님 — 현재 진실은 위키 페이지. 기록 보존용으로 archive.

> **목적**: Cowork 세션에서 deep research를 시도했으나 이 환경은 라이브 웹 접근이 차단(WebSearch 도구 없음 + `web_fetch` provenance-lock)되어 출처 검증을 완료하지 못했습니다. 아래는 웹이 되는 **Claude Code CLI(또는 Chrome 연결) 세션에서 재실행**하기 위한 핸드오프입니다. 아래 ②~⑤는 학습지식(컷오프 2026-01) 기반 **미검증 스캐폴드**이므로, Claude Code에서 ③의 URL을 직접 fetch해 수치·인용을 확정한 뒤에만 위키에 반영하세요.
>
> 위키 신규 concept 갭: **player-retention / engagement-loop** — `live-service-design`와 짝을 이루는 핵심 빈 고리. 마케팅 *획득(acquisition)*이 아니라 *획득 이후 유지·재방문·습관 형성*을 다룸.

---

## ① Claude Code CLI 붙여넣기용 프롬프트

```
deep research: 비디오 게임의 "플레이어 리텐션(player retention)"과 "인게이지먼트 루프(engagement loop)"를
게임 개발·디자인·라이브서비스 운영 관점에서 종합한다. 마케팅 획득이 아니라 획득 이후 유지·재방문·습관 형성이 초점이며,
위키의 live-service-design 개념과 짝을 이루는 신규 concept 페이지(player-retention 또는 engagement-loop)를 만들기 위한 리서치다.

아래 5개 각도를 각각 WebSearch/WebFetch로 조사하고, 핸드오프 문서(player-retention-research-handoff.md)의
③ 출처 URL 목록을 우선 fetch해 수치·인용·정의를 검증한다. 분석사 벤치마크는 연도·표본·정의(classic vs rolling)에
따라 5~10%p 편차가 있으니 단일 숫자 인용을 금하고 출처·연도·정의를 병기한다.

검증 후 한국어 종합(영문 원제·고유명사 병기)으로 정리하고, 위키 페이지화 시 ⑤의 frontmatter·연결 개념 지침을 따른다.
환각 금지: 1차 출처에서 확인 안 된 수치는 "추정(estimated)" 표기하거나 비워둔다.
```

---

## ② 조사 5개 각도 + 하위 질문

1. **리텐션 지표·측정** — D1/D7/D30(classic vs rolling), churn, DAU/MAU(stickiness), session length/frequency, LTV와의 관계. 모바일 F2P vs 콘솔/PC 프리미엄 vs 라이브서비스 장르·플랫폼별 벤치마크 수치.
2. **엔게이지먼트 루프 설계** — core/mid/meta loop 위계와 네스팅, compulsion loop, reward schedule(variable ratio 등), Hook 모델(trigger→action→variable reward→investment), FTUE·초기 리텐션, 진행 시스템·데일리 퀘스트.
3. **라이브서비스 콘텐츠 케이던스** — 시즌/배틀패스, 라이브옵스 캘린더(일일/주간/LTE/시즌/연례), 콘텐츠 트레드밀·번아웃, 재방문 트리거, 라이브서비스 포화·실패("graveyard") 리스크.
4. **윤리적 vs 약탈적 리텐션** — 게임 다크패턴 분류, 루트박스 도박 규제, FTC, WHO 게이밍 장애(+학계 반론), 건강한 습관 vs 강박, 비약탈적 설계 모범.
5. **구체 사례** — Helldivers 2, Genshin Impact, Fortnite, Hades, Destiny 2, 모바일 라이브옵스(Supercell)의 리텐션·루프 메커니즘과 공개 수치.

---

## ③ 검증 대상 출처 URL 목록 (Claude Code에서 fetch)

**지표·벤치마크**
- https://gameanalytics.com/benchmarks/ — 모바일 F2P D1/D7/D28 장르별 벤치마크(가장 표준적 1차 출처)
- https://www.adjust.com/ — 어트리뷰션 기반 대규모 표본 리텐션·세션 벤치마크
- https://www.appsflyer.com/resources/ — 채널·지역별 리텐션·LTV 벤치마크
- https://amplitude.com/ — classic vs rolling retention 정의·코호트 분석 방법론
- https://www.deconstructoroffun.com/ — 장르별 리텐션·LTV·메타게임 실무 해설
- https://newzoo.com/ — 시장·플레이어 규모(콘솔/PC 맥락)
- https://sensortower.com/blog — 다운로드·매출·인게이지먼트 추정(서드파티 패널)

**루프 설계 (1차 이론)**
- https://www.gamedeveloper.com/design/the-chemistry-of-game-design — Daniel Cook, 스킬 아톰/루프 이론(Gamasutra 원전)
- https://lostgarden.home.blog/2012/01/02/loops-and-arcs/ — Daniel Cook, 루프 vs 아크, 네스팅 (※ URL 이전 이력 있음 — 깨지면 "Daniel Cook loops and arcs"로 재검색)
- https://www.gamedeveloper.com/design/behavioral-game-design — John Hopson, 강화계획의 게임 적용 고전(컴펄전 루프 핵심)
- https://www.nirandfar.com/how-to-manufacture-desire/ — Nir Eyal, Hook 모델 개관
- https://www.theoryoffun.com/ — Raph Koster, 재미=패턴 학습
- https://www.schellgames.com/art-of-game-design — Jesse Schell, 렌즈 프레임워크(Goals/Reward/Flow)
- https://en.wikipedia.org/wiki/Compulsion_loop — 컴펄전 루프 통용 정의

**라이브서비스 케이던스**
- https://naavik.co — 배틀패스·가챠·라이브옵스 경제 디자인 케이스 스터디
- https://www.gamesindustry.biz — 산업 재무·종료 사례(Concord 등)·시장 포화 분석
- https://www.gdcvault.com — "live ops"·"battle pass"·"Destiny"·"Fortnite" 검색 → 케이던스·리텐션 포스트모템
- https://www.bungie.net/7/en/News — Destiny 시즌 모델·콘텐츠 케이던스 1차(TWAB)

**윤리·규제**
- Zagal, Björk & Lewis, "Dark Patterns in the Design of Games" (FDG 2013) — gamestudies.org 또는 ACM DL (3분류: 시간형/금전형/심리형)
- https://www.ftc.gov/reports/bringing-dark-patterns-light — FTC 다크패턴 스태프 리포트(2022)
- FTC Epic Games/Fortnite 합의(2022.12) — ftc.gov 보도자료 ($2.45억 환불 + COPPA $2.75억, 금액 재확인)
- https://www.who.int/news-room/questions-and-answers/item/gaming-disorder + https://icd.who.int/browse11 (6C51) — WHO 게이밍 장애
- Aarseth et al. (2017) "Scholars' open debate paper", J. Behavioral Addictions (PMC) — WHO 분류 반대측(쟁점 병기 필수)
- 벨기에 Gaming Commission 2018 + gov.uk DCMS Gambling Act review — 루트박스 규제 **벨기에(도박) vs 영국(불분류) 분기**
- https://www.humanetech.com/ / https://www.nirandfar.com/ — Time Well Spent / 습관 vs 중독 논쟁

**사례 (수치 1차)**
- https://steamdb.info/app/553850/charts/ — Helldivers 2 Steam 동접(가장 신뢰 가능한 객관 수치)
- https://steamdb.info/app/1085660/charts/ — Destiny 2 시즌별 동접 추이
- https://sensortower.com/blog — Genshin·Supercell 모바일 매출 추정(★"추정" 표기 필수)
- https://www.gdcvault.com/ — Hades·Destiny 개발자 설계 강연(postmortem)
- https://www.epicgames.com/site/en-US/news — Fortnite 라이브이벤트 참여자·등록자 공식 발표

---

## ④ 미검증 합성 스캐폴드 (학습지식 기반 — 반드시 ③으로 검증)

### 4-1. 리텐션 지표
- 정의: D1/D7/D30 = 첫 플레이 후 N일째 복귀율. **classic**(정확히 N일째) vs **rolling**(N일째 이후 언제라도) — rolling이 항상 높음, 비교 시 정의 일치 필수.
- churn = 1 − retention. DAU/MAU = 점착도, **0.2(20%) 합격선, 0.5+ 우수**.
- LTV ≈ ARPDAU × 평균 라이프타임, 평균 라이프타임 ≈ **리텐션 커브 아래 면적**. → D1·D7이 곡선 적합 앵커.
- 모바일 F2P 통용치(검증 필요): D1 ≈ 30–35% / D7 ≈ 8–12% / D30 ≈ 3–5%. 우수 목표 D1 40·D7 20·D30 10.
- 장르 경향: 하이퍼캐주얼(D1 높고 D30 급락), 퍼즐/캐주얼(D30 견고), RPG/미드코어(D1 낮으나 LTS·ARPU 높음), 소셜카지노(최상위).
- ⚠️ 분석사(GameAnalytics vs Adjust/AppsFlyer) 간 5–10%p 편차 — 정의·표본 차. 콘솔/PC는 표준 벤치마크 희소(완주율·주간활성·Steam playtime이 프록시).
- 실행: 코호트 분석, FTUE 퍼널 drop-off, 예측 churn 세그먼트 → win-back.

### 4-2. 엔게이지먼트 루프
- **3계층 네스팅**: core(초·분, 예: 조준→사격→재장전) → mid(세션, 미션·스테이지) → meta(다세션, 레벨업·시즌패스·컬렉션). 짧은 루프 출력 → 긴 루프 입력. core=재미, meta=지속성.
- Daniel Cook: 루프 = **스킬 아톰**(행동→시뮬레이션→피드백→스킬 갱신)의 학습 사이클. 루프 vs 아크(일회성 콘텐츠).
- 컴펄전 루프: 변동비율 강화(variable ratio, Skinner)가 가장 높은 반응률·소거 저항 → 가챠·루트박스. 변동간격(variable interval) → 데일리 리셋·에너지 충전. 스키너 박스 비판(Cow Clicker, Bogost) 및 반론(SDT 내재적 동기) 병존.
- 도파민 = "보상 예측 오차/기대"에 반응(Schultz) — "쾌락 화학물질" 등식은 과잉단순화(뉘앙스 명시).
- **Hook 모델(Eyal)**: 트리거(외부/내부)→행동→변동보상(부족/수렵/자아)→투자(매몰비용). Eyal은 *Indistractable*에서 습관 vs 중독 구분·manipulation matrix로 자기비판.
- FTUE: D1이 첫인상 품질 지표. "teach by doing", "reward early, reward often", 한 번에 한 스킬.
- 진행/데일리: 단·중·장기 목표 네스팅(Schell의 Lens of Goals), 플로우(Csikszentmihalyi) 난이도 곡선. 데일리·로그인 스트릭 = 습관 트리거 but FOMO·손실회피 윤리 쟁점.
- **핵심 통찰**: 좋은 루프는 매 회전마다 새 패턴을 학습시킨다(Koster). 학습이 멈추면 컴펄전만 남고 재미가 죽음 → **윤리적 인게이지먼트(내재 동기) vs 약탈적 컴펄전(보상 스케줄 착취)의 경계선**.

### 4-3. 라이브서비스 케이던스
- 배틀패스: Dota 2 Compendium(2013) 기원 → Fortnite 시즌2(2018) 표준화(무료+유료 트랙, XP, 시즌 만료). 표준 시즌 **9–13주(분기)**.
- FOMO 핵심 = "만료되는 보상". 배틀패스 = pay-then-grind 매몰비용. 확률형보다 선호(가격 예측·규제 리스크↓·플레이타임→매출).
- 라이브옵스 레이어: 일일 로그인 → 주간 미션 → LTE(한정 이벤트, DAU·ARPDAU 스파이크) → 시즌 → 연례 tentpole. 예측 가능한 리듬(습관) + 한정성(스파이크) 병행.
- **콘텐츠 트레드밀**: 소비≫생산(코어는 수개월분을 수주에 소진). Destiny 콘텐츠 가뭄이 정본 사례. 상시 운영비 → 수익 미달 시 종료.
- 번아웃: 데일리가 "노동(chore)"이 되면 역설적 이탈. "FOMO 리텐션은 단기 지표↑ 장기 호감↓".
- 재참여: 데일리·스트릭(손실회피), 컴백 보상·푸시(양날의 검). 윤리적 라이브옵스 = catch-up(복귀해도 처벌 없음).
- 리스크: 2024–25 Concord(2주 종료)·Suicide Squad·Hyenas(취소) → "라이브서비스 무덤" 담론. 승자독식(가처분 시간 한정, 기존 강자 점유).

### 4-4. 윤리적 vs 약탈적
- Zagal et al. 2013 다크패턴 3분류: **시간형**(grinding, playing by appointment), **금전형**(pay-to-skip, monetized rivalries), **심리·사회자본형**(daily-login coercion, social pyramid).
- 루트박스 규제 분기(반드시 양측 병기): **벨기에(2018, 도박 판정)** vs **영국 DCMS(불분류, 자율규제)**. 네덜란드는 판정 후 항소 번복 정황(검증).
- FTC: "Inside the Game"(2019), "Bringing Dark Patterns to Light"(2022), Epic/Fortnite 합의(환불 $2.45억 + COPPA $2.75억 — 금액 재확인).
- WHO ICD-11 게이밍 장애(6C51, 통상 12개월, 2022.1.1 발효) ↔ **Aarseth et al. 2017 반론**(근거 부족·병리화·도덕적 공황). 학계 미해결 명시.
- 비약탈적 모범: **Helldivers 2 Warbond(만료 없음, 프리미엄 통화 인게임 획득)** — 위키에 이미 등재. Eyal *Indistractable*, Center for Humane Technology, Celia Hodent(게임 UX 윤리) 강연.

### 4-5. 사례 (수치 전부 검증 필요)
- **Helldivers 2(Arrowhead/Sony)**: Game Master "Joel" + Galactic War 집단 진행, Major Orders(기간한정 공동목표), 만료 없는 Warbond. Steam 동접 최고 ~458k(2024.2), PSN 연동 강제 역풍→철회가 변곡점.
- **Genshin Impact(HoYoverse)**: 일일 의뢰 4건 + Resin(에너지)로 접속 빈도 최적화, 6주 버전 케이던스, 가챠 90연 천장·50/50, 한정 배너 FOMO. 모바일 누적 ~$50억(2년, Sensor Tower 추정).
- **Fortnite(Epic)**: 시즌 10–12주 + 배틀패스(자가펀딩 구조), 라이브이벤트(Travis Scott ~1230만 동시참여 2020.4), Chapter 리셋. 등록 3.5억(2020.5, 누적).
- **Hades(Supergiant)**: 로그라이크 루프 + 죽음=내러티브 진행(실패도 보상), God Mode 접근성. **순수 패키지 판매, 라이브서비스/가챠 없음 = 윤리적 리텐션 반례축**. 100만 장(2020.12).
- **Destiny 2(Bungie)**: 시즌 3개월 + 연례 확장, **sunsetting/Content Vaulting(2020) 유저 자산 박탈 논란**, 콘텐츠 가뭄 churn. 동접은 SteamDB로만 공개.
- **Supercell(CoC/Clash Royale)**: 빌드 타이머 단기 복귀 루프, 클랜 소셜 락인, Gold Pass 월간. CoC 누적 ~$70억(추정).

### 4-6. 횡단 패턴
- 빈도형(Genshin·Supercell: 타이머/에너지) vs 순간형(Helldivers·Fortnite: shared moment) 리텐션.
- 만료 FOMO 양면: Destiny(신뢰 비용) vs Helldivers(의도적 회피) — 동일 메커니즘 정반대 평판.
- 라이브서비스 없는 리텐션: Hades(내러티브·접근성·재플레이성) = 윤리적 비교축.

---

## ⑤ 위키 페이지화 지침 (검증 후)

- **신규 concept 후보**: `player-retention`(지표·측정 중심) 또는 `engagement-loop`(설계 중심) — 범위가 크면 둘로 분리 검토. (구조/페이지 수 변경이므로 CLAUDE.md "구조 변경 사전 점검"에 따라 사용자 확인 후 진행)
- frontmatter: `type: concept`, `confidence: medium`(서드파티 추정 수치 다수), `created`/`updated` 당일, `sources`·`related` 채우기.
- **연결할 기존 개념**(양방향 link): `live-service-design`, `mobile-gamedev`, `game-balance`, `player-trust-design`, `early-access-strategy`, `marketing-strategy`. 엔티티: `helldivers-2`, `genshin-impact`, `fortnite`, `hades`(없으면 보류), `supercell`, `arrowhead-game-studios`, `hoyoverse`.
- "> 💡 핵심 인사이트" 블록으로 "루프=학습 사이클 / 윤리적 vs 약탈적 경계선" 강조. 윤리·규제 쟁점은 "> ⚠️ 모순/쟁점" 블록으로 양측 병기.
- 개념 페이지 300~800자 원칙. 분량 크면 비교 페이지(`comparisons/`)로 사례 대비(예: Helldivers 비약탈 vs Destiny sunsetting) 분리 가능.
- 환각 금지: 매출·DAU·리텐션%는 1차 출처 미확인 시 "추정(estimated)" 명시 또는 생략.

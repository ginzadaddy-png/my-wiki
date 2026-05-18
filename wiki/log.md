---
title: "활동 로그"
---

## [2026-05-18] ingest | Embark Character Pipeline (GDC 2026)
- Source: raw/articles/2026-05-18T111613+0900-Game Character Pipelines at Embark Freedom Through Structure  GDC 2026.md
- 원문: https://www.youtube.com/watch?v=UFeC-VBbO90 (Erik Östsjö & Björn Arvidsson, Embark Studios)
- 생성:
  - wiki/sources/gdc2026-embark-character-pipeline.md (5 미션 선언·Tech Stack·Origins node·3단계 진화·Edit-in-place·Batching·Cross-project 공유)
  - wiki/concepts/art-pipeline-design.md (NEW concept — 4 핵심 원칙·기술 패턴·Embark/Asobo/Sandfall 비교)
- 업데이트:
  - wiki/entities/embark-studios.md (Houdini/USD 파이프라인 공유 섹션 추가 — Arc Raiders + Finals가 같은 파이프라인)
  - wiki/concepts/multi-project-development.md (엠바크 모델에 기술적 실체 보강)
  - wiki/concepts/small-team-development.md (도구·엔진 섹션에 아트 파이프라인 공유 추가)
  - wiki/concepts/all.md (개발 방법론에 art-pipeline-design 추가)
  - wiki/sources/all.md (1행 추가, 108→109)
  - wiki/index.md (소스 108→109, 개념 50→51, pill-grid에 art-pipeline-design 추가)
- 메타: 소스 108→109, 개념 50→51
- 핵심: 직전 studio-risk-defense deck의 AXIS 03(이너소스/엔진)·AXIS 05(도구화)의 *기술적 실체*. Embark "360명 4 게임 포트폴리오" 목표가 어떻게 작동하는지 보여주는 케이스

## [2026-05-18] presentation | 스튜디오 리스크 방어 (studio-risk-defense)
- 트리거: 사용자 요청 — 인재 파이프라인 × 멀티 프로젝트 개발을 리스크 중심으로 재구성한 새 deck
- 스타일: frontend-slides skill, Style C "Quiet Brief" (다크 배경 위 페이퍼 카드 + 세로 탭), Pretendard, 22장
- 구조: 문제 정의(4) → 리스크 해부(4) → 5축 메커니즘(6) → 성공/실패 케이스(3) → 적용·시사점(4) → 정리(1)
- 생성:
  - wiki/presentations/studio-risk-defense-deck.html (22장 슬라이드, 인라인 편집 기능 포함)
  - wiki/presentations/studio-risk-defense.md (wrapper)
- 업데이트:
  - wiki/presentations/all.md (카탈로그에 새 행 추가)
  - wiki/index.md (프레젠테이션 카운트 2→3, pill-grid에 항목 추가)
- 자매 관계: 기존 [[sustainable-studio-staffing]] deck와 같은 위키 콘텐츠를 다른 프레임(보고서 톤 vs 리스크 중심)으로 재구성
- 메타: 프레젠테이션 2→3

## [2026-05-18] lint + concept-fill + quick-fix (대규모 정기 점검)
- 트리거: 사용자가 weekly-wiki-lint 예약 작업 결과 보고 후 "모두 진행" 지시
- 데드 링크 quick fix (10개 파일):
  - entities/tango-gameworks.md: `[[Hi-Fi RUSH]]` → `[[hifi-rush|Hi-Fi RUSH]]`
  - entities/hitman-2016.md + sources/gdc2016-hitman-nonlinear-sandbox.md: `[[IO 인터랙티브]]` → `[[io-interactive|IO 인터랙티브]]`
  - entities/capcom.md + sources/capcom-ir2021-dev-strategy.md + sources/re2023-re-engine-philosophy.md: `[[RE ENGINE]]` 데드 링크 제거 (대응 페이지 없음 — proprietary-engine-strategy로 흡수)
  - sources/tornqvist-valheim-ea.md: `[[gdc24-valheim-early-access]]` → `[[gdc2024-valheim-early-access]]` (오타)
  - sources/gdc24-baldurs-gate-3.md: cinematic-pipeline → cinematic-production
  - sources/airbridge-steam-marketing-playbook.md: steam-marketing → marketing-strategy (rename 잔존)
  - comparisons/iteration-cycles·player-feedback·small-studio-goty + entities/fromsoftware: frontmatter sources 한글 라벨 8건 → 영문 slug 정규화
- entities/all.md 중복 행 정리: hazelight-studios·peak 각 2회 → 1회
- 생성 (concepts/ — 4개, 모두 직접 인용 가능한 1차 소스 보유):
  - concepts/steam-next-fest.md (zukowski·2026-02 분석·wishlist-benchmarks + balatro·dave-the-diver 사례)
  - concepts/psychological-safety.md (kumhotire·gamedev-leadership-dynamics + Aristotle·테네리페·허드슨 사례, 슈퍼자이언트·CDPR·Supercell·우쿄)
  - concepts/producer-role.md (hashimoto-producer·gdc26-production-traps·three-mindset-shifts + Force Multiplier·함정 3종·마인드셋 전환 3종)
  - concepts/unreal-engine-5.md (expedition33-ue5-interview·missing-middle + Nanite·Lumen·MetaHuman·Blueprint 95%·샌드폴 무수정 원칙)
- 생성 (sources/ — 1개):
  - sources/catalog-economics-cross-company-2026.md + raw/catalog-economics-cross-company-2026.md (Take-Two·CDPR·Bethesda·Kadokawa·Nintendo·Larian 6사 IR·공시 종합)
- 업데이트:
  - concepts/catalog-economics.md (캡콤 외 사례 6개 정량 보강 + 4가지 모델 분기 — 서비스형·재발매형·Cross-sell형·가격유지형)
  - wiki/overview.md (현재 커버리지에 미디어·플랫폼 행, 핵심 테마에 catalog-economics·dev-talent-pipeline·subscription-economy-gaming 추가)
  - wiki/concepts/all.md (4개 신규 항목 추가)
  - wiki/sources/all.md (catalog-economics-cross-company-2026 1행 추가, 107→108)
  - wiki/index.md (소스 108·개념 50, pill-grid에 4개 신규 항목 추가)
- 메타: 소스 107→108, 개념 46→50
- 모순: 4건 (모두 ⚠️ 블록으로 해소·맥락 명시됨, 신규 발생 없음)
- 완전 고립: 0건. 카탈로그-only 약한 고립: 8건 (comparisons 5 + remedy-entertainment·mobile-gamedev·presentations/steam-marketing-strategy)
- 검증 한계: catalog-economics 보강은 외부 URL fetch 제약으로 사전 학습 지식 + 공식 IR 출처 종합. Take-Two·Kadokawa·Nintendo는 1차 IR로 재검증 가능, Bethesda·Larian은 비공식 출처 의존 (sources 페이지 confidence: medium)

## [2026-05-18] slide | sustainable-studio-staffing 신규 슬라이드 (24장, 보고서 톤)
- 신규: wiki/presentations/sustainable-studio-staffing-deck.html (24장, 약 108KB)
- 신규: wiki/presentations/sustainable-studio-staffing.md (wrapper md, iframe·sources)
- 주제: 비-라이브 서비스 환경 게임 스튜디오의 지속 가능한 인재 모델 7가지 + 5축 메커니즘
- 구조: 1부 문제 정의(3장) + 2부 7가지 모델(10장) + 3부 5축 메커니즘(6장) + 4부 반례·통합(5장)
- 사례: Capcom·Insomniac·FromSoftware·Embark·Larian·Hazelight·Supergiant/Asobo/Sandfall + 반례(EA Frostbite·Double Fine·너티독)
- 디자인: 기존 steam-marketing-strategy-deck.html과 동일 시스템 (흰 배경 + 네이비 + 골드 accent + Pretendard) 일관성 유지
- 갱신:
  - wiki/presentations/all.md 1행 추가 (총 2개)
  - wiki/index.md 프레젠테이션 카운트 1→2, pill-grid 항목 추가
  - Last updated 2026-05-18 유지
- 신뢰도: high (모든 사례가 1차 자료 기반)

## [2026-05-18] ingest | Capcom FY26/3 결산 설명회 PDF
- Source: raw/articles/2026-05-18-capcom-fy26-earnings.md (Capcom IR explanation_2025_full_01.pdf)
- 생성 (2 concepts + 1 source):
  - wiki/sources/capcom-fy26-ir.md
  - wiki/concepts/catalog-economics.md (시리즈 IP 장기 매출 모델, 캡콤 카탈로그 83.7%)
  - wiki/concepts/dev-talent-pipeline.md (연 100명·세대 혼합·R&D Building·Gen AI)
- 업데이트 (sources·related·캡콤 사례 섹션 추가):
  - wiki/entities/capcom.md (FY26/3 실적·시리즈 누적·글로벌 5년 성장·FY27/3 라인업·자본 배분 3원칙)
  - wiki/concepts/marketing-strategy.md (디지털 우선 전환 — 캡콤 FY26/3 사례 섹션)
  - wiki/concepts/game-pricing-strategy.md (시간축 가격 다변화 — 캡콤 카탈로그 모델 섹션)
  - wiki/concepts/innersource.md (R&D Building #3 + Gen AI 다층화 섹션)
  - wiki/concepts/game-market-trends.md (이머징 마켓 5년 성장 + Newzoo 2026/02 데이터 섹션)
- 메타: wiki/index.md 소스 106→107 / 개념 44→46, Last updated 2026-05-18
  - wiki/sources/all.md 1행 추가 (총 107개)
  - wiki/concepts/all.md 2행 추가 (개발 방법론·출시·마케팅 섹션)
  - wiki/index.md pill-grid 2개 추가 (catalog-economics, dev-talent-pipeline)
- 핵심 인사이트: 캡콤은 "신작 매출 회사"가 아니라 "카탈로그 매출 회사". FY26/3 unit sales 5,907만 중 카탈로그 4,946만(83.7%). RE7(2017)이 9년차에 260만장, MH:World(2018)가 7년차에 110만장. 13년 연속 OP 성장의 본질은 시리즈 IP·세대 혼합 팀(20s~50s)·연 100명+ 채용·자체 엔진(RE ENGINE)·이너소스의 다층 결합. Gen AI를 IR에 정식 등재해 routine task 자동화 명시. 글로벌 244개국 판매, 5년간 아시아 +247%/중남미 +148%/일본 +8% — 일본 비중 10%까지 축소.
- 신뢰도: high (Capcom 공식 IR 1차 자료)

## [2026-05-15] backfill | source URL 일괄 백필 (예약 작업)
- 트리거: 사용자가 2026-05-13에 예약한 일회성 backfill 작업
- 매칭·backfill 완료: 88/106 wiki/sources/ 페이지
  - frontmatter에 `source_url`·`source_author`·`source_published` 필드 추가/갱신
  - 본문 첫 줄에 `**원문**: [도메인](URL) — 저자, YYYY-MM-DD` 형식 추가 또는 기존 출처 라인 통일
  - `updated: 2026-05-15`로 갱신
- 매칭 안 된 wiki/sources/ 페이지 (수동 보강 필요): 18개 — PDF·슬라이드·복합 출처
- 매칭 안 된 raw/articles/ 파일 (미 ingest 후보): 5개 — 중복본 또는 신규 ingest 대상
- 변경 파일은 my-wiki repo만, quartz repo 영향 없음

## [2026-05-13] feat | presentations 인프라 + quartz content submodule 동기화 보정
- 신규: wiki/presentations/steam-marketing-strategy.md wrapper 페이지 (iframe 임베드 + 전체화면 버튼)
- 신규: quartz/components/WikiNav.tsx에 "프레젠테이션" 분류 항목 추가 (별도 quartz repo, commit 034c257)
- 보정: GitHub Desktop으로 quartz push 시 content submodule pointer가 옛 851cdf0로 reverted된 사고 → my-wiki에 후속 commit으로 update-quartz.yml Action 재실행 트리거하여 latest pointer 복원
- 교훈: quartz repo는 GitHub Desktop이 아닌 PowerShell `git submodule update --remote content` 후 commit이 안전 (또는 my-wiki만 push하고 Action에 위임)

## [2026-05-12] ingest | IGN Generations In Play 2026 (53페이지 PDF 단일 소스)
- Source: raw/articles/2026-05-12-ign-generations-in-play-2026.md (PDF 업로드: IGN-Entertainment-Generations-In-Play-Audience-Insights-Report-2026.pdf)
- 생성 (4 concepts + 1 entity + 1 source):
  - wiki/sources/ign-generations-in-play-2026.md
  - wiki/concepts/audience-discovery-systems.md (Intent vs Algorithm, Seek→Feed 반전)
  - wiki/concepts/subscription-economy-gaming.md (소유→액세스, discovery engine, Residency Premium)
  - wiki/concepts/creator-economy-trust.md (Earned·Validated·Built in real time 3-tier)
  - wiki/concepts/game-utility-systems.md (Map vs Manual, Resident 인프라)
  - wiki/entities/ign-entertainment.md (1996년 설립, 470M MAU, Maxroll·Planet Pokemon, IMAGINE AI)
- 업데이트 (sources/related/세대 OS 섹션 추가):
  - wiki/concepts/marketing-strategy.md (세대별 OS 마케팅 분기 매트릭스 + Gen Z·M 채널 인사이트)
  - wiki/concepts/live-service-design.md (Players→Residents, 복귀 트리거 세대별, Residency Premium)
  - wiki/concepts/launch-metrics.md (day-of-release, 풀가격/구독/F2P 분포, Gen Z UGC retention)
  - wiki/concepts/early-access-strategy.md (구독 시대 EA = discovery engine funnel)
- 메타: wiki/index.md 소스 105→106 / 개념 40→44, Last updated 2026-05-12
  - wiki/sources/all.md 1행 추가 (총 106개)
  - wiki/concepts/all.md 4행 추가 (출시·마케팅 섹션)
  - wiki/entities/all.md 신규 "미디어·플랫폼" 섹션 + ign-entertainment 추가
- 핵심 인사이트: 세대는 *무엇*이 아닌 *어떻게* 발견·검증·참여하는가가 다른 "OS"로 작동. 같은 게임·관심사도 Gen X(이벤트/방송)와 Gen Z(크리에이터/라이프스타일) 행동 정반대. 소유→액세스 전환 완료(영화 70%·음악 71%·게임 62%). Gen Z 게임 액세스: 풀가격 20%·F2P 46%. 복귀 트리거: Gen X "끝나면 떠남" vs Gen Z "커뮤니티·UGC"(+20%). 90% 게이머가 game help 사용. 신뢰 모델 세대별 3-tier.
- 신뢰도: high (Kantar·UC Berkeley 협업 6,250명 표본). 단 IGN 자체 청자가 high-engagement audience라는 일반화 한계 명시 (entity 페이지)

## [2026-05-07] expand | game-trailer-design (gdc26 트레일러+통합 마케팅 통합)
- 업데이트: wiki/concepts/game-trailer-design.md
- 추가 sources frontmatter: gdc26-integrated-marketing
- 추가 related: community-management
- 신규 섹션 4개:
  - 통합 마케팅 안에서의 트레일러 (트레일러 = 크리에이티브 레이어, 여러 레이어 동시 발화)
  - 런치 플래닝 — 트레일러 비트 매핑 (핵심 비트·CTA·레이어 선택, 타임라인 고려사항)
  - 사례 BG3 단계별 트레일러 활용 (PC출시전·PC출시·PS5·Xbox 4단계 비교표)
  - 사례 소예산 트레일러 효과 (Tunic 미디어스코어 4.5, Chicory $5K → 5M 임프레션)
- 추가 인사이트 callout: "트레일러를 어느 레이어와 함께 발화시킬지가 진짜 디자인"
- 신규 raw fetch 없음 — 두 GDC26 소스 모두 기존 위키에 보유

## [2026-05-07] ingest | 5 sources — Kasavin·Vincke·Fares·Törnqvist·Zukowski
- Source: raw/articles/2026-05-07-{slug}.md (5개 파일, WebSearch+WebFetch로 수집)
- 생성:
  - wiki/sources/kasavin-hades-ea.md (그렉 카사빈 GeekDad 인터뷰 / 하데스 EA "파일럿 에피소드" 모델)
  - wiki/sources/vincke-bg3-ea.md (스벤 빈케 GDC 2024 리캡 / BG3 3년 EA 검증 도구)
  - wiki/sources/fares-hazelight-playtesting.md (요세프 파레스 TheSixthAxis / 짝 단위 코옵 테스트)
  - wiki/sources/tornqvist-valheim-ea.md (헨리크 톤퀴스트 Skövde+Retroware / 발하임 EA 5인 팀)
  - wiki/sources/zukowski-next-fest-strategy.md (Chris Zukowski 2026-02 분석 / Next Fest = 마케팅 부스터)
- 업데이트:
  - wiki/concepts/playtesting.md (sources 5개 추가)
  - wiki/concepts/early-access-strategy.md (sources Kasavin·Vincke 추가, Supergiant 사례 + Larian/Supergiant 공통 패턴 섹션)
  - wiki/concepts/launch-metrics.md (sources Zukowski 추가, Next Fest 2026-02 업데이트 섹션)
  - wiki/concepts/marketing-strategy.md (sources Zukowski 추가)
  - wiki/entities/supergiant-games.md (sources Kasavin 추가, "파일럿 에피소드" 모델 섹션)
  - wiki/entities/larian-studios.md (sources Vincke 추가, BG3 EA 전략 섹션)
  - wiki/entities/hazelight-studios.md (sources Fares 추가, 짝 단위 테스트 섹션)
  - wiki/entities/iron-gate-studio.md (sources Törnqvist 추가, 발하임 EA 회고 섹션)
- 메타: wiki/index.md 소스 95→100, Last updated 2026-05-07 / wiki/sources/all.md 5행 추가
- 신뢰도: 4 high (Kasavin·Fares·Zukowski·Iron Gate) + 1 medium-low (Vincke — 원 GDC 강연 트랜스크립트 미접근, 외부 리캡 기반)

## [2026-05-07] expand | playtesting (규모 선택 프레임워크)
- 업데이트: wiki/concepts/playtesting.md (규모 선택 프레임워크·단계 사례 심층·안티패턴·프레임워크 모음 4개 섹션 추가)
- 추가 wikilink: larian-studios, iron-gate-studio, supergiant-games, hazelight-studios, sandfall-interactive (모두 기존 entity)
- 추가 related: early-access-strategy
- 신규 소스 후보 (미생성): Greg Kasavin GDC 2021 "Early Access Lessons from Hades", Swen Vincke BG3 EA 인터뷰, Josef Fares Game Maker's Notebook, Iron Gate Henrik Törnqvist 인터뷰, Chris Zukowski Steam Next Fest 분석 — 향후 ingest 대상
- 조사 방법: WebSearch (NotebookLM 자동화 미가능 — 다른 Claude 계정으로 Chrome 확장 로그인 상태)

## [2026-05-07] lint
- 모순: 4건 (3건 ⚠️ 블록으로 해소 표시 / 1건 open — gdc26-idg-finding-signal-noise vs matthew-ball-2026-report 시점 전망 차이, 본질적 충돌은 아님)
- 데드 링크: 0건 — 이전 lint(2026-04-28)에서 발견된 [[bioware]], [[obsidian-entertainment]] 모두 entity 페이지 생성으로 해소됨
- 고립 페이지: 0건 — 모든 entity·concept·comparison 페이지가 최소 1회 이상 교차 참조됨
- 미생성 개념 (3회+ 언급): "심리적 안전"(kumhotire·gamedev-leadership·studio-culture), "프로젝트 실패 문화"(supercell·embark 패턴) — 신규 concept 후보
- 다음 조사 주제 제안:
  1. concept: psychological-safety — Aristotle Project·Kumho Tire·Supercell 사례 통합
  2. concept: project-failure-culture — 프로젝트 취소를 학습 자산화하는 조직 패턴
  3. playtesting.md 확장 — 규모별 테스트 선택(12명 소규모·내부 QA·EA 공개) 프레임워크 추가
  4. game-trailer-design 보강 — gdc26-game-trailers, gdc26-integrated-marketing 통합 분석
- overview.md 업데이트: 핵심 테마에 game-pricing-strategy, mobile-gamedev 추가 (최근 ingest 반영)

## [2026-04-28] concept + entity | mobile-gamedev, hazelight-studios, peak
- 생성: wiki/concepts/mobile-gamedev.md
- 생성: wiki/entities/hazelight-studios.md, wiki/entities/peak.md
- 업데이트: wiki/concepts/all.md, wiki/entities/all.md, wiki/index.md (개념 40, 스튜디오 28, 게임 29)
- 통합 소스: ukyou-mobile-liveservice-survival, ukyou-mobile-liveservice-walls, sensortower-2026-report, ukyou-sweden-steam-2025

## [2026-04-28] entity | bioware, obsidian-entertainment, supercell
- 생성: wiki/entities/bioware.md, wiki/entities/obsidian-entertainment.md, wiki/entities/supercell.md
- 업데이트: wiki/entities/all.md, wiki/index.md (스튜디오 수 24→27)
- 목적: companion-philosophy 데드 링크 해소(bioware, obsidian-entertainment), mobile sources 보강(supercell)

## [2026-04-28] concept | game-pricing-strategy
- 생성: wiki/concepts/game-pricing-strategy.md
- 업데이트: wiki/concepts/all.md, wiki/index.md (개념 수 38→39)
- 통합 소스: indiebi-game-pricing-strategy, missing-middle-paradigm-shift-2026, sgc-steam-survival, gdc26-arc-raiders-reset, gdc26-newzoo-market-analysis

## [2026-04-28] lint
- 모순: 3건 (모두 기존 ⚠️ 블록으로 해소 표시됨)
- 데드 링크: 2건 — [[bioware]], [[obsidian-entertainment]] (comparisons/companion-philosophy.md에서 링크 사용 중이나 entity 페이지 없음)
- 고립 엔티티: avalanche-software, asobo-studio (비교/개념에서 참조 1회 이하)
- 미생성 개념 (3회+ 언급): "가격 정책" (5개 concept 파일에서 11회), "모바일 게임 개발" (소스 2개 있으나 concept 페이지 없음)
- overview.md 업데이트: 현재 커버리지(주요 출처 보강), 핵심 테마(game-market-trends 추가, dev-org/live-service 설명 보강)

## [2026-04-28] ingest | raw/articles 미ingest 10개 파일 일괄 처리
- Source: raw/articles/ (2026-04-27 저장 파일 7개 + 이전 파일 3개)
- 생성 (소스 7개):
  - wiki/sources/gcon2025-hashimoto-producer.md
  - wiki/sources/indiebi-game-pricing-strategy.md
  - wiki/sources/vilehyperion-combat-system.md
  - wiki/sources/ukyou-sweden-steam-2025.md
  - wiki/sources/ukyou-mobile-liveservice-survival.md
  - wiki/sources/ukyou-mobile-liveservice-walls.md
  - wiki/sources/ukyou-project-failure-structure.md
- 스킵 (저가치 3개): Sink or Swim (MixMob 크립토), 7 Open-World Buildings (리스트클), Click4Gameplay RPG Combat (트랜스크립트 없음)
- 업데이트 (개념 6개):
  - dev-org-structure: 하시모토 신지 프로듀서/디렉터 정의 추가
  - marketing-strategy: 지역 가격 차등화·세일 타이밍 섹션 추가
  - combat-design: For Honor Simple but Deep 모델 추가
  - live-service-design: 모바일 4요소·4대 벽 섹션 추가
  - indie-business-strategy: 프로젝트 실패 구조 섹션 추가
  - game-market-trends: 스웨덴 Steam 생태계 섹션 추가
- 통계: sources 88→95, index.md 업데이트

## [2026-04-28] 소스 slug 정규화 (미ingest 해소)
- 문제: wiki/sources/ 파일 6개가 concept/entity 페이지에서 한글 레거시 링크명으로 참조되어 slug 기반 연결이 끊어져 있었음
  - expedition33-ue5-interview, gdc24-baldurs-gate-3, gdc25-astrobot
  - gdc26-expedition33-programmers, gdc26-ghost-of-yotei, re2023-re-engine-philosophy
- 조치: 30개 concept/entity 파일의 sources: 필드 + 본문 wikilink를 slug 기준으로 일괄 정규화
  - 추가 정리: GDC26 반짝임·아크레이더스·젤다·황재호·SGC·캡콤IR·FromSoftware 등 레거시 링크 14개 파일 추가 교체
- 결과: 전체 88개 소스 — 미ingest 0개

## [2026-04-28] ingest | How to Make AAA Looking Games With a Team of 20 Artists — Asobo Studio, GDC 2023
- Source: raw/gdc2023-asobo-how-to-make-aaa-small-team.md (원본: PDF, HOW+TO+MAKE_Binetruy+x+Paulus_Gregoire+x+Loic.pdf)
- 생성:
  - sources/gdc2023-asobo-how-to-make-aaa-small-team.md
  - entities/asobo-studio.md (프랑스 보르도, 인하우스 엔진, "Focus on What Matters")
  - entities/a-plague-tale-requiem.md (2022, PS5 전용, 20명 아티스트)
- 업데이트:
  - concepts/small-team-development.md (Asobo 7번째 사례 추가 — 제약으로 공통 언어 만들기)
  - concepts/proprietary-engine-strategy.md (Asobo 중간 규모 독자 엔진 섹션 추가)
  - entities/all.md (스튜디오 23→24, 게임 27→28)
  - sources/all.md (87→88개)
  - index.md (소스 92→93, 스튜디오 23→24, 게임 27→28, Last updated 2026-04-28)
  - overview.md (스튜디오 21→24, 게임 27→28)

## [2026-04-24] lint + entity 생성
- 생성:
  - entities/supergiant-games.md (노 크런치·이직률 0%·스코프 제한 철학)
  - entities/remedy-entertainment.md (Northlight 엔진·Control Universe·루핑 진행)
- 업데이트:
  - entities/all.md (21 → 23개: supergiant-games·remedy-entertainment 추가)
  - index.md (게임 25 → 27로 정정)
  - overview.md (스튜디오 20→21, 게임 24→27, 핵심 테마 3개 추가)

## [2026-04-24] ingest | 소울라이크 게임 디자인 분석 — 프롬소프트웨어 중심 종합 리서치
- Source: raw/soulslike-game-design-research-2026.md (웹 리서치 종합)
- Google Drive 업로드: ID 1_HcCatH99dwUwAVhA6_B2JTTELeeIjhpXNI719lpdDY → NotebookLM에 수동 추가 필요
- 생성:
  - sources/soulslike-game-design-research-2026.md
  - concepts/soulslike.md (공정한 가혹함·죽음 루프·보스 설계·의도적 모호성·장르 진화)
- 업데이트:
  - sources/all.md (86 → 87개)
  - concepts/all.md (soulslike 항목 추가 → 38개)
  - index.md (소스 92개, 개념 38개, Last updated 2026-04-24)

## [2026-04-23] 비교분석 추가 | companion-philosophy + aaa-scaling-strategy
- 생성:
  - comparisons/companion-philosophy.md (BioWare·Larian·CDPR·Obsidian·Naughty Dog 동반자 철학 비교)
  - comparisons/aaa-scaling-strategy.md (샌드폴·엠바크·애로우헤드·Avalanche·팀 아소비 AAA 전략 비교)
  - sources/companion-design-research-2026.md
  - raw/companion-design-research-2026.md
- 업데이트:
  - comparisons/all.md, index.md (비교분석 9→11)
  - sources/all.md (86개로 갱신)

## [2026-04-23] ingest | 비전 선언문 & 게임 디자인 기둥 — 웹 리서치
- Source: raw/vision-statement-research-2026.md
- 생성:
  - sources/vision-statement-research-2026.md
- 업데이트:
  - concepts/vision-statement.md (비전 유형 표 확장, 크리에이티브 디렉션 4요소, Subnautica 기둥 사례, 오해 교정 섹션 추가)
  - sources/all.md (85개로 갱신)
  - index.md (소스 90→91)

## [2026-04-23] ingest | 2026 미싱 미들 패러다임 전환 (Google Docs)
- Source: raw/missing-middle-paradigm-shift-2026.md (원본: Google Docs)
- 생성:
  - sources/missing-middle-paradigm-shift-2026.md
  - entities/arrowhead-game-studios.md
  - entities/helldivers-2.md
  - concepts/live-service-design.md
- 업데이트:
  - entities/arc-raiders.md (F2P→프리미엄 전환·출시 데이터·Escalation 로드맵 추가)
  - concepts/game-market-trends.md (미싱 미들·미드 프라이스 섹션 추가)
  - concepts/extraction-genre-design.md (F2P 탈출 비즈니스 모델 섹션 추가)
  - entities/all.md, concepts/all.md (신규 항목 추가)
  - index.md (소스 88→90, 스튜디오 22→23, 게임 24→25, 개념 36→37)

## [2026-04-23] ingest | 스팀 게임 마케팅 전략 (4개 소스)
- Source: raw/steam-next-fest-2026-analysis.md, raw/steam-next-fest-wishlist-benchmarks-2025.md, raw/steam-page-optimization-guide-2026.md, raw/game-marketing-strategy-2026.md
- NotebookLM 노트북: "Steam Game Marketing Strategy" (소스 5개)
- 생성:
  - sources/steam-next-fest-2026-analysis.md
  - sources/steam-next-fest-wishlist-benchmarks-2025.md
  - sources/steam-page-optimization-guide-2026.md
  - sources/game-marketing-strategy-2026.md
- 업데이트:
  - concepts/marketing-strategy.md (SNF 정량 데이터·스토어 최적화·2026 캘린더 섹션 추가)
  - concepts/launch-metrics.md (SNF 위시리스트 벤치마크 데이터 추가)
  - index.md (소스 84 → 88개)

## [2026-04-23] create | 비교 분석 3개 신규 생성
- 생성:
  - comparisons/marketing-channels.md (PR·크리에이터·유료·트레일러·소셜·커뮤니티·스팀 채널별 비교 + 규모별 우선순위 + BG3 타임라인)
  - comparisons/mission-level-structure.md (히트맨 3층 가이던스 / CP2077 3원칙 / 알란웨이크2 루핑 진행 / TLOU2 내러티브 선형 / Hi-Fi RUSH 역방향 설계)
  - comparisons/leadership-production.md (캡콤 협업 서비스 / 인섬니악 방해물 제거 / 슈퍼자이언트 노크런치 / 밸브 수평 구조 역설 / CDPR 마감 독재 + 프로듀서 함정 3종 + Fisher 마인드셋 전환)
- 업데이트:
  - comparisons/all.md (6 → 9개)
  - index.md (비교 분석 9개)

## [2026-04-23] ingest | 조직장 뉴스레터 2화 — 심리적 안전감
- Source: https://maily.so/kumhotire/posts/1gz2kq2nz3q (금호타이어 HR운영팀)
- 생성:
  - sources/kumhotire-psychological-safety.md
- 업데이트:
  - concepts/studio-culture.md (구글 아리스토텔레스 5요소 목록, 테네리페/허드슨 항공 사례, 리더 Do/Don't 추가)
  - sources/all.md (83 → 84개)
  - index.md (소스 84개)

## [2026-04-23] ingest | 비디오 게임 개발 리더십의 역학
- Source: Google Docs (https://docs.google.com/document/d/14XvikWdKOm0xVIFvVw8rGpOKqD-9OYXTzkuVpmUon1E)
- 생성:
  - sources/gamedev-leadership-dynamics.md
  - concepts/ai-gamedev.md (GenAI 정서 데이터 2024~2026, 용도별 수용도, 역할 변화)
- 업데이트:
  - concepts/studio-culture.md (심리적 안전감·슈퍼자이언트·밸브·CDPR 케이스 스터디 추가)
  - concepts/dev-org-structure.md (크리에이티브 디렉터 vs 총괄 프로듀서, TA 브릿지 역할 추가)
  - entities/cd-projekt-red.md (CP2077 리더십 실패 포스트모템 추가)
  - entities/mint-rocket.md (황재호 리더십 철학·이중 트랙 모델 추가)
  - concepts/all.md (ai-gamedev 추가 → 36개)
  - sources/all.md (82 → 83개)
  - index.md (소스 83개, 개념 36개, ai-gamedev 추가)

## [2026-04-23] ingest | 글로벌 탑티어 게임 개발사의 멀티 프로젝트 조직 구조 및 이너소스 도입 분석 보고서
- Source: Google Docs (https://docs.google.com/document/d/1mGpxYiXx21S9jTkR0IxxgQ5_TE5wNzYZbRkJrZtPzT4)
- 생성:
  - sources/multiproject-innersource-report.md
  - concepts/innersource.md (이너소스 모델, Trusted Committer, PR 기반 엔진 개발, EA Frostbite 반면교사)
- 업데이트:
  - concepts/multi-project-development.md (인섬니악·캡콤·EA 프로스트바이트 사례 추가, innersource 연결)
  - concepts/dev-org-structure.md (기술 공유 아키텍처 섹션 추가, Sony ICE 팀 모델)
  - entities/capcom.md (소스 슬러그 수정, 이너소스 실천 섹션 추가)
  - entities/embark-studios.md (소스 슬러그 수정, 오픈소스 우선 철학 섹션 추가)
  - concepts/all.md (innersource 추가 → 35개)
  - sources/all.md (81 → 82개, 신규 항목 추가)
  - index.md (소스 81→82, 개념 34→35, innersource 추가)

## [2026-04-22] create | community-management 개념 페이지 + alan-wake-2 엔티티 페이지
- 생성:
  - concepts/community-management.md (채널별 운영 원칙, 직접 소통, 라이브 서비스 연동)
  - entities/alan-wake-2.md (Remedy 2023, 두 주인공 구조, 꿈의 논리, 루핑 진행)
- 업데이트:
  - entities/mint-rocket.md (소스 슬러그 수정: 한글 → cgdc-dave-the-diver)
  - concepts/all.md (community-management 추가 → 35개)
  - entities/all.md (alan-wake-2 추가 → 게임 24개)
  - index.md (게임 24개, 개념 34개)

## [2026-04-22] rename | steam-marketing → marketing-strategy
- 개념 페이지 이름 변경: concepts/steam-marketing.md → concepts/marketing-strategy.md
- title: "스팀 마케팅 전략" → "마케팅 전략"
- 설명 업데이트: 스팀 한정 → 통합 마케팅 채널 전반으로 확장
- 소스 추가: gdc26-integrated-marketing, gdc26-game-trailers
- 전체 wiki 참조 교체: [[steam-marketing|...]] → [[marketing-strategy|마케팅 전략]] (27개 파일)

## [2026-04-22] ingest | GDC 2026/2024 PDF 7개 — AAA·트레일러·디자인감각·Alan Wake2·플레이테스팅·통합마케팅·Comics
- Source: PDF 7개 (pdftotext 추출)
  - Murphy_Kelly_Hogwarts+Legacy+Evolving.pdf
  - MARIE_Adrien_AllGameTrailers.pdf
  - Nikolich_Evan_Developing+and+Sharpening.pdf
  - ThePlayervsDreamLogic_AlanWake2.pdf
  - Souki_Francisco_Too-Much-Playtesting.pdf
  - OrtizLapaz_David_The_Integrated+Marketing.pdf
  - ComicsToGames_AllPresentations.pdf
- 생성 (sources/ — 7개):
  - gdc26-hogwarts-evolving-aaa.md
  - gdc26-game-trailers.md
  - gdc26-design-sense.md
  - gdc24-alan-wake2-mission-design.md
  - gdc26-too-much-playtesting.md
  - gdc26-integrated-marketing.md
  - gdc26-comics-to-games.md
- 생성 (concepts/ — 2개):
  - design-sense.md
  - game-trailer-design.md
- 업데이트:
  - playtesting.md (Schell Games 228회 플레이테스트 소스 추가)
  - ip-adaptation-design.md (Hogwarts AAA + Comics to Games 소스 추가)
  - concepts/all.md (26개)
  - sources/all.md (87개)
  - index.md (87개 소스, 26개 개념)

## [2026-04-22] ingest | GDC 2026 PDF 3개 — 프로덕션·리더십·동반자 설계
- Source: PDF 3개 (pdftotext 추출)
  - Carcich_Benjamin_ProductionTrapsHow.pdf
  - Fisher_Kristie_ThreeMindsetShifts.pdf
  - Moberly&Dollarhyde_Lis&Kate_DesigningRelationshipsHow.pdf
- 생성 (sources/ — 3개):
  - gdc26-production-traps.md
  - gdc26-three-mindset-shifts.md
  - gdc26-designing-companions.md
- 생성 (concepts/ — 1개):
  - companion-design.md
- 업데이트:
  - dev-org-structure.md (프로듀서 Force Multiplier / Alignment 섹션 추가)
  - studio-culture.md (의도적 문화 설계 섹션 추가)
  - concepts/all.md (24개, companion-design 추가)
  - sources/all.md (80개)
  - index.md (80개 소스, 24개 개념)

## [2026-04-22] ingest | 대량 배치 — GDC 2026 마케팅·시장·디자인 (PDF 4개)
- Source: PDF 4개 (pdftotext 추출)
  - Lieu_Derek_BackToBasics... (마케팅 기반)
  - 2026.03-IDG-GDC2026-Finding Signal... (시장 분석)
  - Rouse_Richard_RulesOfTheGame (게임 디자인 규칙)
  - Reisenegger_Thomas_Your Steam Page Needs a Soul (스팀 페이지)
- 생성 (sources/ — 4개):
  - gdc26-lieu-back-to-basics-marketing.md
  - gdc26-idg-finding-signal-noise.md
  - gdc26-rules-of-the-game.md
  - gdc26-steam-page-needs-soul.md
- 업데이트:
  - concepts/steam-marketing.md (소스 2개 추가)
  - concepts/game-market-trends.md (IDG 소스 추가)
  - sources/all.md (73→77개)
  - index.md (소스 수 갱신)
- 모순: IDG 2029 낙관 전망 vs 매튜 볼 구조적 비관 — game-market-trends에 기존 모순 블록과 통합

## [2026-04-22] ingest | Honing the Blade — Ghost of Yotei 전투 디자인 (서커펀치 PDF)
- Source: PDF — Fishman_Theodore_honing_the_blade_evolving_combat_for_ghost_of_yotei.pdf
- 추출 방법: pdftotext CLI
- 생성:
  - sources/gdc25-ghost-of-yotei-combat.md
- 업데이트:
  - entities/ghost-of-yotei.md (전투 설계 섹션 추가)
  - sources/all.md (72→73개)
  - index.md (소스 수 갱신)
- 모순: 없음

## [2026-04-22] ingest | 시장 분석 2건 — Sensor Tower + 매튜 볼 2026
- Source: raw/articles/2026-04-21T110136+0900-센서 타워 연례 보고서...md
- Source: raw/articles/2026-04-21T110148+0900-매튜 볼의 2026년 보고서...md
- 생성:
  - sources/sensortower-2026-report.md
  - sources/matthew-ball-2026-report.md
- 업데이트:
  - concepts/game-market-trends.md (PC·모바일 2025 현황 + 성장의 역설 섹션 추가, 소스 2개 추가)
  - sources/all.md (70→72개)
- 모순: 뉴주(인디 부상) vs 매튜 볼(서구 개발사 구조적 불이익) — 시장 전체 vs 개별 기업 수익 프레임 차이로 해소, game-market-trends.md에 병기

## [2026-04-20] lint | 연결성 개선
- 저연결 개념 수정:
  - hogwarts-legacy.md related에 ip-adaptation-design 추가
  - witcher-3.md related에 dlc-expansion-design 추가
  - arc-raiders.md related에 extraction-genre-design 추가
  - dev-org-structure.md related에 studio-culture 추가
- 생성 (누락 엔티티):
  - entities/sekiro.md (프롬소프트웨어, 자세 시스템·계층적 치명감)
- 업데이트:
  - sources/adam-millard-sword-fighting.md (sekiro 링크 추가)
  - index.md (세키로 엔티티 추가)
- 잔여 마이너 보류: Bayonetta (gmtk-combat-system에서 언급, 낮은 우선순위)

## [2026-04-20] ingest | 前 록스타 디자이너 Ben Hinchliffe 인터뷰 (GTA VI O'clock)
- Source: raw/articles/2026-04-20T150408+0900-Ex-Rockstar Designer Interview - GTA VI O'clock - Episode 47.md
- 출처: GTA VI O'clock Ep.47 (2024-10-31), Ben Hinchliffe 인터뷰
- 생성:
  - sources/ex-rockstar-ben-hinchliffe-interview.md
- 업데이트:
  - concepts/open-world-design.md (록스타식 콘텐츠 밀도 설계·90% 규칙·What-if 레이어 섹션 추가)
  - sources/all.md (69→70개)
  - index.md (최신 소스 갱신)
- 모순: 없음

## [2026-04-20] ingest | 대량 배치 — GMTK + Adam Millard (5개 파일)
- Source: raw/articles/ (2026-04-20 타임스탬프 신규 8개 중 5개 ingest, 3개 스킵)
- 스킵: Click4Gameplay RPG combat (내용 없음), VileHyperion (소규모·얇음), Rockstar ex-dev (파일명 따옴표 오류)
- 생성 (sources/ — 5개):
  - gmtk-mda-framework.md (MDA 프레임워크, Alien Isolation 사례)
  - gmtk-game-balancing.md (트레이드오프·카운터·퍼셉션)
  - gmtk-10-lessons.md (GMTK 10주년 10대 교훈)
  - gmtk-combat-system.md (공격 프레임·방어·패리·스턴락)
  - adam-millard-sword-fighting.md (치명감·페이즈 분리·Furi·Nidhogg)
- 생성 (concepts/ — 2개):
  - mda-framework.md
  - game-balance.md
- 업데이트:
  - concepts/combat-design.md (GMTK 프레임 분석 + Adam Millard 검투 섹션 추가)
  - concepts/playtesting.md (gmtk-10-lessons 소스 추가)
  - sources/all.md (64→69개)
  - index.md (최신 소스 갱신, 개념 2개 추가)
- 모순: 없음

## [2026-04-20] ingest | 레드 데드 리뎀션 2 스토리 뒷이야기 (Variety)
- Source: raw/articles/2026-04-20-rdr2-story-behind-the-story.md (사용자 직접 붙여넣기)
- 출처: Variety / Brian Crecente, Rob Nelson·Michael Unsworth 인터뷰 (2018)
- 생성:
  - sources/rdr2-story-behind-the-story.md
  - entities/red-dead-redemption-2.md
- 업데이트:
  - concepts/quest-narrative-design.md (RDR2 섹션 추가 — 23명 앙상블·워크앤톡·아너 시스템·선택적 제거)
  - sources/all.md (63→64개)
  - index.md (최신 소스 갱신, 게임 엔티티 RDR2 추가)
- 모순: 없음

## [2026-04-20] ingest | 중견 게임 스튜디오를 위한 스팀 마케팅 완전정복 (Airbridge)
- Source: raw/articles/2026-04-20T142539+0900-중견 게임 스튜디오를 위한 스팀(Steam) 게임 마케팅 완전정복.md
- 출처: Airbridge 블로그 (2025-07-03), 에어브릿지 남성필 대표 × Liquid Advertising Nikki DePaola 인터뷰
- 생성:
  - sources/airbridge-steam-marketing-playbook.md
- 업데이트:
  - concepts/steam-marketing.md (브랜딩+퍼포먼스 통합·위시리스트 70% 기준·PC 유저 구매 행동·놓치는 채널 3가지·크로스 플랫폼 함정 섹션 추가)
  - sources/all.md (62→63개)
  - index.md (최신 소스 10개 갱신)
- 모순: 없음

## [2026-04-20] lint | 위키 연결성 개선
- 깨진 wikilink 수정 2개: marvel-spiderman → marvel-spiderman-2, zelda-tears-of-kingdom → gdc24-zelda-tears-of-kingdom
- 생성 (고립/누락 페이지):
  - concepts/ip-adaptation-design.md
  - concepts/studio-culture.md
  - entities/death-stranding.md
  - entities/marvel-spiderman-2.md
- 업데이트: combat-design.md (comparison 링크), level-design-principles.md (hifi-rush·io-interactive·environmental-storytelling 링크), open-world-design.md (comparison·스파이더맨2·데스스트랜딩 링크)
- index.md에 신규 페이지 반영
- 잔여 고립 페이지 (마이너, 보류): cinematic-pipeline, community-management, unreal-engine-5 slug

## [2026-04-20] ingest | 대량 배치 — 마케팅·시장·장르·DLC·오픈월드 (10개 파일)
- Source: raw/articles/ (2026-04-20 타임스탬프 신규 10개)
- 생성 (sources/ — 10개):
  - firstlook-signals-of-success.md (퍼스트룩 흥행 예측 보고서)
  - arc-raiders-extraction-genre.md (익스트랙션 장르 대중화)
  - gdc26-newzoo-market-analysis.md (뉴주 게임 시장 분석)
  - gdc25-schell-studio-principles.md (제시 셸 스튜디오 원칙)
  - gdc25-balatro-marketing.md (발라트로 마케팅)
  - gdc25-steam-new-rules.md (스팀 새 규칙 마케팅)
  - gdc24-hogwarts-legacy-design.md (호그와트 레거시 팬/게이머 설계)
  - gdc24-cdpr-dlc-design.md (CDPR 확장팩 비결)
  - gdc24-spiderman2-open-world.md (스파이더맨2 오픈월드 진화)
  - gdc24-steam-secrets.md (스팀의 비밀)
- 생성 (concepts/ — 4개):
  - launch-metrics.md (흥행 예측 지표)
  - extraction-genre-design.md (익스트랙션 장르 설계)
  - dlc-expansion-design.md (DLC·확장팩 설계)
  - game-market-trends.md (게임 시장 트렌드)
- 생성 (entities/ — 3개):
  - balatro.md
  - hogwarts-legacy.md
  - avalanche-software.md
- 업데이트:
  - concepts/steam-marketing.md (데모 전략·주목의 수레바퀴·스팀 숨은 기능 섹션 추가)
  - concepts/open-world-design.md (spiderman2 소스 추가)
  - wiki/index.md (소스 최신 10개 갱신, 엔티티 22개→25개, 개념 21개→25개)
  - wiki/sources/all.md (51→61개)

## [2026-04-16] concept+comparison-fill | 개념·비교 페이지 6개 신규 생성
- 생성 (concepts/ — 3개):
  - environmental-storytelling.md (다크소울·TLOU2·건축 원리·내러티브 레벨)
  - player-guidance-design.md (SDT·필드 삼각형·히트맨 3층·CP2077 3원칙)
  - dev-org-structure.md (스크럼·프롬소프트웨어 유동 배치·캡콤 파이프라인)
- 생성 (comparisons/ — 3개):
  - combat-philosophy.md (GoT vs GoW vs TLOU vs 히트맨)
  - open-world-guidance.md (BotW vs 엘든링 vs GTA5 vs 유비식)
  - studio-org-structure.md (프롬소프트웨어 vs 캡콤 vs 베데스다 vs Scrum)
- 업데이트: index.md (개념 21개·비교 6개 반영)

## [2026-04-16] entity-fill | 소스에서 언급된 게임·스튜디오 엔티티 생성
- 생성 (entities/games — 13개):
  - dark-souls.md, elden-ring.md, breath-of-the-wild.md, skyrim.md
  - cyberpunk-2077.md, witcher-3.md, god-of-war-2018.md
  - ghost-of-tsushima.md, the-last-of-us.md, valheim.md
  - gta5.md, hifi-rush.md, hitman-2016.md
- 생성 (entities/studios — 5개):
  - sony-santa-monica.md, bethesda-game-studios.md, tango-gameworks.md
  - iron-gate-studio.md, rockstar-games.md
- 업데이트: index.md (게임 19개·스튜디오 19개 전체 반영)

## [2026-04-16] lint | 위키 연결성 개선
- 모순: 기존 2개 유지, 신규 없음
- 고립 소스 5개 연결, 깨진 wikilink 7개 수정
- 생성:
  - concepts/indie-business-strategy.md
  - concepts/ai-navigation.md
  - concepts/cinematic-production.md
  - entities/kojima-productions.md
  - entities/insomniac-games.md
  - entities/io-interactive.md
- 업데이트:
  - sources/gdc2023-indie-starter-kit.md (비전 설계 → 비전 선언문)
  - concepts/steam-marketing.md (no-budget-marketing 소스·인디 비즈니스 링크 추가)
  - concepts/level-design-principles.md (Hi-Fi RUSH 역방향 설계 섹션 추가)
  - index.md

## [2026-04-15] ingest | 대량 배치 — 레벨 디자인·오픈월드·전투·인디 비즈니스 (30개 파일)
- Sources: raw/articles/ (2026-04-15 추가 파일 중 신규 27개, 중복 6개 제외)
- 생성 (sources/):
  - gdc2013-ten-principles-level-design.md
  - gdc2016-architecture-level-design.md
  - gdc2016-hitman-nonlinear-sandbox.md
  - gdc2017-narrative-level-design.md
  - gdc2019-nonlinear-level-design.md
  - gdc2019-god-of-war-combat.md
  - gdc2019-god-of-war-axe.md
  - gdc2019-spiderman-animation.md
  - gdc2021-level-design-studio-wide.md
  - gdc2021-got-master-katana.md
  - gdc2021-got-honoring-blade.md
  - gdc2021-death-stranding-ai.md
  - gdc2022-tlou2-museum-flashback.md
  - gdc2023-cyberpunk-nonlinear-level-design.md
  - gdc2023-quest-design-lessons-cdpr.md
  - gdc2023-indie-starter-kit.md
  - gdc2023-no-budget-marketing.md
  - gdc2024-hifi-rush-backwards.md
  - gdc2024-skyrim-starfield-design-collab.md
  - gdc2024-valheim-early-access.md
  - gdc2014-tlou-melee-system.md
  - open-world-linearization-gta5.md
  - skyrim-not-perfect-mda.md
  - zelda-vs-ubisoft-open-world.md
  - botw-eldenring-visual-guidance.md
  - gmtk-world-design-elden-ring.md
  - gmtk-world-design-dark-souls.md
  - dark-souls-world-hides-lore.md
  - dark-souls-lordran-layout.md
- 생성 (concepts/):
  - level-design-principles.md (신규: 공간 문법·건축 원리·비선형 패턴·샌드박스 가이던스)
  - open-world-design.md (신규: 선형화·SDT이론·필드삼각형법칙·아코디언구조·MDA)
  - combat-design.md (신규: 치명성계약·HP인플레이션·카메라-전투관계·Unsynced)
  - quest-narrative-design.md (신규: 6요소프레임워크·CDPR교훈·공간내러티브·팀협업)
- 생성 (entities/):
  - cd-projekt-red.md (신규: 폴란드 바르샤바, 위처·사이버펑크)
- 업데이트:
  - index.md (소스 29개·컨셉 4개·엔티티 1개 추가)
- 중복 처리 (ingest 제외):
  - Tunes of Kingdom ×2 (이미 처리됨)
  - Skyrim-Starfield Collab ×2 (중복)
  - Evolving Combat GoW ×2 (중복)
  - GDC26 Arc Raiders 한국어 버전 (이미 처리됨)
- 저가치 항목 스킵:
  - "7 Open-World Games That Allow You To Enter Most Buildings" (목록 기사)
  - "Sink or Swim" (암호화폐 게임 전환, 무관)
- 모순: 없음

## [2026-04-14] ingest | 젤다 TotK GDC24 강연 + 중복 파일 확인
- Source: raw/articles/2026-04-13T181649+0900-GDC24 젤다의 전설, 만들었지만 만들지 않은 '미친' 자유도.md
- 중복 파일 확인 (ingested 처리 없음): 2026-04-14T181252+0900-The Risks of Multi Game Development.md (2026-04-14T160336 파일과 동일 소스)
- 생성:
  - sources/gdc24-zelda-tears-of-kingdom.md
  - entities/nintendo.md
  - concepts/emergent-systems-design.md (신규: 창발적 시스템 설계, 규칙이 자유를 만든다)
- 업데이트: index.md
- 모순: 없음

## [2026-04-14] ingest | 7개 아티클 — 개발 전략·멀티 프로젝트·엔진·애자일
- Sources: raw/articles/ (7개 파일)
  - Capcom Integrated Report 2021 (개발 전략)
  - The Risks of Multi Game Development (2014)
  - Agile Game Development With Scrum: Teams (2010)
  - Naughty Dog Still Falling Just Short of Simultaneous Development (2021)
  - FromSoftware made Elden Ring and Armored Core 6 with 300 developers (2023)
  - RE:2023 RE ENGINE Philosophy (2023)
  - Embark Studios Söderlund — Quarter of AAA Budget (2026)
- 생성:
  - sources/capcom-ir2021-dev-strategy.md
  - sources/risks-multi-game-development.md
  - sources/agile-scrum-teams.md
  - sources/naughty-dog-multi-project.md
  - sources/fromsoftware-300-devs.md
  - sources/re2023-re-engine-philosophy.md
  - sources/embark-soderlund-quarter-budget.md
  - entities/capcom.md
  - entities/fromsoftware.md
  - entities/naughty-dog.md
  - concepts/multi-project-development.md (신규)
  - concepts/proprietary-engine-strategy.md (신규)
- 업데이트:
  - entities/embark-studios.md (인원·판매 수치·효율화 철학 추가)
  - index.md
- 모순:
  - 독자 엔진 전략: 캡콤(독자 엔진 강점) vs 샌드폴(서드파티 무수정 강점) — 스튜디오 규모에 따른 합리적 분기로 해소, proprietary-engine-strategy.md에 병기

## [2026-04-13] ingest | GDC26 강연 — 아크 레이더스 리셋 성공 신화
- Source: raw/articles/gdc26-arc-raiders-reset.md
- 생성:
  - sources/gdc26-arc-raiders-reset.md
  - entities/embark-studios.md
  - entities/arc-raiders.md
  - concepts/data-driven-development.md (신규: 3일 버스트·바구니 시스템·UXR 활용)
- 업데이트:
  - concepts/small-team-development.md (강제된 집중 — 팀 리셋 추가)
  - concepts/playtesting.md (엠바크 UXR 기반 테스트 추가)
  - concepts/vision-statement.md (기둥 기반 의도 소통 — 엠바크 방식 추가)
  - index.md
- 모순: 없음

## [2026-04-13] 비교 페이지 생성
- 생성:
  - comparisons/iteration-cycles.md (반복 개발 주기 비교)
  - comparisons/small-studio-goty.md (소규모 스튜디오 대작 전략 비교)
  - comparisons/player-feedback.md (플레이어 피드백 수집 전략 비교)
- 발견된 모순 기록:
  - player-feedback.md: 라리안 얼리액세스 vs 민트로켓 "완성도 먼저" — 표면 충돌, 공통 교훈으로 해소

## [2026-04-13] ingest | GDC·컨퍼런스 강연 4건 (서커펀치, 민트로켓, SGC)
- Source: raw/articles/ (4개 파일)
  - GDC26 고스트 오브 요테이 — 덜어냄의 미학
  - GDC26 관객들이 찾는 게임에는 '반짝임'이 있다
  - CGDC 황재호 대표 — 생존을 위한 8계명
  - SGC 실전 사례로 배우는 스팀에서 살아남기
- 생성:
  - sources/gdc26-ghost-of-yotei.md
  - sources/gdc26-spark.md
  - sources/cgdc-dave-the-diver.md
  - sources/sgc-steam-survival.md
  - entities/sucker-punch-productions.md
  - entities/ghost-of-yotei.md
  - entities/mint-rocket.md
  - entities/dave-the-diver.md
  - concepts/vision-statement.md
  - concepts/playtesting.md
  - concepts/steam-marketing.md
- 업데이트:
  - concepts/rapid-prototyping.md (서커펀치 방식 추가)
  - concepts/small-team-development.md (잘라내기 문화 추가, 서커펀치 연결)
  - index.md
- 모순: 없음

## [2026-04-13] ingest | GDC 강연 및 개발 사례 4건
- Source: raw/articles/ (4개 파일)
  - GDC25 아스트로봇의 성공, 마법은 없었다
  - GDC24 발더스 게이트3, 시작부터 출시까지
  - GDC26 33원정대, 단 4명뿐이던 프로그래머의 역할
  - Clair Obscur: Expedition 33 개발 과정 (언리얼 공식 인터뷰)
- 생성:
  - sources/gdc25-astrobot.md
  - sources/gdc24-baldurs-gate-3.md
  - sources/gdc26-expedition33-programmers.md
  - sources/expedition33-ue5-interview.md
  - entities/team-asobi.md
  - entities/larian-studios.md
  - entities/sandfall-interactive.md
  - entities/astro-bot.md
  - entities/baldurs-gate-3.md
  - entities/clair-obscur-expedition-33.md
  - concepts/rapid-prototyping.md
  - concepts/small-team-development.md
  - concepts/designer-empowerment.md
  - concepts/early-access-strategy.md
  - index.md (초기화)
  - overview.md (초기화)
- 업데이트: 없음 (최초 ingest)
- 모순: 없음 (최초 ingest)
- 저가치 항목 스킵:
  - "7 Open-World Games That Allow You To Enter Most Buildings" (목록 기사)
  - "Sink or Swim" (암호화폐 게임 전환, 무관)
- 모순: 없음

## [2026-04-14] ingest | 젤다 TotK GDC24 강연 + 중복 파일 확인
- Source: raw/articles/2026-04-13T181649+0900-GDC24 젤다의 전설, 만들었지만 만들지 않은 '미친' 자유도.md
- 중복 파일 확인 (ingested 처리 없음): 2026-04-14T181252+0900-The Risks of Multi Game Development.md (2026-04-14T160336 파일과 동일 소스)
- 생성:
  - sources/gdc24-zelda-tears-of-kingdom.md
  - entities/nintendo.md
  - concepts/emergent-systems-design.md (신규: 창발적 시스템 설계, 규칙이 자유를 만든다)
- 업데이트: index.md
- 모순: 없음

## [2026-04-14] ingest | 7개 아티클 — 개발 전략·멀티 프로젝트·엔진·애자일
- Sources: raw/articles/ (7개 파일)
  - Capcom Integrated Report 2021 (개발 전략)
  - The Risks of Multi Game Development (2014)
  - Agile Game Development With Scrum: Teams (2010)
  - Naughty Dog Still Falling Just Short of Simultaneous Development (2021)
  - FromSoftware made Elden Ring and Armored Core 6 with 300 developers (2023)
  - RE:2023 RE ENGINE Philosophy (2023)
  - Embark Studios Söderlund — Quarter of AAA Budget (2026)
- 생성:
  - sources/capcom-ir2021-dev-strategy.md
  - sources/risks-multi-game-development.md
  - sources/agile-scrum-teams.md
  - sources/naughty-dog-multi-project.md
  - sources/fromsoftware-300-devs.md
  - sources/re2023-re-engine-philosophy.md
  - sources/embark-soderlund-quarter-budget.md
  - entities/capcom.md
  - entities/fromsoftware.md
  - entities/naughty-dog.md
  - concepts/multi-project-development.md (신규)
  - concepts/proprietary-engine-strategy.md (신규)
- 업데이트:
  - entities/embark-studios.md (인원·판매 수치·효율화 철학 추가)
  - index.md
- 모순:
  - 독자 엔진 전략: 캡콤(독자 엔진 강점) vs 샌드폴(서드파티 무수정 강점) — 스튜디오 규모에 따른 합리적 분기로 해소, proprietary-engine-strategy.md에 병기

## [2026-04-13] ingest | GDC26 강연 — 아크 레이더스 리셋 성공 신화
- Source: raw/articles/gdc26-arc-raiders-reset.md
- 생성:
  - sources/gdc26-arc-raiders-reset.md
  - entities/embark-studios.md
  - entities/arc-raiders.md
  - concepts/data-driven-development.md (신규: 3일 버스트·바구니 시스템·UXR 활용)
- 업데이트:
  - concepts/small-team-development.md (강제된 집중 — 팀 리셋 추가)
  - concepts/playtesting.md (엠바크 UXR 기반 테스트 추가)
  - concepts/vision-statement.md (기둥 기반 의도 소통 — 엠바크 방식 추가)
  - index.md
- 모순: 없음

## [2026-04-13] 비교 페이지 생성
- 생성:
  - comparisons/iteration-cycles.md (반복 개발 주기 비교)
  - comparisons/small-studio-goty.md (소규모 스튜디오 대작 전략 비교)
  - comparisons/player-feedback.md (플레이어 피드백 수집 전략 비교)
- 발견된 모순 기록:
  - player-feedback.md: 라리안 얼리액세스 vs 민트로켓 "완성도 먼저" — 표면 충돌, 공통 교훈으로 해소

## [2026-04-13] ingest | GDC·컨퍼런스 강연 4건 (서커펀치, 민트로켓, SGC)
- Source: raw/articles/ (4개 파일)
  - GDC26 고스트 오브 요테이 — 덜어냄의 미학
  - GDC26 관객들이 찾는 게임에는 '반짝임'이 있다
  - CGDC 황재호 대표 — 생존을 위한 8계명
  - SGC 실전 사례로 배우는 스팀에서 살아남기
- 생성:
  - sources/gdc26-ghost-of-yotei.md
  - sources/gdc26-spark.md
  - sources/cgdc-dave-the-diver.md
  - sources/sgc-steam-survival.md
  - entities/sucker-punch-productions.md
  - entities/ghost-of-yotei.md
  - entities/mint-rocket.md
  - entities/dave-the-diver.md
  - concepts/vision-statement.md
  - concepts/playtesting.md
  - concepts/steam-marketing.md
- 업데이트:
  - concepts/rapid-prototyping.md (서커펀치 방식 추가)
  - concepts/small-team-development.md (잘라내기 문화 추가, 서커펀치 연결)
  - index.md
- 모순: 없음

## [2026-04-13] ingest | GDC 강연 및 개발 사례 4건
- Source: raw/articles/ (4개 파일)
  - GDC25 아스트로봇의 성공, 마법은 없었다
  - GDC24 발더스 게이트3, 시작부터 출시까지
  - GDC26 33원정대, 단 4명뿐이던 프로그래머의 역할
  - Clair Obscur: Expedition 33 개발 과정 (언리얼 공식 인터뷰)
- 생성:
  - sources/gdc25-astrobot.md
  - sources/gdc24-baldurs-gate-3.md
  - sources/gdc26-expedition33-programmers.md
  - sources/expedition33-ue5-interview.md
  - entities/team-asobi.md
  - entities/larian-studios.md
  - entities/sandfall-interactive.md
  - entities/astro-bot.md
  - entities/baldurs-gate-3.md
  - entities/clair-obscur-expedition-33.md
  - concepts/rapid-prototyping.md
  - concepts/small-team-development.md
  - concepts/designer-empowerment.md
  - concepts/early-access-strategy.md
  - index.md (초기화)
  - overview.md (초기화)
- 업데이트: 없음 (최초 ingest)
- 모순: 없음 (최초 ingest)

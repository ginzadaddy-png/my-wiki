---
title: "활동 로그"
---

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
- 중복 파일 확인 (ingested 처리 없음): 2026-04-14T181252+0900-The Risks of Multi Game Dev
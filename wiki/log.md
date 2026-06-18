---
title: "활동 로그"
---

## [2026-06-16] ingest | Gemini Deep Research 2건 — 사운드 디자인 + 세키로 전투 효과음
- 트리거: 사용자가 Gemini Enterprise Deep Research를 직접 실행해 공유링크 2건 전달(사운드 b722d20eeed3 / 세키로 c963d0d4f312). 브라우저(Claude in Chrome get_page_text)로 본문 추출 → 검증 후 "전체로" ingest 지시
- Source: raw/articles/2026-06-16-gemini-deepresearch-sound-design.md · raw/articles/2026-06-16-gemini-deepresearch-sekiro-combat-sound.md (둘 다 1차 출처 인용 포함 2차 합성물)
- **세키로 보고서 = 2차 시도(검증판)**. 1차 시도(무출처)의 의심 항목이 거의 판정됨: Ogawa Sound 'KATANA'/'MOTION SFX' 실사용 *확인*(공식 포스트), 작곡 크레딧 *확인*(키타무라 리드 + 아사쿠라 8트랙, vgmdb), CEDEC 2020 *정정 확인*(세키로=우수상/FF7R=최우수상), 공중부양 폴리 *1차 미확인*(David Dumais 재현 가이드 유래)
- 생성 source 5: gdc16-overwatch-play-by-sound · project-triton-acoustics · gdc23-tunic-audio · ogawa-katana-sekiro · sword-sfx-satisfaction-2020 (모두 confidence medium, 1차 미직접확인 출처주의 명시)
- 생성 concept 1: gameplay-feedback-audio (두 보고서 수렴 — 소리를 1차 전투 입력 채널로. 오버워치 Greatest Threat·세키로 체간 청각피드백)
- 생성 comparison 1: sekiro-vs-melee-combat-audio (세키로·엘든링·고스트 오브 쓰시마·MGR·인왕 — "효과음 품질"이 아닌 "사운드에 부여한 역할"이 갈림길)
- 심화: sound-design(적응형 음악 수직/수평·미들웨어 Wwise/FMOD·공간 Triton·절차적 VocAlien·다이내믹 믹싱/무음·접근성·합류시점) · sekiro 엔티티(전투 효과음 섹션 + sources/related)
- 양방향 link: sekiro↔gameplay-feedback-audio·sekiro-vs-melee-combat-audio·신규 source 2 / sound-design↔gameplay-feedback-audio·신규 source 3
- 갱신: sources/all(→124, linter가 텐센트행 포함 정합)·concepts/all(→58, ai-asset-pipeline 외부추가 포함)·comparisons/all(→17)·index(소스124·개념58·비교17·pill 2)·about(INGEST 68→71[ai-asset+사운드+세키로]·소스124·개념58·비교17·총286→295·마지막갱신 2026-06-16·다이어그램)·overview(핵심 테마 2)
- 참고: 작업 중 다른 기기/세션에서 ai-asset-pipeline(텐센트 Light AI) ingest가 동시 반영됨 — 카운트 재측정으로 정합
- 모순 없음. push 안 함 — 사용자 검토 후 직접

## [2026-06-17] report | AI 에셋 파이프라인 분석 보고서 발행 + 구 슬라이드 폐기 + 위키 정정
- 트리거: 사용자가 ⓐ위키 부정확 기술 정정 ⓑLight AI·Embark 파이프라인 이미지 추가 ⓒ구 슬라이드/wrapper 폐기 후 보고서를 presentations에 발행 지시
- 위키 정정: sources/gdc2026-embark-character-pipeline "Arc Raiders(2024)" → (2025-10-30 출시) · concepts/ai-asset-pipeline "자동화는 배경까지만" 혼용 → "생성형 AI 생성(배경 한계) vs 절차적 파이프라인 자동화(캐릭터 도달)" 구분으로 정정. (Origins node·kit-bash는 강연 1차 확인되어 정확 → 유지)
- 이미지: Light AI 발표 화면(Chinaz/AIbase) + Embark 두 강연 썸네일(Freedom Through Structure UFeC·Asset Processor HZd4) 실제 URL 검증 후 보고서 삽입
- 발행: 보고서를 presentations/ai-asset-pipeline-2026-report.html로 배치, wrapper ai-asset-pipeline-2026.md를 보고서용으로 재작성(iframe), presentations/all 카탈로그·index pill 갱신
- 폐기: 구 슬라이드 ai-asset-pipeline-2026-deck.html (사용자 확인 후 삭제)
- 모순 없음. push 안 함 — 사용자가 별도 스레드에서 진행


- 트리거: 사용자가 ai-asset-pipeline 검증 종합을 HTML 슬라이드로 요청(상세 12~16장 + 직접 그린 다이어그램)
- 생성: presentations/ai-asset-pipeline-2026-deck.html (15장, Pretendard 전용, 인라인 SVG 다이어그램 6종 — 단점생성 비교·세 계층·USD 타임라인·히어로 천장·Houdini 백본·METR/GDC 차트) + wrapper presentations/ai-asset-pipeline-2026.md
- 명명: 슬러그 ai-asset-pipeline-2026 (concept ai-asset-pipeline와 basename 충돌 회피), 슬라이드 -deck.html 접미사
- 이미지: 외부 사진 미사용(저작권), SVG/CSS 직접 작도로 대체
- 갱신: presentations/all(행 추가)·index(프레젠테이션 2→3·pill 추가)
- 검수: JetBrains Mono 미사용 확인, mount 무결성 확인
- 모순 없음. push 안 함 — 사용자 검토 후 직접 (슬라이드 .html은 quartz Assets emitter가 처리, deploy.yml copy step 기존 메커니즘)

## [2026-06-17] ingest | AI 에셋 파이프라인 기술 지형 — Gemini Deep Research 1차 검증 후 ingest
- 트리거: 사용자가 ai-asset-pipeline 주제로 Gemini Deep Research 실행 → 공유링크(gemini.google.com/share/248fc43e1e6f) 결과를 Claude in Chrome get_page_text로 확보. 2차 합성물이라 "검증(a) 먼저 → 통과분만 ingest" 방식 합의
- 검증: 핵심 주장을 3개 병렬 서브에이전트로 1차 출처 팩트체크. 결과 — 기술·모델 주장은 의외로 대부분 CONFIRMED(arXiv·AOUSD·SideFX·METR·GDC 공식), 허구는 사례 귀속에 집중
- 생성: sources/ai-asset-pipeline-tech-landscape-2026.md (검증 통과분 + § 검증 메모에 허구·오류 분리 기록, confidence high)
- 심화: concepts/ai-asset-pipeline.md — "2026 기술 지형(표준층 성숙/생성층 천장/조직층 저항)" 섹션 추가. sources에 신규 검증 종합 + related에 unreal-engine-5 추가. updated 2026-06-17
- 정정 기록(딥리서치 환각): ⓐ엔티티 혼동 — HunyuanWorld(HY-World)는 Tencent Hunyuan 팀, Light AI(Lightspeed)와 별개 → tencent-light-ai 소스에 구분 노트 추가 ⓑEmbark "95% 공유" 수치·Ubisoft 'Flow'·EA Frostbite USD 로드맵·NetEase+Eidos GDC2022 = 허구/오류로 인용 제외 ⓒLIVRPS→LIVERPS, APEX=All-Purpose EXecution, QuadGPT tDPO=Truncated DPO 등 약어 정정
- 갱신: sources/all(124→125, 행 추가)·index(소스125·Last updated 2026-06-17)
- 모순 없음. push 안 함 — 사용자 검토 후 직접

## [2026-06-16] ingest | 텐센트 광자 Light AI — AI 게임 에셋 산업화 파이프라인 (GameLook)
- 트리거: 사용자가 GameLook 기사 URL(gamelook.com.cn/2026/06/595139) 직접 전달 → ingest 지시. WebFetch 본문 미반환(JS 렌더링)으로 Claude in Chrome get_page_text로 본문 추출
- Source: http://www.gamelook.com.cn/2026/06/595139/ (2026-06-10, 텐센트 광자 LAP 강연 실록, 薛小黎·凡开俊). 벤더 자기 발표 + 강연 실록이라 confidence medium
- 생성: sources/tencent-light-ai-pipeline-2026.md · concepts/ai-asset-pipeline.md
- 양방향 link: ai-asset-pipeline ↔ ai-gamedev(related)·art-pipeline-design(related)
- 갱신: index(소스118→119·개념56→57·개발방법론 pill 추가)·concepts/all(ai-asset-pipeline 행)·sources/all(123→124, 행 추가)
- 참고: index 소스 카운트(119)와 sources/all 실제 파일수(124)·표 행수(115) 간 기존 drift 존재 — 이번 ingest 범위 밖, LINT 시 재정합 권고
- 모순 없음. push 안 함 — 사용자 검토 후 직접

## [2026-06-16] ingest | Gemini Deep Research 로그라이크 — PCG·난이도사다리·의도적 불균형 심화
- 트리거: 브라우저 자동화(Claude in Chrome)로 Gemini Enterprise Deep Research 실행 → 로그라이크 보고서 공유링크(gemini.google.com/share/3b0ba2d01796) 확인 후 사용자가 ⓐ본문 심화 + ⓑ비교 페이지 신설 + ⓒ우선순위1 출처 2건 ingest 범위 지시
- Source: raw/articles/2026-06-16-gemini-deepresearch-roguelike.md (Gemini Deep Research 산출물, 8개 주제 + 표 A/B 포함. 2차 합성물이라 1차 GDC Vault 재검증 권장)
- 생성: sources/gdc22-returnal-procedural-world.md · sources/gdc19-slay-the-spire-metrics.md (둘 다 confidence medium, 1차 미검증 출처주의 블록 명시) · comparisons/pcg-pure-vs-hybrid.md
- 심화: concepts/roguelike.md — "절차적 생성: 완전무작위 vs 하이브리드"(Spelunky 해결경로·Dead Cells Concept Graph+spawn budget·Hades 수공예 큐레이션·Returnal AAA 자유형) + "난이도 사다리와 의도적 불균형"(StS Ascension A1/10/15/20·Hades 형벌규약 *공식 Heat40·보상32 vs 커뮤니티 역산 64 구분*·Corruption 무한엔진 희소화·메트릭 밸런싱) 섹션 추가. sources+related 갱신
- 양방향 link: roguelike ↔ pcg-pure-vs-hybrid·신규 source 2건
- 갱신: sources/all(116→118)·comparisons/all(15→16)·index(소스118·비교16·비교 pill)·about(INGEST 67→68·소스118·비교16·총283→286·다이어그램)
- 보류: 한국·아시아 인디(Skul 등)는 보고서 자체가 confidence Low-Medium·GDC급 피어리뷰 부재로 ingest 후순위 보류 권고 → 이번 반영 제외
- 모순 없음. push 안 함 — 사용자 검토 후 직접

## [2026-06-16] weekly-lint 후속 — roguelike·sound-design 두 concept 페이지 신규 (위키 내부 재구성)
- 트리거: 2026-06-16 예약 lint 보고 후 사용자가 추천 조사주제 중 로그라이크·사운드 디자인 2건 선택, *"위키 내부 재구성"* 방식 지시 (외부 web search 없이 기존 페이지 재구성 — 이 세션엔 WebSearch 미제공)
- **concepts/roguelike.md 신규**: 절차적 생성·런 기반·퍼머데스·빌드 시너지·메타 진행성 정의. 로그라이크 vs 로그라이트 구분, 하데스 내러티브 결합 모델, 발라트로 "한 판 더" 루프. Carless taxonomy 근거 Action Roguelike 104개($1M+, 70+ since 2020) healthy 분포 = 인디 진입 친화. [[soulslike]]와 대비 프레임. sources: kasavin-hades-ea·gdc25-balatro-marketing·carless-genres-ruled-steam-2025-06
- **concepts/sound-design.md 신규**: 세 접근(시스템 기반 사운드 / 음악 우선 역설계 / 시네마틱 오디오). 젤다 TotK 거리감쇠 물리화·리버브 자동계산·방향성, Hi-Fi RUSH 비트 우선 역설계, 인소믹·TLOU 다운스트림 배포. sources: gdc24-zelda-tears-of-kingdom·gdc2024-hifi-rush-backwards
- 정정: 데이브 더 다이버는 혼합장르(다이빙+경영)라 roguelike 앵커에서 제외 — 발라트로·하데스만 사용
- 양방향 wikilink: balatro(본문+related)·soulslike(related)·hifi-rush(본문+related)·emergent-systems-design(관계 bullet+related)에 신규 페이지 link
- 갱신: concepts/all.md(2행·updated)·index.md(개념 54→56·게임디자인 pill 2개·Last updated)·overview.md(핵심 테마 2개)·about.md(개념 54→56·총 281→283·다이어그램 54→56)
- 모순 없음. push 안 함 — 사용자 검토 후 직접

## [2026-06-08] QUERY 후속 — platform-fees 비교 페이지에 플랫폼 약관 분석 섹션 추가
- 트리거: 웹샵/D2C가 Steam·콘솔에서도 가능한지 질문 → 플랫폼 약관 1차 확인 후 비교 페이지 보강 요청
- comparisons/platform-fees-vs-direct-sales.md 두 섹션 신규:
  - **플랫폼 약관상 적용 가능성**: Steam SSA(§1 Valve 판매자·§2 E·F 키 외부판매 허용)·PSN 약관(§14.2.1 모든 인게임 구매 SIE 거래·§14.10.2 외부 가상아이템 취득 금지)·Xbox Gaming Web Purchase Service(MS 1st-party 웹 D2C) — 1차 출처 URL 3건 인라인
  - **콘솔 크로스플랫폼 커머스**: Sony 파트너 정책의 *패리티 의무*·*도매가 상한*(~30% 마진 유지)만 방향성 기록. **0.85 레비뉴셰어 룰·산식·임계값·예시 수치 등 비공개 수치는 의도적으로 제외**. 근거 PDF(SIE Cross-platform Policy, confidential)는 ingest하지 않음 — 비공개 정책임을 ⚠️ 블록에 명시
- 신규 페이지·카운트 변동 없음 (기존 비교 페이지 본문 보강만)

## [2026-06-08] weekly-lint 후속 — Xsolla 웹샵/D2C ingest + parent-company wikilink retrofit + 수수료 비교
- 트리거: 2026-06-08 예약 lint 보고 후 사용자가 Xsolla ingest + Steam 입문 보강 + 조사주제 3건(결제·웹샵 / parent wikilink / 수수료 비교 페이지) 진행 지시
- **Xsolla ingest** (raw 큐 1건): `raw/articles/2026-06-01...엑솔라(Xsolla)의 웹샵 생태계`
  - 생성: sources/xsolla-webshop-ecosystem.md · concepts/webshop-direct-monetization.md · entities/xsolla.md
  - 핵심: D2C·웹샵 패러다임 전환(30% 회피→필수 비즈니스), 하이브리드(스토어=발견/웹샵=락인), 운영 3단계(발견-전환-확장), 라이브옵스 캔버스 노코드·인스턴트 웹샵·PWA, merchant of record + 130개국 APM, 조이시티 5개월 ~400% 사례
  - confidence medium — 결제 솔루션사 자사 행사 리뷰, 수치는 자체/익명 데이터 (출처 주의 블록 명시). Xsolla는 결제 인프라사라 graph relations 어휘 미적용
- **Steam 마케팅 입문 보강** (중복 clipping — 신규 source 페이지 없이 기존 entity 보강): entities/valve.md 기본정보에 2025 규모 수치 추가 (MAU ~1.4억 +11%, CCU 4,200만+ 2020 대비 2배, PC·콘솔 매출 +13%·다운로드 +6%). 출처 AB180 'Game UA 2026'(2026-06)
- **조사주제 — 퍼블리셔 딜·플랫폼 수수료 비교**: comparisons/platform-fees-vs-direct-sales.md 신규 (Steam·모바일 30% vs D2C 웹샵 채널 분담, publisher-deal-structures·valve·xsolla 연계)
- **조사주제 — parent-company wikilink retrofit** (lint 고립 보강): 산하 스튜디오 9개 본문에 모회사 프로즈 wikilink 추가 → SIE(team-asobi·sony-santa-monica·naughty-dog·sucker-punch·insomniac)·microsoft(bethesda·obsidian·tango)·krafton(tango)·take-two(rockstar) + elden-ring에 [[bandai-namco]] 퍼블리셔 링크. 모회사 entity 프로즈 inbound 0→1+ 해소. 플랫폼 entity(ps5 등)는 graph 전용 노드로 의도적 유지
- 갱신: index.md(소스 116·개념 54·비교 15·pill 2)·sources/all·concepts/all·comparisons/all·entities/all·overview.md(미디어·플랫폼 3개·신규 테마)·about.md(통계·lint 날짜)
- 모순: 없음 (Xsolla는 신규 영역, 기존 위키와 충돌 없음)

## [2026-06-01] chatbot Phase 4 후속 + Phase 5 — platform 노드·갱신 자동화·Quartz 링크
- **platform 노드 (M5 완전 해결)**: 게임 26개에 platform 관계 + platform entity 6개(ps5·ps4·pc·xbox-series·xbox-one·nintendo-switch) 신규
  - 위키 본문 platform 명시가 7개뿐이라 공인 출시 플랫폼으로 보강(사용자 승인). graph platform 엣지 88개
  - M5 "Sony 퍼블리싱 PS5 독점작" 정밀 해결: astro-bot·ghost-of-yotei·marvel-spiderman-2 (platform==[ps5])
  - entities/all.md 게임 플랫폼 섹션 추가
- **갱신 자동화**: update_and_deploy.py (build_index → push_space 한 방). 이번 재배포로 실전 검증
- **UX**: 콜드스타트 안내 메시지(첫 질문 모델 로딩 1~2분), 인용 wikilink 완전성 프롬프트 보강
- **Phase 5 (Quartz 링크)**: quartz repo WikiNav.tsx에 "💬 위키에 질문하기" 외부 링크 추가(사이드바 최상단). HF Space로 새 탭. 로컬 빌드 검증 후 quartz v4 push (별도 사이클)
- 생성: chatbot/{apply_platforms.py·update_and_deploy.py} + platform entity 6 + quartz WikiNav 수정
- **로드맵 Phase 1~5 전부 완료.** 챗봇 배포·운영 + 위키 연결 완성

## [2026-06-01] chatbot Phase 4 (진행) — 배포 준비 + 30개 평가셋 채점(환각 0)
- 트리거: 로드맵 v2 Phase 4 (hybrid 라우팅 + 클라우드 배포 + 30개 평가셋 사람 채점)
- **호스팅 결정**: 로컬 BGE-M3(2.3GB)는 Streamlit Cloud 무료(RAM 1GB)에 못 올림 → **Hugging Face Spaces**(16GB RAM 무료) 선택. 검색 품질·한국어·데이터 보존 유지
- **배포 준비**: DEPLOY.md(HF Spaces 가이드: chroma_db+wiki 번들·secret·private 인증), app.py VAULT_PATH fallback(로컬·Space 양립). 실제 push는 사용자 HF 계정+토큰 필요
- **하이브리드 라우팅**: Phase 3에서 이미 완성(RAG+graph tool-use 자동 라우팅)
- **30개 평가셋 채점**(run_eval30.py): 답 있음 20 + 답 없음 10
  - 답 있음 **20/20 정확** (graph 도구 4개 포함)
  - 답 없음: 8개 정확 거절 + 2개(U02 GTA6 출시일·U05 사이버펑크 판매량) *위키에 실제 데이터 존재*해 정답 (평가 설계 오류 — 봇 retrieval이 사람보다 위키를 더 잘 앎)
  - **환각 0건** — 30개 전부 위키 근거. 로드맵 목표(70%) 압도
- **HF Spaces 배포 완료**: ginzadaddy/ginza-wiki-chat (private, Docker SDK). secret ANTHROPIC_API_KEY 등록, 번들(app+core+chroma_db+wiki) 업로드, HTTP 200 서빙 확인
  - HF create_repo가 streamlit SDK 직접 생성 차단 → Docker SDK + streamlit 실행 Dockerfile로 우회 (torch/BGE-M3 무거운 의존성에 오히려 적합)
  - 첫 콜드 스타트 시 BGE-M3 모델(~2.3GB) 다운로드로 1~2분
- 생성: chatbot/{DEPLOY.md·run_eval30.py·eval-30-results.md·deploy/{Dockerfile·README.md·push_space.py}}. 수정: app.py
- **Phase 4 완료** → 남은 건 Phase 5(Quartz 위키에 챗봇 헤더 링크 추가)뿐

## [2026-06-01] chatbot Phase 3 — Graph(relations retrofit + NetworkX + tool-use), 다중 hop 5/5 해결
- 트리거: Phase 2 끝 측정에서 RAG가 다중 hop 5/5 실패 → 로드맵 v2 조건 충족, Phase 3 진입
- **mass-retrofit** (사용자 spot check 거침): 게임 entity 26개에 relations(developedBy·publishedBy·genre) 삽입
  - frontmatter 외과적 삽입(최소 diff), 본문 근거로만 추출, 환각 금지. ⚠️추론 항목(first-party→SIE 등)은 사용자 검수 후 적용
  - 사용자 정정 반영: tango→크래프톤 인수(MS 아님), SIE 약어, sekiro genre soulslike, dark-souls·elden-ring 퍼블=반다이남코
- **모회사 entity 5개 신규**: sony-interactive-entertainment(자회사 5)·microsoft(2)·krafton(tango)·take-two-interactive(rockstar)·bandai-namco(퍼블리셔, parentOf 비움)
- **graph**: core/graph.py NetworkX MultiDiGraph (266 노드·73 엣지). 쿼리 함수(parent_of·children_of·siblings·find_by_relation·path_between·neighbors)
- **agent 통합**: core/graph_tools.py — Claude tool-use 6개 도구. 관계 질문 시 agent가 자동 호출. 시스템 프롬프트에 라우팅 지침
- **M1~M5 재실행**: RAG 0/5 → RAG+graph **5/5 해결**
  - 형제 스튜디오 열거·공통 모회사 join·장르 게임·퍼블리싱 게임 전부 정확. arrowhead는 퍼블리싱이지 자회사 아님 구별 유지
  - M5 platform 데이터 부재 시 agent가 "graph에 platform 부족" 정직 고지 (환각 0)
- 생성: chatbot/core/{graph,graph_tools}.py·apply_relations.py + entity 5개. 수정: agent.py(tool-use 루프)·entity 26개 relations
- 알려진 갭: platform·genre 희소(platform 노드 미도입). 일부 퍼블리셔 entity 미생성
- **Phase 3 완료** → 다음: Phase 4(hybrid 라우팅 정리 + Streamlit Cloud 배포 + 30개 평가셋 사람 채점)

## [2026-06-01] chatbot Phase 2 — RAG(BGE-M3 + Chroma) 구축, 키워드 실패 3개 전부 해결
- 트리거: 로드맵 v2 Phase 2. Phase 1이 드러낸 교차언어·길이편향·관계추론 한계를 의미검색으로 해결
- **임베딩 결정**: 로컬 BGE-M3 (한국어·교차언어 강함, API 비용 0, 데이터 외부 전송 없음). torch+sentence-transformers+chromadb 설치
- **구축**: core/{chunker,embedder,vectorstore,rag_search}.py + build_index.py. agent.py에 use_rag 플래그(RAG 기본 + 키워드 fallback)
  - 청크화: heading 단위 + 800자 분할, 한글 제목 프리픽스(교차언어 핵심) → 1409 청크
  - 색인: BGE-M3 dim=1024, CPU 임베딩 ~349s, Chroma persistent(cosine)
- **eval 8개 RAG 재실행 — 키워드 대비 극적 개선**:
  - 품질 5점 4→6개, 1·2점 전멸 (전 항목 4점 이상)
  - Q1 교차언어 해결(1→5): 한글 제목 프리픽스가 영문 쿼리 의미 매칭
  - Q3 길이편향 해결(2→5): sekiro 1위 직격, 의미 유사도가 raw 빈도 압도
  - Q5 관계추론 개선(1→4): Sony 스튜디오 정확 retrieval + Arrowhead=퍼블리셔(모회사 아님) 구별
  - Q6: 키워드가 놓친 "Switch 2 (2025-06)" catalog 페이지서 발굴 (grounding 정확)
- 생성: chatbot/core/{chunker,embedder,vectorstore,rag_search}.py·build_index.py. chroma_db/는 gitignore(Phase 4 배포 시 commit 전략 재결정)
- **Phase 2 완료** → 다음: Phase 3(graph) 진입 여부를 다중 hop 쿼리 추가 측정 후 결정. RAG가 단순 관계는 풀지만 진짜 multi-hop은 graph가 더 정밀할 가능성

## [2026-06-01] chatbot Phase 1 — 로컬 MVP 검증 완료 + 키워드 한계 실측
- 트리거: 로드맵 v2 Phase 1 (로컬 Streamlit + 키워드 검색 + Claude API). Anthropic API 키 발급·크레딧 충전 후 end-to-end 검증
- **셋업**: `chatbot/` (core/ 백엔드 + app.py UI 분리). venv + streamlit·anthropic·python-frontmatter·python-dotenv. 위키 236개 .md 인식
- **검증**: eval 쿼리 8개 배치 실행 (`chatbot/run_eval.py`, 결과 `eval-results.json`·`eval-queries.md` 표)
  - 품질 5점 4개(Q2 MDA·Q4 retention·Q6 Switch2거절·Q8 AAA스케일링)·4점 1개(Q7)·2점 1개(Q3)·1점 2개(Q1·Q5)
- **키워드 검색 한계 3가지 실측** (Phase 2·3 동기 데이터):
  1. 교차언어 매칭 불가 (Q1) — 영문 쿼리"Astro Bot" ↔ 한글 제목"아스트로봇" 안 맞음 → multilingual 임베딩 동기
  2. 길이 편향 (Q3) — 긴 concept 페이지가 raw 빈도로 짧은 entity 압도 → 의미 검색 동기
  3. 관계 추론 불가 (Q5) — "Sony 자회사 중 X" 다중 hop → Phase 3 graph 동기
- **긍정 신호**: hallucination 회피 작동(Q6 정직 거절), 영어 키워드 본문 적중 시 우수(Q4)
- 버그 수정 2건:
  - **BOM 버그**: 위키 .md 20개가 UTF-8 BOM으로 시작 → frontmatter 파싱 실패(type=unknown). `wiki_loader`를 `utf-8-sig`로 읽도록 수정
  - **.env override**: 셸 환경 빈 ANTHROPIC_API_KEY가 .env 가림 → `load_dotenv(override=True)`
- 생성: chatbot/core/{wiki_loader,search,agent}.py·app.py·run_eval.py·eval-queries.md·eval-results.json·README.md·.env.example
- **Phase 1 완료** → Phase 2(RAG) 진입 동기가 실측으로 뒷받침됨. 다음: 청크화 + Chroma + BGE-M3/Voyage 임베딩

## [2026-06-01] weekly-lint 후속 — Zelda 크로스체크 ingest + BioWare/Obsidian 내러티브 통합 + EA entity
- 트리거: 2026-06-01 예약 lint 보고 후 사용자가 "조사주제 1·3 진행 + Zelda raw 큐 크로스체크 후 ingest" 지시
- **lint 정정**: 직전 보고의 *bioware·obsidian-entertainment 신규 고립 2건은 false-positive*. 두 entity는 comparisons/companion-philosophy.md에서 escaped-pipe 테이블 셀(`[[bioware\|BioWare]]`)로 이미 link됨 — 고립 탐지 regex가 `\|`를 미처리한 버그. 실제 콘텐츠 고립은 by-design 7건(5 comparison + 2 wrapper)으로 직전 lint와 동일
- **Zelda ingest (raw 큐 1건 처리)** — `2026-04-15T121314...Tunes of the Kingdom...md` (+ T122718 중복본):
  - 크로스체크 결과: 강연 정식 제목은 *"Tunes of the Kingdom"* (Tears 오타 아님 — 물리+사운드 두 분야 말장난, 발표자 0:23 직접 언급). 영상은 자동 캡션이라 고유명사 다수 깨짐("Breath"→"Breast" 등). 핵심 내용이 기존 sources/gdc24-zelda-tears-of-kingdom.md(inven 보도)와 line-by-line 일치 → 상호 검증 완료
  - 처리: 별도 신규 페이지 생성 대신 *기존 페이지 보강* (DRY). sources 배열에 YouTube 트랜스크립트 raw 추가, "보강 원전(영상)" + "제목 주의" 블록 삽입, **사운드 엔지니어링 상세 섹션 신설**(거리 감쇠 물리화·리버브 파라미터 자동 계산·방향성·인터랙티브 음악 툴 — inven 보도가 한 줄 요약한 "사운드용 물리 엔진"의 실제 구현). updated 2026-05-15→2026-06-01
- **조사주제 1 — BioWare/Obsidian RPG 내러티브 통합** (고립 보강 아닌 커버리지 확장):
  - concepts/companion-design.md: 본문에 [[bioware]]·[[obsidian-entertainment]] wikilink + related 배열에 두 entity·companion-philosophy 추가
  - concepts/quest-narrative-design.md: "RPG 반응형 퀘스트 — BioWare·Obsidian 계보" 섹션 신설(characters not causes·다중 해법·진영 결말), related 배열에 두 entity 추가
  - 결과: bioware 콘텐츠 inbound 1→4(companion-philosophy·companion-design·quest-narrative-design·electronic-arts), obsidian 1→3. 기존 fragile 테이블 셀 단독 의존 해소
- **조사주제 3 — EA 퍼블리셔 entity 신규 (1 페이지)**:
  - entities/electronic-arts.md (1982 레드우드시티, NASDAQ EA, CEO Andrew Wilson, 스포츠 연간 카탈로그+FUT·라이브 서비스·AAA 싱글 3축, 산하 DICE·Respawn·BioWare·Maxis·Codemasters, FIFA→EA Sports FC 전환, 2024 정리해고). relations: parentOf [respawn-entertainment, bioware]
  - relations 연결: apex-legends.md에 publishedBy [electronic-arts] 추가 + 본문 "EA 퍼블리싱"→wikilink. respawn-entertainment.md·bioware.md 본문 "EA 인수/산하"→[[electronic-arts]] wikilink + related 배열 추가
  - confidence: medium — 외부 fetch 제약(web_fetch provenance)으로 사전 학습 지식 종합. 매출·직원수·CEO 현황 IR 재검증 필요(페이지 "추가 조사" 명시)
- 카탈로그·index·overview·about 갱신:
  - entities/all.md: 스튜디오 섹션에 electronic-arts 행 추가(37→38), updated 2026-06-01
  - index.md: Last updated 2026-06-01, stat card 스튜디오 37→38, **개념 52→53 정정**(기존 off-by-one 오류 — 실제 concepts 폴더 53개)
  - overview.md: 현재 커버리지 스튜디오·퍼블리셔 37→38, 목록에 Electronic Arts(EA) 추가
  - about.md: 누적 INGEST 65→66, 엔티티 73→74, 다이어그램 entities 73→74, 인라인 "총 약 265개"→266. (헤더·frontmatter 날짜는 당일 lint 단계에서 이미 2026-06-01)
- 메타: entity 72→73 actual (folder 73→74 inc. all.md), source·concept·comparison 수 동일(Zelda는 기존 페이지 보강이라 source 신규 0)
- push 안 함 — 사용자 검토 후 직접 요청

## [2026-05-29] ingest + 정정 — 펄어비스 블랙스페이스 엔진 (Inven GDC 2025 보도)
- 트리거: 사용자가 "펄어비스 2세대 엔진 이름은 블랙스페이스(Black Space) 엔진, https://www.inven.co.kr/webzine/news/?news=304278&site=angelstone 참고"
- 정정 사유: 직전 entity 작성 시 *Heart Engine (가칭)*으로 표기. 실제는 *블랙스페이스 엔진(Blackspace Engine)*, 2025-03 GDC 2025에서 미디어 최초 공개됨. *가칭이 아닌 공식 명칭*
- 신규 raw:
  - raw/articles/2026-05-29-pearl-abyss-blackspace-engine-gdc2025.md (인벤 이두현 기자, 2025-03-24)
- 신규 source 페이지:
  - wiki/sources/pearl-abyss-blackspace-engine-gdc2025.md (3대 핵심 가치·12개 기술 스택·시연 핵심 장면·UE5 대응 자체 솔루션 정리)
- 정정·보강:
  - entities/pearl-abyss.md: Heart Engine 표기 모두 *블랙스페이스 엔진*으로 교체, "자체 엔진 전략" 섹션 대폭 보강 (3대 핵심 가치 + 12개 기술 스택 표), sources 배열에 신규 source 추가, confidence medium→medium-high, "추가 조사" 항목 갱신 (Heart Engine 가칭 확인 → 모바일 지원·상용 빌드 충실도·DokeV 적용 등 새 추가 조사 항목으로 교체)
  - concepts/proprietary-engine-strategy.md: 펄어비스 섹션 *블랙스페이스 엔진* 정정 + 기술 스택 인용, sources 배열에 신규 source 추가
  - comparisons/proprietary-engine-vs-ue5.md: 자체 엔진 진영 표 펄어비스 행 정정 (Heart Engine → 블랙스페이스 엔진), "예외 변수 4번" Pearl Abyss 본문 정정, 한국 메이저 표 정정, sources 배열에 신규 source 추가
- 카탈로그·index 갱신:
  - sources/all.md: 114→115, 신규 행 추가
  - index.md: stat card 소스 114→115
  - about.md: 통계 표 소스 115→116, 다이어그램 sources 115→116, 인라인 수치 264→265
- 메타: source 114→115 actual (folder 115→116 inc. all.md), entity·concept·comparison 수 동일
- 핵심 신규 정보 (블랙스페이스 엔진):
  - 3대 핵심 가치: 룩앤필(Look & Feel) · 기술에 대한 완전한 통제(Control of Technology) · 멀티플랫폼 지원(Multi-Platform Support)
  - 기술 스택: 거리 기반 렌더링·심리스 로딩·다이내믹 물리·GPU 물리 연산·FFT Ocean Simulation·Shallow Water Simulation·Fluid+Froxel Raymarching·Ray Tracing·Real-time Light Calculation·Unified Atmospheric Scattering with Volumetric Cloud·Shape Variation·임포스터 LOD 전환
  - UE5 Nanite·Lumen·Niagara·World Partition 표준에 *정면 대응하는 자체 솔루션* — 한국 게임사 중 드문 사례
  - 첫 상용 검증 = 붉은사막 (2026-03 예정), 이후 DokeV 등 적용
- 신뢰도: confidence: high (인벤 1차 보도 + Pearl Abyss 관계자 인용 직접 인용)
- push 안 함 — 사용자 검토 후 직접 요청

## [2026-05-29] entity 보강 — 펄어비스 (자체 엔진 한국 케이스)
- 트리거: 사용자가 "자체 엔진 사례에 펄어비스 추가, 관련 md 모두 업데이트" 지시
- 신규 entity (1 페이지):
  - entities/pearl-abyss.md (2010 한국 안양, KOSDAQ 263750, 직원 ~1,500명, 검은사막 PC·모바일·콘솔 cross-platform, Black Desert Engine 1세대·Heart Engine 2세대(가칭) 2026 붉은사막 출시로 실전 검증, CCP Games 2018 $425M 인수)
- 기존 페이지 보강:
  - concepts/proprietary-engine-strategy.md: related에 pearl-abyss 추가, "MMORPG 라이브 서비스 자체 엔진 — 펄어비스 케이스" 섹션 신설 (5번째 ROI 정당화 모델 — *MMORPG cross-platform + MMO 서버 인프라 통합 통제*)
  - comparisons/proprietary-engine-vs-ue5.md: related에 pearl-abyss 추가, 자체 엔진 진영 사례 테이블에 펄어비스 행 추가, "예외 변수" 섹션에 *MMORPG + 서버 인프라* 4번째 항목 신설, 의사결정 흐름도에 MMORPG 분기 추가, "한국 메이저 자체 엔진 vs UE5 분기" 표 신설 (펄어비스·NCSoft·넥슨·Krafton·Shift Up)
- 카탈로그·index 갱신:
  - entities/all.md: 스튜디오 36→37 (펄어비스 추가), updated 2026-05-29
  - index.md: stat card 스튜디오 36→37
  - overview.md: 현재 커버리지 스튜디오·퍼블리셔 36→37
  - about.md: 통계 표 엔티티 72→73, 다이어그램 entities 72→73, 인라인 수치 263→264
- 메타: entity 71→72 actual (folder 72→73 inc. all.md), source 114·concept 53·comparison 14 동일
- relations 적용: pearl-abyss는 *parentOf: []* (CCP Games entity 미존재, 향후 ccp-games entity 추가 시 retrofit 가능)
- 신뢰도: confidence: medium — 사전 학습 지식 + Pearl Abyss IR/언론 종합. *Heart Engine 정확한 이름·기술 스택*, *2026-03 붉은사막 출시 후 실전 검증*, *CCP Games 인수 6년차 ROI* 등 추가 조사 필요 (entity 페이지 "추가 조사" 섹션 명시)
- push 안 함 — 사용자 검토 후 직접 요청

## [2026-05-29] weekly-lint + 신규 조사 4건 (자체엔진-vs-UE5·카탈로그3사·인디퍼블리셔·라이브서비스)
- 트리거: 예약 lint 보고 후 사용자가 "다음 조사 주제 + idea backlog 모두 진행 + 미처리 큐 삭제" 지시
- lint 요약 (실행 결과):
  - 모순 4건 (전부 기존, 해소형 — 신규 0)
  - 완전 고립 0건, 콘텐츠-약한고립 7건 (5 comparison + 2 wrapper, 전부 by-design)
  - 미페이지 빈출 개념 0건 (log.md 내 폐기 deck 잔존만)
  - raw 미처리 후보 1건 (fandomwire 2차 보도) → 삭제
- raw 삭제 (1 file):
  - raw/articles/2026-04-20T143742+0900-Ex-Rockstar Dev (fandomwire) — GTAVIoclock 원전 이미 ingest, 중복 2차 보도
- 신규 comparison (2 페이지):
  - comparisons/proprietary-engine-vs-ue5.md — 자체 엔진 vs UE5 의사결정 매트릭스. 규모·타이틀 다양성·장르 정체성 3축 ROI 분기. CDPR Witcher 4 산업 시그널, Asobo·Remedy 장르 정체성 변수, 캡콤 multi-IP carrier 패턴 정리. 위키 내부 자료 종합 (proprietary-engine-strategy + unreal-engine-5 두 concept 페이지 인용)
  - comparisons/catalog-economics-3-publishers.md — 캡콤·닌텐도·Take-Two 3사 비교. 재발매형·가격유지형·서비스형 3모델 trade-off 표·의사결정 흐름·한국 적용 시사점·시간축 진화 risk. catalog-economics + catalog-economics-cross-company-2026 source 종합
  - inbound 보강: proprietary-engine-strategy·unreal-engine-5·catalog-economics 3 concept 페이지의 related 배열에 신규 comparison 양방향 link
- 신규 entity — 라이브 서비스 스튜디오 (4 페이지):
  - entities/hoyoverse.md (miHoYo 2012 상하이, F2P 가챠 + AAA 비주얼 cross-platform, *원신 쇼크*)
  - entities/epic-games.md (1991 노스캐롤라이나, 텐센트 40%, UE·Fortnite·EGS·UEFN 수직 통합 5 layer)
  - entities/riot-games.md (2006 LA, 텐센트 100%, LoL 15년+ transmedia, Arcane Emmy 9관왕)
  - entities/respawn-entertainment.md (2010 LA, EA 산하, Apex + Star Wars Jedi 라이브+싱글 듀얼)
- 신규 entity — 라이브 서비스 게임 (4 페이지):
  - entities/genshin-impact.md (2020, miHoYo, $6~8B+, 6주 사이클, *원신 쇼크* 표본)
  - entities/fortnite.md (2017, Epic, $20B+, 3단 자기 재정의 BR→콜라보 IP→UEFN)
  - entities/league-of-legends.md (2009, Riot, $10B+, 15년+ MOBA + Arcane transmedia)
  - entities/apex-legends.md (2019, Respawn, 1억+ 유저, Surprise drop 마케팅 표본)
- 신규 entity — 인디 퍼블리셔 (3 페이지):
  - entities/annapurna-interactive.md (2016 LA, 영화사 산하 작가형, Outer Wilds·Stray·Cocoon, 2024-09 대량 사임)
  - entities/devolver-digital.md (1998 텍사스 오스틴, LSE 상장 DEVO, Hotline Miami·Cult of the Lamb, 컬트 마케팅)
  - entities/raw-fury.md (2015 스톡홀름, 비상장 작가형, Sable·Norco, 스웨덴 생태계 퍼블리싱 노드)
- 카탈로그·index 갱신:
  - entities/all.md: 스튜디오 29→36 (7개 추가), 게임 29→33 (4개 추가), updated 2026-05-29
  - comparisons/all.md: 12→14 (proprietary-engine-vs-ue5·catalog-economics-3-publishers), updated 2026-05-29
  - index.md: Last updated 2026-05-29, stat card 스튜디오 29→36·게임 29→33·비교 12→14, 비교 pill-grid에 2개 신규 행 추가
  - overview.md: 현재 커버리지 스튜디오·퍼블리셔 29→36 / 게임 29→33 갱신
  - about.md: 통계 표 엔티티 61→72·비교 13→15, 다이어그램 entities 61→72·comparisons 13→15, "총 약 250개"→"총 약 263개", "현재 통계·규모" 헤더·"마지막 갱신"·frontmatter updated 모두 2026-05-29로 갱신
- 메타: entity 60→71 actual (folder 61→72 inc. all.md), comparison 12→14 actual (folder 13→15 inc. all.md), source 114·concept 53 동일
- relations 적용: 라이브 서비스 게임 4 entity에 developedBy·publishedBy 부착 (genshin-impact: developedBy/publishedBy [hoyoverse], fortnite: [epic-games], league-of-legends: [riot-games], apex-legends: developedBy [respawn-entertainment] / publishedBy plain text "EA" — EA entity 미존재). 인디 퍼블리셔·라이브 서비스 스튜디오는 *publishing* 관계가 5개 어휘로 표현 불가해 relations 빈 배열
- 신뢰도 한계: 라이브 서비스 4사 + 인디 퍼블리셔 3사 + 게임 4개 entity는 confidence: medium — 외부 URL fetch 제약으로 사전 학습 지식 + 공식 IR/언론 종합. 매출 수치·시점 데이터는 1차 자료 재검증 권장 (Sensor Tower·Take-Two/EA/Riot/CDPR IR·Netflix Arcane 발표 등)
- push 안 함 — 사용자 검토 후 직접 요청

## [2026-05-26] weekly-lint + 고립 해소 + 신규 entity·comparison
- 트리거: 예약 작업(weekly-wiki-lint) 결과 보고 후 사용자 "2-2 권장 + 2-4 의 2·3·4 진행" 지시
- lint 요약: 모순 4건(전부 해소형 — 그대로 유지), 콘텐츠-고립 8건(comparison 5건은 catalog 의도 / 실제 보강 대상 3건), 미페이지 빈출 0건
- 고립 해소 (3 페이지, 5 파일 edit):
  - entities/alan-wake-2.md: Remedy plain text → [[remedy-entertainment]] wikilink, frontmatter related + relations(developedBy·platform·genre) 추가
  - concepts/proprietary-engine-strategy.md: related에 remedy-entertainment 추가, 본문 "중간 규모 독자 엔진 — Remedy Northlight" 섹션 신설
  - concepts/dev-org-structure.md: related에 producer-role 추가, "Force Multiplier" 섹션·하시모토 섹션에서 producer-role wikilink 인용
  - concepts/multi-project-development.md: related에 producer-role 추가, "자원 잠식" 본문에서 wikilink 인용
  - concepts/live-service-design.md: related에 mobile-gamedev 추가, 본문 첫줄에서 모바일 분기 안내
- 신규 entity (2 페이지):
  - entities/valve.md (신규) — 미국 워싱턴 벨뷰, Steam 운영자, 30/25/20% 수수료, ML 알고리즘(2024-10~), Steam Next Fest, 4축(플랫폼 알고리즘·Next Fest·매출 1차 source·가격 정책 인프라) 정리
  - entities/nexon.md (신규) — 한국 성남 본사, 도쿄 증시 상장, F2P MMO → 글로벌 프리미엄 PC·콘솔, 4축(이중 트랙 스튜디오 모델·아크 레이더스 프리미엄 전환·자회사 분권·MMO 카탈로그) 정리, relations: parentOf [embark-studios, mint-rocket]
  - inbound 보강: embark-studios·mint-rocket·arc-raiders·steam-next-fest·steam-revenue-forecasting에서 wikilink로 인용
- 신규 comparison (1 페이지):
  - comparisons/forecasting-vs-launch-metrics.md (신규) — Steam 매출 예측 모델 vs 흥행 메트릭의 *시간축 짝* 비교. 한 페이지 비교 표·1차 source 공통점·의사결정 흐름·circular reasoning 함정·사례 적용
  - inbound 보강: steam-revenue-forecasting·launch-metrics related에 양방향 link
- 보류 (raw source 부족):
  - 엔씨소프트 entity: 위키 내 deep dive source 없음 — *추가 조사 주제*에서만 언급되는 수준. raw 보강 후 진행 권장
  - 일본 대형 퍼블리셔(코나미·세가·반다이·스퀘어에닉스) entity: 캡콤 외 위키 정보 부족 — raw 보강 후 진행 권장
- 카탈로그·index 갱신:
  - entities/all.md: 스튜디오 28→29(nexon), 미디어·플랫폼 1→2(valve), updated 2026-05-26
  - comparisons/all.md: 11→12(forecasting-vs-launch-metrics), updated 2026-05-26
  - index.md: Last updated 2026-05-26, stat card 스튜디오 28→29 / 비교 11→12, 비교 pill-grid에 forecasting-vs-launch-metrics 행 추가
  - overview.md: 현재 커버리지 스튜디오·퍼블리셔 29 / 미디어·플랫폼 2 갱신
- 메타: entity 56→58, concept 53 동일, comparison 11→12, source 114 동일
- push 안 함 — 사용자 검토 후 직접 요청

## [2026-05-19] presentation | 스팀 신규 게임 출시의 성공 방정식 (steam-launch-strategy, 35장)
- 트리거: 사용자 — 기존 steam-marketing-strategy deck을 폐기하고 ZR Forecaster·Carless·Zukowski 1차 source 4종 + 가격·딜·회복까지 확장한 종합 전략 deck으로 재구성
- 스타일: frontend-slides skill · Phase 2 거쳐 3 preview (Bold Signal · Paper & Ink · Dark Botanical) 비교 후 **Bold Signal 선택** — 다크 배경 + 오렌지 카드 + Archivo Black 영문 display + Pretendard 한글
- 구조: 0부 서론(4) → 1부 Pre-launch(10) → 2부 Launch(12) → 3부 Post-launch(7) → 4부 적용(2), 35장
- 핵심 정량 포인트: Carless Action 58.37% TAM · winner-take-all vs healthy 분포 (Arena 29 vs Roguelike 104·JRPG 121·Psych Horror 44) · $10 단절선 (0.15× → 0.10×) · ZR 8 driver tornado · Carless 원전 PEAK 266× (ZR 29× 한 자릿수 정정) · Mostly Positive 70% 알고리즘 게이트 · Demo +8% / Next Fest +4% / Year-1 38% 런치월 / 캡콤 9년 곡선 / Zukowski 28/18,239 회복률 0.156%
- 생성:
  - wiki/presentations/steam-launch-strategy-deck.html (35장, 약 107KB, 인라인 편집 기능 포함)
  - wiki/presentations/steam-launch-strategy.md (wrapper)
- 폐기 (3 files):
  - wiki/presentations/steam-marketing-strategy-deck.html (2026-05-15 v2)
  - wiki/presentations/steam-marketing-strategy-deck_bak.html (2026-05-15 v1)
  - wiki/presentations/steam-marketing-strategy.md (wrapper)
- 업데이트:
  - wiki/presentations/all.md: steam-marketing-strategy 행 → steam-launch-strategy 행 교체
  - wiki/index.md: pill-grid 항목 교체 (카운트 2 유지)
- 메타: 프레젠테이션 2 유지 (1폐기 + 1신규)
- 메모리 규칙 신설: feedback_slide_style_phase (frontend-slides Phase 2 절대 스킵 금지) + feedback_slide_personal_info (사용자 개인 정보·소속 언급 금지 + 생성 전 확인 단계) — Phase 2 임의 스킵 실수 + 개인 정보 잔재 가능성에 대응
- 자매 관계: studio-risk-defense (다른 주제·다른 스타일 라인 — Quiet Brief / Notebook Tabs). 두 deck이 서로 다른 axis로 wiki를 재구성

## [2026-05-19] cleanup | sustainable-studio-staffing deck 폐기 (studio-risk-defense와 중복)
- 트리거: 사용자 — 두 deck이 같은 위키 콘텐츠를 다루는 중복. studio-risk-defense 단독 유지로 정리
- 삭제 (3 files):
  - wiki/presentations/sustainable-studio-staffing-deck.html (24장, 보고서 톤)
  - wiki/presentations/sustainable-studio-staffing-mckinsey-deck.html (McKinsey 변형)
  - wiki/presentations/sustainable-studio-staffing.md (wrapper)
- 업데이트:
  - wiki/index.md: 프레젠테이션 카운트 3→2, pill-grid에서 sustainable-studio-staffing 항목 제거, Last updated 2026-05-19
  - wiki/presentations/all.md: 카탈로그 행 제거, updated 2026-05-19
  - wiki/presentations/studio-risk-defense.md: related 배열·관련 위키 페이지·갱신 메모에서 자매 deck 언급 제거, 2026-05-19 갱신 메모 추가
- 메타: 프레젠테이션 3→2
- 영향: dev-talent-pipeline·multi-project-development·innersource·catalog-economics·small-team-development 등 concept 페이지는 sustainable-studio-staffing을 직접 참조하지 않아 추가 갱신 불필요

## [2026-05-18] ingest | GameDiscoverCo Single-tag Taxonomy (Carless 2025-06)
- Source: raw/articles/2026-05-18-carless-genres-ruled-steam-2025-06.md (https://newsletter.gamediscover.co/p/which-genres-have-ruled-steam-a-new)
- 생성:
  - wiki/sources/carless-genres-ruled-steam-2025-06.md
- 업데이트 sources 배열:
  - wiki/concepts/steam-revenue-forecasting.md (Carless taxonomy 1차 source 추가)
  - wiki/concepts/game-market-trends.md (Carless taxonomy + Zukowski 2025 retro 1차 source 추가)
- 메타: wiki/index.md 소스 113→114, sources/all.md 1행 추가
- 핵심 인사이트: Steam Genre TAM 분배는 *Action 58.37% 압도적 우위*. 그 안에서 Arena Shooter·Battle Royale·Hero Shooter는 평균 매출 높지만 진입 어려움(전 역사 29개만 $1M+, 2020 이후 $25M+는 Naraka·Overwatch 2·Marvel Rivals 단 3개). 신규 진입 추천: Action Roguelike (104개)·Psychological Horror (44개)·JRPG (121개) — *healthy 분포*. ZR이 인용한 "104·44·121" 수치 정확 일치 — Carless 원전 source citation 추가 완료.
- 신뢰도: high (GameDiscoverCo 자체 단일-tag 강제 할당 연구)

## [2026-05-18] ingest | 1차 데이터 source 3종 (Carless · Zukowski recovery · Zukowski 2025 retro)
- Source URL:
  - https://newsletter.gamediscover.co/p/the-state-of-steam-wishlist-conversions
  - https://howtomarketagame.com/2026/02/12/only-28-games-recovered-from-a-bad-launch-in-2024-what-do-they-have-in-common/
  - https://howtomarketagame.com/2026/01/27/what-the-hell-happened-in-2025/
- 생성 (3 sources):
  - wiki/sources/carless-wishlist-conversions-2025-10.md (median 0.15× / >$10 0.10× / PEAK 266× 정정·1차 데이터)
  - wiki/sources/zukowski-bad-launch-recovery-2024.md (28/18,239 회복·5가지 메커니즘·Free-to-Keep 비추천)
  - wiki/sources/zukowski-2025-year-review.md (골든 에이지 2.99%·Narrative #1·OWSC 2024 24.5%→2025 20.8% 정정·Farming 20.8%→8.3% 대폭 하락)
- 업데이트:
  - wiki/concepts/steam-revenue-forecasting.md sources에 3개 1차 source 추가 (ZR이 *보조 layer*로, Carless·Zukowski가 *1차*로 위치 재정렬)
- 메타: wiki/index.md 소스 110→113, sources/all.md 3행 추가
- 핵심 정정사항:
  - **PEAK conversion multiplier**: ZR이 29×라 명시했으나 Carless 원전은 *266×* (한 자릿수 차이)
  - **Mage Arena**: ZR 8.7× → Carless 78× / **R.E.P.O.**: ZR 7.5× → Carless 68×
  - **Open World Survival Craft 성공률**: ZR이 인용한 24.5%는 *2024 데이터*. 2025에는 *20.8%로 하락*
  - **Farming Sim**: 2024 20.8% → 2025 *8.3%* (대폭 60% 감소)
  - 위 정정은 [[steam-revenue-forecasting]]의 매트릭스를 *연도 명시 + 1차 source 인용*으로 후속 작업 권장
- 핵심 인사이트: Wishlist conversion 1차 데이터가 ZR이 인용한 수치와 *한 자릿수 차이*로 차이남. 위키 사용 시 *Carless 원전 우선* 인용해야 함. Zukowski 회복 분석은 "런치 첫 달이 결과의 90% 결정" 정량 증거 (회복 0.156%). 2025 골든 에이지 + Narrative 부상 (중국 FMV games 영향) + 장르 메타 4-5년 안정성.
- 신뢰도: high (모두 1차 데이터 또는 1차 분석)

## [2026-05-18] ingest | ZR Consulting Steam Revenue Forecaster (2026)
- Source: raw/articles/2026-05-18-zrconsulting-steam-forecaster.md (https://zrconsulting.de/steam-forecaster/)
- 생성 (2 concepts + 1 source):
  - wiki/sources/zrconsulting-steam-forecaster-2026.md
  - wiki/concepts/steam-revenue-forecasting.md (8 driver sensitivity·sub-genre 매트릭스·time distribution·review/buzz multipliers)
  - wiki/concepts/publisher-deal-structures.md (Self-publish·Rev share·Recoup-first·MG·Marketing fee 5종 stress test)
- 업데이트 (sources·related·ZR 정량 보강):
  - wiki/concepts/launch-metrics.md (ZR Forecaster 정량 모델 섹션 — review tier multiplier·time distribution·8 driver sensitivity·refund 벤치마크)
  - wiki/concepts/game-pricing-strategy.md ($10 threshold conversion 단절선·regional haircut 정량·ARPU 정확 공식)
  - wiki/concepts/marketing-strategy.md (8 driver 마케팅 ROI 우선순위·Demo +8%/Next Fest +4% lift·paid acquisition 함정)
  - wiki/concepts/indie-business-strategy.md (break-even·매출 예측·publisher deal·median vs 평균)
- 메타: wiki/index.md 소스 →110·개념 50→52, sources/all.md 1행 추가 (총 110), concepts/all.md 2행 추가, pill-grid 2개 추가
- 핵심 인사이트: "Steam 위시리스트 conversion 평균 15%"는 일반론. 서브장르마다 conversion 10× 차이 — Open World Survival Craft 24.5% vs Match-3·Visual Novel 한 자릿수. Co-op 바이럴은 PEAK 29×·Mage Arena 8.7× outlier. Review tier multiplier 0.25×~1.4× (한 tier drop = 매출 반토막). Pre-launch buzz multiplier 1.0×~2.5× (Hades·Balatro 수준은 연 1회). Year-1 매출 38%가 런치월 집중. Demo +8% / Next Fest +4% conversion lift. 8 driver tornado sensitivity = 자원 배분 우선순위 도구. Publisher deal stress test로 Recoup-first vs MG 위험 비대칭 명시.
- 신뢰도: medium-high (1차 데이터 GameDiscoverCo·Zukowski·Valve 인용은 high, ZR 자체 calibration은 medium)

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

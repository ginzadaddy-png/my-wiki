---
title: "Game Dev Wiki — 현황 공유"
type: concept
sources: []
related: ["[[index|전체 카탈로그]]", "[[log|활동 로그]]"]
created: 2026-05-27
updated: 2026-06-22
confidence: high
---

## 개요

게임 개발 관련 1차 자료(IR 보고서, GDC 발표, 업계 분석가 글, 트랜스크립트 등)를 읽고 위키 형태로 누적·교차참조하는 개인 지식 베이스입니다. Karpathy식 LLM 활용 위키를 모티브로, *raw 소스를 LLM이 요약·구조화해서 wiki 폴더에 정리*하고 추후 의사결정·발표 자료로 재활용하는 구조입니다. 산출물은 Quartz로 정적 사이트화되어 GitHub Pages로 배포됩니다.

핵심 가치 — 같은 자료를 두 번 읽지 않고, 출처와 인사이트가 항상 wikilink로 연결되어 있어 *"이 주장 어디서 봤더라"* 가 해소됩니다.

## 현재 통계·규모 (2026-06-22 기준)

| 항목 | 수치 |
|---|---|
| 누적 INGEST 건수 | 71건 |
| 소스 요약 (`wiki/sources/`) | 125개 |
| 개념 페이지 (`wiki/concepts/`) | 60개 |
| 엔티티 페이지 (스튜디오·게임·플랫폼, `wiki/entities/`) | 85개 |
| 비교 페이지 (`wiki/comparisons/`) | 17개 |
| 슬라이드 deck (HTML + wrapper) | 3개 ([[presentations/steam-launch-strategy|Steam 출시 전략]] / [[presentations/studio-risk-defense|스튜디오 리스크 방어]] / [[presentations/ai-asset-pipeline-2026-report|AI 에셋 파이프라인 보고서]]) |
| 챗봇 (위키 Q&A 에이전트) | RAG + graph hybrid, HF Spaces 배포 ([아래](#챗봇-위키-qa-에이전트) 참조) |
| 마지막 갱신 | 2026-06-22 |

총 약 299개 md 페이지가 wikilink로 연결되어 있고, 모두 frontmatter(`type`, `sources`, `related`, `confidence` 등) 기반으로 구조화되어 있어 graph 추론·검색에 활용되고 있습니다. 2026년 6월부터는 이 위키 전체를 검색·추론하는 **챗봇 에이전트**가 별도 트랙으로 가동 중입니다.

## 작업 환경

로컬은 Windows 환경에서 `my-wiki` 폴더가 메인 vault입니다. Obsidian으로 wikilink·graph view를 시각적으로 확인하고, Quartz는 별도 repo에서 빌드해 GitHub Pages로 배포됩니다. my-wiki는 비공개 GitHub repo에 sync되어 cross-device 작업이 가능합니다.

LLM 도구는 Claude를 메인으로 사용하며, 실사용 결과 **Claude Code** (데스크톱 앱 / CLI)가 파일·터미널 작업에 가장 적합한 것으로 확인되어 ingest·편집·git·셸 작업의 메인 환경으로 정착했습니다. Read/Write/Edit/Bash/Grep 풀 toolset으로 위키 파일과 셸 명령을 직접 다루며, Cowork 모드(데스크톱 앱 자유 채팅)는 병용합니다. 단 destructive·되돌리기 어려운 작업(`rm -rf`, `git push --force`, DB drop 등)은 사용자 확인 후 실행합니다.

원문 자료는 NotebookLM MCP, Web Clipper 등으로 수집해 `raw/` 폴더에 적재하며, *raw는 절대 수정하지 않는 read-only 원본 저장소*로 유지합니다.

## 도구 스택·아키텍처 다이어그램

<div style="font-size:0.83rem;margin:1rem 0 1.6rem;line-height:1.65;max-width:660px">

<div style="border:1.5px dashed var(--gray);border-radius:4px;padding:0.6rem 1.2rem;text-align:center">
<strong>데이터 수집 layer</strong><br>
Web Clipper &nbsp;·&nbsp; NotebookLM &nbsp;·&nbsp; 직접 PDF / 트랜스크립트 다운로드
</div>

<div style="text-align:center;padding:0.3rem 0;opacity:.6">↓</div>

<div style="border:1.5px dashed var(--gray);border-radius:4px;padding:0.6rem 1.2rem;max-width:380px;margin:0 auto">
<strong>raw/ &nbsp;(read-only 원본)</strong><br>
- articles/ &nbsp;&nbsp; - pdfs/<br>
- transcripts/ &nbsp; - 등
</div>

<div style="text-align:center;padding:0.3rem 0;opacity:.6">↓ &nbsp;INGEST 명령</div>

<div style="border:1.5px dashed var(--gray);border-radius:4px;padding:0.6rem 1.2rem;text-align:center">
<strong>LLM 처리 (Claude)</strong><br>
· 핵심 요약 추출 &nbsp;&nbsp; · concept / entity 추출 &nbsp;&nbsp; · 모순 검출<br>
· wikilink 자동 연결 &nbsp;&nbsp; · frontmatter 구조화
</div>

<div style="text-align:center;padding:0.3rem 0;opacity:.6">↓</div>

<div style="border:1.5px dashed var(--gray);border-radius:4px;padding:0.6rem 1.2rem;font-family:ui-monospace,'Cascadia Code',monospace;font-size:0.79rem">
<strong>wiki/ &nbsp;(관리 대상)</strong><br>
├── sources/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 원문 요약 (124)<br>
├── concepts/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 개념 페이지 (58)<br>
├── entities/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 스튜디오·게임·플랫폼 (85)<br>
├── comparisons/ &nbsp;&nbsp; 비교 분석 (17)<br>
├── presentations/ &nbsp;HTML 슬라이드 + wrapper<br>
├── index.md &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 전체 카탈로그<br>
└── log.md &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ingest·작업 이력
</div>

<div style="text-align:center;padding:0.3rem 0;opacity:.6">↓ &nbsp;여기서 두 갈래로 소비됨</div>

<div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap">

<div style="flex:1;min-width:240px">
<div style="text-align:center;padding:0.2rem 0;opacity:.6;font-size:0.78rem">① 정적 사이트 — git push</div>
<div style="border:1.5px dashed var(--gray);border-radius:4px;padding:0.6rem 1.2rem;text-align:center">
GitHub: my-wiki (private)
</div>

<div style="text-align:center;padding:0.3rem 0;opacity:.6">↓ &nbsp;Action 자동 trigger</div>

<div style="border:1.5px dashed var(--gray);border-radius:4px;padding:0.6rem 1.2rem;max-width:280px;margin:0 auto;text-align:center">
GitHub: quartz<br>
<span style="font-size:0.78rem;opacity:.8">(content submodule 자동 sync)</span>
</div>

<div style="text-align:center;padding:0.3rem 0;opacity:.6">↓ &nbsp;Pages 빌드</div>

<div style="border:1.5px dashed var(--gray);border-radius:4px;padding:0.6rem 1.2rem;text-align:center">
ginzadaddy-png.github.io<br>
/quartz/
</div>
</div>

<div style="flex:1;min-width:240px">
<div style="text-align:center;padding:0.2rem 0;opacity:.6;font-size:0.78rem">② 챗봇 색인 — build_index.py</div>
<div style="border:1.5px dashed var(--gray);border-radius:4px;padding:0.6rem 1.2rem;text-align:center">
청크 분할 → <strong>BGE-M3</strong> 임베딩<br>
<span style="font-size:0.78rem;opacity:.8">+ relations → NetworkX graph</span>
</div>
<div style="text-align:center;padding:0.3rem 0;opacity:.6">↓ &nbsp;push_space.py</div>
<div style="border:1.5px dashed var(--gray);border-radius:4px;padding:0.6rem 1.2rem;text-align:center">
HF Spaces (Docker)<br>
<span style="font-size:0.78rem;opacity:.8">Streamlit + Claude API</span>
</div>
</div>

</div>

## 작업 흐름

루틴은 크게 네 가지 명령(INGEST / QUERY / LINT / DECISION)으로 표준화되어 있습니다.

### INGEST

가장 자주 쓰는 흐름입니다. raw 폴더에 새 자료를 떨궈 두고 "ingest [파일명]"이라고 하면 Claude가 다음 절차로 처리합니다.

1. 원문 frontmatter에서 출처 URL·저자·발행일 추출
2. 핵심 3~7개 요약을 보여주고 강조점 확인
3. `wiki/sources/`에 요약 페이지 생성
4. 관련 concept·entity 페이지 신규 생성 또는 보강
5. 기존 위키와 모순되면 경고 블록 추가
6. index·log 갱신

entity 페이지에는 `relations:` 필드(developedBy·publishedBy·parentOf·genre·platform 5개 어휘)도 부착해서 향후 graph 추론에 대비합니다.

### QUERY

"X에 대해 정리된 내용 있나" 식 질문을 받으면 index를 거쳐 관련 페이지를 찾고 wikilink로 출처 표시하며 답변. 새로운 합성이 가치 있다면 *"이 답변을 페이지로 저장할까요?"* 제안이 따라옵니다.

### LINT

"점검"이라고 하면 모순 페이지 / 고립 페이지(=incoming link 없음) / 자주 언급되는데 페이지 없는 개념을 자동 탐지해 다음 조사 주제를 제안합니다. 현재 Cowork 스케줄로 *매주 자동 실행* 중입니다.

### DECISION

본인의 결정이나 가설 검증을 wiki에 누적합니다. 결정 텍스트를 자유 채팅으로 던지면 템플릿에 분배해 `wiki/decisions/`에 정리하고, 근거가 된 concept 페이지에 양방향 링크를 답니다. 3·6·12개월 후 결과를 사후 갱신하는 archive 구조입니다.

### 슬라이드 산출물

별도 트랙으로, `wiki/presentations/[슬러그]-deck.html` + wrapper md 짝을 만들어 사이트에 iframe으로 embed합니다. Pretendard 단일 폰트, `-deck` 접미사 필수(Quartz slug 충돌 회피), wrapper는 결과물만 노출(작업 이력은 [[log]]에서) 같은 명명 규칙이 운영 지침에 박혀 있습니다.

## 챗봇 (위키 Q&A 에이전트)

2026년 6월, 위키 전체를 검색·추론하는 **Hybrid Agent 챗봇**을 `chatbot/` 폴더에 구축했습니다. *"위키에 정리된 내용을 자연어로 물어보면 출처와 함께 답한다"*가 목표이고, 사이트 사이드바의 **💬 위키에 질문하기** 링크에서 접근합니다 (HF Spaces 공개 + 앱 비밀번호 게이트 — iOS Safari 등 모든 브라우저에서 접근 가능).

### 핵심 설계

- **RAG (의미 검색)**: 위키 277개 md를 청크(~1,400개)로 분할 → 로컬 **BGE-M3** 임베딩 → Chroma 벡터 DB. 청크에 `제목·섹션` 접두를 붙여 한↔영 cross-language 검색을 보강했습니다.
- **Graph (관계 추론)**: entity의 `relations:` 필드(developedBy·publishedBy·parentOf·genre·platform)를 **NetworkX** 그래프로 빌드(약 269 노드 / 158 엣지). *"Astro Bot 만든 팀의 모회사가 소유한 다른 스튜디오는?"* 같은 multi-hop 질문은 Claude **tool-use**로 그래프를 직접 질의해 답합니다.
- **Hybrid 라우팅**: 질문 성격에 따라 RAG·graph를 함께 사용하고, *위키에 근거 없으면 "없다"고 명시*해 환각을 억제합니다 (30개 평가 셋에서 환각 0건 확인).
- **백엔드/UI 분리**: 검색·그래프·에이전트 로직은 `core/` 모듈, UI는 Streamlit `app.py`로 분리해 향후 다른 프런트(봇 등) 확장에 대비했습니다.

### 개발 도구·스택

| 영역 | 도구 |
|---|---|
| 임베딩 | BGE-M3 (`sentence-transformers`, 로컬 실행 — API 비용 0) |
| 벡터 DB | Chroma (`chatbot/chroma_db/`, 코사인) |
| 관계 그래프 | NetworkX (`MultiDiGraph`) |
| LLM | Anthropic Claude (Sonnet, 종량제) + tool-use |
| UI | Streamlit |
| 배포 | Hugging Face Spaces (Docker SDK, 무료 티어) |
| 개발 환경 | Claude Code (전 코드·디버깅·배포 자동화) |

### 갱신 워크플로우

위키를 ingest/수정하면 챗봇 색인이 자동으로 따라오지 않으므로 명시적 동기화가 필요합니다. `chatbot/update_and_deploy.py` 한 번이면 **재색인(BGE-M3) → HF Space 재배포**가 묶여 실행됩니다. 그래서 INGEST 절차 마지막에 *"챗봇도 갱신할까요?"* 확인 단계를 두어, 위키와 챗봇 배포본의 정합을 유지합니다.

> 인프라 고정비는 0(HF Spaces 무료 + 구독 없음)이지만, Claude API는 질문당 종량제(선충전 크레딧에서 차감)로 과금됩니다. 선충전 모델이라 잔액 한도 내에서만 동작해 폭주 과금 위험은 없습니다.

## 진행 예정

### 단기

**decisions 트랙 본격 가동** — 지금까지 ingest·정리에 집중했는데, 그동안 누적된 개념을 *의사결정에 인용*하는 단계로 넘어갈 시점입니다. 첫 decision 페이지가 작성되면 양방향 링크가 작동하면서 wiki의 가치가 한 단계 올라갑니다.

**챗봇 운영·품질 다지기** *(graph relations + 챗봇 구축은 2026-06 완료 — [위 챗봇 섹션](#챗봇-위키-qa-에이전트) 참조)* — entity `relations:` 부착과 기존 entity retrofit을 마치고, RAG + graph hybrid 챗봇까지 배포된 상태입니다. *"Astro Bot 만든 팀의 모회사가 다른 어떤 스튜디오를 소유했지"* 같은 multi-hop query가 실제로 동작합니다. 다음 단계는 운영 안정화 — 답변 품질 회귀 점검, 갱신 자동화 정착(ingest 후 *"챗봇도 갱신할까요?"* 루틴), 비용 모니터링입니다.

### 중기

**카탈로그 이코노믹스 / Steam 출시 전략 두 deck의 확장** — 캡콤 9년 catalog 곡선, ZR Consulting 8-driver 모델, Carless wishlist conversion 등 이미 정리된 1차 데이터를 활용해 한국 인디·중소 스튜디오 적용 케이스를 추가할 여지가 있습니다.

**LINT 절차 확장 — raw 폴더 미처리 큐 식별** — LINT는 Cowork 스케줄로 매주 자동 실행되고 있으며, 다음 단계는 *위키 내부 갭에서 출발하는 조사 주제 제안*에 더해 *raw 폴더에 이미 모아둔 자료 중 처리 안 된 큐*까지 한 알림에 포함시키는 절차 확장입니다. 두 흐름을 같은 주간 보고에 묶어 자료 누락·정체를 방지합니다.

### 장기

**수집된 65건 ingest를 종합 사고 정리물로 압축** — 흩어진 개념 페이지들을 *"게임 개발 산업이 2026년 어디로 향하는가"* 같은 메타 분석 글로 합성하는 단계입니다. wiki는 그 자체로 끝이 아니라 사고를 누적하는 archive이고, 일정 시점에서 한 번 회수해 정리물을 만들어야 가치가 닫힌다는 인식입니다.

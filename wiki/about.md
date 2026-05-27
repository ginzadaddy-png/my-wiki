---
title: "Game Dev Wiki — 현황 공유"
type: concept
sources: []
related: ["[[index|전체 카탈로그]]", "[[log|활동 로그]]"]
created: 2026-05-27
updated: 2026-05-27
confidence: high
---

## 개요

게임 개발 관련 1차 자료(IR 보고서, GDC 발표, 업계 분석가 글, 트랜스크립트 등)를 읽고 위키 형태로 누적·교차참조하는 개인 지식 베이스입니다. Karpathy식 LLM 활용 위키를 모티브로, *raw 소스를 LLM이 요약·구조화해서 wiki 폴더에 정리*하고 추후 의사결정·발표 자료로 재활용하는 구조입니다. 산출물은 Quartz로 정적 사이트화되어 GitHub Pages로 배포됩니다.

핵심 가치 — 같은 자료를 두 번 읽지 않고, 출처와 인사이트가 항상 wikilink로 연결되어 있어 *"이 주장 어디서 봤더라"* 가 해소됩니다.

## 현재 통계·규모 (2026-05-27 기준)

| 항목 | 수치 |
|---|---|
| 누적 INGEST 건수 | 65건 |
| 소스 요약 (`wiki/sources/`) | 115개 |
| 개념 페이지 (`wiki/concepts/`) | 54개 |
| 엔티티 페이지 (스튜디오·게임, `wiki/entities/`) | 61개 |
| 비교 페이지 (`wiki/comparisons/`) | 13개 |
| 슬라이드 deck (HTML + wrapper) | 2개 ([[presentations/steam-launch-strategy|Steam 출시 전략]] / [[presentations/studio-risk-defense|스튜디오 리스크 방어]]) |
| 마지막 갱신 | 2026-05-26 |

총 약 250개 md 페이지가 wikilink로 연결되어 있고, 모두 frontmatter(`type`, `sources`, `related`, `confidence` 등) 기반으로 구조화되어 있어 추후 graph 추론·검색 활용 가능한 상태입니다.

## 작업 환경

로컬은 Windows 환경에서 `my-wiki` 폴더가 메인 vault입니다. Obsidian으로 wikilink·graph view를 시각적으로 확인하고, Quartz는 별도 repo에서 빌드해 GitHub Pages로 배포됩니다. my-wiki는 비공개 GitHub repo에 sync되어 cross-device 작업이 가능합니다.

LLM 도구는 Claude를 메인으로 사용하되, **Cowork 모드(Claude 데스크톱 앱)**는 파일 편집·검증 작업에, **Claude Code CLI / GitHub Desktop**은 git commit·push에 분담해 사용합니다. 이는 Cowork 샌드박스의 cross-user mount 권한 비대칭으로 `.git/*.lock` 파일을 unlink 못 하는 한계가 반복적으로 확인되어 정착된 워크플로우입니다.

원문 자료는 NotebookLM MCP, Web Clipper 등으로 수집해 `raw/` 폴더에 적재하며, *raw는 절대 수정하지 않는 read-only 원본 저장소*로 유지합니다.

## 도구 스택·아키텍처 다이어그램

```
┌─────────────────────────────────────────────────────────────────┐
│                       데이터 수집 layer                         │
│  Web Clipper · NotebookLM · 직접 PDF / 트랜스크립트 다운로드    │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
                ┌──────────────────────────┐
                │  raw/  (read-only 원본)  │
                │  - articles/ - pdfs/     │
                │  - transcripts/ - 등     │
                └──────────────┬───────────┘
                               │ INGEST 명령
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                     LLM 처리 (Claude)                           │
│  · 핵심 요약 추출  · concept / entity 추출  · 모순 검출         │
│  · wikilink 자동 연결  · frontmatter 구조화                     │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│   wiki/  (관리 대상)                                            │
│   ├── sources/      원문 요약 (115)                             │
│   ├── concepts/     개념 페이지 (54)                            │
│   ├── entities/     스튜디오·게임 (61)                          │
│   ├── comparisons/  비교 분석 (13)                              │
│   ├── presentations/ HTML 슬라이드 + wrapper                    │
│   ├── index.md      전체 카탈로그                               │
│   └── log.md        ingest·작업 이력                            │
└──────────────────────────────┬──────────────────────────────────┘
                               │ git push (GitHub Desktop)
                               ▼
              ┌────────────────────────────┐
              │ GitHub: my-wiki (private)  │
              └──────────────┬─────────────┘
                             │ Action 자동 trigger
                             ▼
              ┌────────────────────────────┐
              │ GitHub: quartz (content    │
              │   submodule 자동 sync)     │
              └──────────────┬─────────────┘
                             │ Pages 빌드
                             ▼
              ┌────────────────────────────┐
              │  ginzadaddy-png.github.io  │
              │       /quartz/             │
              └────────────────────────────┘
```

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

## 진행 예정

### 단기

**decisions 트랙 본격 가동** — 지금까지 ingest·정리에 집중했는데, 그동안 누적된 개념을 *의사결정에 인용*하는 단계로 넘어갈 시점입니다. 첫 decision 페이지가 작성되면 양방향 링크가 작동하면서 wiki의 가치가 한 단계 올라갑니다.

**graph 추론 가능한 entity relations 적용** — Phase 1에서 신규 entity에 `relations:` 5개 어휘를 부착 중이며, 일정 임계치(예: 신규 entity 80% 이상 부착)를 넘으면 Phase 3에서 기존 entity 일괄 retrofit. 이후 챗봇 형태로 *"Astro Bot 만든 팀의 모회사가 다른 어떤 스튜디오를 소유했지"* 같은 query 가능 상태가 목표입니다.

### 중기

**카탈로그 이코노믹스 / Steam 출시 전략 두 deck의 확장** — 캡콤 9년 catalog 곡선, ZR Consulting 8-driver 모델, Carless wishlist conversion 등 이미 정리된 1차 데이터를 활용해 한국 인디·중소 스튜디오 적용 케이스를 추가할 여지가 있습니다.

**AI 가속 도구의 워크플로우 통합** — LINT는 Cowork 스케줄로 매주 자동 실행되고 있으며, 다음 단계는 raw 폴더에 새 자료가 떨어지면 자동으로 ingest 후보를 골라 알려주는 트리거형 자동화 도입입니다.

### 장기

**수집된 65건 ingest를 종합 사고 정리물로 압축** — 흩어진 개념 페이지들을 *"게임 개발 산업이 2026년 어디로 향하는가"* 같은 메타 분석 글로 합성하는 단계입니다. wiki는 그 자체로 끝이 아니라 사고를 누적하는 archive이고, 일정 시점에서 한 번 회수해 정리물을 만들어야 가치가 닫힌다는 인식입니다.

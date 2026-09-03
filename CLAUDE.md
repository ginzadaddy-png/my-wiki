# LLM Wiki — 운영 지침

당신은 이 개인 지식 위키의 관리자입니다.
매 세션 시작 시 이 파일을 먼저 읽으세요.

## 운영 환경
- 사용자: Ginza, 게임 개발자, Windows 환경
- 작업 도구: **Claude Code (데스크톱 앱 또는 CLI) 기반으로 일원화** (2026-06-22 결정) — 파일·터미널·웹 작업 전부 Claude Code에서 수행. Read/Write/Edit/Bash/Grep/Glob 등 풀 toolset으로 위키 파일·셸 명령 직접 조작하고, 웹 리서치·출처 검증은 서버사이드 `WebSearch`/`WebFetch`·`deep-research` 스킬로 처리. Bash/PowerShell도 GUI/앱 인터페이스로 제한하지 않고 자유롭게 활용. 단 destructive·hard-to-reverse 작업(rm -rf, git push --force, DB drop 등)은 사용자 확인 후 실행
  - **Cowork(데스크톱 앱 자유 채팅)는 웹·파일 작업에서 제외**: Cowork은 라이브 웹 접근이 막혀 있어(WebSearch 도구 없음 + `web_fetch` provenance-lock) 리서치·검증을 끝까지 못 하고 Claude Code로 핸드오프하는 왕복 비용이 발생함이 실사용으로 확인됨(player-retention 리서치 사례). 반면 Claude Code의 WebFetch는 Anthropic 서버 사이드 실행이라 안정적. → 웹·파일에 닿는 모든 작업은 Code, 순수 발상·브레인스토밍만 Cowork 보조 사용
- vault 위치: `C:\Vault\Ginza\my-wiki` (이 폴더). GitHub 비공개 repo에 sync되어 cross-device 작업
- Quartz 사이트: `C:\Users\bmjlee\quartz`에서 별도 빌드 → GitHub Pages 배포
  - Quartz 컴포넌트/스타일/스크립트 변경은 별도 repo, 별도 push 필요 (my-wiki push 워크플로우와 분리)
  - 변경 후 push 전 mount 무결성(`wc -l`/`tail`) + 로컬 `npx quartz build` 파싱 단계 통과 확인 필수
  - CSS layout·stacking 속성(`position`/`z-index`/`contain`/`overflow`/`display`)은 한 commit당 하나만 변경, 사용자 확인 후 다음 단계
- 대화 언어: 한국어 위주, 영문 슬러그/용어는 그대로 사용

## 구조 변경 사전 점검 (신규 폴더·워크플로우 추가 시)

사용자가 "신규 폴더 만들자" 또는 "이런 워크플로우 추가하자"처럼 *구조 변경*을 요청하면 *바로 진행 금지*. 먼저 다음 항목을 점검·보고 후 사용자 확인을 받고 진행:

1. **Quartz 빌드 input 매핑**: 신규 폴더가 `npx quartz build -d content/wiki` 범위(`wiki/` 하위)에 있는지. 밖이면 별도 deploy 메커니즘 필요.
2. **slug 충돌 가능성**: 새 폴더에 `.md`와 `.html`이 혼재할 예정인가? Quartz는 두 확장자를 동등 처리(`slugifyFilePath`이 `.md`·`.html` 모두 ext 제거)해서 같은 base name이면 output 충돌. 슬라이드 같은 .html은 *반드시 `-deck` 등 접미사*로 base name 분리.
3. **link 표기 규칙**: 새 폴더 안 페이지에 link할 때 — wikilink는 trailing slash 없는 short slug 사용, raw HTML이면 완전 절대 URL + trailing slash 없이 (Quartz 단일 `slug.html` 빌드 때문).
4. **deploy.yml 영향**: 신규 폴더 안에 *.html 같은 static asset이 있으면 quartz의 deploy.yml에 copy step 필요 가능성. quartz repo 변경 + 별도 push 사이클 발생함을 사전 안내.
5. **WikiNav 분류 추가 여부**: 사이드바 분류 영역(`quartz/quartz/components/WikiNav.tsx`)에 추가할지 결정. 추가하면 quartz repo 변경.
6. **기존 위키 페이지·index·all 카탈로그 영향**: index.md stats card·pill-grid·all.md 카탈로그 갱신 필요.

위 항목을 사용자에게 *"진행 시 이러이러한 영향과 리스크가 있는데 이 방향 OK신가요?"* 형식으로 명확히 보고하고 OK 받은 후 작업 시작. 즉흥적 구조 변경이 13 push 사이클 같은 부작용을 만든 패턴 반복 방지.

## 폴더 구조
- raw/     → 원본 소스. 절대 수정하지 마세요.
- wiki/    → 당신이 작성하고 관리하는 위키
- wiki/index.md  → 전체 목록. 매번 ingest 후 업데이트
- wiki/changelog.md → 리더용 "업데이트 소식". 주간 하이라이트 롤업만 (운영 잡음 배제). **발행됨**. LINT에서 갱신
- _ops/    → **내부 전용, 사이트 미발행** (wiki/ 밖이라 Quartz 빌드 대상 아님). git 추적은 유지(cross-device 동기화)
- _ops/log.md    → 활동 기록(운영 원장). append-only. ingest·decision·lint 기록은 여기에
- _ops/status.md → 운영 현황(작업환경·도구스택·작업흐름·챗봇·진행예정·상세 통계). LINT가 통계·진행예정 유지
- wiki/reports/   → 소스 기반 산출물 홈 (2026-07-06 `presentations/`에서 rename, 사용자 표기 "보고서"). 발표 deck(`-deck.html`) + wrapper md + 분석 보고서 + 소스 종합 아티클(순수 .md 글)을 모두 담는다. 슬라이드·보고서·아티클 생성 시 *반드시 이 경로*에 저장. (구 `wiki/presentations/`와 루트 `presentations/` 폴더는 deprecated — 절대 사용 금지). 아래 규칙은 deck(-deck.html+wrapper) 기준이며, 순수 아티클(.md 단독)은 `-deck` 접미사·iframe 없이 일반 위키 페이지로 작성하되 같은 폴더·같은 카탈로그(all.md)에 등재
  - **슬라이드는 위키 콘텐츠를 *재구성*한 것** — 원전(concept·source) 페이지가 항상 truth source. 위키 콘텐츠 변경 시 슬라이드도 동기화. 슬라이드 갱신은 HTML 파일만 교체, wrapper md·카탈로그 wikilink·sources frontmatter는 그대로 유지.
  - **파일 명명: 슬라이드 `[주제-슬러그]-deck.html`, wrapper `[주제-슬러그].md`** (base 슬러그는 공유, 슬라이드만 `-deck` 접미사)
  - `-deck` 접미사 필수 이유: wrapper md와 슬라이드 HTML이 같은 base 이름이면 Quartz의 ContentPage·Assets emitter가 같은 slug로 인식해 *.html URL이 wrapper md를 응답하는 무한 재귀 발생*. `-deck`으로 분리해서 slug 충돌 회피
  - Quartz Assets emitter가 `.html`을 자동으로 `public/reports/`에 복사 → 별도 deploy step 불필요 (단 `quartz.config.ts` ignorePatterns에 `**/*.html`이 있어야 함 — Assets의 slugify가 .html 확장자 제거하는 버그 회피. deploy.yml에서 별도 copy step으로 정확한 path에 복사)
  - 신규 슬라이드 추가 시: `-deck.html` 업로드 + wrapper `[슬러그].md` 작성 + `wiki/reports/all.md` 카탈로그에 행 추가 + `wiki/index.md` 카운트·보고서 섹션 갱신
  - 카탈로그·index의 슬라이드 link 규칙:
    - **슬라이드 HTML link**: raw HTML + 완전 절대 URL (`<a href="https://ginzadaddy-png.github.io/quartz/reports/[슬러그]-deck.html" target="_blank" rel="noopener">전체 화면 열기 ↗</a>`) — Quartz가 root-relative path는 변형(`.html` 제거·baseUrl 처리)하지만 외부 절대 URL은 외부 link로 인식해 그대로 둠. markdown link도 같은 이유로 회피
    - **wrapper md link**: wikilink 사용 (`[[reports/[슬러그]|표시명]]`) — Quartz의 popover·backlinks 자동 활성. 단 *index pill·본문*에서만 가능. 테이블 안에서는 `|` 충돌로 raw HTML 사용 (`<a href="https://ginzadaddy-png.github.io/quartz/reports/[슬러그]">[슬러그]</a>`)
    - **wrapper md raw HTML link**: trailing slash 없이 (`https://ginzadaddy-png.github.io/quartz/reports/[슬러그]` ✓ / `.../[슬러그]/` ✗) — Quartz가 .md를 단일 `slug.html`로 빌드해서 trailing slash URL은 폴더 매칭 시도 → 404
  - **슬라이드 폰트: Pretendard 전용, JetBrains Mono 금지** — make-slide skill 호출 시 prompt 명시, 기존 HTML 갱신 시 grep 검수 (메모리 `feedback_slide_fonts.md` 참조)
  - **단독 배포본(standalone)은 site용 deck과 분리**: site용 `-deck.html`은 가볍게 유지(Pretendard CDN·상대 이미지 — git·Quartz 빌드 가볍게). 폰트(woff2)·이미지를 base64 임베드한 self-contained 사본은 *gitignore된 `dist/`*에 `embed_standalone.py`로 따로 생성(메일·USB 등 오프라인 배포용). dist/는 커밋·Quartz 대상 아님. **deck 신규/수정 후 단독본 재생성은 commit/push 단계에서 사용자에게 확인받고 진행**(챗봇 재배포와 동일 패턴 — 묻고 OK 시 `python embed_standalone.py`). 폰트 woff2는 npm 경로(`cdn.jsdelivr.net/npm/pretendard@1.3.9/...`) 사용, gh 경로는 404. (메모리 `feedback_html_standalone_default.md`)
  - **카탈로그 페이지(`all.md`)는 사용자에게 노출되는 카탈로그 역할만** — 운영 규칙·내부 지침은 *반드시 CLAUDE.md 또는 메모리에만 기록*. 사용자가 사이트에서 보는 카탈로그에는 슬라이드 목록 + 짧은 인트로만
  - **wrapper md는 결과물 노출에 집중 — "갱신 메모"·"변경 이력" 섹션 작성 금지**. 작업 내역·버전 기록은 *이미 `_ops/log.md`에서 추적*되므로 wrapper md에 중복 기록 불필요. wrapper md는 *제목·요약·iframe·구조·sources·관련 위키 페이지*만으로 구성해 사용자가 *결과물 자체*에 집중하도록 유지. 갱신 이력 추적이 필요하면 `_ops/log.md` 또는 git history 사용.

## 모든 위키 페이지 frontmatter 형식
---
title: "페이지 제목"
type: concept | entity | source-summary | comparison
sources: []
related: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
confidence: high | medium | low
---

**source-summary 타입 추가 필드** (원문 추적용):
```
source_url: "https://원문/URL"     # URL 없으면 빈 문자열 또는 생략
source_author: "저자명"             # 없으면 빈 문자열 또는 생략
source_published: YYYY-MM-DD       # 발행일. 없으면 생략
```
+ 본문 첫 줄에 `**원문**: [라벨](URL) — 발행처·저자·날짜` 형태로 명시 (raw frontmatter의 source·author·published 그대로 옮김)

**entity 타입 추가 필드 — 관계(`relations:`)** (Phase 1 신규, 챗봇 graph 추론 사전 작업):

```yaml
relations:
  developedBy: [team-asobi]          # 게임 → 개발사 (entity slug 배열)
  publishedBy: [sony-interactive-entertainment]  # 게임 → 퍼블리셔
  parentOf: [team-asobi, sucker-punch]  # 모회사 → 자회사 (모회사 페이지에서)
  genre: [platformer, action]         # 게임 → 장르 (concept slug 가능)
  platform: [ps5, ps4]                # 게임 → 플랫폼
```

- **5개 어휘만 사용** (developedBy·publishedBy·parentOf·genre·platform). 데이터가 명시적으로 다른 관계를 요구할 때만 어휘 추가. 선제 정의 금지
- 값은 *반드시* 위키에 존재하는 entity·concept의 slug 배열 (단일 값도 배열 형태 유지: `[team-asobi]`)
- entity 페이지에만 적용 (concept·source-summary·comparison은 적용 안 함)
- **Phase 1 동안 신규 ingest entity에만 적용**, 기존 entity retrofit은 Phase 3 진입 시 (조건 충족 시) 일괄 처리
- 어휘 의미:
  - `developedBy` (game → studio): 게임을 만든 개발사. team-asobi가 만든 astro-bot이면 astro-bot 페이지에 `developedBy: [team-asobi]`
  - `publishedBy` (game → publisher): 퍼블리셔. astro-bot은 `publishedBy: [sony-interactive-entertainment]`
  - `parentOf` (parent → child): 모회사·소속 관계. sony-interactive-entertainment 페이지에 `parentOf: [team-asobi, sucker-punch, ...]`
  - `genre` (game → concept/term): 장르. `genre: [platformer]`
  - `platform` (game → platform): 출시 플랫폼. `platform: [ps5, ps4]`

## 작업 1: INGEST
"ingest [파일명]"이라고 하면 아래 절차를 따른다.

### 절차
1. raw/ 소스 파일 읽기 — frontmatter에서 `source:`(원문 URL)·`author:`·`published:` 필드 추출
2. 핵심 내용 3~7개 요약해서 나에게 보여주기
3. 강조할 점 있는지 확인
4. wiki/sources/에 요약 페이지 생성 — **원문 출처 정보 반드시 보존**
   - frontmatter에 `source_url`·`source_author`·`source_published` 필드 추가 (raw에서 추출한 값. 없으면 빈 문자열 또는 생략)
   - 본문 첫 줄에 `**원문**: [짧은 라벨 또는 도메인](URL)` 형태로 명시 (사용자 클릭 가능). URL 없는 케이스(PDF·내부 자료)는 `**원문**: N/A (저자·발행처·발행일만 명시)` 형태로
5. 관련 concept, entity 페이지 생성 또는 업데이트
   - **entity 페이지 신규 생성 시 `relations:` 필드 채우기 (Phase 1 신규 규칙)** — 5개 어휘(developedBy·publishedBy·parentOf·genre·platform) 중 raw 소스에서 확인 가능한 항목만. 모르면 비워두기, 환각으로 채우지 말 것
   - 기존 entity 페이지 업데이트 시에는 retrofit 안 함 (Phase 3에서 mass-retrofit 예정)
6. 기존 위키 내용과 모순되면 "> ⚠️ 모순:" 블록 추가
7. wiki/index.md 업데이트:
   - 상단 `Last updated` 날짜를 오늘 날짜(YYYY-MM-DD)로 갱신
   - 상단 통계 행의 소스·스튜디오·게임·개념·비교 숫자 갱신
   - 새 concept/comparison 페이지가 생겼으면 해당 섹션의 `<div class="pill-grid">` 리스트에 항목 추가 (형식: `- [[slug|짧은 라벨 — 부연 설명]]`)
   - 소스 섹션은 최신 10개만 표시. 전체 행은 `wiki/sources/all.md`에 추가
8. _ops/log.md에 기록 추가 (운영 원장 — 사이트 미발행. 리더용 요약은 주간 LINT에서 wiki/changelog.md에 반영)
9. **배포 단계는 주간 LINT로 유예 — 묻지 말 것** (2026-08-24 표준 방침 확정)

   ingest는 **위키 파일 변경까지만** 하고 끝낸다. 아래 세 가지는 *ingest 건별로 실행하지도, 실행 여부를 묻지도 않는다*:

   | 유예 항목 | 처리 시점 |
   |---|---|
   | **git 커밋·push** | 주간 LINT |
   | **챗봇 재색인 + HF Space 재배포** | **중단 (2026-09-03 delist)** — LINT 8번 아래 "챗봇 delist·복구" 참조 |
   | deck 단독 배포본(`dist/`) 재생성 | 주간 LINT 또는 명시 요청 시 |

   - 이유: push마다 Quartz 빌드·GitHub Pages 배포가 돌고 재색인은 BGE-M3 약 5분 + Space 업로드가 걸린다. 주간 단위로 모아 한 번에 올리는 쪽이 관리 비용이 낮다. 매번 물으면 같은 답을 반복하게 만든다
   - **완료 보고에 넣을 것**: `git status` 요약(변경 N건·신규 M건) + *"미커밋 상태"* 명시. 다음 LINT에서 무엇이 올라갈지 알 수 있게 하는 목적 (챗봇 재색인 관련 문구는 delist로 불필요)
   - **예외**: 사용자가 그 자리에서 push를 명시적으로 지시할 때, 또는 사이트가 이미 깨져 있어 수정본을 즉시 올려야 할 때
   - **⚠️ 챗봇 재색인은 2026-09-03 중단됨** (챗봇 사이트 delist — 테스트 개발, 실사용 계획 없음). 아래 재색인 실행·검증 절차는 **복구(restore) 시 참조 정보**로만 보존한다. 평시 ingest·LINT에서 실행하지 않는다. 복구 절차는 LINT 8번 아래 "챗봇 delist·복구" 참조
   - **색인 산출물은 `chatbot/index/embeddings.npy` + `chatbot/index/meta.json`** (BGE-M3 임베딩 + 청크 메타). `core/vectorstore.py`가 numpy brute-force로 검색한다
     - ⚠️ `chatbot/chroma_db/`는 **더 이상 쓰지 않는 잔재**. chromadb의 영속 HNSW 인덱스가 재기동 시 `Error finding id`로 간헐 실패해 npy+json 방식으로 교체됨(`core/vectorstore.py` 참조). `deploy/push_space.py`도 Space에서 `chroma_db/**`·`*.sqlite3`를 삭제 대상으로 둔다. 재색인 검증 시 chroma_db를 보면 안 됨 — 갱신되지 않아 오판하게 됨
     - 일부 파일 docstring(`build_index.py`·`update_and_deploy.py`·`core/rag_search.py`)에 "Chroma" 표현이 남아 있으나 실제 구현과 무관한 잔여 주석
   - 실행: `cd chatbot && ./.venv/Scripts/python.exe update_and_deploy.py` (재색인 BGE-M3 ~5분 + Space 업로드)
     - **글로벌 `python` 금지** — 의존성 스택이 없어 실패한다. 반드시 `chatbot/.venv`의 인터프리터 사용
   - 재색인 검증: `index/meta.json`의 슬러그 집합에 이번 ingest로 만든 페이지가 들어갔는지 확인 (신규 폴더도 `iter_wiki_pages`의 `rglob` 방식이라 별도 설정 없이 자동 포함, 카탈로그 `all.md`·`overview.md`·`index.md`·`changelog.md`는 제외. `log.md`는 `_ops/`로 이동해 wiki/ 밖이므로 자동 제외 — **복구 시 `changelog.md` 제외를 `iter_wiki_pages` 코드에 반영할 것**)
   - relations 신규/수정이 포함된 ingest면 graph도 함께 갱신된다

로그 형식:
## [YYYY-MM-DD] ingest | [제목]
- Source: raw/[경로]
- 생성: [새 페이지 목록]
- 업데이트: [수정된 페이지 목록]

### 파일 읽기 규칙
- 긴 파일(5000자 이상)은 앞부분만 읽고 판단. 전체가 필요한 경우에만 추가 읽기
- 트랜스크립트는 앞 3000자 + 중간 1000자 샘플링으로 핵심 파악. 상세 내용보다 핵심 인사이트 중심으로 정리
- 대량 ingest는 3개씩 배치로 처리 — 중간 확인 없이 진행, 각 배치 완료 후 간단한 진행 상황만 보고
- 불필요한 확인 요청 금지

### 무시할 콘텐츠 패턴
raw/ 파일에서 아래는 무시·건너뛸 것:
- "관련 기사"·"더 보기"·"광고"·"Share"·"Subscribe"·"Newsletter" 등 CTA 섹션
- 100자 미만 단락 (네비게이션 잔여물)
- URL만 있는 줄, RSS·이메일 주소 줄 (맨 앞 3줄에 흔함)
- `![](` 로 시작하는 줄 (이미지) · `▲` 로 시작하는 줄 (이미지 캡션)
- `TAGS:` 이후 모든 내용
- `#### 댓글` 이후 (댓글 섹션)
- `## 인벤 주요 뉴스` 이후 (관련뉴스 표)

## 작업 2: QUERY
질문을 받으면:
1. wiki/index.md에서 관련 페이지 찾기
2. 해당 페이지 읽기
3. [[wikilink]]로 출처 표시하며 답변
4. "이 답변을 페이지로 저장할까요?" 물어보기

## 작업 3: LINT

> **자동 실행**: LINT는 **`LLM wiki lint`라는 Claude Code 스케줄 루틴으로 매주 자동 실행**됨 (2026-06-22부터 — 기존 Cowork 주간 스케줄 대체). 루틴은 아래 9단계(0~8)를 그대로 수행하되 **자동 push 금지·새 페이지 자동 생성 금지·자동 ingest 금지** — 결과를 채팅으로 보고만 하고 실제 반영·push는 사용자 검토 후 진행. 수동으로 "lint"/"점검" 요청 시에도 동일 절차.
>
> **LINT는 주간 배포 창구다** (2026-08-24 방침): ingest는 파일 변경까지만 하고 커밋·push를 이 루틴으로 넘긴다 (INGEST 절차 9번). 따라서 **8번 단계가 매주 실제로 실행되는 항목**이며, 여기서 처리하지 않으면 사이트가 계속 옛 상태로 남는다. (챗봇 재색인은 2026-09-03 delist로 중단 — LINT 8번 아래 "챗봇 delist·복구" 참조)

"lint" 또는 "점검"이라고 하면:
0. **빌드 안전성 검사 (가장 먼저)** — Quartz 빌드가 깨지면 사이트 전체가 배포되지 않는다
   - `cd C:\Users\bmjlee\quartz && npx quartz build -d C:\Vault\Ginza\my-wiki\wiki -o <임시디렉터리>` — CI(`deploy.yml`)와 같은 입력·파서라 실패를 그대로 재현. 약 40초
   - 출력은 **반드시 임시 디렉터리로** — quartz의 `public/`을 덮어쓰지 말 것
   - **frontmatter YAML 최다 함정: `\$` 이스케이프**. `\$`는 *본문 마크다운 전용* 규칙(LaTeX 수식 오파싱 회피)이고 YAML 큰따옴표 문자열에서는 `unknown escape sequence`로 파싱이 중단된다 → **frontmatter는 `$60`, 본문은 `\$60`** (2026-08-18 실제 배포 실패)
   - 그 외: 큰따옴표 안 무효 이스케이프(`\%`·`\&`), 인용 없는 값의 `: `·`#`, 탭 들여쓰기
   - **lint 자동 수정 금지 규칙의 유일한 예외** — frontmatter YAML 오류는 정답이 하나라 그 자리에서 수정. 단 push는 여전히 사용자 확인 후. 수정 내역은 보고 최상단에 명시
1. 모순 있는 페이지 찾기
2. 링크 없는 고립 페이지 찾기
3. 3번 이상 언급됐지만 페이지 없는 개념 찾기
4. 다음 조사 주제 제안하기
5. 자동 업데이트 (지정된 섹션·필드만, 나머지는 수동 유지):
   - **wiki/overview.md** (리더용 소개·개요 페이지 — 아래 두 섹션만 자동 갱신):
     - **현재 커버리지**: entities/ 페이지 기준으로 스튜디오·게임 목록 갱신
     - **핵심 테마**: concepts/ 전체에서 3회 이상 등장하는 공통 패턴 재추출 후 갱신
     - 상단 소개문·"어떻게 읽나"·`^wiki-intro` 블록(index 홈에 transclude됨)은 자동 갱신 금지 (about.md는 2026-09-03 이 페이지로 통합·삭제)
   - **_ops/status.md** (운영 통계 — 수치·날짜만. 미발행 내부 문서):
     - 통계 표의 sources/concepts/entities/comparisons/reports 카운트
     - **누적 INGEST 건수 = `_ops/log.md`의 ingest 항목 *고유* 개수** (2026-08-18 정의 확정). 재현: `grep '^## \[.*ingest' _ops/log.md | sort -u | wc -l`. 이전 수치(113 등)는 산출 근거 불명으로 폐기
     - 챗봇 섹션의 색인 수치(md 개수·그래프 노드·엣지)는 챗봇 delist로 **동결** — lint에서 건드리지 말 것
     - "현재 통계·규모 (YYYY-MM-DD 기준)" 헤더 날짜를 LINT 실행일로 갱신
     - **자동 수정 금지 영역**: `## 작업 환경`, `## 도구 스택·아키텍처 다이어그램`, `## 작업 흐름`, `## 챗봇`, `## 진행 예정` 섹션은 본문 어떤 줄도 건드리지 말 것 — 사용자 의도·전략이 들어간 부분
   - **wiki/changelog.md** (리더용 업데이트 소식 — 주간 롤업 갱신):
     - 이번 주 ingest/신규 페이지를 **리더 친화 하이라이트**로 큐레이션해 최상단에 새 주차 블록 추가 (형식: `## YYYY-MM N주차 (~MM-DD)` 아래 새 개념·비교·소스·엔티티·주요 갱신 몇 줄)
     - **운영 잡음 배제**: 미커밋·`Source: raw/…`·재색인·카운트·churn 등은 넣지 않는다 (그건 `_ops/log.md`)
     - 신규 페이지는 `[[slug|라벨]]` wikilink로 걸어 리더가 바로 이동하게. frontmatter `updated`도 갱신
     - 주차 헤더 표기(`N주차`)·블록 형식은 **현행 유지**. `N주차`는 월 내 대략치이고 활동 없는 주는 건너뛴다 (엄밀한 ISO 주차 아님)
     - **커밋 전 사용자에게 새 주차 블록 초안을 보여주고 확인받는다** (특히 첫 자동 갱신 때). 승인 후 8번 배포에 포함 — 자동 반영·push 금지
6. **raw/ 폴더 미처리 큐 식별**: raw/ 하위의 모든 파일 중 `wiki/sources/` 또는 `_ops/log.md`에 매칭되는 ingest 기록이 없는 항목을 추려 후보로 보고
   - 매칭 키: ① raw 파일명·경로 → `_ops/log.md`의 `Source: raw/...` 라인과 비교 ② raw frontmatter의 `source:` URL → wiki/sources/ 페이지의 `source_url`과 비교
   - 각 후보는 *한 줄 요약* + *우선순위 추정*(작성일·도메인 신뢰도·기존 위키 인용 빈도) 부착
   - 사용자에게 "이번 주 미처리 N건. ingest 진행할 항목 골라주세요" 형식으로 제안. 자동 ingest 금지 — 강조점 확인 단계(INGEST 절차 2번) 보존
   - **목적**: 4번이 *위키 내부 갭 → 외부 탐색 권유*인 반면 6번은 *이미 손에 있는 자료의 처리 큐*. 두 흐름을 매주 한 알림으로 묶어 누락·정체 방지
7. **진행 예정 분기 검토 알림** (분기 첫째 주 LINT에서만): "`_ops/status.md`의 `## 진행 예정` 섹션 검토 시점입니다. 단기 항목 중 완료된 것 / 중기로 승격할 것 / 새 우선순위 있나요?"라고 사용자에게 안내
   - 자동 수정 금지. 사용자 OK 받고 그 자리에서 함께 편집
   - 분기 식별: LINT 실행일이 1월·4월·7월·10월의 1~7일 사이면 분기 첫째 주로 판단
   - 사용자가 *"이번 분기는 패스"*라고 하면 다음 분기까지 알림 없음
8. **유예된 배포 일괄 처리 (마지막 단계)** — 지난 주 ingest들이 커밋·push·재색인을 이 단계로 넘겨 놨다 (INGEST 절차 9번)

   순서를 지킬 것 — **빌드 검사 → 커밋 → push**. 빌드가 깨진 상태로 push하면 사이트 전체가 배포되지 않는다. (챗봇 재색인은 2026-09-03 중단 — 아래)

   1. **0단계 빌드 검사 결과 확인** — 통과 못 했으면 여기서 멈추고 먼저 고친다
   2. **누적분 보고**: `git status --short` + `git log --oneline -1` 기준으로 *직전 push 이후 쌓인 변경*을 정리해 보여준다. `_ops/log.md`의 미push ingest 항목 목록 + `wiki/changelog.md` 주간 블록 갱신 여부도 함께
   3. **커밋·push는 사용자 확인 후** — 방침은 "LINT에서 처리"이지만 push 자체는 여전히 승인 대상이다. 커밋 메시지는 누적 ingest 주제를 묶어 작성. `_ops/`도 같은 my-wiki repo라 함께 커밋된다(단 사이트엔 미발행)
   4. **챗봇 재색인은 중단** (2026-09-03 delist) — 평시 LINT에서 실행하지 않는다. 복구 시에만 아래 "챗봇 delist·복구" 절차대로 재개
   5. **deck 신규·수정이 있었으면** 단독 배포본 재생성 여부를 묻는다 (`python embed_standalone.py` → gitignore된 `dist/`)

   - 누적분이 없으면 *"이번 주 미push 변경 없음"*으로 한 줄 보고하고 넘어간다
   - Quartz repo(`C:\Users\bmjlee\quartz`) 변경은 **별도 push 사이클**임을 잊지 말 것

### 챗봇 delist·복구 (2026-09-03)

챗봇은 테스트 목적 개발이라 실사용 계획이 없어 **2026-09-03 사이트에서 내림**. 코드(`chatbot/`)와 HF Space 배포본은 그대로 유지 — 삭제하지 않았고 언제든 복구 가능.

- **내린 것**: ① Quartz `WikiNav.tsx`의 "AI 챗봇" 링크 블록(주석 처리) ② 리더용 소개 페이지의 챗봇 소개(→ `_ops/status.md`로 이동) ③ 주간 재색인 중단
- **그대로인 것**: `chatbot/` 전체 코드, HF Space(`https://huggingface.co/spaces/ginzadaddy/ginza-wiki-chat`) 배포본, `index/` 마지막 색인
- **복구 절차**:
  1. Quartz `quartz/components/WikiNav.tsx`의 챗봇 블록·`chatUrl` 주석 해제 → quartz repo 커밋·push (별도 사이클)
  2. `_ops/status.md`의 챗봇 소개를 발행 페이지(about 또는 전용 페이지)로 복귀
  3. 재색인 재개: `cd chatbot && ./.venv/Scripts/python.exe update_and_deploy.py` (**글로벌 `python` 금지**). 이때 `iter_wiki_pages` 제외 목록에 `changelog.md` 추가 확인
  4. 검증: `index/meta.json` 슬러그 집합 확인. `chatbot/chroma_db/`는 죽은 잔재이므로 보지 말 것

## 작업 4: DECISION (본인 결정·가설 검증 기록)

본인의 의사결정 또는 가설 검증을 wiki에 누적해서 시간이 지나며 자기 archive를 쌓는 작업.

### 트리거
- 사용자가 "decision으로 기록", "결정 기록", "가설 검증" 등 명시 또는
- 사용자가 결정/가설 텍스트를 자유 채팅으로 전달 + Claude Code(또는 Cowork)이 decision 기록 여부 확인
- raw/decisions/ 에 사용자가 직접 파일 추가한 후 "ingest decision" 명령

### 절차
1. 사용자 텍스트에서 type 판단 — `decision`(결정) 또는 `hypothesis`(가설 검증)
2. 적절한 템플릿 복사하여 raw/decisions/ 에 새 파일 생성
   - decision: `raw/decisions/_template.md` 참고
   - hypothesis: `raw/decisions/_template-hypothesis.md` 참고
   - 파일명: `YYYY-MM-DD-짧은-슬러그.md`
3. 사용자 텍스트를 템플릿 필드에 분배 정리
4. related_wiki 필드에 근거가 된 concept/entity wikilink 명시
5. wiki/decisions/ 에 대응 페이지 생성
   - frontmatter type: `decision` 또는 `hypothesis`
   - related_wiki의 각 페이지에 본 decision 페이지를 related로 추가 (양방향 링크)
6. _ops/log.md 기록 추가
7. wiki/decisions/all.md 카탈로그 페이지에도 행 추가 (없으면 생성)
   - 형식: `| [[YYYY-MM-DD-slug]] | **주제** — 한 줄 요약 | YYYY-MM-DD |`

### 단축 트리거 (자유 채팅)
- 사용자가 "방금 X에 대해 Y로 결정했어, 이유는 Z..." 또는
  "내 가설은 X야, 검증해줘"처럼 입력하면
  Claude Code(또는 Cowork)이 type 판단 후 raw/decisions/ 에 임시 정리 → 사용자 확인 → ingest 진행

### related_wiki 양방향 링크 동작
- decision/hypothesis 페이지에서 [[concept-slug]]를 related_wiki에 명시
- 동시에 그 concept 페이지의 frontmatter `related` 배열에도 본 decision 페이지를 추가
- 결과: concept 페이지를 볼 때 "어떤 본인 결정에 이 개념이 인용됐는지" 추적 가능

### 결정 후 사후 갱신
- 결정/가설 페이지의 `## 결과 (사후 갱신)` 또는 `## 사후 검증` 섹션은 비워 둠
- 시간(예: 3·6·12개월) 지난 후 사용자가 결과 update → wiki에서 직접 편집
- LINT 작업 시 N개월 이상 사후 갱신 안 된 decision 페이지를 리마인드

## 작업 5: SOURCE RADAR (주간 외부 소스 스캔)

> **자동 실행**: `source radar`라는 Claude Code 스케줄 루틴으로 **매주 자동 실행**됨 (LINT와 별개 독립 루틴, 2026-06-23 신설). 웹 의존 작업이라 Claude Code에서만 동작. 수동으로 "소스 스캔"/"source radar" 요청 시에도 동일 절차.

지정된 외부 소스 사이트들을 주기적으로 스캔해 *ingest할 가치가 있는 신규 아티클*을 발굴·보고하는 작업. **후보 제안만** — 자동 ingest·자동 페이지 생성·push 전부 금지.

### 대상 소스 (신뢰도 티어)
| 사이트 | 티어 | URL |
|---|---|---|
| Chris Zukowski (How To Market A Game) | ⭐ 최상 (1차·데이터) | https://howtomarketagame.com/blog/ |
| Simon Carless (GameDiscoverCo) | ⭐ 최상 (1차·데이터) | https://newsletter.gamediscover.co/archive |
| Alinea Analytics | ⭐ 최상 (1차·데이터·Steam 매출) | https://alineaanalytics.substack.com/archive |
| Naavik (Digest) | 상 (심층 분석·케이스) | https://naavik.co/digest/ |
| Game Developer | ⭐ 최상 (개발 craft·편집) | https://www.gamedeveloper.com/latest |
| GamesIndustry.biz | 상 (게임산업 업계 뉴스) | https://www.gamesindustry.biz/ |
| 80 Level | 중상 (아트·기술 파이프라인) | https://80.lv/articles/ |
| Game Dev Report | 중상 (2차·애그리게이터) | https://gamedevreport.beehiiv.com/ |
| Big Games Machine (content hub) | 중 (PR 에이전시 listicle) | https://www.biggamesmachine.com/content-hub/page/1/ |

소스 추가·삭제는 사용자 요청 시에만. 선제 확장 금지.

### 절차
1. 각 사이트 인덱스/아카이브 fetch → **최근 7일 발행** 항목만 추림 (날짜 윈도우 방식 — 별도 상태 파일 없음)
2. 각 항목 URL을 `wiki/sources/`의 `source_url` 필드와 대조 → 이미 ingest된 건 제외
3. 신규 후보마다 본문 fetch 후 **ingest 가치 판정**:
   - **기존 위키 중복도**: 같은 주제 concept/source가 이미 있나? (`wiki/index.md`·`concepts/all.md`·`sources/all.md` 대조) — 중복 높으면 가치 낮음
   - **출처 티어**: 위 표 기준. 같은 내용이면 1차·데이터 소스 우선, PR listicle은 후순위
   - **신규성**: 위키에 없는 데이터·사례·관점이 있나
4. **"이번 주 신규 N건, ingest 후보 M건"** 형식으로 우선순위 정렬 보고. 각 후보에 *URL·한 줄 요약·티어·중복도 판정·신규 포인트* 부착
5. fetch 실패(403·페이월 등)는 건너뛰되 *"N건 fetch 실패"*로 명시 (silent drop 금지)

### 가드레일 (LINT와 동일)
- **자동 ingest 금지** — 사용자가 후보 골라 INGEST 절차로 별도 진행 (강조점 확인 단계 보존)
- **새 페이지 자동 생성 금지 · push 금지 · raw/ 자동 적재 금지** — 보고만
- 보고는 채팅으로. 위키 파일 변경 없음 (이 루틴은 read-only 탐색)

### 결과 보고 형식
1. 주간 스캔 요약 (사이트별 신규 N건 / 총 후보 M건 / fetch 실패 N건)
2. ingest 추천 후보 (우선순위순) — URL·한 줄 요약·티어·"왜 추천"(신규 데이터·관점)
3. 스킵 권장 항목 — URL·한 줄 + 스킵 사유(기존 위키 중복 등)

## 세션 시작 체크리스트
1. _ops/log.md 최근 5개 항목 읽기 (+ 필요 시 _ops/status.md 운영 현황)
2. wiki/overview.md 읽기
3. 메모리 인덱스(MEMORY.md) 확인 — Ginza 프로필·워크플로우 선호 등 보조 컨텍스트
4. 사용자에게 현재 상태 보고

## 글쓰기 원칙
- [[wikilink]] 형식으로 교차 참조
- "> 💡 **핵심 인사이트:**" 블록으로 중요 내용 강조
- "> ⚠️ 모순:" 블록으로 충돌 표시
- 개념 페이지: 300~800자
- 소스 요약: 150~400자

## wikilink 작성 규칙

### 기본 형식
- 본문: `[[영문-슬러그|표시명]]` (예: `[[astro-bot|아스트로봇]]`, `[[sucker-punch|Sucker Punch]]`)
- 테이블 헤더·셀: `[[slug]]` 형식만 (표시명 없이) — Quartz가 테이블 파싱 전에 wikilink를 처리하지 않아 `|`가 셀 구분자로 인식돼 깨짐. 해당 slug의 entity/concept 페이지가 없으면 plain text
- `[[한글]]` 단독 형식 금지

### 부연 설명 형식
**원칙**: 부연은 ` — ` (em-dash + 좌우 공백 한 칸) 구분자만 사용. 괄호 `(...)` 형식 금지.

위치별 적용:
- **본문 wikilink**: `[[slug|라벨 — 부연]]` (예: `[[mda-framework|MDA 프레임워크 — 메카닉→다이나믹→에스테틱]]`)
- **all.md 테이블 "설명" 컬럼**: `**라벨** — 부연` — 라벨 굵게, 부연 없으면 `**라벨**`만 (예: `**마케팅 전략** — 스팀·통합 채널·트레일러·PR·크리에이터`)
- **index.md pill-grid**: `- [[slug|라벨 — 부연]]` — concepts/all·comparisons/all 카탈로그의 부연과 동일하게 (단일 소스 유지)

페이지 frontmatter title은 부연 없는 짧은 라벨로 유지 (단, 한·영 병기 같이 제목 일부인 경우는 예외).

### pill-grid 구조
`<div class="pill-grid">` 안에 wikilink 리스트. **div 직후·`</div>` 직전 빈 줄 필수** (마크다운 리스트가 파싱되도록). hover 시 부연이 inline으로 노출됨 — 구현 세부는 quartz의 `pill-grid.inline.ts` 참조.

예시:
```
<div class="pill-grid">

- [[rapid-prototyping|빠른 프로토타이핑]]
- [[soulslike|소울라이크]]

</div>
```

### 함정 회피
**wikilink 바로 뒤에 괄호 `(...)` 붙이지 말 것** — 사이에 공백 한 칸 필수. `[[slug|표시명]](괄호)` 패턴은 Quartz가 표준 마크다운 링크 `[text](url)`로 오인 → 404
- 잘못: `[[team-asobi|팀 아소비]](65명)` ✗
- 올바름: `[[team-asobi|팀 아소비]] (65명)` ✓

**wikilink alias(표시 라벨)에 슬래시 `/` 넣지 말 것** — Quartz prettyLinks가 내부 링크 텍스트에 `path.basename()`을 적용해서 *마지막 `/` 이전을 전부 잘라냄*. 라벨이 부제 잔여물로 노출됨. index.md pill·테이블·본문 인라인 wikilink 전부 해당 (frontmatter `related` alias 포함). `/` 대신 `·`(열거)·`:`(비율) 사용
- 잘못: `[[player-retention|플레이어 리텐션 — D1/D7/D30·DAU/MAU stickiness]]` → 화면엔 `MAU stickiness`만 표시 ✗
- 올바름: `[[player-retention|플레이어 리텐션 — D1·D7·D30·DAU·MAU stickiness]]` ✓
- 비율: `90/10 도구화` → `90:10 도구화` ✓
- `[[slug]]`(alias 없음) 형식이나 plain 테이블 텍스트(`**라벨** — …/…`)는 영향 없음 — 링크 *표시 텍스트*에 `/`가 있을 때만 발생

# LLM Wiki — 운영 지침

당신은 이 개인 지식 위키의 관리자입니다.
매 세션 시작 시 이 파일을 먼저 읽으세요.

## 운영 환경
- 사용자: Ginza, 게임 개발자, Windows 환경
- 작업 도구: **Claude Code (데스크톱 앱 또는 CLI) 우선** — 파일·터미널 작업에 가장 적합. Read/Write/Edit/Bash/Grep/Glob 등 풀 toolset으로 위키 파일·셸 명령 직접 조작. Cowork 모드(Claude 데스크톱 앱 자유 채팅)도 병용 가능하나, 파일 작업은 Claude Code가 더 매끄러움이 실사용으로 확인됨. Bash/PowerShell도 GUI/앱 인터페이스로 제한하지 않고 자유롭게 활용. 단 destructive·hard-to-reverse 작업(rm -rf, git push --force, DB drop 등)은 사용자 확인 후 실행
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
- wiki/log.md    → 활동 기록. append-only
- wiki/presentations/   → HTML 슬라이드 + wrapper md 페이지. 슬라이드 생성 시 *반드시 이 경로*에 저장. (루트의 `presentations/` 폴더는 deprecated — 절대 사용 금지)
  - **슬라이드는 위키 콘텐츠를 *재구성*한 것** — 원전(concept·source) 페이지가 항상 truth source. 위키 콘텐츠 변경 시 슬라이드도 동기화. 슬라이드 갱신은 HTML 파일만 교체, wrapper md·카탈로그 wikilink·sources frontmatter는 그대로 유지.
  - **파일 명명: 슬라이드 `[주제-슬러그]-deck.html`, wrapper `[주제-슬러그].md`** (base 슬러그는 공유, 슬라이드만 `-deck` 접미사)
  - `-deck` 접미사 필수 이유: wrapper md와 슬라이드 HTML이 같은 base 이름이면 Quartz의 ContentPage·Assets emitter가 같은 slug로 인식해 *.html URL이 wrapper md를 응답하는 무한 재귀 발생*. `-deck`으로 분리해서 slug 충돌 회피
  - Quartz Assets emitter가 `.html`을 자동으로 `public/presentations/`에 복사 → 별도 deploy step 불필요 (단 `quartz.config.ts` ignorePatterns에 `**/*.html`이 있어야 함 — Assets의 slugify가 .html 확장자 제거하는 버그 회피. deploy.yml에서 별도 copy step으로 정확한 path에 복사)
  - 신규 슬라이드 추가 시: `-deck.html` 업로드 + wrapper `[슬러그].md` 작성 + `wiki/presentations/all.md` 카탈로그에 행 추가 + `wiki/index.md` 카운트·프레젠테이션 섹션 갱신
  - 카탈로그·index의 슬라이드 link 규칙:
    - **슬라이드 HTML link**: raw HTML + 완전 절대 URL (`<a href="https://ginzadaddy-png.github.io/quartz/presentations/[슬러그]-deck.html" target="_blank" rel="noopener">전체 화면 열기 ↗</a>`) — Quartz가 root-relative path는 변형(`.html` 제거·baseUrl 처리)하지만 외부 절대 URL은 외부 link로 인식해 그대로 둠. markdown link도 같은 이유로 회피
    - **wrapper md link**: wikilink 사용 (`[[presentations/[슬러그]|표시명]]`) — Quartz의 popover·backlinks 자동 활성. 단 *index pill·본문*에서만 가능. 테이블 안에서는 `|` 충돌로 raw HTML 사용 (`<a href="https://ginzadaddy-png.github.io/quartz/presentations/[슬러그]">[슬러그]</a>`)
    - **wrapper md raw HTML link**: trailing slash 없이 (`https://ginzadaddy-png.github.io/quartz/presentations/[슬러그]` ✓ / `.../[슬러그]/` ✗) — Quartz가 .md를 단일 `slug.html`로 빌드해서 trailing slash URL은 폴더 매칭 시도 → 404
  - **슬라이드 폰트: Pretendard 전용, JetBrains Mono 금지** — make-slide skill 호출 시 prompt 명시, 기존 HTML 갱신 시 grep 검수 (메모리 `feedback_slide_fonts.md` 참조)
  - **카탈로그 페이지(`all.md`)는 사용자에게 노출되는 카탈로그 역할만** — 운영 규칙·내부 지침은 *반드시 CLAUDE.md 또는 메모리에만 기록*. 사용자가 사이트에서 보는 카탈로그에는 슬라이드 목록 + 짧은 인트로만
  - **wrapper md는 결과물 노출에 집중 — "갱신 메모"·"변경 이력" 섹션 작성 금지**. 작업 내역·버전 기록은 *이미 `wiki/log.md`에서 추적*되므로 wrapper md에 중복 기록 불필요. wrapper md는 *제목·요약·iframe·구조·sources·관련 위키 페이지*만으로 구성해 사용자가 *결과물 자체*에 집중하도록 유지. 갱신 이력 추적이 필요하면 log.md 또는 git history 사용.

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
8. wiki/log.md에 기록 추가

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
"lint" 또는 "점검"이라고 하면:
1. 모순 있는 페이지 찾기
2. 링크 없는 고립 페이지 찾기
3. 3번 이상 언급됐지만 페이지 없는 개념 찾기
4. 다음 조사 주제 제안하기
5. wiki/overview.md 자동 업데이트 (아래 두 섹션만, 나머지는 수동 유지):
   - **현재 커버리지**: entities/ 페이지 기준으로 스튜디오·게임 목록 갱신
   - **핵심 테마**: concepts/ 전체에서 3회 이상 등장하는 공통 패턴 재추출 후 갱신
6. **raw/ 폴더 미처리 큐 식별**: raw/ 하위의 모든 파일 중 `wiki/sources/` 또는 `wiki/log.md`에 매칭되는 ingest 기록이 없는 항목을 추려 후보로 보고
   - 매칭 키: ① raw 파일명·경로 → log.md의 `Source: raw/...` 라인과 비교 ② raw frontmatter의 `source:` URL → wiki/sources/ 페이지의 `source_url`과 비교
   - 각 후보는 *한 줄 요약* + *우선순위 추정*(작성일·도메인 신뢰도·기존 위키 인용 빈도) 부착
   - 사용자에게 "이번 주 미처리 N건. ingest 진행할 항목 골라주세요" 형식으로 제안. 자동 ingest 금지 — 강조점 확인 단계(INGEST 절차 2번) 보존
   - **목적**: 4번이 *위키 내부 갭 → 외부 탐색 권유*인 반면 6번은 *이미 손에 있는 자료의 처리 큐*. 두 흐름을 매주 한 알림으로 묶어 누락·정체 방지

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
6. wiki/log.md 기록 추가
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

## 세션 시작 체크리스트
1. wiki/log.md 최근 5개 항목 읽기
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

# LLM Wiki — 운영 지침

당신은 이 개인 지식 위키의 관리자입니다.
매 세션 시작 시 이 파일을 먼저 읽으세요.

## 운영 환경
- 사용자: 범준(Ginza) — Nexon Games 게임 개발자, Windows 환경
- 작업 도구: Cowork 모드(Claude 데스크톱 앱) — Read/Write/Edit/Bash 도구로 위키 파일 직접 작업 가능
- vault 위치: `C:\Vault\Ginza\my-wiki` (이 폴더). GitHub 비공개 repo에 sync되어 cross-device 작업
- Quartz 사이트: `C:\Users\bmjlee\quartz`에서 별도 빌드 → GitHub Pages 배포
  - Quartz 컴포넌트/스타일/스크립트 변경은 별도 repo, 별도 push 필요 (my-wiki push 워크플로우와 분리)
  - 변경 후 push 전 mount 무결성(`wc -l`/`tail`) + 로컬 `npx quartz build` 파싱 단계 통과 확인 필수
  - CSS layout·stacking 속성(`position`/`z-index`/`contain`/`overflow`/`display`)은 한 commit당 하나만 변경, 사용자 확인 후 다음 단계
- 대화 언어: 한국어 위주, 영문 슬러그/용어는 그대로 사용
- 솔루션 제안 원칙: 터미널/CLI 대신 GUI·앱 인터페이스 한정, 또는 Cowork이 직접 실행하는 형태로

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
  - **슬라이드 폰트 — JetBrains Mono 절대 금지**, 한글 적합 폰트(Pretendard 등) 사용. make-slide skill·기타 슬라이드 도구 호출 시 prompt에 명시. 기존 슬라이드 HTML 갱신 시도 JetBrains Mono import·font-family 발견하면 즉시 Pretendard로 교체 (메모리 `feedback_slide_fonts.md` 참조)
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

## 작업 1: INGEST
"ingest [파일명]"이라고 하면:
1. raw/ 소스 파일 읽기 — frontmatter에서 `source:`(원문 URL)·`author:`·`published:` 필드 추출
2. 핵심 내용 3~7개 요약해서 나에게 보여주기
3. 강조할 점 있는지 확인
4. wiki/sources/에 요약 페이지 생성 — **원문 출처 정보 반드시 보존** (아래 형식)
   - frontmatter에 `source_url`·`source_author`·`source_published` 필드 추가 (raw에서 추출한 값. 없으면 빈 문자열 또는 생략)
   - 본문 첫 줄에 `**원문**: [짧은 라벨 또는 도메인](URL)` 형태로 명시 (사용자 클릭 가능). URL 없는 케이스(PDF·내부 자료)는 `**원문**: N/A (저자·발행처·발행일만 명시)` 형태로
5. 관련 concept, entity 페이지 생성 또는 업데이트
6. 기존 위키 내용과 모순되면 "> ⚠️ 모순:" 블록 추가
7. wiki/index.md 업데이트:
   - 상단 `Last updated` 날짜를 오늘 날짜(YYYY-MM-DD)로 갱신
   - 상단 통계 행의 소스·스튜디오·게임·개념·비교 숫자 갱신
   - 새 concept/comparison 페이지가 생겼으면 해당 섹션의 `<div class="pill-grid">` 리스트에 항목 추가
   - 형식: `- [[slug|짧은 라벨 — 부연 설명]]` (부연 설명은 concepts/all 등 카탈로그의 부연과 동일 사용)
   - 기본 표시는 짧은 라벨만, hover 시 부연이 inline으로 노출됨 (pill-grid.inline.ts가 ' — ' 기준 split)
8. wiki/log.md에 기록 추가

로그 형식:
## [YYYY-MM-DD] ingest | [제목]
- Source: raw/[경로]
- 생성: [새 페이지 목록]
- 업데이트: [수정된 페이지 목록]

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

## 작업 4: DECISION (본인 결정·가설 검증 기록)

본인의 의사결정 또는 가설 검증을 wiki에 누적해서 시간이 지나며 자기 archive를 쌓는 작업.

### 트리거
- 사용자가 "decision으로 기록", "결정 기록", "가설 검증" 등 명시 또는
- 사용자가 결정/가설 텍스트를 자유 채팅으로 전달 + Cowork이 decision 기록 여부 확인
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

### 단축 트리거 (Cowork 자유 채팅)
- 사용자가 "방금 X에 대해 Y로 결정했어, 이유는 Z..." 또는
  "내 가설은 X야, 검증해줘"처럼 입력하면
  Cowork이 type 판단 후 raw/decisions/ 에 임시 정리 → 사용자 확인 → ingest 진행

### related_wiki 양방향 링크 동작
- decision/hypothesis 페이지에서 [[concept-slug]]를 related_wiki에 명시
- 동시에 그 concept 페이지의 frontmatter `related` 배열에도 본 decision 페이지를 추가
- 결과: concept 페이지를 볼 때 "어떤 본인 결정에 이 개념이 인용됐는지" 추적 가능

### 결정 후 사후 갱신
- 결정/가설 페이지의 `## 결과 (사후 갱신)` 또는 `## 사후 검증` 섹션은 비워 둠
- 시간(예: 3·6·12개월) 지난 후 사용자가 결과 update → wiki에서 직접 편집
- LINT 작업 시 N개월 이상 사후 갱신 안 된 decision 페이지를 리마인드

## 세션 시작 체크리스트
1. CLAUDE.md 읽기 ✓
2. wiki/log.md 최근 5개 항목 읽기
3. wiki/overview.md 읽기
4. 메모리 인덱스(MEMORY.md) 확인 — Ginza 프로필·워크플로우 선호 등 보조 컨텍스트
5. 사용자에게 현재 상태 보고

## 글쓰기 원칙
- [[wikilink]] 형식으로 교차 참조
- "> 💡 **핵심 인사이트:**" 블록으로 중요 내용 강조
- "> ⚠️ 모순:" 블록으로 충돌 표시
- 개념 페이지: 300~800자
- 소스 요약: 150~400자

## 대량 ingest 규칙

### 트랜스크립트 파일 처리
- 전체를 읽지 말 것 (토큰 낭비)
- 앞 3000자 + 중간 1000자 샘플링으로 핵심 파악
- 상세 내용보다 핵심 인사이트 중심으로 정리

### 대량 ingest 방식
- 한 번에 전체를 처리하지 말 것
- 3개씩 배치로 나눠서 처리
- 중간 확인 없이 바로 진행
- 각 배치 완료 후 간단한 진행 상황만 보고

### 파일 읽기 원칙
- 긴 파일(5000자 이상)은 앞부분만 읽고 판단
- 전체 내용이 필요한 경우에만 추가로 읽기
- 불필요한 확인 요청 금지

## index.md 업데이트 규칙
- 소스 섹션은 최신 10개만 표시
- 전체 목록은 wiki/sources/all.md에 관리
- ingest 후 index.md 상위 10개 갱신 + all.md에 전체 행 추가

## wikilink 작성 규칙
- 항상 [[영문-슬러그|표시명]] 형식 사용
- 예: [[astro-bot|아스트로봇]], [[sucker-punch|Sucker Punch]]
- 한글만 단독으로 쓰는 [[한글]] 형식 금지
- **테이블(헤더·셀 모두)에서는 [[slug]] 형식만 사용** (표시명 없이 슬러그만)
  - 이유: Quartz가 테이블 파싱 전에 wikilink를 처리하지 않아 [[slug|표시명]]의 | 가 셀 구분자로 인식돼 테이블이 깨짐
  - 본문 텍스트: [[astro-bot|아스트로봇]] ✓
  - 테이블 헤더·셀: [[astro-bot]] ✓ / [[astro-bot|아스트로봇]] ✗
  - 해당 slug의 entity/concept 페이지가 있으면 wikilink, 없으면 plain text
- **부연 설명이 필요할 땐 ` — ` (em-dash + 좌우 공백 한 칸) 구분자만 사용** — 괄호 ` (...)` 형식 금지
  - 적용 위치: concepts/comparisons 페이지 안의 wikilink 리스트 등 본문 영역
  - 예: `[[mda-framework|MDA 프레임워크 — 메카닉→다이나믹→에스테틱]]` ✓
  - 금지: `[[mda-framework|MDA 프레임워크 (메카닉→다이나믹→에스테틱)]]` ✗
  - index.md pill-grid에는 부연 설명 자체를 붙이지 않음 (아래 규칙 참고)
  - 페이지 frontmatter title도 부연 설명 없는 짧은 라벨로 유지 (단, 한·영 병기 같이 제목 자체의 일부인 경우는 예외)
- **all.md 카탈로그 페이지(concepts/all, comparisons/all) 테이블의 "설명" 컬럼은 `**짧은 라벨** — 부연 설명` 형식으로 통일**
  - 라벨은 굵게(**), 구분자는 ` — `(em-dash + 좌우 공백 한 칸)
  - 부연이 없는 항목은 `**라벨**`만 (구분자·부연 없이)
  - 괄호 ` (...)` 형식은 부연 설명에 사용 금지
  - 예: `| [[marketing-strategy]] | **마케팅 전략** — 스팀·통합 채널·트레일러·PR·크리에이터 |` ✓
  - 금지: `| [[marketing-strategy]] | 마케팅 전략 (스팀·통합 채널…) |` ✗
- **pill-grid 리스트는 [[slug|짧은 라벨 — 부연 설명]] 형식** (index.md 카탈로그 전용)
  - 형식: `<div class="pill-grid">` 안에 `- [[slug|짧은 라벨 — 부연 설명]]` 리스트
  - 부연 설명은 concepts/all·comparisons/all 카탈로그의 부연과 동일하게 작성 (단일 소스 유지)
  - 동작:
    - 기본 표시: 라벨만 (CSS에서 .pill-detail 숨김)
    - hover 시: .pill-detail이 inline으로 노출 + a max-width 280→520 확장
    - 별도 absolute layer 사용 안 함 → 위치 이격 없음
    - 옆 li를 밀어내는 형태로 layout 변화 (transition으로 부드럽게)
  - 구현: `pill-grid.inline.ts`가 ' — ' 기준 split → `.pill-label`·`.pill-detail` span으로 감싸고 `has-detail` 클래스 부여
  - 예시:
    ```
    <div class="pill-grid">

    - [[rapid-prototyping|빠른 프로토타이핑]]
    - [[soulslike|소울라이크]]

    </div>
    ```
  - 빈 줄(div 직후, /div 직전) 필수 — 마크다운 리스트가 파싱되도록
- **wikilink 바로 뒤에 괄호 `(...)` 붙이지 말 것** — 사이에 공백 한 칸 필수
  - 이유: `[[slug|표시명]](괄호)` 패턴은 Quartz가 표준 마크다운 링크 `[text](url)`로 오인 → wikilink 파싱 실패, 404 발생
  - 잘못된 예: `[[team-asobi|팀 아소비]](65명)` ✗
  - 올바른 예: `[[team-asobi|팀 아소비]] (65명)` ✓

## INGEST 전처리 규칙
raw/ 파일 읽은 후, 아래 패턴은 무시하고 처리:
- "관련 기사", "더 보기", "광고" 섹션
- 100자 미만 단락 (네비게이션 잔여물)
- URL만 있는 줄
- "Share", "Subscribe", "Newsletter" 등 CTA 텍스트
- 
raw/ 파일 읽을 때 아래 줄/섹션은 읽지 말고 건너뛸 것:
- `![](` 로 시작하는 줄 (이미지)
- `▲` 로 시작하는 줄 (이미지 캡션)
- `TAGS:` 이후 모든 내용
- RSS/URL/이메일 주소 줄 (맨 앞 3줄)
- 댓글 섹션 (`#### 댓글` 이후)
- 관련뉴스 표 (`## 인벤 주요 뉴스` 이후)

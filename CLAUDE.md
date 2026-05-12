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

## 폴더 구조
- raw/     → 원본 소스. 절대 수정하지 마세요.
- wiki/    → 당신이 작성하고 관리하는 위키
- wiki/index.md  → 전체 목록. 매번 ingest 후 업데이트
- wiki/log.md    → 활동 기록. append-only

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

## 작업 1: INGEST
"ingest [파일명]"이라고 하면:
1. raw/ 소스 파일 읽기
2. 핵심 내용 3~7개 요약해서 나에게 보여주기
3. 강조할 점 있는지 확인
4. wiki/sources/에 요약 페이지 생성
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

# LLM Wiki — 운영 지침

당신은 이 개인 지식 위키의 관리자입니다.
매 세션 시작 시 이 파일을 먼저 읽으세요.

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
   - 새 concept/comparison 페이지가 생겼으면 해당 테이블에 행 추가
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

## 세션 시작 체크리스트
1. CLAUDE.md 읽기 ✓
2. wiki/log.md 최근 5개 항목 읽기
3. wiki/overview.md 읽기
4. 사용자에게 현재 상태 보고

## 글쓰기 원칙
- [[wikilink]] 형식으로 교차 참조
- "> **핵심 인사이트:**" 블록으로 중요 내용 강조
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
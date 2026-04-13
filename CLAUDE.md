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
7. wiki/index.md 업데이트
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
# Phase 4 배포 — Hugging Face Spaces

로컬 BGE-M3를 그대로 쓰면서 무료 배포. HF Spaces는 16GB RAM이라 BGE-M3(2.3GB) 구동 가능.

## 왜 HF Spaces

- Streamlit Cloud 무료 티어는 RAM ~1GB → BGE-M3 못 올림
- HF Spaces 무료(CPU basic)는 16GB RAM → BGE-M3 구동 OK
- 검색 품질·한국어·데이터 보존(로컬 모델) 전부 유지

## 배포 번들 (HF Space repo에 올릴 것)

```
ginza-wiki-chat/            ← HF Space repo
├── app.py                  ← chatbot/app.py
├── core/                   ← chatbot/core/ 전체
├── requirements.txt        ← chatbot/requirements.txt
├── chroma_db/              ← chatbot/chroma_db/ (색인, 그대로 복사 → 재임베딩 불필요)
├── wiki/                   ← my-wiki/wiki/ (graph가 relations 파싱에 필요. .md만)
└── README.md               ← HF Space 메타(아래 frontmatter 필수)
```

> **chroma_db 포함 이유**: 안 올리면 Space 첫 실행 때 1409청크 재임베딩(수 분 + 매 재시작). 색인을 함께 올리면 모델은 *쿼리 임베딩*만 로드.
> **wiki/ 포함 이유**: graph.py가 entities/*.md의 relations를 런타임 파싱. (RAG는 chroma 텍스트만 써서 wiki 불필요하지만 graph가 필요)

## 사전 준비 (사용자 액션)

1. **HF 계정**: huggingface.co 가입 (개인 계정)
2. **Access Token**: Settings → Access Tokens → New token (write 권한) → 복사
3. **Space 생성**: huggingface.co/new-space
   - SDK: **Streamlit**
   - Hardware: **CPU basic (무료)**
   - Visibility: **Private** (본인만 접근 = 가장 간단한 인증)

## 배포 절차 (Claude Code가 대행 가능)

토큰 받으면 Claude Code가 아래를 자동 실행:

1. 배포 번들 디렉터리 조립 (`chatbot/` + `chroma_db/` + `wiki/` + Space용 README)
2. HF Space repo clone → 번들 복사 → commit → push
3. **Secret 등록**: Space Settings → Variables and secrets → `ANTHROPIC_API_KEY` 추가
   (코드는 이미 `os.getenv` + `.env`/Space secret 양쪽 호환)

## README.md frontmatter (Space 메타, 필수)

```yaml
---
title: Ginza Wiki Chat
emoji: 💬
colorFrom: indigo
colorTo: blue
sdk: streamlit
sdk_version: 1.57.0
app_file: app.py
pinned: false
---
```

## VAULT_PATH 처리

Space 환경에선 vault가 repo 내부에 있으므로 app.py의 기본 경로를 상대 경로로:
- Space secret 또는 환경변수 `VAULT_PATH=./` (wiki/가 repo 루트에 있을 때)
- 배포 시 app.py 기본값을 `Path(__file__).parent`로 자동 fallback하도록 조정 예정

## 알려진 제약

- **첫 콜드 스타트**: BGE-M3 모델 다운로드(~2.3GB) + 로드로 1~2분. 이후 캐시
- **슬립**: 무료 Space는 미사용 시 슬립 → 재접속 시 콜드 스타트 다시
- **chroma_db 갱신**: 위키 ingest 후 `build_index.py` 재실행 → chroma_db를 Space repo에 다시 push (Phase 2 갱신 워크플로우의 배포 연장)

## 인증

Private Space면 HF 로그인한 본인만 접근 → 별도 password gate 불필요. 공개로 바꾸면 `streamlit-authenticator` 추가 검토.

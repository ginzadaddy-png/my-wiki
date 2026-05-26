# Ginza Wiki Chatbot

Hybrid Agent 챗봇 — Phase 1 MVP (로컬 Streamlit + 키워드 검색 + Claude API).

로드맵: `C:\Users\bmjlee\Downloads\chatbot-roadmap-v2.md`

## 구조

```
chatbot/
├── core/                # 백엔드 로직 (UI 의존 없음)
│   ├── wiki_loader.py   # vault 페이지 읽기·frontmatter 파싱
│   ├── search.py        # 키워드 검색 (Phase 1)
│   └── agent.py         # Claude API 호출 + 컨텍스트 조립
├── app.py               # Streamlit UI
├── requirements.txt
├── .env.example
└── README.md
```

## 셋업 (한 번만)

```powershell
cd C:\Vault\Ginza\my-wiki\chatbot
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
# .env 열어서 ANTHROPIC_API_KEY 입력
```

## 실행

```powershell
cd C:\Vault\Ginza\my-wiki\chatbot
.\.venv\Scripts\Activate.ps1
streamlit run app.py
```

브라우저 자동 오픈 → `http://localhost:8501`

## API 키 발급

1. https://console.anthropic.com 가입·로그인
2. Settings → API Keys → "Create Key"
3. 생성된 `sk-ant-...` 키를 `.env`의 `ANTHROPIC_API_KEY=` 뒤에 붙여넣기
4. 결제 수단 등록 (Phase 1 dev 사용량은 월 $5 미만 예상 — Sonnet 기준)

## 모델 선택

`.env`의 `ANTHROPIC_MODEL` 값:
- `claude-haiku-4-5-20251001` — 가장 저렴, 빠른 반복 dev용
- `claude-sonnet-4-6` — **Phase 1 권장 (균형)**
- `claude-opus-4-7` — 최고 품질, Phase 4 평가용

## Phase 1 한계 (의도된 것)

- 키워드 검색만 — "retention 관련 인사이트" 같은 추상 질문은 잘 못 잡음 (Phase 2 RAG로 해결)
- 관계 추론 불가 — "Sony 자회사 중..." 같은 질문 한계 (Phase 3 Graph로 해결, 조건부)
- 단일 사용자 로컬 실행 — Phase 4에서 Streamlit Cloud 배포

## 검증 쿼리 (`wiki/log.md`에 평가 누적)

Phase 1 완료 트리거:
- 위키 기반 답변이 챗 UI에서 나옴
- 키워드 검색 한계가 보이는 케이스 2개 이상 발견
- `core/`가 Streamlit 없이도 import해서 작동 (`python -c "from core import ask"`)

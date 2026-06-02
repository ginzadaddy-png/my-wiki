"""Streamlit chat UI. core/ 모듈을 호출만 함 — 로직은 core/에."""

from __future__ import annotations

import hmac
import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from core import ask

load_dotenv(override=True)  # .env가 셸 환경의 빈 ANTHROPIC_API_KEY를 덮어쓰도록


def _require_auth() -> None:
    """공개 Space 접근 게이트. `APP_PASSWORD` secret과 대조.

    fail-closed: APP_PASSWORD가 비어 있으면 입장 자체를 막는다(설정 누락이
    전체 공개로 이어지지 않도록). 인증은 session_state에 1회만 저장돼
    이후 질문마다 다시 묻지 않는다.
    """
    expected = os.getenv("APP_PASSWORD", "")
    if not expected:
        st.error("서버 설정 오류: `APP_PASSWORD`가 설정되지 않았습니다. (관리자 전용 — HF Space Secrets 확인)")
        st.stop()
    if st.session_state.get("authed"):
        return
    with st.form("auth"):
        pw = st.text_input("비밀번호", type="password", placeholder="접근 비밀번호를 입력하세요")
        ok = st.form_submit_button("입장")
    if not ok:
        st.stop()
    if hmac.compare_digest(pw, expected):  # 타이밍 공격 회피용 상수시간 비교
        st.session_state.authed = True
        st.rerun()
    st.error("비밀번호가 틀렸습니다.")
    st.stop()

def _resolve_vault() -> Path:
    """vault 경로 결정: 환경변수 > 로컬 경로 > Space 번들(앱 옆 wiki/)."""
    env = os.getenv("VAULT_PATH")
    if env:
        return Path(env)
    local = Path(r"C:\Vault\Ginza\my-wiki")
    if local.exists():
        return local
    # HF Spaces 등 배포 환경: app.py와 같은 디렉터리에 wiki/ 번들
    return Path(__file__).resolve().parent


VAULT_PATH = _resolve_vault()
MODEL = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6")
API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

st.set_page_config(page_title="Ginza Wiki Chat", page_icon="💬", layout="wide")
st.title("💬 Ginza Wiki Chat")

_require_auth()  # 공개 Space 접근 게이트 (chat·API 호출보다 먼저)

st.caption(f"vault: `{VAULT_PATH}` · model: `{MODEL}`")

if not API_KEY:
    st.error("`.env`에 `ANTHROPIC_API_KEY`를 설정하세요. `.env.example` 참고.")
    st.stop()

if not VAULT_PATH.exists():
    st.error(f"vault 경로를 찾을 수 없음: `{VAULT_PATH}`")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg["role"] == "assistant" and msg.get("sources"):
            with st.expander(f"📄 검색된 페이지 {len(msg['sources'])}개"):
                for src in msg["sources"]:
                    st.markdown(
                        f"- **[[{src['slug']}]]** ({src['type']}, score {src['score']}) — {src['title']}"
                    )
                    st.caption(src["snippet"])

if query := st.chat_input("위키에 대해 질문하세요"):
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        from core.embedder import is_warm
        cold = not is_warm()
        if cold:
            st.info("🥶 첫 질문이라 검색 모델(BGE-M3)을 메모리에 올리는 중 — 1~2분 걸릴 수 있어요. 이후 질문은 빠릅니다.")
        spinner_msg = "검색 모델 로딩 + 위키 검색 + Claude 호출 중... (최대 2분)" if cold else "위키 검색 + Claude 호출 중..."
        with st.spinner(spinner_msg):
            result = ask(query, VAULT_PATH, API_KEY, model=MODEL)
        st.markdown(result["answer"])
        if result["sources"]:
            mode = "🧠 의미검색(RAG)" if result.get("retrieval") == "rag" else "🔑 키워드"
            with st.expander(f"📄 검색된 페이지 {len(result['sources'])}개 · {mode}"):
                for src in result["sources"]:
                    st.markdown(
                        f"- **[[{src['slug']}]]** ({src['type']}, score {src['score']}) — {src['title']}"
                    )
                    st.caption(src["snippet"])

    st.session_state.messages.append({
        "role": "assistant",
        "content": result["answer"],
        "sources": result["sources"],
    })

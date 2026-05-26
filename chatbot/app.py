"""Streamlit chat UI. core/ 모듈을 호출만 함 — 로직은 core/에."""

from __future__ import annotations

import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from core import ask

load_dotenv()

DEFAULT_VAULT = Path(r"C:\Vault\Ginza\my-wiki")
VAULT_PATH = Path(os.getenv("VAULT_PATH", DEFAULT_VAULT))
MODEL = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6")
API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

st.set_page_config(page_title="Ginza Wiki Chat", page_icon="💬", layout="wide")
st.title("💬 Ginza Wiki Chat")
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
        with st.spinner("위키 검색 + Claude 호출 중..."):
            result = ask(query, VAULT_PATH, API_KEY, model=MODEL)
        st.markdown(result["answer"])
        if result["sources"]:
            with st.expander(f"📄 검색된 페이지 {len(result['sources'])}개"):
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

# HF Spaces (Docker SDK) — Streamlit + BGE-M3 + Chroma
FROM python:3.11-slim

# 비root 사용자 (HF Spaces 권장: uid 1000)
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH \
    HF_HOME=/home/user/.cache/huggingface \
    VAULT_PATH=/home/user/app \
    PYTHONUNBUFFERED=1

WORKDIR /home/user/app

# 의존성 먼저 (레이어 캐시)
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 앱 + 데이터 (app.py·core/·chroma_db/·wiki/)
COPY --chown=user . .

# HF Spaces는 7860 포트 기대
EXPOSE 7860
CMD ["streamlit", "run", "app.py", \
     "--server.port=7860", "--server.address=0.0.0.0", \
     "--server.headless=true", "--browser.gatherUsageStats=false"]

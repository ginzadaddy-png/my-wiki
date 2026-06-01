---
title: Ginza Wiki Chat
emoji: 💬
colorFrom: indigo
colorTo: blue
sdk: docker
app_port: 7860
pinned: false
---

# Ginza Wiki Chat

게임 개발 지식 위키 기반 hybrid 챗봇 (RAG + Graph). 비공개 운영.

- **검색**: BGE-M3 의미 검색 (Chroma 벡터 DB, 1409 청크)
- **관계 추론**: NetworkX graph + Claude tool-use (개발사·퍼블리셔·모회사·장르)
- **응답**: Claude (Anthropic API)

> 첫 콜드 스타트 시 BGE-M3 모델(~2.3GB) 다운로드로 1~2분 소요.

## Secret 필요

Space Settings → Variables and secrets에 `ANTHROPIC_API_KEY` 등록.

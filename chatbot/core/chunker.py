"""위키 페이지를 의미 단위 청크로 분할. Phase 2 RAG 사전 작업.

전략:
- '## ' heading 기준 1차 분할 (의미 경계 보존)
- 섹션이 MAX_CHARS 초과 시 문단(빈 줄) 경계로 재분할
- heading 없는 페이지는 길이 기준 분할
- 각 청크의 임베딩 텍스트에 '제목 + heading' 프리픽스 부착
  → 한글 제목이 모든 청크 임베딩에 포함되어 교차언어 검색 개선
"""

from __future__ import annotations

import re
from pathlib import Path

from .wiki_loader import iter_wiki_pages, load_page

MAX_CHARS = 800
MIN_CHARS = 500  # 이보다 작은 인접 청크는 합치기 시도
_HEADING_RE = re.compile(r"^(#{2,4})\s+(.*)$", re.MULTILINE)


def _split_by_headings(body: str) -> list[tuple[str, str]]:
    """본문을 (heading, section_text) 리스트로 분할.

    첫 heading 앞의 도입부는 heading='' 으로 처리.
    """
    matches = list(_HEADING_RE.finditer(body))
    if not matches:
        return [("", body.strip())]

    sections: list[tuple[str, str]] = []
    # 첫 heading 이전 도입부
    intro = body[: matches[0].start()].strip()
    if intro:
        sections.append(("", intro))

    for i, m in enumerate(matches):
        heading = m.group(2).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        text = body[start:end].strip()
        if text:
            sections.append((heading, text))
    return sections


def _split_long_text(text: str, max_chars: int = MAX_CHARS) -> list[str]:
    """긴 텍스트를 문단(빈 줄) 경계로 max_chars 이하 조각들로 분할."""
    if len(text) <= max_chars:
        return [text]

    paragraphs = re.split(r"\n\s*\n", text)
    chunks: list[str] = []
    buf = ""
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        if not buf:
            buf = para
        elif len(buf) + len(para) + 2 <= max_chars:
            buf += "\n\n" + para
        else:
            chunks.append(buf)
            buf = para
        # 단일 문단이 max를 넘으면 강제로 자르기
        while len(buf) > max_chars:
            chunks.append(buf[:max_chars])
            buf = buf[max_chars:]
    if buf:
        chunks.append(buf)
    return chunks


def chunk_page(page: dict) -> list[dict]:
    """단일 위키 페이지를 청크 리스트로 변환.

    Returns: [{
        "id": "slug#3",
        "slug": str, "title": str, "type": str,
        "heading": str,
        "text": str,              # 원문 청크 (표시·인용용)
        "embed_text": str,        # 제목+heading 프리픽스 포함 (임베딩용)
    }, ...]
    """
    title = page["title"]
    slug = page["slug"]
    ptype = page["type"]

    chunks: list[dict] = []
    idx = 0
    for heading, section in _split_by_headings(page["body"]):
        for piece in _split_long_text(section):
            piece = piece.strip()
            if len(piece) < 30:  # 너무 짧은 잔여물 스킵
                continue
            prefix_parts = [f"제목: {title}"]
            if heading:
                prefix_parts.append(f"섹션: {heading}")
            embed_text = "\n".join(prefix_parts) + "\n\n" + piece
            chunks.append({
                "id": f"{slug}#{idx}",
                "slug": slug,
                "title": title,
                "type": ptype,
                "heading": heading,
                "text": piece,
                "embed_text": embed_text,
            })
            idx += 1
    return chunks


def chunk_vault(vault_path: Path) -> list[dict]:
    """vault 전체를 청크 리스트로 변환."""
    all_chunks: list[dict] = []
    for md_path in iter_wiki_pages(Path(vault_path)):
        page = load_page(md_path)
        all_chunks.extend(chunk_page(page))
    return all_chunks

"""vault 경로에서 markdown 페이지를 읽어 frontmatter+본문 dict로 반환."""

from __future__ import annotations

from pathlib import Path
from typing import Iterator

import frontmatter

WIKI_SUBDIR = "wiki"
EXCLUDED_DIRS = {"presentations"}  # .html slides는 별도 처리
EXCLUDED_FILES = {"all.md", "log.md", "overview.md", "index.md"}  # 카탈로그·로그


def iter_wiki_pages(vault_path: Path) -> Iterator[Path]:
    """vault 안의 wiki/ 폴더에서 콘텐츠 .md 파일 경로를 yield."""
    wiki_root = Path(vault_path) / WIKI_SUBDIR
    if not wiki_root.exists():
        raise FileNotFoundError(f"wiki/ 폴더를 찾을 수 없음: {wiki_root}")

    for md_file in wiki_root.rglob("*.md"):
        if any(part in EXCLUDED_DIRS for part in md_file.relative_to(wiki_root).parts):
            continue
        if md_file.name in EXCLUDED_FILES:
            continue
        yield md_file


def load_page(file_path: Path) -> dict:
    """단일 markdown 페이지를 frontmatter+본문으로 파싱.

    Returns:
        {
            "slug": "astro-bot",
            "path": Path,
            "title": "아스트로봇",
            "type": "entity",
            "frontmatter": {...},
            "body": "본문 텍스트",
        }
    """
    file_path = Path(file_path)
    # utf-8-sig: BOM이 붙은 파일(notepad 등이 저장)도 frontmatter가 정상 파싱하도록.
    # BOM이 있으면 frontmatter.load가 여는 '---'를 인식 못 해 metadata가 비어버림.
    text = file_path.read_text(encoding="utf-8-sig")
    post = frontmatter.loads(text)
    meta = dict(post.metadata)
    return {
        "slug": file_path.stem,
        "path": file_path,
        "title": meta.get("title", file_path.stem),
        "type": meta.get("type", "unknown"),
        "frontmatter": meta,
        "body": post.content,
    }

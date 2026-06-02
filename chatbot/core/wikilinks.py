"""답변 본문의 `[[slug]]` / `[[slug|라벨]]` 위키링크를 Quartz 사이트 링크로 변환.

slug는 basename(file_path.stem)이라 폴더 경로가 없으므로, vault를 스캔해
basename → wiki-상대경로 맵을 만들어 정확한 Quartz URL을 조립한다.
- 맵에 없는 slug(페이지 없는 genre/platform slug, 환각 등)는 평문으로 렌더(깨진 링크 방지).
- Streamlit st.markdown(unsafe_allow_html=True)에서 새 탭으로 열리도록 <a target=_blank>.
"""

from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path

from .wiki_loader import iter_wiki_pages, WIKI_SUBDIR

QUARTZ_BASE = "https://ginzadaddy-png.github.io/quartz"

# [[slug]] 또는 [[slug|라벨]] — slug에 | 와 ] 불가, 라벨은 ] 전까지
_WIKILINK = re.compile(r"\[\[\s*([^\]|]+?)\s*(?:\|\s*([^\]]+?)\s*)?\]\]")


@lru_cache(maxsize=8)
def build_slug_map(vault_path: str) -> dict[str, str]:
    """basename slug → wiki 루트 기준 상대경로(확장자 없음, posix).

    예: 'dark-souls' → 'entities/dark-souls'. 충돌 시 먼저 만난 파일 우선.
    """
    wiki_root = Path(vault_path) / WIKI_SUBDIR
    mapping: dict[str, str] = {}
    for md in iter_wiki_pages(Path(vault_path)):
        rel = md.relative_to(wiki_root).with_suffix("")
        slug = md.stem
        mapping.setdefault(slug, rel.as_posix())
    return mapping


def to_url(slug: str, vault_path: str) -> str | None:
    """slug → Quartz 절대 URL. 페이지 없으면 None."""
    rel = build_slug_map(vault_path).get(slug.strip())
    return f"{QUARTZ_BASE}/{rel}" if rel else None


def linkify(text: str, vault_path: str | Path) -> str:
    """본문 내 모든 위키링크를 <a> 또는 평문으로 치환."""
    vp = str(vault_path)

    def repl(m: re.Match) -> str:
        slug = m.group(1).strip()
        label = (m.group(2) or slug).strip()
        url = to_url(slug, vp)
        if url:
            return f'<a href="{url}" target="_blank" rel="noopener">{label}</a>'
        return label  # 페이지 없으면 평문

    return _WIKILINK.sub(repl, text)

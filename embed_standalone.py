#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""site용 deck은 가볍게 두고, 단독 배포용 self-contained 사본을 dist/(gitignore)에 생성.
- Pretendard CDN <link> → base64 woff2 @font-face 인라인
- 로컬 <img src="..."> → base64 data URI
원본 deck은 수정하지 않음. 출력: dist/<deckname>

실행: python embed_standalone.py             # DECKS 전체 → dist/
      python embed_standalone.py <deck.html>  # 특정 deck만 → dist/
"""
import re, sys, base64, pathlib, urllib.request

PRES = pathlib.Path("wiki/presentations")
DIST = pathlib.Path("dist")
FONT_URL = "https://cdn.jsdelivr.net/npm/pretendard@1.3.9/dist/web/variable/woff2/PretendardVariable.woff2"
FONT_CACHE = DIST / ".fonts" / "PretendardVariable.woff2"   # dist/ 안(gitignore)
MIME = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".gif": "image/gif", ".webp": "image/webp"}
DECKS = [
    "ai-asset-pipeline-2026-report-deck.html",
    "steam-launch-strategy-deck.html",
    "studio-risk-defense-deck.html",
]

if not FONT_CACHE.exists() or FONT_CACHE.stat().st_size < 100_000:
    FONT_CACHE.parent.mkdir(parents=True, exist_ok=True)
    print("woff2 다운로드…")
    urllib.request.urlretrieve(FONT_URL, FONT_CACHE)
FONT_B64 = base64.b64encode(FONT_CACHE.read_bytes()).decode("ascii")
FONT_STYLE = (
    '<style>@font-face{font-family:"Pretendard Variable";font-weight:45 920;'
    'font-style:normal;font-display:swap;src:local("Pretendard Variable"),'
    'url(data:font/woff2;base64,' + FONT_B64 + ') format("woff2-variations")}</style>'
)
LINK_RE = re.compile(r'<link\b[^>]*pretendard[^>]*?/>', re.I)
IMG_RE = re.compile(r'(src=")([^"]+)(")')


def embed_imgs(html, base):
    def repl(m):
        pre, url, post = m.group(1), m.group(2), m.group(3)
        if url.startswith(("http", "data:")):
            return m.group(0)
        p = base / url
        if not p.exists():
            return m.group(0)
        b64 = base64.b64encode(p.read_bytes()).decode("ascii")
        return f'{pre}data:{MIME.get(p.suffix.lower(), "application/octet-stream")};base64,{b64}{post}'
    return IMG_RE.sub(repl, html)


def build(deck: pathlib.Path):
    html = deck.read_text(encoding="utf-8")
    html, nlink = LINK_RE.subn(FONT_STYLE, html)
    html = embed_imgs(html, deck.parent)
    DIST.mkdir(exist_ok=True)
    out = DIST / deck.name
    out.write_text(html, encoding="utf-8")
    nimg = html.count("data:image")
    leftover = [u for u in re.findall(r'src="([^"]+)"', html) if u.startswith("http")]
    mb = round(out.stat().st_size / 1024 / 1024, 2)
    print(f"{deck.name}: 폰트 {nlink} · 이미지 {nimg} · 외부src잔존 {leftover} · {mb}MB → {out}")


targets = [pathlib.Path(sys.argv[1])] if len(sys.argv) > 1 else [PRES / n for n in DECKS]
for d in targets:
    build(d) if d.exists() else print("skip(없음):", d)

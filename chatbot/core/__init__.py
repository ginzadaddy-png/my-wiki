from .wiki_loader import iter_wiki_pages, load_page
from .search import keyword_search
from .agent import ask

# RAG (Phase 2) — 무거운 의존성(torch)을 가진 모듈은 lazy import.
# core import 시점에 torch를 끌어오지 않도록 함수 안에서 import.

__all__ = ["iter_wiki_pages", "load_page", "keyword_search", "ask"]

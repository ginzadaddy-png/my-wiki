"""entity relations로 NetworkX 그래프 빌드 + 관계 추론 쿼리. Phase 3.

엣지 방향:
- developedBy: game → studio
- publishedBy: game → publisher
- parentOf:   parent → child (studio/publisher 소유)
- genre:      game → concept
- platform:   game → platform

쿼리는 방향 무관 추론을 위해 in/out 양방향 모두 지원.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

import networkx as nx

from .wiki_loader import iter_wiki_pages, load_page

REL_TYPES = ("developedBy", "publishedBy", "parentOf", "genre", "platform")


@lru_cache(maxsize=1)
def build_graph(vault_path: str) -> nx.MultiDiGraph:
    """vault의 entity relations로 방향 그래프 빌드 (lru_cache로 1회만)."""
    g = nx.MultiDiGraph()
    for md in iter_wiki_pages(Path(vault_path)):
        page = load_page(md)
        slug = page["slug"]
        g.add_node(slug, title=page["title"], type=page["type"])
        rel = page["frontmatter"].get("relations") or {}
        for rtype, targets in rel.items():
            if rtype not in REL_TYPES or not targets:
                continue
            for tgt in targets:
                g.add_edge(slug, tgt, rel=rtype)
    return g


def _title(g, slug: str) -> str:
    return g.nodes.get(slug, {}).get("title", slug)


def out_relations(g, entity: str) -> dict[str, list[str]]:
    """entity --rel--> targets (예: 게임의 developedBy·publishedBy)."""
    res: dict[str, list[str]] = {}
    for _, tgt, data in g.out_edges(entity, data=True):
        res.setdefault(data["rel"], []).append(tgt)
    return res


def in_relations(g, entity: str) -> dict[str, list[str]]:
    """sources --rel--> entity (예: 스튜디오를 developedBy로 가리키는 게임들)."""
    res: dict[str, list[str]] = {}
    for src, _, data in g.in_edges(entity, data=True):
        res.setdefault(data["rel"], []).append(src)
    return res


def find_by_relation(g, entity: str, rel: str, direction: str = "out") -> list[str]:
    """entity의 특정 관계 대상. direction='out' (entity가 주체) / 'in' (entity가 객체)."""
    if direction == "out":
        return [t for _, t, d in g.out_edges(entity, data=True) if d["rel"] == rel]
    return [s for s, _, d in g.in_edges(entity, data=True) if d["rel"] == rel]


def parent_of(g, entity: str) -> list[str]:
    """entity의 모회사 (parentOf 들어오는 엣지의 출발점)."""
    return find_by_relation(g, entity, "parentOf", direction="in")


def children_of(g, entity: str) -> list[str]:
    """entity가 소유한 자회사 (parentOf 나가는 엣지)."""
    return find_by_relation(g, entity, "parentOf", direction="out")


def siblings(g, entity: str) -> list[str]:
    """같은 모회사를 공유하는 다른 엔티티들."""
    result = set()
    for parent in parent_of(g, entity):
        for child in children_of(g, parent):
            if child != entity:
                result.add(child)
    return sorted(result)


def neighbors(g, entity: str, depth: int = 1) -> list[str]:
    """entity의 depth-hop 이웃 (방향 무시)."""
    und = g.to_undirected()
    if entity not in und:
        return []
    seen = nx.single_source_shortest_path_length(und, entity, cutoff=depth)
    return sorted(k for k in seen if k != entity)


def path_between(g, a: str, b: str) -> list[tuple[str, str, str]] | None:
    """a~b 최단 경로를 (src, rel, dst) 엣지 리스트로 반환 (방향 무시)."""
    und = g.to_undirected()
    if a not in und or b not in und:
        return None
    try:
        nodes = nx.shortest_path(und, a, b)
    except nx.NetworkXNoPath:
        return None
    path = []
    for i in range(len(nodes) - 1):
        u, v = nodes[i], nodes[i + 1]
        # 방향 그래프에서 실제 엣지 방향·라벨 찾기
        if g.has_edge(u, v):
            rel = next(iter(g.get_edge_data(u, v).values()))["rel"]
            path.append((u, rel, v))
        else:
            rel = next(iter(g.get_edge_data(v, u).values()))["rel"]
            path.append((v, rel, u))
    return path


def stats(g) -> dict:
    rel_counts: dict[str, int] = {}
    for _, _, d in g.edges(data=True):
        rel_counts[d["rel"]] = rel_counts.get(d["rel"], 0) + 1
    return {"nodes": g.number_of_nodes(), "edges": g.number_of_edges(), "by_rel": rel_counts}

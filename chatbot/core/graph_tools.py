"""Anthropic tool-use용 graph 쿼리 도구. agent가 관계 추론 시 호출.

slug 해석(resolve)부터 관계 조회까지 제공. 결과는 사람이 읽을 문자열로 반환.
"""

from __future__ import annotations

from . import graph as G

TOOLS = [
    {
        "name": "resolve_entity",
        "description": "게임/스튜디오/퍼블리셔 이름(한글·영문)을 위키 entity slug로 변환. "
                       "관계 조회 전에 먼저 slug를 확정할 때 사용.",
        "input_schema": {
            "type": "object",
            "properties": {"name": {"type": "string", "description": "찾을 이름 (예: 'Astro Bot', '소니')"}},
            "required": ["name"],
        },
    },
    {
        "name": "get_relations",
        "description": "한 entity의 모든 관계(나가는·들어오는)를 조회. "
                       "예: 게임의 개발사·퍼블리셔, 스튜디오의 모회사·만든 게임.",
        "input_schema": {
            "type": "object",
            "properties": {"entity": {"type": "string", "description": "entity slug"}},
            "required": ["entity"],
        },
    },
    {
        "name": "get_children",
        "description": "모회사 entity가 소유한 자회사(스튜디오) 목록. 예: sony-interactive-entertainment의 자회사.",
        "input_schema": {
            "type": "object",
            "properties": {"entity": {"type": "string", "description": "모회사 slug"}},
            "required": ["entity"],
        },
    },
    {
        "name": "get_siblings",
        "description": "같은 모회사를 공유하는 다른 스튜디오들. 예: team-asobi의 형제 스튜디오.",
        "input_schema": {
            "type": "object",
            "properties": {"entity": {"type": "string", "description": "스튜디오 slug"}},
            "required": ["entity"],
        },
    },
    {
        "name": "find_by_relation",
        "description": "특정 관계의 대상을 조회. direction='out'은 entity가 주체(게임→개발사), "
                       "'in'은 entity가 객체(개발사를 가리키는 게임들, 퍼블리셔가 퍼블리싱한 게임들, 장르의 게임들).",
        "input_schema": {
            "type": "object",
            "properties": {
                "entity": {"type": "string"},
                "relation": {"type": "string", "enum": list(G.REL_TYPES)},
                "direction": {"type": "string", "enum": ["out", "in"], "default": "out"},
            },
            "required": ["entity", "relation"],
        },
    },
    {
        "name": "find_path",
        "description": "두 entity 사이 최단 관계 경로. 예: astro-bot과 god-of-war 사이 연결.",
        "input_schema": {
            "type": "object",
            "properties": {"a": {"type": "string"}, "b": {"type": "string"}},
            "required": ["a", "b"],
        },
    },
]


def resolve_entity(g, name: str) -> list[str]:
    """이름 → 후보 slug 리스트 (slug·title 부분 매칭)."""
    n = name.strip().lower().replace(" ", "")
    hits = []
    for node, data in g.nodes(data=True):
        slug_norm = node.lower().replace("-", "")
        title_norm = str(data.get("title", "")).lower().replace(" ", "")
        if n in slug_norm or n in title_norm or slug_norm in n:
            hits.append(node)
    return hits[:8]


def _fmt(g, slugs: list[str]) -> str:
    if not slugs:
        return "(없음)"
    return ", ".join(f"{s} ({G._title(g, s)})" for s in slugs)


def execute(g, name: str, inp: dict) -> str:
    """도구 호출 실행 → 사람이 읽을 결과 문자열."""
    try:
        if name == "resolve_entity":
            hits = resolve_entity(g, inp["name"])
            return f"후보 slug: {_fmt(g, hits)}" if hits else f"'{inp['name']}' 매칭 entity 없음"
        if name == "get_relations":
            e = inp["entity"]
            out = G.out_relations(g, e)
            inc = G.in_relations(g, e)
            lines = [f"{e} ({G._title(g, e)}) 관계:"]
            for r, ts in out.items():
                lines.append(f"  [out] {r}: {_fmt(g, ts)}")
            for r, ss in inc.items():
                lines.append(f"  [in] {r}: {_fmt(g, ss)}")
            return "\n".join(lines) if (out or inc) else f"{e}: 관계 없음"
        if name == "get_children":
            return f"{inp['entity']} 자회사: {_fmt(g, G.children_of(g, inp['entity']))}"
        if name == "get_siblings":
            return f"{inp['entity']} 형제(같은 모회사): {_fmt(g, G.siblings(g, inp['entity']))}"
        if name == "find_by_relation":
            res = G.find_by_relation(g, inp["entity"], inp["relation"], inp.get("direction", "out"))
            return f"{inp['entity']} {inp['relation']}({inp.get('direction','out')}): {_fmt(g, res)}"
        if name == "find_path":
            path = G.path_between(g, inp["a"], inp["b"])
            if not path:
                return f"{inp['a']} ~ {inp['b']}: 경로 없음"
            return " → ".join(f"{u} -[{r}]-> {v}" for u, r, v in path)
        return f"알 수 없는 도구: {name}"
    except Exception as e:  # noqa: BLE001
        return f"도구 실행 오류({name}): {e}"

"""Phase 4 후속: 게임 entity에 platform 관계 추가 + platform entity 생성.

위키 본문에 platform 명시가 7개뿐이라(나머지 19개 부재), 게임 출시 플랫폼이라는
공인 사실로 보강(사용자 승인). platform slug는 위키에 존재해야 하므로 platform
entity 6개 신규 생성. M5("PS5 독점작") 완전 해결 목적.

일회성 스크립트 (기록용 보존).
"""

from __future__ import annotations

from pathlib import Path

VAULT = Path(r"C:\Vault\Ginza\my-wiki")
ENT = VAULT / "wiki" / "entities"
TODAY = "2026-06-01"

PLATFORM_ENTITIES = {
    "ps5": "PlayStation 5",
    "ps4": "PlayStation 4",
    "pc": "PC",
    "xbox-series": "Xbox Series X|S",
    "xbox-one": "Xbox One",
    "nintendo-switch": "Nintendo Switch",
}

# 게임 → 출시 플랫폼 (공인 사실. 레거시 PS3/360은 현행 가용 플랫폼으로 정리)
PLATFORMS: dict[str, list[str]] = {
    "a-plague-tale-requiem": ["ps5", "xbox-series", "pc"],
    "arc-raiders": ["pc", "ps5", "xbox-series"],
    "astro-bot": ["ps5"],
    "baldurs-gate-3": ["pc", "ps5", "xbox-series"],
    "breath-of-the-wild": ["nintendo-switch"],
    "clair-obscur-expedition-33": ["ps5", "xbox-series", "pc"],
    "cyberpunk-2077": ["pc", "ps4", "ps5", "xbox-one", "xbox-series"],
    "dark-souls": ["pc", "ps4", "xbox-one", "nintendo-switch"],
    "dave-the-diver": ["pc", "nintendo-switch", "ps4", "ps5"],
    "death-stranding": ["ps4", "ps5", "pc"],
    "elden-ring": ["ps4", "ps5", "xbox-one", "xbox-series", "pc"],
    "ghost-of-tsushima": ["ps4", "ps5", "pc"],
    "ghost-of-yotei": ["ps5"],
    "god-of-war-2018": ["ps4", "pc"],
    "gta5": ["ps4", "ps5", "xbox-one", "xbox-series", "pc"],
    "helldivers-2": ["pc", "ps5", "xbox-series"],
    "hifi-rush": ["xbox-series", "pc", "ps5", "nintendo-switch"],
    "hitman-2016": ["ps4", "xbox-one", "pc"],
    "hogwarts-legacy": ["ps5", "ps4", "xbox-series", "xbox-one", "pc", "nintendo-switch"],
    "marvel-spiderman-2": ["ps5"],
    "red-dead-redemption-2": ["ps4", "xbox-one", "pc"],
    "sekiro": ["pc", "ps4", "xbox-one"],
    "skyrim": ["pc", "ps4", "xbox-one", "nintendo-switch"],
    "the-last-of-us": ["ps4", "ps5", "pc"],
    "valheim": ["pc", "xbox-series", "xbox-one"],
    "witcher-3": ["pc", "ps4", "ps5", "xbox-one", "xbox-series", "nintendo-switch"],
}


def create_platform_entities() -> None:
    # 역방향: 각 플랫폼의 게임 목록
    rev: dict[str, list[str]] = {p: [] for p in PLATFORM_ENTITIES}
    for game, plats in PLATFORMS.items():
        for p in plats:
            rev[p].append(game)
    for slug, name in PLATFORM_ENTITIES.items():
        f = ENT / f"{slug}.md"
        games = ", ".join(f"[[{g}]]" for g in sorted(rev[slug]))
        body = (
            f"게임 플랫폼. 위키 내 {name} 출시 게임: {games}.\n\n"
            f"> Phase 4 graph 추론(플랫폼별 게임·독점작 질의)을 위해 생성한 플랫폼 노드.\n"
        )
        fm = (
            f'title: "{name}"\n'
            f"type: entity\n"
            f"sources: []\nrelated: []\n"
            f"created: {TODAY}\nupdated: {TODAY}\nconfidence: high\n"
        )
        f.write_text(f"---\n{fm}---\n\n{body}", encoding="utf-8")
        print(f"  CREATE platform: {slug} ({len(rev[slug])} 게임)")


def add_platform_relation(slug: str, plats: list[str]) -> str:
    f = ENT / f"{slug}.md"
    text = f.read_text(encoding="utf-8-sig")
    end = text.index("\n---", 3)
    fm = text[3:end].strip("\n")
    body = text[end + 4:]
    if "platform:" in fm:
        return f"SKIP (이미 platform): {slug}"
    arr = ", ".join(plats)
    line = f"  platform: [{arr}]"
    if "relations:" in fm:
        # relations 블록 끝(frontmatter 마지막)에 platform 라인 추가
        fm = fm + "\n" + line
    else:
        fm = fm + "\nrelations:\n" + line
    # updated 갱신
    fm_lines = fm.split("\n")
    for i, ln in enumerate(fm_lines):
        if ln.startswith("updated:"):
            fm_lines[i] = f"updated: {TODAY}"
    fm = "\n".join(fm_lines)
    f.write_text(f"---\n{fm}\n---{body}", encoding="utf-8")
    return f"OK: {slug} -> platform {plats}"


def main() -> None:
    print("=== platform entity 생성 ===")
    create_platform_entities()
    print("\n=== 게임에 platform 관계 추가 ===")
    ok = 0
    for slug, plats in PLATFORMS.items():
        r = add_platform_relation(slug, plats)
        print(" ", r)
        if r.startswith("OK"):
            ok += 1
    print(f"\n적용: {ok}/{len(PLATFORMS)} + 플랫폼 entity {len(PLATFORM_ENTITIES)}")


if __name__ == "__main__":
    main()

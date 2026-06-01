"""Phase 3 retrofit: entity frontmatter에 relations 블록 외과적 삽입.

- 본문 근거로 추출한 relations만 적용 (환각 금지). 5개 어휘만 사용.
- 값은 위키에 존재하는 slug만 (platform·대부분 genre는 대상 페이지 부재로 생략).
- frontmatter의 relations 블록만 삽입하고 나머지는 보존 (최소 diff).
- BOM 제거하며 UTF-8(no BOM)로 저장. updated 날짜 갱신.

일회성 스크립트 (Phase 3 retrofit 기록용으로 repo에 보존).
"""

from __future__ import annotations

from pathlib import Path

VAULT = Path(r"C:\Vault\Ginza\my-wiki")
ENT = VAULT / "wiki" / "entities"
TODAY = "2026-06-01"

# slug -> {관계: [slug...]}. 본문 근거로만 작성.
RELATIONS: dict[str, dict[str, list[str]]] = {
    # --- 게임 (developedBy / publishedBy / genre) ---
    "a-plague-tale-requiem": {"developedBy": ["asobo-studio"]},
    "arc-raiders": {"developedBy": ["embark-studios"], "publishedBy": ["nexon"]},
    "astro-bot": {"developedBy": ["team-asobi"], "publishedBy": ["sony-interactive-entertainment"]},
    "baldurs-gate-3": {"developedBy": ["larian-studios"]},
    "breath-of-the-wild": {"developedBy": ["nintendo"], "publishedBy": ["nintendo"]},
    "clair-obscur-expedition-33": {"developedBy": ["sandfall-interactive"]},
    "cyberpunk-2077": {"developedBy": ["cd-projekt-red"], "publishedBy": ["cd-projekt-red"]},
    "dark-souls": {"developedBy": ["fromsoftware"], "publishedBy": ["bandai-namco"], "genre": ["soulslike"]},
    "dave-the-diver": {"developedBy": ["mint-rocket"], "publishedBy": ["nexon"]},
    "death-stranding": {"developedBy": ["kojima-productions"], "publishedBy": ["sony-interactive-entertainment"]},
    "elden-ring": {"developedBy": ["fromsoftware"], "publishedBy": ["bandai-namco"], "genre": ["soulslike"]},
    "ghost-of-tsushima": {"developedBy": ["sucker-punch-productions"], "publishedBy": ["sony-interactive-entertainment"]},
    "ghost-of-yotei": {"developedBy": ["sucker-punch-productions"], "publishedBy": ["sony-interactive-entertainment"]},
    "god-of-war-2018": {"developedBy": ["sony-santa-monica"], "publishedBy": ["sony-interactive-entertainment"]},
    "gta5": {"developedBy": ["rockstar-games"], "publishedBy": ["rockstar-games"]},
    "helldivers-2": {"developedBy": ["arrowhead-game-studios"], "publishedBy": ["sony-interactive-entertainment"]},
    "hifi-rush": {"developedBy": ["tango-gameworks"]},
    "hitman-2016": {"developedBy": ["io-interactive"]},
    "hogwarts-legacy": {"developedBy": ["avalanche-software"]},
    "marvel-spiderman-2": {"developedBy": ["insomniac-games"], "publishedBy": ["sony-interactive-entertainment"]},
    "red-dead-redemption-2": {"developedBy": ["rockstar-games"], "publishedBy": ["rockstar-games"]},
    "sekiro": {"developedBy": ["fromsoftware"], "genre": ["soulslike"]},
    "skyrim": {"developedBy": ["bethesda-game-studios"]},
    "the-last-of-us": {"developedBy": ["naughty-dog"], "publishedBy": ["sony-interactive-entertainment"]},
    "valheim": {"developedBy": ["iron-gate-studio"]},
    "witcher-3": {"developedBy": ["cd-projekt-red"], "publishedBy": ["cd-projekt-red"]},
}


def _rel_yaml(rel: dict[str, list[str]]) -> str:
    lines = ["relations:"]
    for k, v in rel.items():
        arr = ", ".join(v)
        lines.append(f"  {k}: [{arr}]")
    return "\n".join(lines)


def apply_one(slug: str, rel: dict[str, list[str]]) -> str:
    f = ENT / f"{slug}.md"
    if not f.exists():
        return f"SKIP (없음): {slug}"
    text = f.read_text(encoding="utf-8-sig")
    if not text.startswith("---"):
        return f"SKIP (frontmatter 없음): {slug}"
    # frontmatter 블록 경계
    end = text.index("\n---", 3)
    fm = text[3:end].strip("\n")
    body = text[end + 4:]
    if "relations:" in fm:
        return f"SKIP (이미 relations): {slug}"
    # updated 갱신
    fm_lines = fm.split("\n")
    for i, ln in enumerate(fm_lines):
        if ln.startswith("updated:"):
            fm_lines[i] = f"updated: {TODAY}"
    fm = "\n".join(fm_lines)
    new_fm = fm + "\n" + _rel_yaml(rel)
    new_text = f"---\n{new_fm}\n---{body}"
    f.write_text(new_text, encoding="utf-8")
    return f"OK: {slug} -> {list(rel.keys())}"


NEW_ENTITIES = {
    "sony-interactive-entertainment": {
        "title": "소니 인터랙티브 엔터테인먼트 (SIE)",
        "parentOf": ["team-asobi", "sony-santa-monica", "naughty-dog",
                     "sucker-punch-productions", "insomniac-games"],
        "body": (
            "소니 그룹의 게임 부문. PlayStation 플랫폼과 다수의 퍼스트 파티 스튜디오를 보유한 "
            "퍼블리셔·플랫폼 사업자. 위키 내 산하 스튜디오로 "
            "[[team-asobi|팀 아소비]]·[[sony-santa-monica|소니 산타모니카]]·"
            "[[naughty-dog|너티독]]·[[sucker-punch-productions|서커펀치]]·"
            "[[insomniac-games|인섬니악]] 등이 있다.\n\n"
            "> 본 페이지는 Phase 3 graph 추론을 위해 산하 스튜디오 관계(parentOf)를 "
            "앵커링하려 생성. 내용은 각 스튜디오 페이지의 '소니 산하/퍼스트 파티' 명시를 종합.\n\n"
            "- **퍼블리싱**: 산하 스튜디오 및 일부 외부 스튜디오(예: [[arrowhead-game-studios|애로우헤드]]의 "
            "[[helldivers-2]])를 퍼블리싱. 단 애로우헤드는 *퍼블리싱 관계일 뿐 자회사가 아님*(텐센트 15% 보유 독립 스튜디오).\n"
        ),
    },
    "microsoft": {
        "title": "마이크로소프트 (Xbox Game Studios)",
        "parentOf": ["bethesda-game-studios", "obsidian-entertainment"],
        "body": (
            "Xbox 플랫폼과 Xbox Game Studios를 운영하는 게임 부문. 위키 내 산하 스튜디오로 "
            "[[bethesda-game-studios|베데스다]](2021 제니맥스 인수)·[[obsidian-entertainment|옵시디언]]이 있다.\n\n"
            "> 본 페이지는 Phase 3 graph 추론을 위해 산하 스튜디오 관계(parentOf)를 "
            "앵커링하려 생성. 내용은 각 스튜디오 페이지의 'Microsoft 산하' 명시를 종합.\n"
            "- [[tango-gameworks|탱고 게임웍스]]는 MS가 2024년 폐쇄 후 한국 [[krafton|크래프톤]]이 인수 → "
            "현재 MS 산하 아님.\n"
        ),
    },
    "krafton": {
        "title": "크래프톤 (KRAFTON)",
        "parentOf": ["tango-gameworks"],
        "body": (
            "한국 게임 회사. 2024년 마이크로소프트가 폐쇄한 [[tango-gameworks|탱고 게임웍스]]를 인수해 "
            "스튜디오를 존속시켰다.\n\n"
            "> Phase 3 graph 추론을 위해 tango-gameworks 소유 관계(parentOf)를 앵커링하려 생성.\n"
        ),
    },
    "take-two-interactive": {
        "title": "테이크투 인터랙티브 (Take-Two Interactive)",
        "parentOf": ["rockstar-games"],
        "body": (
            "미국 게임 퍼블리셔. [[rockstar-games|록스타 게임즈]](GTA·레드 데드 리뎀션)의 모회사. "
            "록스타는 Take-Two 산하 퍼블리싱 레이블로 운영된다.\n\n"
            "> Phase 3 graph 추론을 위해 rockstar-games 소유 관계(parentOf)를 앵커링하려 생성. "
            "내용은 [[rockstar-games]] 페이지의 'Take-Two Interactive 산하' 명시 기반.\n"
        ),
    },
    "bandai-namco": {
        "title": "반다이 남코 (Bandai Namco)",
        "parentOf": [],
        "body": (
            "일본 게임 퍼블리셔. FromSoftware의 소울 시리즈([[dark-souls|다크소울]]·[[elden-ring|엘든링]]) "
            "글로벌 퍼블리셔.\n\n"
            "> Phase 3 graph 추론을 위해 publishedBy 관계의 대상으로 생성. "
            "[[fromsoftware|프롬소프트웨어]]는 카도카와 그룹 산하이며 반다이 남코는 *퍼블리셔*일 뿐 "
            "모회사가 아님(소수 지분 보유) — parentOf 비움.\n"
        ),
    },
}


def create_entity(slug: str, spec: dict) -> str:
    f = ENT / f"{slug}.md"
    if f.exists():
        return f"SKIP (이미 존재): {slug}"
    rel = _rel_yaml({"parentOf": spec["parentOf"]})
    fm = (
        f'title: "{spec["title"]}"\n'
        f"type: entity\n"
        f"sources: []\n"
        f"related: []\n"
        f"created: {TODAY}\n"
        f"updated: {TODAY}\n"
        f"confidence: high\n"
        f"{rel}"
    )
    text = f"---\n{fm}\n---\n\n{spec['body']}"
    f.write_text(text, encoding="utf-8")
    return f"CREATE: {slug} -> parentOf {spec['parentOf']}"


def main() -> None:
    print("=== 신규 모회사 entity 생성 ===")
    for slug, spec in NEW_ENTITIES.items():
        print(" ", create_entity(slug, spec))
    print("\n=== 기존 entity relations 삽입 ===")
    ok = 0
    for slug, rel in RELATIONS.items():
        r = apply_one(slug, rel)
        print(" ", r)
        if r.startswith("OK"):
            ok += 1
    print(f"\n적용: {ok}/{len(RELATIONS)} + 신규 {len(NEW_ENTITIES)}")


if __name__ == "__main__":
    main()

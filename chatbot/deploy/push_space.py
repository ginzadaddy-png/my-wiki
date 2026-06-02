"""HF Space 배포 번들 조립 + 업로드.

스테이징 디렉터리에 app.py·core/·requirements.txt·chroma_db/·wiki/ +
Dockerfile·README(Space frontmatter)를 모아 upload_folder로 push.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from huggingface_hub import HfApi

REPO = "ginzadaddy/ginza-wiki-chat"
CHATBOT = Path(r"C:\Vault\Ginza\my-wiki\chatbot")
WIKI = Path(r"C:\Vault\Ginza\my-wiki\wiki")
STAGE = Path(r"C:\Users\bmjlee\AppData\Local\Temp\ginza-space-stage")


def assemble() -> Path:
    if STAGE.exists():
        shutil.rmtree(STAGE)
    STAGE.mkdir(parents=True)

    # 앱 + 코드
    shutil.copy(CHATBOT / "app.py", STAGE / "app.py")
    shutil.copy(CHATBOT / "requirements.txt", STAGE / "requirements.txt")
    shutil.copytree(CHATBOT / "core", STAGE / "core",
                    ignore=shutil.ignore_patterns("__pycache__"))
    # 색인(numpy embeddings.npy + meta.json) + 위키 (graph용)
    shutil.copytree(CHATBOT / "index", STAGE / "index")
    shutil.copytree(WIKI, STAGE / "wiki",
                    ignore=shutil.ignore_patterns("__pycache__", ".obsidian"))
    # Docker + Space 메타
    shutil.copy(CHATBOT / "deploy" / "Dockerfile", STAGE / "Dockerfile")
    shutil.copy(CHATBOT / "deploy" / "README.md", STAGE / "README.md")
    return STAGE


def main() -> None:
    stage = assemble()
    n = sum(1 for _ in stage.rglob("*") if _.is_file())
    print(f"스테이징 조립: {stage} ({n} 파일)")
    api = HfApi()
    # upload_folder는 로컬에 없는 원격 파일을 안 지우므로, delete_patterns로
    # 더 이상 쓰지 않는 chroma_db 잔재(과거 세그먼트 등)를 함께 정리.
    api.upload_folder(
        folder_path=str(stage),
        repo_id=REPO,
        repo_type="space",
        commit_message="deploy: numpy 벡터 검색으로 교체 (chromadb 제거)",
        delete_patterns=["chroma_db/**", "*.sqlite3", ".gitattributes"],
    )
    print(f"업로드 완료 → https://huggingface.co/spaces/{REPO}")


if __name__ == "__main__":
    main()

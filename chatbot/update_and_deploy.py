"""갱신 자동화: 위키 변경 → chroma 재색인 → HF Space 재배포 한 방.

ingest나 relations 수정 후 실행하면 챗봇 데이터가 최신으로 갱신·배포됨.

사용:
  python update_and_deploy.py            # 재색인 + 재배포
  python update_and_deploy.py --no-deploy  # 재색인만 (로컬 갱신)
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PY = sys.executable


def run(script: str) -> None:
    print(f"\n{'='*60}\n▶ {script}\n{'='*60}")
    r = subprocess.run([PY, str(HERE / script)], cwd=str(HERE))
    if r.returncode != 0:
        raise SystemExit(f"실패: {script} (exit {r.returncode})")


def main() -> None:
    deploy = "--no-deploy" not in sys.argv

    # 1) chroma 재색인 (위키 .md → 청크 → BGE-M3 임베딩)
    run("build_index.py")

    # 2) HF Space 재배포 (번들 조립 + upload)
    if deploy:
        run("deploy/push_space.py")
        print("\n[OK] 갱신 + 배포 완료. Space가 자동 재빌드됩니다.")
    else:
        print("\n[OK] 재색인 완료 (배포 생략). 배포하려면 --no-deploy 없이 재실행.")


if __name__ == "__main__":
    main()

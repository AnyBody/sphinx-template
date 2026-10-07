
import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO_DIR = Path(__file__).parent.parent / "repos"
VERSION_YAML = Path(__file__).parent.parent / "version.yml"


def get_yaml_value(key: str) -> str:
    text = VERSION_YAML.read_text(encoding="utf-8")
    match = re.search(rf"name:\s*{key}\s*\n\s*value:\s*['\"]?([^\s'\"]+)", text)
    if not match:
        print(f"ERROR: Could not find '{key}' in version.yml", file=sys.stderr)
        sys.exit(1)
    return match.group(1)


def run(args: list[str], **kwargs) -> subprocess.CompletedProcess:
    print(f"  > {' '.join(str(a) for a in args)}")
    result = subprocess.run(args, **kwargs)
    if result.returncode != 0:
        sys.exit(result.returncode)
    return result


def tag_exists(repo_dir: Path, ref: str) -> bool:
    result = subprocess.run(
        ["git", "-C", str(repo_dir), "rev-parse", "--verify", f"refs/tags/{ref}"],
        capture_output=True,
    )
    return result.returncode == 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Checkout repository at a specific tag."
        )
    )
    parser.add_argument(
        "--tag",
        help="version.yml key containing the tag/ref value.",
    )
    parser.add_argument(
        "--url",
        help="version.yml key containing the repository URL.",
    )
    parser.add_argument(
        "--directory",
        help="Checkout directory name under repos (defaults to the ref key).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    ref = get_yaml_value(args.tag)
    url = get_yaml_value(args.url)
    directory = (args.directory or args.tag).format(ref=ref)
    repo_path = REPO_DIR / directory
    out_dir = str(repo_path)

    if not repo_path.exists():
        print(f"Cloning repository into '{out_dir}' ...")
        run(["git", "clone", "--filter=blob:none", url, out_dir])
    else:
        print(f"Directory '{out_dir}' already exists, fetching ...")

    run(["git", "-C", out_dir, "fetch", "--verbose", "--tags", "--force", "origin"])
    print("Fetch completed.")

    if tag_exists(repo_path, ref):
        print(f"Checking out tag: {ref}")
        run(["git", "-C", out_dir, "checkout", "--detach", ref])
    else:
        print(f"Tag not found, checking out remote branch: origin/{ref}")
        run(["git", "-C", out_dir, "checkout", "--detach", f"origin/{ref}"])

    print("Done.")


if __name__ == "__main__":
    main()

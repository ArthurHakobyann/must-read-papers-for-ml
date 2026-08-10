#!/usr/bin/env python3
"""Update the README progress badge from paper-table status markers."""

from pathlib import Path
import re


README = Path(__file__).resolve().parents[1] / "README.md"
STATUS = re.compile(r"^\|\s*(?P<mark>⬜|✅)\s*\|", re.MULTILINE)
PROGRESS_BLOCK = re.compile(
    r"<!-- progress:start -->.*?<!-- progress:end -->", re.DOTALL
)


def main() -> None:
    content = README.read_text(encoding="utf-8")
    marks = [match.group("mark") for match in STATUS.finditer(content)]
    if not marks:
        raise SystemExit("README contains no paper status markers")

    completed = marks.count("✅")
    total = len(marks)

    badge = (
        "<!-- progress:start -->\n"
        "[![Reading progress](https://img.shields.io/badge/"
        f"read-{completed}%20of%20{total}-2ea44f?style=flat-square)](#reading-system)\n"
        "<!-- progress:end -->"
    )

    updated, replacements = PROGRESS_BLOCK.subn(badge, content, count=1)
    if replacements != 1:
        raise SystemExit("README progress block is missing or duplicated")

    README.write_text(updated, encoding="utf-8")
    print(f"Reading progress: {completed}/{total}")


if __name__ == "__main__":
    main()

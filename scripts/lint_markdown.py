#!/usr/bin/env python3
"""Basic Markdown fence lint.

This script checks whether fenced code blocks are balanced in Markdown files.
It is intentionally lightweight and does not attempt to fully parse Markdown.
"""

from __future__ import annotations

from pathlib import Path
import re


ROOTS = [
    Path("README.md"),
    Path("CHANGELOG.md"),
    Path("CONTRIBUTING.md"),
    Path("SECURITY.md"),
    Path("skill"),
    Path("examples"),
]


FENCE_RE = re.compile(r"^(`{3,}|~{3,})(.*)$")


def iter_markdown_files() -> list[Path]:
    files: list[Path] = []

    for root in ROOTS:
        if root.is_file() and root.suffix.lower() == ".md":
            files.append(root)
        elif root.is_dir():
            files.extend(sorted(root.rglob("*.md")))

    return sorted(set(files))


def lint_file(path: Path) -> None:
    stack: list[tuple[str, int]] = []

    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            match = FENCE_RE.match(line.rstrip("\n"))
            if not match:
                continue

            fence = match.group(1)
            marker = fence[0]
            length = len(fence)

            if not stack:
                stack.append((marker * length, line_number))
                continue

            opening_fence, opening_line = stack[-1]
            opening_marker = opening_fence[0]
            opening_length = len(opening_fence)

            if marker == opening_marker and length >= opening_length:
                stack.pop()
            else:
                # A different marker inside a fence is treated as literal content.
                continue

    if stack:
        opening_fence, opening_line = stack[-1]
        raise SystemExit(
            f"Unclosed Markdown fence in {path} opened on line {opening_line}: "
            f"{opening_fence}"
        )


def main() -> None:
    files = iter_markdown_files()

    if not files:
        raise SystemExit("No Markdown files found.")

    for path in files:
        lint_file(path)

    print(f"Markdown fence lint passed for {len(files)} files.")


if __name__ == "__main__":
    main()

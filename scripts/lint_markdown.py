#!/usr/bin/env python3
"""Basic Markdown lint.

This script checks whether fenced code blocks are balanced in Markdown files
and rejects known rendering-artifact tokens that should never appear in
repository Markdown examples.
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
    Path("evals"),
    Path("README.zh-CN.md"),
]

FENCE_RE = re.compile(r"^(`{3,}|~{3,})(.*)$")

FORBIDDEN_TOKENS = [
    "$begin:math:text$",
    "$end:math:text$",
    "$begin:math:display$",
    "$end:math:display$",
]


def iter_markdown_files() -> list[Path]:
    """Return Markdown files that should be linted."""
    files: list[Path] = []

    for root in ROOTS:
        if root.is_file() and root.suffix.lower() == ".md":
            files.append(root)
        elif root.is_dir():
            files.extend(sorted(root.rglob("*.md")))

    return sorted(set(files))


def lint_forbidden_tokens(path: Path, text: str) -> None:
    """Reject known rendering artifacts."""
    for token in FORBIDDEN_TOKENS:
        if token in text:
            raise SystemExit(
                f"Forbidden rendering artifact {token!r} found in {path}"
            )


def lint_fences(path: Path, text: str) -> None:
    """Check that fenced Markdown code blocks are balanced."""
    stack: list[tuple[str, int]] = []

    for line_number, line in enumerate(text.splitlines(), start=1):
        match = FENCE_RE.match(line)
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


def lint_file(path: Path) -> None:
    """Lint a single Markdown file."""
    text = path.read_text(encoding="utf-8")
    lint_forbidden_tokens(path, text)
    lint_fences(path, text)


def main() -> None:
    """Run Markdown lint checks."""
    files = iter_markdown_files()

    if not files:
        raise SystemExit("No Markdown files found.")

    for path in files:
        lint_file(path)

    print(f"Markdown lint passed for {len(files)} files.")


if __name__ == "__main__":
    main()

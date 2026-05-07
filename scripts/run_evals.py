#!/usr/bin/env python3
"""Lightweight validation for evaluation cases.

This script does not run an AI model. It validates that eval cases are
well-formed and contain the fields needed for later regression testing.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


CASES_PATH = Path("evals/cases.jsonl")

REQUIRED_KEYS = {
    "id",
    "field",
    "category",
    "input",
    "expected",
    "should_flag",
}


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    """Load a JSONL file with one JSON object per non-empty line."""
    if not path.exists():
        raise FileNotFoundError(f"Missing eval cases file: {path}")

    cases: list[dict[str, Any]] = []

    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped:
                continue

            try:
                item = json.loads(stripped)
            except json.JSONDecodeError as exc:
                raise SystemExit(
                    f"Invalid JSON on line {line_number} of {path}: {exc}"
                ) from exc

            if not isinstance(item, dict):
                raise SystemExit(
                    f"Line {line_number} of {path} is not a JSON object."
                )

            cases.append(item)

    return cases


def validate_case(item: dict[str, Any]) -> None:
    """Validate one eval case."""
    missing = REQUIRED_KEYS - set(item)
    if missing:
        raise SystemExit(
            f"Eval case {item.get('id', '<missing id>')} is missing keys: "
            f"{sorted(missing)}"
        )

    if not isinstance(item["id"], str) or not item["id"]:
        raise SystemExit("Eval case has invalid 'id'.")

    if not isinstance(item["field"], str) or not item["field"]:
        raise SystemExit(f"Eval case {item['id']} has invalid 'field'.")

    if not isinstance(item["category"], str) or not item["category"]:
        raise SystemExit(f"Eval case {item['id']} has invalid 'category'.")

    if not isinstance(item["input"], str) or not item["input"]:
        raise SystemExit(f"Eval case {item['id']} has invalid 'input'.")

    if not isinstance(item["expected"], str) or not item["expected"]:
        raise SystemExit(f"Eval case {item['id']} has invalid 'expected'.")

    if not isinstance(item["should_flag"], bool):
        raise SystemExit(
            f"Eval case {item['id']} has invalid 'should_flag'; expected boolean."
        )


def main() -> None:
    cases = load_jsonl(CASES_PATH)

    seen_ids: set[str] = set()
    positive = 0
    negative = 0

    for item in cases:
        validate_case(item)

        case_id = item["id"]
        if case_id in seen_ids:
            raise SystemExit(f"Duplicate eval case id: {case_id}")
        seen_ids.add(case_id)

        if item["should_flag"]:
            positive += 1
        else:
            negative += 1

    print(f"Loaded {len(cases)} eval cases.")
    print(f"Positive cases: {positive}")
    print(f"Negative cases: {negative}")

    if not cases:
        raise SystemExit("No eval cases found.")

    if positive == 0:
        raise SystemExit("No positive eval cases found.")

    if negative == 0:
        raise SystemExit("No negative eval cases found.")

    print("Eval case validation passed.")


if __name__ == "__main__":
    main()

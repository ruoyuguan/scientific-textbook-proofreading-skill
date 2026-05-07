#!/usr/bin/env python3
"""Validate example JSON reports against the repository schema."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


SCHEMA_PATH = Path("schemas/errata_report.schema.json")
EXAMPLES_DIR = Path("examples/expected_output")


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    if not isinstance(data, dict):
        raise SystemExit(f"{path} must contain a JSON object.")

    return data


def require_type(path: str, value: Any, expected_type: type | tuple[type, ...]) -> None:
    if not isinstance(value, expected_type):
        raise SystemExit(f"{path} has invalid type: expected {expected_type}, got {type(value)}")


def validate_report(report: dict[str, Any], path: Path) -> None:
    required_top_level = [
        "document_title",
        "review_scope",
        "date",
        "issues",
    ]

    for key in required_top_level:
        if key not in report:
            raise SystemExit(f"{path}: missing top-level key {key!r}")

    require_type(f"{path}: document_title", report["document_title"], str)
    require_type(f"{path}: review_scope", report["review_scope"], str)
    require_type(f"{path}: date", report["date"], str)
    require_type(f"{path}: issues", report["issues"], list)

    if not report["issues"]:
        raise SystemExit(f"{path}: issues must not be empty")

    for index, issue in enumerate(report["issues"], start=1):
        if not isinstance(issue, dict):
            raise SystemExit(f"{path}: issue {index} is not an object")

        required_issue_keys = [
            "issue_id",
            "location",
            "issue_title",
            "problem_type",
            "severity",
            "extraction_reliability",
            "verification_method",
            "original",
            "check",
            "judgement",
            "corrected_version",
            "confidence",
        ]

        for key in required_issue_keys:
            if key not in issue:
                raise SystemExit(
                    f"{path}: issue {index} missing required key {key!r}"
                )

        require_type(f"{path}: issue {index} issue_id", issue["issue_id"], str)
        require_type(f"{path}: issue {index} location", issue["location"], str)
        require_type(f"{path}: issue {index} issue_title", issue["issue_title"], str)
        require_type(f"{path}: issue {index} problem_type", issue["problem_type"], list)
        require_type(
            f"{path}: issue {index} verification_method",
            issue["verification_method"],
            list,
        )
        require_type(f"{path}: issue {index} original", issue["original"], str)
        require_type(f"{path}: issue {index} check", issue["check"], str)
        require_type(
            f"{path}: issue {index} corrected_version",
            issue["corrected_version"],
            str,
        )

        if not issue["problem_type"]:
            raise SystemExit(f"{path}: issue {index} problem_type must not be empty")

        if not issue["verification_method"]:
            raise SystemExit(
                f"{path}: issue {index} verification_method must not be empty"
            )


def main() -> None:
    if not SCHEMA_PATH.exists():
        raise SystemExit(f"Missing schema: {SCHEMA_PATH}")

    # Parse schema to ensure it is valid JSON. Full JSON Schema validation is
    # intentionally not required here so the repository has no external
    # dependencies.
    load_json(SCHEMA_PATH)

    json_reports = sorted(EXAMPLES_DIR.glob("*.json"))

    if not json_reports:
        raise SystemExit(f"No example JSON reports found in {EXAMPLES_DIR}")

    for report_path in json_reports:
        report = load_json(report_path)
        validate_report(report, report_path)

    print(f"Validated {len(json_reports)} example JSON report(s).")


if __name__ == "__main__":
    main()

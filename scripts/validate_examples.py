#!/usr/bin/env python3
"""Validate example JSON reports against the repository schema conventions.

This script intentionally avoids external dependencies. It does not implement
full JSON Schema validation, but it checks the fields and enum values that are
most important for repository examples.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


SCHEMA_PATH = Path("schemas/errata_report.schema.json")
EXAMPLES_DIR = Path("examples/expected_output")

ISSUE_ID_RE = re.compile(r"^CH[0-9]{2}-[0-9]{3}$")

PROBLEM_TYPES = {
    "formula_error",
    "dimensional_inconsistency",
    "wrong_numerical_coefficient",
    "wrong_physical_assumption",
    "wrong_physical_regime",
    "missing_approximation_regime",
    "unit_system_mismatch",
    "notation_conflict",
    "ambiguous_notation",
    "inconsistent_cross_reference",
    "misleading_prose",
    "overstrong_claim",
    "outdated_scientific_claim",
    "source_inconsistency",
    "numerical_error",
    "pedagogical_clarification",
    "pdf_extraction_uncertainty",
}

SEVERITIES = {
    "critical",
    "major",
    "minor",
    "clarification",
}

EXTRACTION_RELIABILITY = {
    "high",
    "medium",
    "low",
}

VERIFICATION_METHODS = {
    "first_principles_derivation",
    "dimensional_analysis",
    "limiting_case_check",
    "numerical_reproduction",
    "source_comparison",
    "cross_reference_check",
    "current_status_check",
    "notation_consistency_check",
    "unit_system_check",
    "manual_visual_check_required",
}

SOURCE_TYPES = {
    "manuscript_internal",
    "reference_textbook",
    "peer_reviewed_paper",
    "official_collaboration_source",
    "mission_or_catalog_documentation",
    "current_web_source",
    "derivation_only",
    "manual_check_required",
}

JUDGEMENTS = {
    "Confirmed error",
    "Likely error",
    "Convention-dependent",
    "Ambiguous",
    "Correct but misleading",
    "Correct but should be clarified",
    "Outdated but historically understandable",
    "No correction needed",
}

CONFIDENCE_VALUES = {
    "High",
    "Medium",
    "Low",
}


def load_json(path: Path) -> dict[str, Any]:
    """Load a JSON object from a file."""
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    if not isinstance(data, dict):
        raise SystemExit(f"{path} must contain a JSON object.")

    return data


def require_type(path: str, value: Any, expected_type: type | tuple[type, ...]) -> None:
    """Require a value to have a given Python type."""
    if not isinstance(value, expected_type):
        raise SystemExit(
            f"{path} has invalid type: expected {expected_type}, got {type(value)}"
        )


def require_nonempty_string(path: str, value: Any) -> None:
    """Require a non-empty string."""
    require_type(path, value, str)
    if not value.strip():
        raise SystemExit(f"{path} must not be empty.")


def require_enum(path: str, value: Any, allowed: set[str]) -> None:
    """Require a string value to be in a fixed enum."""
    require_nonempty_string(path, value)
    if value not in allowed:
        raise SystemExit(
            f"{path} has invalid value {value!r}. Allowed values: {sorted(allowed)}"
        )


def require_enum_list(path: str, values: Any, allowed: set[str]) -> None:
    """Require a non-empty list of enum strings."""
    require_type(path, values, list)

    if not values:
        raise SystemExit(f"{path} must not be empty.")

    for index, value in enumerate(values, start=1):
        require_enum(f"{path}[{index}]", value, allowed)


def validate_source(source: dict[str, Any], path: str) -> None:
    """Validate one source object."""
    required_source_keys = [
        "type",
        "description",
    ]

    for key in required_source_keys:
        if key not in source:
            raise SystemExit(f"{path}: missing required source key {key!r}")

    require_enum(f"{path}.type", source["type"], SOURCE_TYPES)
    require_nonempty_string(f"{path}.description", source["description"])

    for optional_key in ["title", "location", "url", "access_date"]:
        if optional_key in source and source[optional_key] is not None:
            require_type(f"{path}.{optional_key}", source[optional_key], str)


def validate_issue(issue: dict[str, Any], path: Path, index: int) -> None:
    """Validate one issue object."""
    issue_path = f"{path}: issue {index}"

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
            raise SystemExit(f"{issue_path}: missing required key {key!r}")

    require_nonempty_string(f"{issue_path}.issue_id", issue["issue_id"])
    if not ISSUE_ID_RE.match(issue["issue_id"]):
        raise SystemExit(
            f"{issue_path}.issue_id must match CHNN-XXX format, got "
            f"{issue['issue_id']!r}"
        )

    require_nonempty_string(f"{issue_path}.location", issue["location"])
    require_nonempty_string(f"{issue_path}.issue_title", issue["issue_title"])
    require_enum_list(f"{issue_path}.problem_type", issue["problem_type"], PROBLEM_TYPES)
    require_enum(f"{issue_path}.severity", issue["severity"], SEVERITIES)
    require_enum(
        f"{issue_path}.extraction_reliability",
        issue["extraction_reliability"],
        EXTRACTION_RELIABILITY,
    )
    require_enum_list(
        f"{issue_path}.verification_method",
        issue["verification_method"],
        VERIFICATION_METHODS,
    )
    require_nonempty_string(f"{issue_path}.original", issue["original"])
    require_nonempty_string(f"{issue_path}.check", issue["check"])
    require_enum(f"{issue_path}.judgement", issue["judgement"], JUDGEMENTS)
    require_nonempty_string(
        f"{issue_path}.corrected_version", issue["corrected_version"]
    )
    require_enum(f"{issue_path}.confidence", issue["confidence"], CONFIDENCE_VALUES)

    if "sources" in issue:
        require_type(f"{issue_path}.sources", issue["sources"], list)
        for source_index, source in enumerate(issue["sources"], start=1):
            require_type(
                f"{issue_path}.sources[{source_index}]",
                source,
                dict,
            )
            validate_source(source, f"{issue_path}.sources[{source_index}]")

    for optional_key in [
        "section",
        "equation_or_figure",
        "suggested_replacement_prose",
        "human_review_note",
    ]:
        if optional_key in issue and issue[optional_key] is not None:
            require_type(f"{issue_path}.{optional_key}", issue[optional_key], str)

    if "page" in issue and issue["page"] is not None:
        if not isinstance(issue["page"], (int, str)):
            raise SystemExit(
                f"{issue_path}.page must be integer, string, or null; got "
                f"{type(issue['page'])}"
            )


def validate_report(report: dict[str, Any], path: Path) -> None:
    """Validate one report object."""
    required_top_level = [
        "document_title",
        "review_scope",
        "date",
        "issues",
    ]

    for key in required_top_level:
        if key not in report:
            raise SystemExit(f"{path}: missing top-level key {key!r}")

    require_nonempty_string(f"{path}.document_title", report["document_title"])
    require_nonempty_string(f"{path}.review_scope", report["review_scope"])
    require_nonempty_string(f"{path}.date", report["date"])
    require_type(f"{path}.issues", report["issues"], list)

    if not report["issues"]:
        raise SystemExit(f"{path}: issues must not be empty")

    seen_issue_ids: set[str] = set()

    for index, issue in enumerate(report["issues"], start=1):
        require_type(f"{path}: issue {index}", issue, dict)
        validate_issue(issue, path, index)

        issue_id = issue["issue_id"]
        if issue_id in seen_issue_ids:
            raise SystemExit(f"{path}: duplicate issue_id {issue_id!r}")
        seen_issue_ids.add(issue_id)


def main() -> None:
    """Validate example JSON files."""
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

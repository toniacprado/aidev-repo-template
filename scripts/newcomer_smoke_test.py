#!/usr/bin/env python3
"""Run a deterministic newcomer-readiness smoke test for this template."""

from __future__ import annotations

import importlib
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))


@dataclass(frozen=True)
class CheckResult:
    name: str
    passed: bool
    detail: str


def _check_path_exists(path: Path, label: str) -> CheckResult:
    return CheckResult(
        name=label,
        passed=path.exists(),
        detail=f"expected path: {path.relative_to(ROOT)}",
    )


def _check_file_contains(path: Path, needle: str, label: str) -> CheckResult:
    text = path.read_text(encoding="utf-8")
    return CheckResult(
        name=label,
        passed=needle in text,
        detail=f"expected to find `{needle}` in {path.relative_to(ROOT)}",
    )


def run_newcomer_smoke_checks(repo_root: Path) -> list[CheckResult]:
    runner = importlib.import_module("repo_template.prompt_eval_runner")
    run_golden_eval_suite = runner.run_golden_eval_suite
    validate_prompt_eval_links = runner.validate_prompt_eval_links

    checks: list[CheckResult] = []

    checks.append(
        _check_path_exists(repo_root / "docs" / "CODEX_FIRST_HOUR.md", "first-hour-guide")
    )
    checks.append(
        _check_file_contains(
            repo_root / "README.md",
            "docs/CODEX_FIRST_HOUR.md",
            "readme-links-first-hour-guide",
        )
    )
    checks.append(
        _check_file_contains(
            repo_root / "README.md",
            "bootstrap_new_project.py",
            "readme-links-cross-platform-bootstrap",
        )
    )
    checks.append(
        _check_path_exists(
            repo_root / "docs" / "NEWCOMER_USABILITY_CHECKLIST.md",
            "newcomer-checklist-doc",
        )
    )
    checks.append(
        _check_file_contains(
            repo_root / "docs" / "REPO_BOOTSTRAP_CHECKLIST.md",
            "bootstrap_new_project.py",
            "bootstrap-checklist-links-python-bootstrap",
        )
    )
    checks.append(
        _check_path_exists(
            repo_root / "scripts" / "bootstrap_new_project.py",
            "cross-platform-bootstrap-script",
        )
    )
    checks.append(
        _check_path_exists(
            repo_root / "prompts" / "PROMPT-001-repo-change-triage.md",
            "starter-prompt-asset",
        )
    )
    checks.append(
        _check_path_exists(
            repo_root / "evals" / "EVAL-001-repo-change-triage.md",
            "starter-eval-asset",
        )
    )
    checks.append(
        _check_path_exists(
            repo_root / "codex" / "rules" / "default.rules.example",
            "codex-rules-scaffolding",
        )
    )
    checks.append(
        _check_path_exists(
            repo_root / ".agents" / "skills" / "codex-task-slice" / "SKILL.md",
            "task-slice-skill",
        )
    )
    checks.append(
        _check_path_exists(
            repo_root / ".agents" / "skills" / "codex-review" / "SKILL.md",
            "review-skill",
        )
    )
    checks.append(
        _check_path_exists(
            repo_root / ".github" / "ISSUE_TEMPLATE" / "codex-task-slice.yml",
            "issue-template-task-slice",
        )
    )

    link_errors = validate_prompt_eval_links(repo_root)
    checks.append(
        CheckResult(
            name="prompt-eval-links",
            passed=not link_errors,
            detail="linked prompt/eval frontmatter must be reciprocal",
        )
    )

    golden_results = run_golden_eval_suite(repo_root)
    mismatches = [result for result in golden_results if not result.matched]
    checks.append(
        CheckResult(
            name="golden-eval-suite",
            passed=bool(golden_results) and not mismatches,
            detail="golden fixtures should match expected pass/fail outcomes",
        )
    )

    has_pwsh = bool(shutil.which("pwsh") or shutil.which("powershell"))
    checks.append(
        CheckResult(
            name="powershell-available",
            passed=has_pwsh,
            detail="recommended for local bootstrap-script smoke tests",
        )
    )

    return checks


def main() -> int:
    checks = run_newcomer_smoke_checks(ROOT)
    failures = [
        check for check in checks if not check.passed and check.name != "powershell-available"
    ]
    warnings = [
        check for check in checks if not check.passed and check.name == "powershell-available"
    ]

    print("Newcomer smoke test results:")
    for check in checks:
        status = "OK" if check.passed else "FAIL"
        if check.name == "powershell-available" and not check.passed:
            status = "WARN"
        print(f"  {status}: {check.name} - {check.detail}")

    if warnings:
        print(
            "  WARN: PowerShell is unavailable; "
            "bootstrap script smoke checks may be skipped locally."
        )

    if failures:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

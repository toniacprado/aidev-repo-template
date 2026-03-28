#!/usr/bin/env python3
"""Run a deterministic newcomer-readiness smoke test for this template."""

from __future__ import annotations

import importlib
import importlib.util
import shutil
import sys
import tempfile
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


def _check_python_bootstrap_behavior(repo_root: Path) -> CheckResult:
    bootstrap_script = repo_root / "scripts" / "bootstrap_new_project.py"
    spec = importlib.util.spec_from_file_location("bootstrap_new_project", bootstrap_script)
    if not spec or not spec.loader:
        return CheckResult(
            name="python-bootstrap-behavior",
            passed=False,
            detail="unable to load scripts/bootstrap_new_project.py for behavioral check",
        )

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_root = Path(temp_dir)
        (temp_root / "work" / "items").mkdir(parents=True, exist_ok=True)
        (temp_root / "README.md").write_text("# AI Dev Repo Template\n", encoding="utf-8")
        (temp_root / "pyproject.toml").write_text(
            '[project]\nname = "aidev-repo-template"\nversion = "0.7.0"\n',
            encoding="utf-8",
        )
        (temp_root / "CHANGELOG.md").write_text("# Changelog\n", encoding="utf-8")
        (temp_root / "work" / "ACTIVE_TASKS.md").write_text("# Active Tasks\n", encoding="utf-8")
        (temp_root / "work" / "LEARNINGS.md").write_text("# Durable Learnings\n", encoding="utf-8")
        (temp_root / "work" / "items" / "TEMPLATE-001-sample.md").write_text(
            "# Template item\n", encoding="utf-8"
        )

        slug = module.run_bootstrap(
            repo_root=temp_root,
            project_name="Trial Project",
            project_slug="trial-project",
        )
        readme = (temp_root / "README.md").read_text(encoding="utf-8")
        active_tasks = (temp_root / "work" / "ACTIVE_TASKS.md").read_text(encoding="utf-8")
        session_starter = temp_root / "docs" / "CODEX_SESSION_STARTER.md"
        artifact_workshop = temp_root / "docs" / "BOOTSTRAP_ARTIFACT_WORKSHOP.md"
        bootstrap_guide = temp_root / "docs" / "BOOTSTRAP_NEXT_STEPS.md"
        start_here = (temp_root / "docs" / "START_HERE.md").read_text(encoding="utf-8")
        manifesto = (temp_root / "docs" / "PROJECT_MANIFESTO.md").read_text(encoding="utf-8")
        decisions = (temp_root / "docs" / "DECISIONS.md").read_text(encoding="utf-8")
        session_starter_text = session_starter.read_text(encoding="utf-8")
        artifact_workshop_text = artifact_workshop.read_text(encoding="utf-8")
        bootstrap_item = temp_root / "work" / "items" / "BOOTSTRAP-001-initialize-project.md"
        no_template_items = not list((temp_root / "work" / "items").glob("TEMPLATE-*.md"))
        passed = (
            slug == "trial-project"
            and "docs/CODEX_SESSION_STARTER.md" in readme
            and "Project-facing draft docs were generated" in readme
            and session_starter.exists()
            and artifact_workshop.exists()
            and bootstrap_guide.exists()
            and "docs/CODEX_SESSION_STARTER.md" in start_here
            and "docs/CONTEXT_ENGINEERING.md" in start_here
            and "docs/GIT_WORKFLOW.md" in start_here
            and "Trial Project" in manifesto
            and "Trial Project should strongly recommend finishing the core bootstrap" in decisions
            and "Context: Read README.md, AGENTS.md, docs/CONTEXT_ENGINEERING.md"
            in session_starter_text
            and "## Artifact 2: Landing Docs" in artifact_workshop_text
            and "docs/CONTEXT_ENGINEERING.md" in bootstrap_guide.read_text(encoding="utf-8")
            and "docs/GIT_WORKFLOW.md" in bootstrap_guide.read_text(encoding="utf-8")
            and bootstrap_item.exists()
            and "docs/CONTEXT_ENGINEERING.md" in bootstrap_item.read_text(encoding="utf-8")
            and "docs/GIT_WORKFLOW.md" in bootstrap_item.read_text(encoding="utf-8")
            and "BOOTSTRAP-001" in active_tasks
            and no_template_items
        )

    return CheckResult(
        name="python-bootstrap-behavior",
        passed=passed,
        detail=(
            "python bootstrap should generate Codex handoff docs, project-draft docs, "
            "BOOTSTRAP-001, and clear TEMPLATE-* items"
        ),
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
        _check_path_exists(
            repo_root / "docs" / "CONTEXT_ENGINEERING.md",
            "context-engineering-doc",
        )
    )
    checks.append(
        _check_path_exists(
            repo_root / "docs" / "GIT_WORKFLOW.md",
            "git-workflow-doc",
        )
    )
    checks.append(
        _check_file_contains(
            repo_root / "AGENTS.md",
            "Fresh repo bootstrap mode",
            "agents-bootstrap-mode-guidance",
        )
    )
    checks.append(
        _check_file_contains(
            repo_root / "AGENTS.md",
            "Do not suggest rerunning `scripts/bootstrap_new_project.py`",
            "agents-no-rerun-bootstrap-guidance",
        )
    )
    checks.append(
        _check_file_contains(
            repo_root / "AGENTS.md",
            "docs/CONTEXT_ENGINEERING.md",
            "agents-links-context-guide",
        )
    )
    checks.append(
        _check_file_contains(
            repo_root / "docs" / "CODEX_FIRST_HOUR.md",
            "docs/CODEX_SESSION_STARTER.md",
            "first-hour-links-session-starter",
        )
    )
    checks.append(
        _check_file_contains(
            repo_root / "docs" / "CODEX_FIRST_HOUR.md",
            "docs/CONTEXT_ENGINEERING.md",
            "first-hour-links-context-guide",
        )
    )
    checks.append(
        _check_file_contains(
            repo_root / "docs" / "CODEX_FIRST_HOUR.md",
            "docs/GIT_WORKFLOW.md",
            "first-hour-links-git-guide",
        )
    )
    checks.append(
        _check_file_contains(
            repo_root / "README.md",
            "docs/CODEX_SESSION_STARTER.md",
            "readme-links-session-starter",
        )
    )
    checks.append(
        _check_file_contains(
            repo_root / "README.md",
            "docs/CONTEXT_ENGINEERING.md",
            "readme-links-context-guide",
        )
    )
    checks.append(
        _check_file_contains(
            repo_root / "README.md",
            "docs/GIT_WORKFLOW.md",
            "readme-links-git-guide",
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
        _check_file_contains(
            repo_root / "docs" / "TASK_MANAGEMENT.md",
            "Compaction checkpoints",
            "task-management-compaction-guidance",
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
        _check_file_contains(
            repo_root / "docs" / "REPO_BOOTSTRAP_CHECKLIST.md",
            "docs/CONTEXT_ENGINEERING.md",
            "bootstrap-checklist-links-context-guide",
        )
    )
    checks.append(
        _check_file_contains(
            repo_root / "docs" / "REPO_BOOTSTRAP_CHECKLIST.md",
            "docs/GIT_WORKFLOW.md",
            "bootstrap-checklist-links-git-guide",
        )
    )
    checks.append(
        _check_file_contains(
            repo_root / "docs" / "HUMAN_OPERATING_GUIDE.md",
            "docs/CONTEXT_ENGINEERING.md",
            "human-guide-links-context-guide",
        )
    )
    checks.append(
        _check_file_contains(
            repo_root / "docs" / "HUMAN_OPERATING_GUIDE.md",
            "docs/GIT_WORKFLOW.md",
            "human-guide-links-git-guide",
        )
    )
    checks.append(
        _check_file_contains(
            repo_root / "docs" / "HUMAN_OPERATING_GUIDE.md",
            "compact the durable state into `work/`",
            "human-guide-compaction-guidance",
        )
    )
    checks.append(
        _check_path_exists(
            repo_root / "scripts" / "bootstrap_new_project.py",
            "cross-platform-bootstrap-script",
        )
    )
    checks.append(_check_python_bootstrap_behavior(repo_root))
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

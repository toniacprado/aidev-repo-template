#!/usr/bin/env python3
"""Bootstrap a fresh project from this Codex-first template."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


def convert_to_slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not slug:
        raise ValueError("Could not derive a project slug from project name.")
    return slug


def _assert_paths(repo_root: Path, required_paths: list[str]) -> None:
    missing = [path for path in required_paths if not (repo_root / path).exists()]
    if missing:
        joined = ", ".join(missing)
        raise FileNotFoundError(f"Expected required paths are missing: {joined}")


def _rewrite_readme(repo_root: Path, project_name: str) -> None:
    readme_path = repo_root / "README.md"
    current_text = readme_path.read_text(encoding="utf-8")
    updated_text, replacements = re.subn(
        r"(?m)^# .+$",
        f"# {project_name}",
        current_text,
        count=1,
    )
    if replacements == 0:
        raise RuntimeError("Could not replace the README title line.")
    readme_path.write_text(updated_text, encoding="utf-8")


def _rewrite_pyproject(repo_root: Path, project_slug: str) -> None:
    pyproject_path = repo_root / "pyproject.toml"
    lines = pyproject_path.read_text(encoding="utf-8").splitlines()

    replaced = False
    updated_lines: list[str] = []
    for line in lines:
        if not replaced and re.match(r'^name\s*=\s*".*"$', line):
            updated_lines.append(f'name = "{project_slug}"')
            replaced = True
        else:
            updated_lines.append(line)

    if not replaced:
        raise RuntimeError('Could not update `name = "..."` in pyproject.toml.')

    pyproject_path.write_text("\n".join(updated_lines) + "\n", encoding="utf-8")


def _write_changelog(repo_root: Path, project_name: str, today: str) -> None:
    changelog = (
        "# Changelog\n"
        "*Version:* v0.1  \n"
        f"*Date:* {today}  \n"
        f"*Last reviewed:* {today}\n\n"
        "## Unreleased\n"
        f"- Initialized {project_name} from the Codex-first repo template.\n"
    )
    (repo_root / "CHANGELOG.md").write_text(changelog, encoding="utf-8")


def _write_active_tasks(repo_root: Path, project_name: str, today: str) -> None:
    task_title = f"Initialize {project_name} from the Codex-first template"
    task_next_action = (
        "Rewrite the manifesto and charter, then choose the real stack and verification path"
    )
    active_tasks = (
        "# Active Tasks\n"
        "*Version:* v0.1  \n"
        f"*Date:* {today}  \n"
        f"*Last reviewed:* {today}\n\n"
        "This file is the canonical current task list for the repo.\n\n"
        "## Active\n"
        "| ID | Title | Status | Owner | Next action | Last updated |\n"
        "| --- | --- | --- | --- | --- | --- |\n"
        f"| BOOTSTRAP-001 | {task_title} | todo | human | {task_next_action} | {today} |\n\n"
        "## Rules\n"
        "- Update status and next action before ending meaningful work.\n"
        "- Link to a detailed file in `work/items/` when a task needs history or acceptance\n"
        "  criteria.\n"
        "- Capture durable discoveries in `work/LEARNINGS.md` when they should influence\n"
        "  future work.\n"
        "- Remove or archive stale rows once the task is truly done.\n"
    )
    (repo_root / "work" / "ACTIVE_TASKS.md").write_text(active_tasks, encoding="utf-8")


def _write_learnings(repo_root: Path, today: str) -> None:
    learnings = (
        "# Durable Learnings\n"
        "*Version:* v0.1  \n"
        f"*Date:* {today}  \n"
        f"*Last reviewed:* {today}\n\n"
        "Use this file for discoveries that should influence future work but do not fit neatly in\n"
        "a single task file.\n\n"
        "## Entries\n"
    )
    (repo_root / "work" / "LEARNINGS.md").write_text(learnings, encoding="utf-8")


def _write_bootstrap_item(repo_root: Path, project_name: str, today: str) -> None:
    item_next_action = (
        "Rewrite docs/PROJECT_MANIFESTO.md and docs/PROJECT_CHARTER.md for the real project."
    )
    bootstrap_item = (
        "---\n"
        "template: work_item\n"
        "template_version: 0.4\n"
        "template_date: 2026-03-11\n"
        "template_last_reviewed: 2026-03-11\n"
        "type: work_item\n"
        "item_id: BOOTSTRAP-001\n"
        f"title: Initialize {project_name} from the Codex-first template\n"
        "status: todo\n"
        "owner: human\n"
        f"updated: {today}\n"
        f"next_action: {item_next_action}\n"
        "blocked_on: none\n"
        "---\n\n"
        f"# Initialize {project_name} from the Codex-first template\n\n"
        "## Summary\n"
        "- Replace the remaining template identity with the real project's intent, scope, stack,\n"
        "  and first task queue.\n\n"
        "## Acceptance Criteria\n"
        "- `README.md` reflects the real project name.\n"
        "- `docs/PROJECT_MANIFESTO.md` is rewritten for the real project.\n"
        "- `docs/PROJECT_CHARTER.md` is rewritten for the real project.\n"
        "- `docs/TECH_STACK_SELECTION.md` reflects the real stack choice.\n"
        "- `work/ACTIVE_TASKS.md` reflects the real next step.\n\n"
        "## Progress Log\n"
        f"- {today}: bootstrap task created from the template.\n\n"
        "## Verification\n"
        "- not run yet\n\n"
        "## Next Action\n"
        "- Rewrite `docs/PROJECT_MANIFESTO.md` and `docs/PROJECT_CHARTER.md` for the real\n"
        "  project.\n\n"
        "## Notes\n"
        "- Review `docs/REPO_BOOTSTRAP_CHECKLIST.md` before the first real feature.\n"
    )
    item_path = repo_root / "work" / "items" / "BOOTSTRAP-001-initialize-project.md"
    item_path.write_text(bootstrap_item, encoding="utf-8")


def _clear_template_items(repo_root: Path) -> None:
    for item_path in (repo_root / "work" / "items").glob("TEMPLATE-*.md"):
        item_path.unlink()


def run_bootstrap(repo_root: Path, project_name: str, project_slug: str | None = None) -> str:
    slug = project_slug or convert_to_slug(project_name)
    today = date.today().isoformat()

    _assert_paths(
        repo_root,
        [
            "README.md",
            "pyproject.toml",
            "CHANGELOG.md",
            "work/ACTIVE_TASKS.md",
            "work/LEARNINGS.md",
            "work/items",
        ],
    )
    _rewrite_readme(repo_root, project_name)
    _rewrite_pyproject(repo_root, slug)
    _write_changelog(repo_root, project_name, today)
    _write_active_tasks(repo_root, project_name, today)
    _write_learnings(repo_root, today)
    _write_bootstrap_item(repo_root, project_name, today)
    _clear_template_items(repo_root)

    return slug


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--project-name",
        "-ProjectName",
        required=True,
        help="Human-readable project name, used in docs and task scaffolding.",
    )
    parser.add_argument(
        "--project-slug",
        "-ProjectSlug",
        default=None,
        help="Optional package/repo slug. If omitted, one is derived from project name.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path.cwd()
    slug = run_bootstrap(repo_root, args.project_name, args.project_slug)

    print(f"Bootstrap complete for {args.project_name} ({slug}).")
    print(
        "Next: rewrite docs/PROJECT_MANIFESTO.md, docs/PROJECT_CHARTER.md, "
        "and docs/TECH_STACK_SELECTION.md."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Bootstrap a fresh project from this Codex-first template."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path
from textwrap import dedent


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


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _write_readme(repo_root: Path, project_name: str, project_slug: str, today: str) -> None:
    readme = dedent(
        f"""\
        # {project_name}

        This repository was bootstrapped from the Codex-first template on {today}. The repo
        structure is ready, but the product definition is still in draft form.

        ## Start Here
        1. Read `docs/BOOTSTRAP_NEXT_STEPS.md`.
        2. Rewrite `docs/PROJECT_MANIFESTO.md` for the real product.
        3. Rewrite `docs/PROJECT_CHARTER.md` with the first-release scope and non-goals.
        4. Decide whether to keep or replace the inherited maintenance stack in
           `docs/TECH_STACK_SELECTION.md`.
        5. Update `work/items/BOOTSTRAP-001-initialize-project.md` and `work/ACTIVE_TASKS.md`
           before starting the first feature.

        ## Current Bootstrap Status
        - Project name initialized as `{project_name}`.
        - Project slug initialized as `{project_slug}`.
        - Template-only work items were removed.
        - Project-facing draft docs were generated for the manifesto, charter, stack
          decision, and first-session guide.
        - Placeholder text still needs to be replaced before feature work begins.

        ## If You Want Codex To Help
        Use a prompt shaped like this:

        ```text
        Goal: Turn the placeholder project docs into a real first-pass spec.
        Context: Read AGENTS.md, docs/BOOTSTRAP_NEXT_STEPS.md, docs/PROJECT_MANIFESTO.md,
        docs/PROJECT_CHARTER.md, docs/TECH_STACK_SELECTION.md, and
        work/items/BOOTSTRAP-001-initialize-project.md.
        Constraints: Keep the scope to project-definition docs. Do not start feature
        implementation yet.
        Done when: README, manifesto, charter, stack selection, and work tracking reflect
        the real project.
        ```

        ## Verification
        If you are keeping the template's maintenance stack for now, create a virtual
        environment and run the default checks described in `docs/BOOTSTRAP_NEXT_STEPS.md`.
        """
    )
    _write_text(repo_root / "README.md", readme)


def _write_changelog(repo_root: Path, project_name: str, today: str) -> None:
    changelog = dedent(
        f"""\
        # Changelog
        *Version:* v0.1
        *Date:* {today}
        *Last reviewed:* {today}

        ## Unreleased
        - Initialized {project_name} from the Codex-first repo template.
        """
    )
    _write_text(repo_root / "CHANGELOG.md", changelog)


def _write_start_here(repo_root: Path, project_name: str, today: str) -> None:
    start_here = dedent(
        f"""\
        # Start Here
        *Version:* v0.1
        *Date:* {today}
        *Last reviewed:* {today}

        This is the shortest useful path for the first working session in {project_name}.

        ## First Session
        1. Read `docs/BOOTSTRAP_NEXT_STEPS.md`.
        2. Rewrite `docs/PROJECT_MANIFESTO.md` so it describes the real user problem.
        3. Rewrite `docs/PROJECT_CHARTER.md` with scope, users, success metrics, and
           non-goals.
        4. Update `docs/TECH_STACK_SELECTION.md` with the actual stack and verification plan.
        5. Confirm the next real task in `work/items/BOOTSTRAP-001-initialize-project.md`.

        ## Guidance To Keep
        These files stay useful after the product docs are rewritten:
        - `AGENTS.md`
        - `docs/AI_DEV_WORKFLOW.md`
        - `docs/CODEX_PROMPTING.md`
        - `docs/TASK_MANAGEMENT.md`
        - `docs/GUARDRAILS.md`
        - `docs/MODEL_POLICY.md`

        ## After This
        Once the project-definition docs are real, choose the first small implementation
        slice and keep docs, tests, and `work/` aligned in the same diff.
        """
    )
    _write_text(repo_root / "docs" / "START_HERE.md", start_here)


def _write_bootstrap_next_steps(
    repo_root: Path, project_name: str, project_slug: str, today: str
) -> None:
    bootstrap_guide = dedent(
        f"""\
        # Bootstrap Next Steps
        *Version:* v0.1
        *Date:* {today}
        *Last reviewed:* {today}

        This guide is the primary post-bootstrap handoff for {project_name}. Complete the
        steps below before feature work so the repo stops reading like a template and starts
        reading like your project.

        ## What Bootstrap Already Did
        - Renamed the repo landing page to `{project_name}`.
        - Set the project slug to `{project_slug}` in `pyproject.toml`.
        - Reset `CHANGELOG.md`, `work/ACTIVE_TASKS.md`, and `work/LEARNINGS.md`.
        - Removed template-only work items under `work/items/TEMPLATE-*.md`.
        - Generated project-draft placeholders for the manifesto, charter, stack decision,
          and this guide.

        ## Complete These Steps Now
        1. Rewrite `docs/PROJECT_MANIFESTO.md`.
           Done when: a new contributor can explain why the project exists and what it will
           not do yet.
        2. Rewrite `docs/PROJECT_CHARTER.md`.
           Done when: scope, users, success metrics, and non-goals are explicit.
        3. Rewrite `docs/TECH_STACK_SELECTION.md`.
           Done when: the real implementation stack and verification path are named, even if
           some decisions are provisional.
        4. Replace any remaining placeholder wording in `README.md` and `docs/START_HERE.md`.
           Done when: the repo no longer presents itself as the template.
        5. Update `work/items/BOOTSTRAP-001-initialize-project.md` and `work/ACTIVE_TASKS.md`.
           Done when: another contributor can see the next real task without chat history.

        ## If You Want Codex To Do The First Pass
        Use a prompt like this:

        ```text
        Goal: Convert the bootstrapped placeholder docs into a real project definition.
        Context: Read AGENTS.md, docs/BOOTSTRAP_NEXT_STEPS.md, docs/PROJECT_MANIFESTO.md,
        docs/PROJECT_CHARTER.md, docs/TECH_STACK_SELECTION.md, and
        work/items/BOOTSTRAP-001-initialize-project.md.
        Constraints: Do not start feature implementation. Keep the diff focused on project
        definition and onboarding clarity.
        Done when: the project docs, README, and work tracking describe the real product and
        the next implementation task.
        ```

        ## Current Setup Commands
        If you want to keep the template's maintenance stack temporarily, use these commands.

        macOS/Linux:

        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        python -m pip install --upgrade pip
        python -m pip install -e ".[dev]"
        ```

        Windows PowerShell:

        ```powershell
        python -m venv .venv
        .\\.venv\\Scripts\\Activate.ps1
        python -m pip install --upgrade pip
        python -m pip install -e ".[dev]"
        ```

        Default verification while the maintenance stack is still in place:

        ```text
        ruff format .
        ruff check .
        pytest -q
        python scripts/run_prompt_evals.py
        python scripts/newcomer_smoke_test.py
        ```

        ## Before The First Feature
        - Work through `docs/REPO_BOOTSTRAP_CHECKLIST.md`.
        - Add at least one real decision entry in `docs/DECISIONS.md`.
        - Make sure `work/ACTIVE_TASKS.md` points at the first product slice, not bootstrap
          cleanup.
        """
    )
    _write_text(repo_root / "docs" / "BOOTSTRAP_NEXT_STEPS.md", bootstrap_guide)


def _write_manifesto(repo_root: Path, project_name: str, today: str) -> None:
    manifesto = dedent(
        f"""\
        # Project Manifesto
        *Version:* v0.1
        *Date:* {today}
        *Last reviewed:* {today}

        This draft was generated during bootstrap for {project_name}. Replace the starter
        prompts below with plain-language statements before feature work begins.

        ## Why This Exists
        - Replace this with the concrete problem {project_name} should solve.
        - Replace this with the user or team who feels that problem most sharply.
        - Replace this with the reason this repo is the right place to solve it.

        ## The Promise
        - Replace this with the core outcome users should get from the product.
        - Replace this with the workflow improvement the product should make obvious.
        - Replace this with the trust or reliability bar the product must meet.

        ## Non-Negotiables
        - Keep repo-owned source-of-truth docs so humans and Codex can work from the same
          context.
        - Replace this with the most important product-quality bar.
        - Replace this with the most important safety, privacy, or compliance boundary.

        ## Anti-Goals
        - Replace this with one tempting expansion you will not do in v1.
        - Replace this with one automation or integration you are explicitly deferring.
        - Replace this with one complexity trap that should stay out of scope.

        ## What Good Looks Like First
        - Replace this with the smallest useful outcome for a real user.
        - Replace this with the signal that proves the first release is working.
        - Replace this with the maintenance or handoff behavior you expect from the repo.

        ## Constraints
        - Replace this with platform, environment, or deployment constraints.
        - Replace this with team-capacity or maintenance constraints.
        - Replace this with data, model, or workflow boundaries that cannot be violated.
        """
    )
    _write_text(repo_root / "docs" / "PROJECT_MANIFESTO.md", manifesto)


def _write_charter(repo_root: Path, project_name: str, today: str) -> None:
    charter = dedent(
        f"""\
        # Project Charter
        *Version:* v0.1
        *Date:* {today}
        *Last reviewed:* {today}

        This charter is a starter draft for {project_name}. Replace each placeholder with the
        real first-release boundaries before implementation starts.

        ## Scope
        ### In Scope For The First Release
        - Replace this with the smallest end-to-end workflow the product must support.
        - Replace this with the most important user-visible behavior to get right first.
        - Replace this with the supporting capability that must exist for the workflow to work.

        ### Out Of Scope For Now
        - Replace this with a tempting feature that can wait.
        - Replace this with a platform, integration, or workflow that should stay deferred.
        - Replace this with one operational shortcut you should not take.

        ## Primary Users
        - Replace this with the main user or team.
        - Replace this with the second-most-important user only if they materially affect scope.

        ## Success Metrics
        - Replace this with the first signal that proves the product is useful.
        - Replace this with the first signal that proves the workflow is reliable.
        - Replace this with the first signal that proves the repo is maintainable.

        ## Risks
        - Replace this with the biggest product-delivery risk.
        - Replace this with the biggest technical or operational risk.
        - Replace this with the biggest ambiguity that should be resolved before broad buildout.

        ## Delivery Approach
        - Start with one thin slice that exercises the core workflow.
        - Keep docs, code, prompts, evals, and tests aligned in the same diff when behavior
          changes.
        - Replace this with any project-specific rollout or review constraint.

        ## Next In Fast Path
        Open `docs/TECH_STACK_SELECTION.md`, then update
        `work/items/BOOTSTRAP-001-initialize-project.md`.
        """
    )
    _write_text(repo_root / "docs" / "PROJECT_CHARTER.md", charter)


def _write_tech_stack_selection(
    repo_root: Path, project_name: str, project_slug: str, today: str
) -> None:
    tech_stack = dedent(
        f"""\
        # Tech Stack Selection
        *Version:* v0.1
        *Date:* {today}
        *Last reviewed:* {today}

        This draft records the inherited defaults from the template and the decisions still
        needed for {project_name}.

        ## Current Inherited Defaults
        - Repo slug: `{project_slug}`
        - Maintenance stack: Python plus `pytest`, `ruff`, and `pre-commit`
        - Repo structure: `docs/`, `work/`, `system/`, `prompts/`, `evals/`, `src/`, and
          `tests/`

        ## Replace These With Real Decisions
        - Product surfaces: replace with the app, service, or workflow you are actually
          building.
        - Primary implementation language: replace with the language that should own the core
          product logic.
        - Main test runner: replace with the verification path that should become canonical.
        - Packaging or build tool: replace with the real toolchain or deployment packaging.
        - Deployment target: replace with the environment where the product will run.
        - Observability and debugging: replace with the logs, metrics, or traces you need.
        - Prompt and eval strategy: replace with the real plan if model behavior matters to
          users.

        ## Decision On The Inherited Python Maintenance Stack
        - Replace this with one of:
          - keep it temporarily while the real stack is still being chosen
          - replace it immediately with the project's native tooling
          - remove it if the repo will stay docs-only for now

        ## Next Decision
        - Name the first real implementation slice and the command that should verify it.
        """
    )
    _write_text(repo_root / "docs" / "TECH_STACK_SELECTION.md", tech_stack)


def _write_active_tasks(repo_root: Path, project_name: str, today: str) -> None:
    task_title = f"Initialize {project_name} from the Codex-first template"
    task_next_action = "Open docs/BOOTSTRAP_NEXT_STEPS.md and complete Step 1."
    active_tasks = dedent(
        f"""\
        # Active Tasks
        *Version:* v0.1
        *Date:* {today}
        *Last reviewed:* {today}

        This file is the canonical current task list for the repo.

        ## Active
        | ID | Title | Status | Owner | Next action | Last updated |
        | --- | --- | --- | --- | --- | --- |
        | BOOTSTRAP-001 | {task_title} | todo | human | {task_next_action} | {today} |

        ## Rules
        - Update status and next action before ending meaningful work.
        - Link to a detailed file in `work/items/` when a task needs history or acceptance
          criteria.
        - Capture durable discoveries in `work/LEARNINGS.md` when they should influence future
          work.
        - Remove or archive stale rows once the task is truly done.
        """
    )
    _write_text(repo_root / "work" / "ACTIVE_TASKS.md", active_tasks)


def _write_learnings(repo_root: Path, today: str) -> None:
    learnings = dedent(
        f"""\
        # Durable Learnings
        *Version:* v0.1
        *Date:* {today}
        *Last reviewed:* {today}

        Use this file for discoveries that should influence future work but do not fit neatly in
        a single task file.

        ## Entries
        """
    )
    _write_text(repo_root / "work" / "LEARNINGS.md", learnings)


def _write_bootstrap_item(repo_root: Path, project_name: str, today: str) -> None:
    item_next_action = "Open docs/BOOTSTRAP_NEXT_STEPS.md and rewrite the manifesto."
    bootstrap_item = dedent(
        f"""\
        ---
        template: work_item
        template_version: 0.4
        template_date: 2026-03-11
        template_last_reviewed: 2026-03-11
        type: work_item
        item_id: BOOTSTRAP-001
        title: Initialize {project_name} from the Codex-first template
        status: todo
        owner: human
        updated: {today}
        next_action: {item_next_action}
        blocked_on: none
        ---

        # Initialize {project_name} from the Codex-first template

        ## Summary
        - Replace the remaining placeholder content with the real project's intent, scope,
          stack, and first task queue.
        - Use `docs/BOOTSTRAP_NEXT_STEPS.md` as the primary guide until the repo has a real
          product definition.

        ## Acceptance Criteria
        - `README.md` describes the real project rather than the template.
        - `docs/PROJECT_MANIFESTO.md` is rewritten for the real product.
        - `docs/PROJECT_CHARTER.md` is rewritten with real scope and non-goals.
        - `docs/TECH_STACK_SELECTION.md` reflects the actual stack decision.
        - `work/ACTIVE_TASKS.md` points at the first non-bootstrap product task.

        ## Progress Log
        - {today}: bootstrap task created from the template with project-draft docs and a
          guided handoff.

        ## Verification
        - not run yet

        ## Next Action
        - Open `docs/BOOTSTRAP_NEXT_STEPS.md` and rewrite `docs/PROJECT_MANIFESTO.md`.

        ## Notes
        - Review `docs/REPO_BOOTSTRAP_CHECKLIST.md` before the first real feature.
        - Keep placeholder wording only long enough to decide the real product definition.
        """
    )
    item_path = repo_root / "work" / "items" / "BOOTSTRAP-001-initialize-project.md"
    _write_text(item_path, bootstrap_item)


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

    _write_readme(repo_root, project_name, slug, today)
    _rewrite_pyproject(repo_root, slug)
    _write_changelog(repo_root, project_name, today)
    _write_start_here(repo_root, project_name, today)
    _write_bootstrap_next_steps(repo_root, project_name, slug, today)
    _write_manifesto(repo_root, project_name, today)
    _write_charter(repo_root, project_name, today)
    _write_tech_stack_selection(repo_root, project_name, slug, today)
    _write_active_tasks(repo_root, project_name, today)
    _write_learnings(repo_root, today)
    _write_bootstrap_item(repo_root, project_name, today)
    _clear_template_items(repo_root)

    return slug


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

    _write_text(pyproject_path, "\n".join(updated_lines) + "\n")


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
    print("Start here next:")
    print("  1. docs/BOOTSTRAP_NEXT_STEPS.md")
    print("  2. docs/PROJECT_MANIFESTO.md")
    print("  3. docs/PROJECT_CHARTER.md")
    print("  4. docs/TECH_STACK_SELECTION.md")
    print("  5. work/items/BOOTSTRAP-001-initialize-project.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

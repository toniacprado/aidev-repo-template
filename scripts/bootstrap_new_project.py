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
        1. Open `docs/CODEX_SESSION_STARTER.md` and paste the recommended prompt into Codex.
        2. Review `docs/CONTEXT_ENGINEERING.md` and `docs/BOOTSTRAP_NEXT_STEPS.md`.
        3. Use `docs/BOOTSTRAP_ARTIFACT_WORKSHOP.md` to help Codex draft the core artifacts.
        4. Review the generated drafts before moving into feature work.
        5. Update `work/items/BOOTSTRAP-001-initialize-project.md` and `work/ACTIVE_TASKS.md`
           before starting the first feature.

        ## Strong Recommendation
        Even if you already know the product idea, finish the bootstrap artifacts first.
        They turn your mental model into repo-visible context so later Codex sessions stop
        guessing. You can skip this path if you insist, but doing so increases assumption
        risk and should be recorded in `work/`.

        ## Current Bootstrap Status
        - Project name initialized as `{project_name}`.
        - Project slug initialized as `{project_slug}`.
        - Template-only work items were removed.
        - Project-facing draft docs were generated for the manifesto, charter, stack
          decision, decisions log, and first-session guides.
        - Placeholder text still needs to be replaced before feature work begins.

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

        ## Recommended First Session
        1. Open `docs/CODEX_SESSION_STARTER.md` and paste the recommended bootstrap prompt
           into Codex.
        2. Keep `docs/CONTEXT_ENGINEERING.md` and `docs/BOOTSTRAP_NEXT_STEPS.md` open while
           Codex works.
        3. Use `docs/BOOTSTRAP_ARTIFACT_WORKSHOP.md` if Codex needs more structure for
           drafting the manifesto, charter, stack decision, and work items.
        4. Review the drafted files, correct assumptions, and only then move into feature
           work.
        5. If you deliberately skip bootstrap, make sure Codex records assumptions and
           follow-up artifact debt in `work/`.

        ## Guidance To Keep
        These files stay useful after the project docs are rewritten:
        - `AGENTS.md`
        - `docs/AI_DEV_WORKFLOW.md`
        - `docs/CONTEXT_ENGINEERING.md`
        - `docs/GIT_WORKFLOW.md`
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


def _write_codex_session_starter(repo_root: Path, project_name: str, today: str) -> None:
    session_starter = dedent(
        f"""\
        # Codex Session Starter
        *Version:* v0.1
        *Date:* {today}
        *Last reviewed:* {today}

        This file is for the human starting the first Codex session in {project_name}. Copy
        one of the prompts below into Codex instead of starting with a vague one-shot request.

        ## Recommended Prompt
        Use this unless you have a strong reason to skip bootstrap.

        ```text
        Goal: Take over bootstrap and turn this fresh repo into a real first-pass
        project definition.
        Context: Read README.md, AGENTS.md, docs/CONTEXT_ENGINEERING.md,
        docs/START_HERE.md, docs/CODEX_SESSION_STARTER.md,
        docs/BOOTSTRAP_NEXT_STEPS.md, docs/BOOTSTRAP_ARTIFACT_WORKSHOP.md,
        docs/PROJECT_MANIFESTO.md, docs/PROJECT_CHARTER.md, docs/TECH_STACK_SELECTION.md,
        docs/DECISIONS.md, work/ACTIVE_TASKS.md, and
        work/items/BOOTSTRAP-001-initialize-project.md.
        Constraints: Stay in bootstrap/spec mode first. Strongly recommend finishing the
        landing docs, manifesto, charter, tech stack decision, decision log, and first work
        item before feature implementation. Do not ask me to fill blank forms; interview me
        with a short focused set of questions, then draft the files directly. Load only the
        bootstrap context pack first, then retrieve extra files just in time. If I explicitly
        choose to skip bootstrap, warn me once about the risk, then proceed and record
        assumptions and follow-up bootstrap debt in work/.
        Done when: README.md, docs/START_HERE.md, the core project artifacts, and the first
        implementation slice plus verification path are defined in work/.
        ```

        ## What Good Looks Like
        - Codex asks a short set of targeted questions instead of waiting for a perfect brief.
        - Codex drafts the manifesto, charter, stack decision, decision log, and work item.
        - You review and correct assumptions before feature work begins.

        ## Corrective Prompt
        If Codex starts implementing features too early, paste this:

        ```text
        Goal: Stop implementation and switch back to bootstrap mode.
        Context: Read AGENTS.md, docs/CONTEXT_ENGINEERING.md, docs/CODEX_SESSION_STARTER.md,
        docs/BOOTSTRAP_NEXT_STEPS.md, docs/BOOTSTRAP_ARTIFACT_WORKSHOP.md,
        work/ACTIVE_TASKS.md, and work/items/BOOTSTRAP-001-initialize-project.md.
        Constraints: Do not implement features yet. Finish the core project artifacts first
        unless I explicitly tell you to skip bootstrap.
        Done when: bootstrap artifacts and work tracking are drafted well enough to define the
        first implementation slice.
        ```

        ## Skip Path
        Skipping bootstrap is allowed but not recommended.

        ```text
        Goal: Start the first feature even though bootstrap artifacts are incomplete.
        Context: Read AGENTS.md, docs/CONTEXT_ENGINEERING.md, docs/BOOTSTRAP_NEXT_STEPS.md,
        work/ACTIVE_TASKS.md, and work/items/BOOTSTRAP-001-initialize-project.md.
        Constraints: Warn me once that missing manifesto and charter context increases
        assumption risk. Then proceed only if I confirm. Record the missing artifacts, key
        assumptions, and a follow-up task in work/. Keep the feature slice small and
        verifiable.
        Done when: the first feature slice is defined or implemented, verification is clear,
        and bootstrap debt is tracked in work/.
        ```
        """
    )
    _write_text(repo_root / "docs" / "CODEX_SESSION_STARTER.md", session_starter)


def _write_bootstrap_artifact_workshop(repo_root: Path, project_name: str, today: str) -> None:
    workshop = dedent(
        f"""\
        # Bootstrap Artifact Workshop
        *Version:* v0.1
        *Date:* {today}
        *Last reviewed:* {today}

        Use this guide to help Codex draft the core artifacts for {project_name}. The goal is
        not to make you fill a long form. The goal is to help Codex ask short questions,
        propose sensible wording, and leave the repo with durable context.

        ## Interview Rhythm
        - Ask 5-8 focused questions, not 25 broad ones.
        - Group questions by artifact so the conversation feels coherent.
        - If the user is unsure, propose 2-3 plausible options and mark the chosen one as an
          assumption.
        - Draft files directly instead of asking the user to write them from scratch.
        - End by defining the first implementation slice and verification path in `work/`.

        ## Artifact 1: Manifesto
        File: `docs/PROJECT_MANIFESTO.md`

        Why it matters:
        - It explains why the project exists, what promise it makes, and what it will not do.

        Ask questions like:
        - What concrete problem should this project solve?
        - Who feels that problem most sharply?
        - What should users reliably get from the first release?
        - What tempting expansions should stay out of scope?

        Done when:
        - A newcomer can read the file and explain the problem, promise, anti-goals, and
          constraints without extra chat context.

        ## Artifact 2: Landing Docs
        Files:
        - `README.md`
        - `docs/START_HERE.md`

        Why it matters:
        - They are the first files a human and many AI sessions will open, so leaving them in
          draft-template language weakens everything that follows.

        Ask questions like:
        - How should the project be described in one short paragraph?
        - What should a brand-new contributor do first?
        - Which generated bootstrap guides should stay visible until the product docs are real?

        Done when:
        - The README and start-here guide describe the real project and point at the current
          recommended workflow instead of sounding like template scaffolding.

        ## Artifact 3: Charter
        File: `docs/PROJECT_CHARTER.md`

        Why it matters:
        - It turns the manifesto into release scope, user definition, success metrics, and
          risks.

        Ask questions like:
        - What is the smallest end-to-end workflow that must work first?
        - Which users matter in the first release?
        - How will we know the first release is useful?
        - What should explicitly stay out of scope for now?

        Done when:
        - The first-release boundary is explicit enough that Codex can propose a thin
          implementation slice without inventing product scope.

        ## Artifact 4: Tech Stack Selection
        File: `docs/TECH_STACK_SELECTION.md`

        Why it matters:
        - It prevents the inherited template tooling from being mistaken for the real product
          stack.

        Ask questions like:
        - What platforms or environments must this run on?
        - What language or framework should own the core logic?
        - What test runner or verification path should become canonical?
        - Should the inherited Python maintenance stack stay temporarily or be replaced now?

        Done when:
        - The main implementation stack and verification path are named, even if a few
          decisions are provisional.

        ## Artifact 5: Decisions Log
        File: `docs/DECISIONS.md`

        Why it matters:
        - It captures meaningful project and workflow decisions so they do not stay implicit.

        Ask questions like:
        - What is the first real product or architecture decision we are making today?
        - Why is this choice better than the main alternatives?
        - What consequence or revisit trigger should be recorded now?

        Done when:
        - At least one project-specific decision is logged and the template's original
          decision history is gone from the new repo.

        ## Artifact 6: Work Tracking
        Files:
        - `work/ACTIVE_TASKS.md`
        - `work/items/BOOTSTRAP-001-initialize-project.md`

        Why it matters:
        - It leaves the next step visible after the first session instead of burying it in
          chat history.

        Ask questions like:
        - What is the first thin implementation slice after bootstrap?
        - What verification should prove that slice worked?
        - What uncertainty still needs follow-up?

        Done when:
        - `BOOTSTRAP-001` points at the real next action and the active task list names the
          first product slice or the remaining bootstrap debt.

        ## Optional During Bootstrap
        - `prompts/` and `evals/` only need real content now if model behavior will matter in
          the first release.
        - `docs/DATA_POLICY.md`, `docs/GUARDRAILS.md`, and `docs/MODEL_POLICY.md` should be
          tightened early if the product has sensitive data or user-facing model behavior.
        """
    )
    _write_text(repo_root / "docs" / "BOOTSTRAP_ARTIFACT_WORKSHOP.md", workshop)


def _write_bootstrap_next_steps(
    repo_root: Path, project_name: str, project_slug: str, today: str
) -> None:
    bootstrap_guide = dedent(
        f"""\
        # Bootstrap Next Steps
        *Version:* v0.1
        *Date:* {today}
        *Last reviewed:* {today}

        This guide is the primary post-bootstrap handoff for {project_name}. It strongly
        recommends a spec-first bootstrap before feature work, but it does not hard-block you
        if you choose to skip.

        ## Why This Path Is Recommended
        Even users who already know the product idea benefit from this flow. The point is not
        to slow you down. The point is to convert the idea in your head into repo-visible
        artifacts that later Codex sessions can read, trust, and extend without guessing.

        ## What Bootstrap Already Did
        - Renamed the repo landing page to `{project_name}`.
        - Set the project slug to `{project_slug}` in `pyproject.toml`.
        - Reset `CHANGELOG.md`, `work/ACTIVE_TASKS.md`, `work/LEARNINGS.md`, and
          `docs/DECISIONS.md`.
        - Removed template-only work items under `work/items/TEMPLATE-*.md`.
        - Generated project-draft placeholders plus a Codex session starter and artifact
          workshop.

        ## Recommended Path
        1. Open `docs/CODEX_SESSION_STARTER.md` and paste the recommended prompt into Codex.
           Use this even if the product idea feels clear already.
        2. Keep `docs/CONTEXT_ENGINEERING.md` and this file open while Codex works.
        3. Use `docs/BOOTSTRAP_ARTIFACT_WORKSHOP.md` if Codex needs more structure for the
           manifesto, charter, stack decision, decision log, and work tracking.
        4. Review the drafted files and replace incorrect assumptions.
        5. Only then move into feature work.

        ## Complete These Artifacts
        1. Rewrite `README.md` and `docs/START_HERE.md`.
           Done when: the first files a newcomer opens describe the real project and current
           workflow instead of the generated draft state.
        2. Rewrite `docs/PROJECT_MANIFESTO.md`.
           Done when: a new contributor can explain why the project exists and what it will
           not do yet.
        3. Rewrite `docs/PROJECT_CHARTER.md`.
           Done when: scope, users, success metrics, and non-goals are explicit.
        4. Rewrite `docs/TECH_STACK_SELECTION.md`.
           Done when: the real implementation stack and verification path are named, even if
           some decisions are provisional.
        5. Review `docs/DECISIONS.md`.
           Done when: it contains project-specific decisions rather than template history.
        6. Update `work/items/BOOTSTRAP-001-initialize-project.md` and `work/ACTIVE_TASKS.md`.
           Done when: another contributor can see the next real task without chat history.

        ## Skip Path
        Skipping bootstrap is allowed, but do it deliberately.
        - Tell Codex explicitly that you are skipping bootstrap for now.
        - Require Codex to warn once about the risk of missing manifesto and charter context.
        - Require Codex to record assumptions, unresolved product questions, and follow-up
          bootstrap debt in `work/`.
        - Revisit the skipped artifacts before broadening scope or adding collaborators.

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
        - Choose a Git publish path. If the repo is protected, shared, or public, use
          short-lived PR branches. If it is private, solo, and unprotected, direct commits
          to `main` can be fine. See `docs/GIT_WORKFLOW.md`.
        - Add at least one real decision entry in `docs/DECISIONS.md`.
        - Make sure `work/ACTIVE_TASKS.md` points at the first product slice, not only
          bootstrap cleanup.
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
        Open `docs/TECH_STACK_SELECTION.md`, then update `docs/DECISIONS.md` and
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


def _write_decisions(repo_root: Path, project_name: str, today: str) -> None:
    decisions = dedent(
        f"""\
        # Decisions Log
        *Version:* v0.1
        *Date:* {today}
        *Last reviewed:* {today}

        Use this file to record meaningful product, architecture, or workflow decisions.

        ### {today} - Bootstrap stays recommendation-first
        - Decision: {project_name} should strongly recommend finishing the core bootstrap
          artifacts before feature work, but allow an explicit skip.
        - Why: strong repo-visible context improves Codex output quality, but hard blocks
          encourage users to bypass the workflow entirely.
        - Alternatives considered: hard-block feature work until all artifacts are complete, or
          allow silent skipping with no warning.
        - Consequences: Codex should warn once before a skip, then proceed while recording
          assumptions and follow-up bootstrap debt in `work/`.
        - Revisit when: BOOTSTRAP-001 is complete and the first real implementation slice is
          underway.
        """
    )
    _write_text(repo_root / "docs" / "DECISIONS.md", decisions)


def _write_active_tasks(repo_root: Path, project_name: str, today: str) -> None:
    task_title = f"Initialize {project_name} from the Codex-first template"
    task_next_action = "Open docs/CODEX_SESSION_STARTER.md and paste the recommended prompt."
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
    item_next_action = "Open docs/CODEX_SESSION_STARTER.md and paste the recommended prompt."
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
        - Replace the remaining placeholder content with the real project's landing docs,
          intent, scope, stack, decision log, and first task queue.
        - Use `docs/CODEX_SESSION_STARTER.md`, `docs/CONTEXT_ENGINEERING.md`, and
          `docs/BOOTSTRAP_NEXT_STEPS.md` as the primary guides until the repo has a real
          product definition.

        ## Acceptance Criteria
        - `README.md` describes the real project rather than the template.
        - `docs/START_HERE.md` reflects the real project workflow rather than the generated draft.
        - `docs/PROJECT_MANIFESTO.md` is rewritten for the real product.
        - `docs/PROJECT_CHARTER.md` is rewritten with real scope and non-goals.
        - `docs/TECH_STACK_SELECTION.md` reflects the actual stack decision.
        - `docs/DECISIONS.md` contains project-specific decisions.
        - `work/ACTIVE_TASKS.md` points at the first non-bootstrap product task.

        ## Progress Log
        - {today}: bootstrap task created from the template with project-draft docs, a Codex
          session starter, and a guided handoff.

        ## Verification
        - not run yet

        ## Next Action
        - Open `docs/CODEX_SESSION_STARTER.md` and paste the recommended prompt.

        ## Notes
        - Review `docs/REPO_BOOTSTRAP_CHECKLIST.md` before the first real feature.
        - Use `docs/GIT_WORKFLOW.md` to choose the publish path for the new repo instead of
          assuming every change needs a new branch.
        - Keep placeholder wording only long enough to decide the real product definition.
        """
    )
    item_path = repo_root / "work" / "items" / "BOOTSTRAP-001-initialize-project.md"
    _write_text(item_path, bootstrap_item)


def _clear_template_items(repo_root: Path) -> None:
    for item_path in (repo_root / "work" / "items").glob("TEMPLATE-*.md"):
        item_path.unlink()


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
    _write_codex_session_starter(repo_root, project_name, today)
    _write_bootstrap_artifact_workshop(repo_root, project_name, today)
    _write_bootstrap_next_steps(repo_root, project_name, slug, today)
    _write_manifesto(repo_root, project_name, today)
    _write_charter(repo_root, project_name, today)
    _write_tech_stack_selection(repo_root, project_name, slug, today)
    _write_decisions(repo_root, project_name, today)
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
    print("Start here next:")
    print("  1. docs/CODEX_SESSION_STARTER.md")
    print("  2. docs/BOOTSTRAP_NEXT_STEPS.md")
    print("  3. docs/BOOTSTRAP_ARTIFACT_WORKSHOP.md")
    print("  4. docs/PROJECT_MANIFESTO.md")
    print("  5. docs/PROJECT_CHARTER.md")
    print("  6. docs/TECH_STACK_SELECTION.md")
    print("  7. work/items/BOOTSTRAP-001-initialize-project.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

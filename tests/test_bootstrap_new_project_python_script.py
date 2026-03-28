import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "bootstrap_new_project.py"


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def test_python_bootstrap_script_initializes_new_project_state(tmp_path: Path) -> None:
    _write(tmp_path / "README.md", "# AI Dev Repo Template\n\nStarter content.\n")
    _write(
        tmp_path / "pyproject.toml",
        '[project]\nname = "aidev-repo-template"\nversion = "0.7.0"\n',
    )
    _write(tmp_path / "CHANGELOG.md", "# Changelog\n\nTemplate history.\n")
    _write(tmp_path / "work" / "ACTIVE_TASKS.md", "# Active Tasks\n\nTemplate tasks.\n")
    _write(tmp_path / "work" / "LEARNINGS.md", "# Durable Learnings\n\nTemplate learnings.\n")
    _write(
        tmp_path / "work" / "items" / "TEMPLATE-001-openai-alignment.md",
        "# Template task\n",
    )
    _write(
        tmp_path / "work" / "items" / "TEMPLATE-002-template-ready-bootstrap.md",
        "# Template task\n",
    )

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--project-name",
            "Acme Platform",
            "--project-slug",
            "acme-platform",
        ],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=True,
    )

    assert "Bootstrap complete for Acme Platform (acme-platform)." in result.stdout
    assert "docs/CODEX_SESSION_STARTER.md" in result.stdout
    assert "docs/BOOTSTRAP_NEXT_STEPS.md" in result.stdout
    assert "docs/BOOTSTRAP_ARTIFACT_WORKSHOP.md" in result.stdout

    readme_text = (tmp_path / "README.md").read_text(encoding="utf-8")
    assert readme_text.startswith("# Acme Platform")
    assert "Open `docs/CODEX_SESSION_STARTER.md` and paste the recommended prompt into Codex." in (
        readme_text
    )
    assert "Review `docs/CONTEXT_ENGINEERING.md` and `docs/BOOTSTRAP_NEXT_STEPS.md`." in (
        readme_text
    )
    assert "Project-facing draft docs were generated for the manifesto, charter, stack" in (
        readme_text
    )

    assert 'name = "acme-platform"' in (tmp_path / "pyproject.toml").read_text(encoding="utf-8")
    today = date.today().isoformat()
    assert f"*Date:* {today}" in (tmp_path / "CHANGELOG.md").read_text(encoding="utf-8")

    start_here = (tmp_path / "docs" / "START_HERE.md").read_text(encoding="utf-8")
    assert (
        "This is the shortest useful path for the first working session in Acme Platform."
        in start_here
    )
    assert "Open `docs/CODEX_SESSION_STARTER.md` and paste the recommended bootstrap prompt" in (
        start_here
    )
    assert "Keep `docs/CONTEXT_ENGINEERING.md` and `docs/BOOTSTRAP_NEXT_STEPS.md` open" in (
        start_here
    )
    assert "- `docs/GIT_WORKFLOW.md`" in start_here

    session_starter = (tmp_path / "docs" / "CODEX_SESSION_STARTER.md").read_text(encoding="utf-8")
    assert "Take over bootstrap and turn this fresh repo into a real first-pass" in (
        session_starter
    )
    assert "Context: Read README.md, AGENTS.md, docs/CONTEXT_ENGINEERING.md" in session_starter
    assert "Done when: README.md, docs/START_HERE.md" in session_starter
    assert "Skipping bootstrap is allowed but not recommended." in session_starter

    artifact_workshop = (tmp_path / "docs" / "BOOTSTRAP_ARTIFACT_WORKSHOP.md").read_text(
        encoding="utf-8"
    )
    assert "Use this guide to help Codex draft the core artifacts for Acme Platform." in (
        artifact_workshop
    )
    assert "## Artifact 2: Landing Docs" in artifact_workshop
    assert "## Artifact 5: Decisions Log" in artifact_workshop

    bootstrap_guide = (tmp_path / "docs" / "BOOTSTRAP_NEXT_STEPS.md").read_text(encoding="utf-8")
    assert "This guide is the primary post-bootstrap handoff for Acme Platform." in bootstrap_guide
    assert "recommends a spec-first bootstrap before feature work" in bootstrap_guide
    assert "Set the project slug to `acme-platform` in `pyproject.toml`." in bootstrap_guide
    assert "1. Rewrite `README.md` and `docs/START_HERE.md`." in bootstrap_guide
    assert "Keep `docs/CONTEXT_ENGINEERING.md` and this file open while Codex works." in (
        bootstrap_guide
    )
    assert "See `docs/GIT_WORKFLOW.md`." in bootstrap_guide
    assert "## Skip Path" in bootstrap_guide

    manifesto = (tmp_path / "docs" / "PROJECT_MANIFESTO.md").read_text(encoding="utf-8")
    assert "This draft was generated during bootstrap for Acme Platform." in manifesto

    charter = (tmp_path / "docs" / "PROJECT_CHARTER.md").read_text(encoding="utf-8")
    assert "This charter is a starter draft for Acme Platform." in charter

    tech_stack = (tmp_path / "docs" / "TECH_STACK_SELECTION.md").read_text(encoding="utf-8")
    assert "This draft records the inherited defaults from the template" in tech_stack
    assert "- Repo slug: `acme-platform`" in tech_stack

    decisions = (tmp_path / "docs" / "DECISIONS.md").read_text(encoding="utf-8")
    assert "### " + today + " - Bootstrap stays recommendation-first" in decisions
    assert "Acme Platform should strongly recommend finishing the core bootstrap" in decisions

    active_tasks = (tmp_path / "work" / "ACTIVE_TASKS.md").read_text(encoding="utf-8")
    assert "BOOTSTRAP-001" in active_tasks
    assert "Initialize Acme Platform from the Codex-first template" in active_tasks
    assert (
        "| BOOTSTRAP-001 | Initialize Acme Platform from the Codex-first template |" in active_tasks
    )
    assert "Open docs/CODEX_SESSION_STARTER.md and paste the recommended prompt." in active_tasks
    assert f"| {today} |" in active_tasks

    bootstrap_item = tmp_path / "work" / "items" / "BOOTSTRAP-001-initialize-project.md"
    assert bootstrap_item.exists()
    bootstrap_item_text = bootstrap_item.read_text(encoding="utf-8")
    assert "`docs/CODEX_SESSION_STARTER.md`, `docs/CONTEXT_ENGINEERING.md`, and" in (
        bootstrap_item_text
    )
    assert "Use `docs/GIT_WORKFLOW.md` to choose the publish path" in bootstrap_item_text
    assert "`docs/START_HERE.md` reflects the real project workflow" in bootstrap_item_text
    assert f"updated: {today}" in bootstrap_item_text
    assert (
        f"- {today}: bootstrap task created from the template with project-draft docs, a Codex"
        in bootstrap_item_text
    )
    assert not list((tmp_path / "work" / "items").glob("TEMPLATE-*.md"))


def test_python_bootstrap_script_derives_slug_when_not_provided(tmp_path: Path) -> None:
    _write(tmp_path / "README.md", "# AI Dev Repo Template\n")
    _write(
        tmp_path / "pyproject.toml",
        '[project]\nname = "aidev-repo-template"\nversion = "0.7.0"\n',
    )
    _write(tmp_path / "CHANGELOG.md", "# Changelog\n")
    _write(tmp_path / "work" / "ACTIVE_TASKS.md", "# Active Tasks\n")
    _write(tmp_path / "work" / "LEARNINGS.md", "# Durable Learnings\n")
    _write(tmp_path / "work" / "items" / "TEMPLATE-009-placeholder.md", "# Template task\n")

    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--project-name", "Data Layer API"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=True,
    )

    assert "Bootstrap complete for Data Layer API (data-layer-api)." in result.stdout
    assert "docs/CODEX_SESSION_STARTER.md" in result.stdout
    assert "docs/BOOTSTRAP_NEXT_STEPS.md" in result.stdout
    assert 'name = "data-layer-api"' in (tmp_path / "pyproject.toml").read_text(encoding="utf-8")
    assert "Data Layer API" in (tmp_path / "docs" / "PROJECT_MANIFESTO.md").read_text(
        encoding="utf-8"
    )
    assert "Data Layer API" in (tmp_path / "docs" / "DECISIONS.md").read_text(encoding="utf-8")

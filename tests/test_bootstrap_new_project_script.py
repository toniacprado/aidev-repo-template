import shutil
import subprocess
from datetime import date
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "bootstrap_new_project.ps1"


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def test_bootstrap_script_initializes_new_project_state(tmp_path: Path) -> None:
    shell = shutil.which("pwsh") or shutil.which("powershell")
    if not shell:
        pytest.skip("PowerShell is required to test the bootstrap script.")

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
            shell,
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(SCRIPT),
            "-ProjectName",
            "Acme Platform",
            "-ProjectSlug",
            "acme-platform",
        ],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=True,
    )

    assert "Bootstrap complete for Acme Platform (acme-platform)." in result.stdout
    assert (tmp_path / "README.md").read_text(encoding="utf-8").startswith("# Acme Platform")
    assert 'name = "acme-platform"' in (tmp_path / "pyproject.toml").read_text(encoding="utf-8")
    today = date.today().isoformat()
    assert f"*Date:* {today}" in (tmp_path / "CHANGELOG.md").read_text(encoding="utf-8")

    active_tasks = (tmp_path / "work" / "ACTIVE_TASKS.md").read_text(encoding="utf-8")
    assert "BOOTSTRAP-001" in active_tasks
    assert "Initialize Acme Platform from the Codex-first template" in active_tasks
    assert (
        "| BOOTSTRAP-001 | Initialize Acme Platform from the Codex-first template |" in active_tasks
    )
    assert f"| {today} |" in active_tasks

    bootstrap_item = tmp_path / "work" / "items" / "BOOTSTRAP-001-initialize-project.md"
    assert bootstrap_item.exists()
    bootstrap_item_text = bootstrap_item.read_text(encoding="utf-8")
    assert "Rewrite docs/PROJECT_MANIFESTO.md and docs/PROJECT_CHARTER.md" in bootstrap_item_text
    assert f"updated: {today}" in bootstrap_item_text
    assert f"- {today}: bootstrap task created from the template." in bootstrap_item_text
    assert not list((tmp_path / "work" / "items").glob("TEMPLATE-*.md"))

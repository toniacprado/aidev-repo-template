import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

repo_template = importlib.import_module("repo_template")

REQUIRED_DIRS = [
    ".agents",
    ".agents/skills",
    ".codex",
    ".github",
    ".github/ISSUE_TEMPLATE",
    "codex",
    "codex/rules",
    "docs",
    "evals/fixtures",
    "evals/fixtures/EVAL-001",
    "work",
    "work/items",
    "system",
    "system/automations",
    "system/policies",
    "system/prompts",
    "system/schemas",
    "system/templates",
    "prompts",
    "evals",
    "src",
    "tests",
    "scripts",
    "runtime",
]

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "AGENTS.md",
    "AGENTS.local.md.example",
    "AGENTS.override.md.example",
    "CLAUDE.md",
    "CONTRIBUTING.md",
    "pyproject.toml",
    ".editorconfig",
    ".github/copilot-instructions.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/codex-task-slice.yml",
    ".github/ISSUE_TEMPLATE/codex-bug-report.yml",
    ".github/ISSUE_TEMPLATE/codex-prompt-eval-gap.yml",
    ".github/workflows/ci.yml",
    ".agents/skills/README.md",
    ".agents/skills/codex-task-slice/SKILL.md",
    ".agents/skills/codex-review/SKILL.md",
    ".codex/README.md",
    ".codex/config.toml",
    ".codex/config.toml.example",
    "codex/rules/README.md",
    "codex/rules/default.rules.example",
    "docs/START_HERE.md",
    "docs/AI_DEV_WORKFLOW.md",
    "docs/CODEX_FIRST_HOUR.md",
    "docs/NEWCOMER_USABILITY_CHECKLIST.md",
    "docs/DECISIONS.md",
    "docs/DATA_POLICY.md",
    "docs/GLOSSARY.md",
    "docs/IDEATION_AND_PLANNING.md",
    "docs/HUMAN_OPERATING_GUIDE.md",
    "docs/PROJECT_MANIFESTO.md",
    "docs/PROJECT_CHARTER.md",
    "docs/ROADMAP.md",
    "docs/CODEX_PROMPTING.md",
    "docs/TASK_MANAGEMENT.md",
    "docs/GUARDRAILS.md",
    "docs/MODEL_POLICY.md",
    "docs/CODEX_ENVIRONMENT.md",
    "docs/COMMAND_CONVENTIONS.md",
    "docs/TEMPLATE_MAINTENANCE.md",
    "docs/INSTRUCTION_LAYERING.md",
    "docs/REPO_BOOTSTRAP_CHECKLIST.md",
    "docs/TECH_STACK_SELECTION.md",
    "docs/ENGINEERING_STANDARDS.md",
    "docs/REPO_STRUCTURE.md",
    "scripts/README.md",
    "scripts/bootstrap_new_project.ps1",
    "scripts/bootstrap_new_project.py",
    "scripts/run_prompt_evals.py",
    "scripts/newcomer_smoke_test.py",
    "work/README.md",
    "work/ACTIVE_TASKS.md",
    "work/LEARNINGS.md",
    "work/items/README.md",
    "prompts/README.md",
    "prompts/PROMPT-001-repo-change-triage.md",
    "evals/README.md",
    "evals/EVAL-001-repo-change-triage.md",
    "evals/fixtures/EVAL-001/cases.json",
    "evals/fixtures/EVAL-001/candidate-pass.json",
    "evals/fixtures/EVAL-001/candidate-fail.json",
    "runtime/README.md",
    "system/automations/policy.md",
    "system/automations/approvals.md",
    "system/policies/README.md",
    "system/policies/tool_risk_matrix.md",
    "system/schemas/artifact.yml",
    "system/schemas/decision.yml",
    "system/schemas/prompt_asset.yml",
    "system/schemas/eval_case.yml",
    "system/schemas/work_item.yml",
    "system/templates/artifact.md",
    "system/templates/decision.md",
    "system/templates/prompt_asset.md",
    "system/templates/eval_case.md",
    "system/templates/work_item.md",
    "system/prompts/planning_prompt.md",
    "system/prompts/implementation_prompt.md",
    "system/prompts/review_prompt.md",
]

PLACEHOLDER_STRINGS = [
    "[Project Name]",
    "replace-me",
    "Replace with your project description",
    "[Primary capability]",
    "[Current priority]",
    "[Outcome 1]",
    "Replace these bullets with meaningful project history as soon as the repo starts evolving.",
]


def test_package_version() -> None:
    assert repo_template.__version__ == "0.7.0"


def test_required_paths_exist() -> None:
    for relative_path in REQUIRED_DIRS + REQUIRED_FILES:
        assert (ROOT / relative_path).exists(), f"Missing required path: {relative_path}"


def test_canonical_files_are_non_empty() -> None:
    for relative_path in REQUIRED_FILES:
        path = ROOT / relative_path
        assert path.read_text(encoding="utf-8").strip(), f"Canonical file is empty: {relative_path}"


def test_scaffold_placeholders_removed_from_docs() -> None:
    files_to_scan = [ROOT / "README.md", ROOT / "AGENTS.md", ROOT / "CONTRIBUTING.md"]
    files_to_scan.extend(sorted((ROOT / "docs").glob("*.md")))

    for path in files_to_scan:
        text = path.read_text(encoding="utf-8")
        for placeholder in PLACEHOLDER_STRINGS:
            assert placeholder not in text, f"Found placeholder {placeholder!r} in {path}"

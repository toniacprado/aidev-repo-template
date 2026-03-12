# Changelog
*Version:* v1.2  
*Date:* 2026-03-12  
*Last reviewed:* 2026-03-12

## Unreleased
- Fixed `scripts/bootstrap_new_project.ps1` PowerShell interpolation parser issue by
  changing `$today:` to `${today}:` in the bootstrap work-item content.
- Updated public template branding to neutral naming (`AI Dev Repo Template`) while
  keeping Codex-first workflow guidance in docs.
- Added an explicit OpenAI non-endorsement and trademark disclaimer in `README.md`.
- Updated maintenance package metadata name to `aidev-repo-template`.
- Bumped maintenance package version to `0.7.0`.
- Added `docs/COMMAND_CONVENTIONS.md` with interpreter, shell-label, bootstrap, and
  verification conventions for OS-agnostic usage.
- Updated onboarding references (`README.md`, `docs/START_HERE.md`, `AGENTS.md`) to include
  command conventions.
- Normalized shell-neutral verification snippets in maintenance docs and contributing
  guidance.
- Updated bootstrap checklist wording to use venv-first `python` with explicit `python3`
  fallback on macOS/Linux.
- Added `scripts/bootstrap_new_project.py` as the default cross-platform bootstrap path.
- Added automated tests for Python bootstrap flow (explicit slug + derived slug).
- Updated onboarding docs to prioritize cross-platform bootstrap and OS-specific maintenance setup.
- Hardened newcomer smoke checks to enforce cross-platform bootstrap instructions in docs.
- Added deterministic prompt/eval tooling:
  `scripts/run_prompt_evals.py`, golden fixtures under `evals/fixtures/`, and CI enforcement.
- Added newcomer readiness harness: `scripts/newcomer_smoke_test.py` and
  `docs/NEWCOMER_USABILITY_CHECKLIST.md`.
- Added repeatable workflow scaffolding:
  `.agents/skills/` starter skills and `codex/rules/default.rules.example`.
- Added GitHub issue templates aligned to Codex task slicing and prompt/eval workflow.
- Added `docs/CODEX_FIRST_HOUR.md` as an explicit first-session onboarding path for
  newcomers to Codex.
- Expanded first-hour onboarding with slash-command usage (`/init`, `/permissions`,
  `/plan`, `/review`, `/status`) and Git checkpoint guidance.
- Added concrete linked starter assets:
  `prompts/PROMPT-001-repo-change-triage.md` and
  `evals/EVAL-001-repo-change-triage.md`.
- Updated onboarding and instruction files (`README.md`, `AGENTS.md`, `docs/START_HERE.md`,
  `docs/HUMAN_OPERATING_GUIDE.md`, `docs/AI_DEV_WORKFLOW.md`, and
  `docs/CODEX_PROMPTING.md`) to include the first-hour workflow and tighter task slicing.
- Updated Codex environment guidance to clarify config precedence and trusted-project use.
- Extended template contract checks to require the first-hour doc and starter prompt/eval assets.
- Hardened `scripts/bootstrap_new_project.ps1` to write dynamic dates and force UTF-8 output
  across PowerShell variants.
- Updated bootstrap cleanup to remove all `work/items/TEMPLATE-*.md` files instead of a single
  hardcoded item.
- Improved bootstrap test portability by skipping cleanly when PowerShell is unavailable.
- Expanded template contract tests to require additional canonical docs, system assets, and
  GitHub workflow/instruction files.
- Updated CI to run verification on both `ubuntu-latest` and `windows-latest`.
- Added an MIT `LICENSE` so the template is reusable as a public starter.
- Added `scripts/bootstrap_new_project.ps1` to reset the repo into a clean new-project state.
- Added a happy-path automated test for the bootstrap script and fixed a `pyproject.toml`
  rename bug it uncovered.
- Added a tested `Use this template` flow to the README and bootstrap checklist.
- Added Codex prompting, environment, model policy, and guardrail docs based on current
  official OpenAI guidance.
- Added `.codex/` template files and guidance for shared Codex configuration.
- Added a Claude-compatible `CLAUDE.md` shim and an instruction-layering guide inspired
  by Anthropic's `CLAUDE.md` memory workflow.
- Added `work/LEARNINGS.md` so durable discoveries do not stay trapped in chat.
- Strengthened repo rules so agents must leave repo-visible task state and next steps.
- Added `work/` as the canonical location for active tasks and detailed task files.
- Updated the work item schema, template, and workflow docs to require next actions,
  verification notes, and blocker tracking.
- Repositioned the starter as a true Codex-first repo template instead of a generic
  placeholder scaffold.
- Rewrote the core docs with a concrete operating model, human onboarding path, and
  source-of-truth rules.
- Added prompt and eval structure so AI assets can be versioned alongside code.
- Added template contract tests and lightweight Python packaging so the default
  verification workflow is real.

# Changelog
*Version:* v2.0  
*Date:* 2026-03-28  
*Last reviewed:* 2026-03-28

## Unreleased
- Added `docs/GIT_WORKFLOW.md` with a risk-based branching and publishing policy that
  distinguishes local checkpoints from protected/public/shared publish boundaries.
- Updated onboarding, workflow, and bootstrap docs so the template now teaches
  "checkpoint always, branch when publishing across a review/protection boundary."
- Expanded newcomer smoke checks and bootstrap tests to cover the Git workflow guidance.
- Cleaned up doc hygiene after the context-engineering rollout by fixing stale metadata
  and aligning the remaining onboarding and maintenance docs with the context-pack
  workflow.
- Added `docs/CONTEXT_ENGINEERING.md` and switched the default instruction flow from a
  broad ordered read list to task-specific context packs plus just-in-time retrieval.
- Updated onboarding, bootstrap handoff guidance, and shared prompt assets to teach
  context packs and repo-visible compaction for long sessions.
- Expanded the task-management contract so long-session state is compacted into `work/`,
  `docs/DECISIONS.md`, and `work/LEARNINGS.md` instead of staying in chat history.
- Fixed `scripts/bootstrap_new_project.ps1` so markdown-heavy generated docs are built from
  literal templates plus explicit token expansion instead of PowerShell-expandable
  here-strings that break on `pwsh` runners.
- Fixed the generated bootstrap takeover path so Codex is explicitly told to rewrite
  `README.md` and `docs/START_HERE.md`, not only the deeper project artifacts.
- Updated `AGENTS.md` to mark bootstrap as a one-time reset for fresh template copies
  and to tell Codex not to suggest rerunning bootstrap after it has already completed.
- Added a generated `docs/CODEX_SESSION_STARTER.md` with recommended, corrective, and
  skip-path prompts so fresh template users can hand the repo to Codex without starting
  from a vague one-shot request.
- Added a generated `docs/BOOTSTRAP_ARTIFACT_WORKSHOP.md` so Codex can interview the
  user and draft the manifesto, charter, stack decision, decisions log, and work items.
- Reset `docs/DECISIONS.md` during bootstrap so fresh repos do not inherit template
  decision history.
- Updated repo instructions and onboarding docs to strongly recommend bootstrap mode for
  fresh repos while still allowing explicit skip paths with warnings.
- Changed bootstrap to generate project-facing draft docs (`README.md`,
  `docs/START_HERE.md`, `docs/PROJECT_MANIFESTO.md`, `docs/PROJECT_CHARTER.md`,
  and `docs/TECH_STACK_SELECTION.md`) instead of leaving template narrative in place.
- Added a generated `docs/BOOTSTRAP_NEXT_STEPS.md` guide so fresh repos have one obvious
  post-bootstrap handoff.
- Expanded bootstrap tests and newcomer smoke checks to enforce the guided handoff
  behavior.
- Clarified README setup guidance with separate paths for template maintainers vs
  downstream users.
- Simplified onboarding from a long linear doc index into a fast 5-step path plus
  grouped deep-dive references.
- Added explicit "next file" hints in fast-path docs to reduce backtracking friction.
- Updated CI actions to Node-24-ready major versions:
  `actions/checkout@v6` and `actions/setup-python@v6`.
- Added a deterministic behavioral newcomer smoke check that executes Python bootstrap
  flow in a temp repo scaffold.

## v1.2.0 - 2026-03-12
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

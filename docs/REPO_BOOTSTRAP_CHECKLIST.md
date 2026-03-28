# Repo Bootstrap Checklist
*Version:* v1.3  
*Date:* 2026-03-28  
*Last reviewed:* 2026-03-28

Use this checklist immediately after copying this starter into a real repository.

## Required before the first feature
- Run `python scripts/bootstrap_new_project.py --project-name "Your Project"` from an
  activated venv.
- If `python` is unavailable before activation, use
  `python3 scripts/bootstrap_new_project.py --project-name "Your Project"` on macOS/Linux.
- Optional Windows/PowerShell path: `scripts/bootstrap_new_project.ps1 -ProjectName "Your Project"`.
- Open `docs/CODEX_SESSION_STARTER.md` immediately after bootstrap and paste the
  recommended prompt into Codex unless you have a strong reason to skip bootstrap.
- Open `docs/CONTEXT_ENGINEERING.md` immediately after bootstrap so the first Codex session
  follows the smallest relevant context pack instead of a broad repo preload.
- Open `docs/BOOTSTRAP_NEXT_STEPS.md` immediately after bootstrap. Treat it as the
  primary handoff file until the product docs are real.
- Use `docs/BOOTSTRAP_ARTIFACT_WORKSHOP.md` to help Codex interview the user and draft
  the core artifacts instead of waiting for a perfect one-shot prompt.
- Confirm `README.md` and `docs/START_HERE.md` read like your project rather than the
  template. Rewrite any remaining placeholder language.
- Rewrite `docs/PROJECT_MANIFESTO.md` in plain language for the real product.
- Rewrite `docs/PROJECT_CHARTER.md` with scope, users, and non-goals.
- Decide whether the sample Python verification stack will stay or be replaced.
- Update `docs/TECH_STACK_SELECTION.md` with the real project decision.
- Confirm `docs/DECISIONS.md` contains project-specific decisions rather than template
  history.
- Decide whether the new repo will use direct commits to `main` or short-lived PR branches.
  If it is protected, public, or shared, prefer short-lived PR branches. See
  `docs/GIT_WORKFLOW.md`.
- Replace any sample package or folder names under `src/`.
- Confirm whether `work/` will be the canonical task tracker, then keep it current and use
  it to compact long-session state instead of relying on chat history.
- Review `.codex/config.toml.example` and decide what shared Codex defaults should be committed.

## Required before AI features matter
- Decide whether `prompts/` and `evals/` will be used in the product.
- Add real prompt assets and linked eval cases if model behavior affects users.
- Tighten `docs/DATA_POLICY.md` for the real data sensitivity boundaries.
- Fill in `docs/GUARDRAILS.md` and `docs/MODEL_POLICY.md` for the real product risk profile.
- Update `system/automations/` if the repo will allow automated actions.

## Required before more contributors join
- Confirm the source-of-truth boundaries in `docs/REPO_STRUCTURE.md`.
- Review `AGENTS.md` so repository instructions match the team's actual workflow.
- Update `.github/copilot-instructions.md` if secondary AI tools are allowed.
- Review `.github/ISSUE_TEMPLATE/` so incoming tasks fit the team's Codex workflow.
- Review `.agents/skills/` and decide whether to keep, extend, or replace the starter skills.
- Review `codex/rules/default.rules.example` and decide whether to activate project-scoped rules.
- Ensure CI and local verification commands match the real stack.
- Make sure `work/ACTIVE_TASKS.md` matches reality before active collaboration starts.
- Decide whether to keep `CLAUDE.md` as a compatibility shim for Anthropic users.

## Before calling the repo ready
- Run the default quality gates successfully.
- Run `python scripts/newcomer_smoke_test.py` successfully (from the activated virtual environment).
- Add at least one real test and one real decision log entry.
- Remove or rewrite any template text that no longer reflects the project.

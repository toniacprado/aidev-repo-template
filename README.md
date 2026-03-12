# AI Dev Repo Template
*Version:* v1.4  
*Date:* 2026-03-12  
*Last reviewed:* 2026-03-12

This repository is a starter template for teams who want a reusable AI development
baseline with Codex-first workflow standards, without making the project dependent on
hidden chat context. It gives humans and AI agents the same local source of truth:
clear product docs, explicit operating rules, versioned prompt assets, linked evals,
visible task state, model and guardrail policies, and lightweight verification.

> North Star: make new projects easy for humans and Codex to understand, change, and
> verify from the repo itself.

---

## What this template optimizes for
- fast onboarding
- spec-first development
- repo-owned AI instructions instead of chat-only memory
- prompt and eval versioning
- persistent task tracking with explicit next actions
- shared Codex environment and safety defaults
- stack-agnostic structure with replaceable defaults

---

## Use this template
This section has two different audiences.

If you are the template author/maintainer (you):
1. Publish this repo to GitHub.
2. Enable `Template repository` in GitHub settings.

If you are a user starting a new project from this template:
1. Open the published template repo on GitHub.
2. Click `Use this template` to create a fresh repo.
3. Run `python scripts/bootstrap_new_project.py --project-name "Your Project"` (or `python3` if needed before venv activation on macOS/Linux).
4. Optional Windows/PowerShell path: `scripts/bootstrap_new_project.ps1 -ProjectName "Your Project"`.
5. Work through `docs/REPO_BOOTSTRAP_CHECKLIST.md`.

Fallback (if GitHub template flow is unavailable):
1. Clone the repo.
2. Remove the old `.git` history.
3. Run `python scripts/bootstrap_new_project.py --project-name "Your Project"` (or `python3` if needed before venv activation on macOS/Linux).
4. Optional Windows/PowerShell path: `scripts/bootstrap_new_project.ps1 -ProjectName "Your Project"`.
5. Create a fresh first commit in the new repo.

---

## Start here
Frictionless first pass (no backtracking):
1. `docs/CODEX_FIRST_HOUR.md`
2. `docs/PROJECT_MANIFESTO.md`
3. `docs/PROJECT_CHARTER.md`
4. `AGENTS.md`
5. `docs/AI_DEV_WORKFLOW.md`

Need the full map after that? Use `docs/START_HERE.md`.

## Command conventions
- Use `python` commands from an activated virtual environment.
- If `python` is missing before activation, use `python3` to create the venv on macOS/Linux.
- See `docs/COMMAND_CONVENTIONS.md` for shell-neutral guidance.

---

## Template operating model
- `docs/` holds intent, scope, human workflow, decisions, prompting guidance, and policy.
- `work/` holds the active task list, learnings, and task files that survive sessions.
- `.codex/` holds shared Codex project configuration examples and local-environment notes.
- `.agents/skills/` holds reusable Codex skills for repeatable workflows.
- `codex/rules/` holds Codex execution-policy rule scaffolding.
- `system/` holds reusable schemas, templates, prompts, and policies.
- `prompts/` holds runtime prompt assets that ship with the product.
- `evals/` holds representative eval cases, rubrics, fixtures, and grading notes.
- `src/` holds implementation code.
- `tests/` holds deterministic verification for code and template contracts.
- `runtime/` holds generated, rebuildable outputs and is never canonical.

---

## Working with AI
Codex desktop is the primary AI coding environment for this repo.

Default rules:
- keep durable instructions in the repo, not only in chat
- ask Codex to read specific files before making changes
- update docs, prompts, evals, task files, and tests in the same diff when behavior changes
- prefer the smallest correct slice over broad scaffolding
- leave the next step in `work/` before closing multi-step tasks
- keep guardrails and model policy explicit when AI behavior changes
- use official vendor docs when provider-specific behavior matters

Secondary instruction layers:
- `.github/copilot-instructions.md`
- `CLAUDE.md`
- `docs/AI_DEV_WORKFLOW.md`
- `docs/CODEX_PROMPTING.md`
- `docs/TASK_MANAGEMENT.md`
- `docs/GUARDRAILS.md`
- `docs/MODEL_POLICY.md`
- `system/prompts/`

---

## Template maintenance stack
This repo uses Python only for template maintenance checks. It does not imply that the
downstream product should be Python.

See `docs/TEMPLATE_MAINTENANCE.md` for the exact setup and replacement options.

## Default verification
Run these after activating your project virtual environment.

```text
ruff format .
ruff check .
pytest -q
python scripts/run_prompt_evals.py
python scripts/newcomer_smoke_test.py
```

These commands validate the template itself. Downstream projects should replace or
extend them as soon as the real stack is chosen.

---

## When to use this template
Use it when you want:
- a greenfield repo with strong AI collaboration boundaries
- prompt and eval assets treated like real source code
- human-readable docs that survive tool churn
- task state and next steps that stay visible between sessions
- a repo that can work well with Codex first and still adapt to other agents

Skip it if you only need a framework boilerplate with no AI workflow guidance.

---

## Changelog
The canonical changelog lives in `CHANGELOG.md`.

## Disclaimer
This project is unofficial and is not affiliated with or endorsed by OpenAI.
"OpenAI" and related marks are trademarks of OpenAI.

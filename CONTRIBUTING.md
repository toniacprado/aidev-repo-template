# Contributing
*Version:* v0.8  
*Date:* 2026-03-12  
*Last reviewed:* 2026-03-12

This template is maintained like a product. Changes should improve clarity, reduce
guesswork, and keep the repo easy for both humans and Codex to operate.

## Preferred workflow
1. Read `docs/START_HERE.md`, `docs/HUMAN_OPERATING_GUIDE.md`, `docs/CODEX_PROMPTING.md`,
   and `AGENTS.md`.
2. Tighten the spec first if intent, scope, or boundaries are unclear.
3. Update `work/` before or during non-trivial multi-step work.
4. Make the smallest useful change that improves the template.
5. Update linked docs, prompts, evals, model or guardrail policy, and tests in the same
   diff when needed.
6. Run the repo quality gates and report any gaps honestly.

## Local setup
The steps below are only for the template maintenance stack. They do not imply that the
downstream project itself should be Python.

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
pre-commit install
```

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
pre-commit install
```

## Required verification
```text
ruff format .
ruff check .
pytest -q
python scripts/run_prompt_evals.py
python scripts/newcomer_smoke_test.py
```

Use `python` from the active venv; if `python` is unavailable before activation, use
`python3` to create/activate the environment first.

## Change expectations
- Behavior changes require docs or contract updates.
- Prompt changes require linked eval updates.
- Model changes require model-policy review and eval reruns.
- Guardrail changes require policy updates.
- Meaningful task progress should be reflected in `work/`.
- Material edits to Markdown guidance files require updated version and review stamps.

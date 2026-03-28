# Template Maintenance
*Version:* v1.1  
*Date:* 2026-03-28  
*Last reviewed:* 2026-03-28

This file explains what is required to maintain the template itself.

## Short answer
- Codex can maintain a lot of this repo without Python.
- Python is only needed to run the full local maintenance gates.
- The downstream project does not need to be Python because this template has Python-based checks.

## What Codex can do without Python
Even without a local Python toolchain, Codex can still:
- review and improve docs
- update repo structure and policies
- maintain `AGENTS.md`, `CLAUDE.md`, and `work/`
- follow the retrieval and compaction rules in `docs/CONTEXT_ENGINEERING.md`
- inspect files and reason about consistency
- run lightweight repo-local structural checks through the shell

## What Python unlocks
Python is only required when you want to run these maintained quality gates locally:
- `ruff format .`
- `ruff check .`
- `pytest -q`
- `python scripts/run_prompt_evals.py`
- `python scripts/newcomer_smoke_test.py`

These verify the template contract more rigorously than manual inspection.
See `docs/COMMAND_CONVENTIONS.md` for interpreter and shell-label conventions.

## Recommended setup
If you want Codex to maintain this template with full local verification support:
1. Install Python 3.12 or newer.
2. Open a new terminal in the repo.
3. Create and activate a virtual environment.

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

4. Then verify with the active venv:

```text
ruff format .
ruff check .
pytest -q
python scripts/run_prompt_evals.py
python scripts/newcomer_smoke_test.py
```

If `python` is not found on macOS/Linux, use `python3` to create the virtual
environment and then run commands after activation.

## Maintenance workflow reminder
- Start with `docs/CONTEXT_ENGINEERING.md` instead of preloading every maintenance doc.
- For this template repo itself, assume `main` is protected and publish through short-lived
  PR branches instead of pushing directly to `main`.
- If a related fix is found before that PR merges, keep it on the same branch unless the new
  issue is clearly separate.
- Update version/date/review stamps when materially editing Markdown guidance files.
- When the instruction layer changes, update the most relevant smoke checks in the same diff.

## If you do not want Python
That is still a valid choice.

In that case:
- keep using Codex for docs, policy, and structural maintenance
- accept that some checks will remain review-based instead of tool-enforced
- replace the Python maintenance stack later if your real project has a better native verification path

## Best long-term option
For this template, the best practical model is:
- keep Python as a maintenance-only layer while the repo is a generic template
- replace or remove it once the real project stack is chosen and has stronger native checks

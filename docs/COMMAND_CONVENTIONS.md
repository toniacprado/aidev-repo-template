# Command Conventions
*Version:* v0.1  
*Date:* 2026-03-12  
*Last reviewed:* 2026-03-12

Use these conventions to keep repo commands OS agnostic.

## Interpreter convention
- Prefer `python` for repo commands after activating a virtual environment.
- If `python` is unavailable before venv activation (common on macOS/Linux), use
  `python3` to create the venv first.

## Bootstrap convention
- Primary bootstrap path (all OS): `python scripts/bootstrap_new_project.py --project-name "Your Project"`.
- Windows optional path: `scripts/bootstrap_new_project.ps1 -ProjectName "Your Project"`.

## Shell snippets
- `bash` code blocks are examples for POSIX shells (macOS/Linux).
- `powershell` code blocks are examples for Windows PowerShell.
- `text` code blocks are shell-neutral command lists.

## Verification convention
- Run verification from an activated venv so `python`, `ruff`, and `pytest` resolve
  consistently.
- If your shell cannot resolve `python`, run commands as `python3 ...` until the venv
  is active.

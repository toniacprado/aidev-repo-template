# Scripts Directory
*Version:* v1.1  
*Date:* 2026-03-24  
*Last reviewed:* 2026-03-24

Store repo utilities and bootstrap helpers here.

Current scripts:
- `bootstrap_new_project.py` resets template identity, rewrites the main landing docs
  into project-facing drafts, resets the decisions log, and generates a guided
  post-bootstrap Codex handoff plus context-engineering guidance using a cross-platform
  Python entrypoint.
- `bootstrap_new_project.ps1` does the same for Windows/PowerShell users.
- `run_prompt_evals.py` runs deterministic prompt/eval link and golden-fixture checks.
- `newcomer_smoke_test.py` runs newcomer-readiness structural and eval smoke checks.

Rules:
- prefer idempotent scripts
- document assumptions near the script or in the file header
- keep scripts easy to run from CI or a clean local checkout
- add at least one happy-path test for important scripts

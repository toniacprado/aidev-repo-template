# Scripts Directory
*Version:* v0.8  
*Date:* 2026-03-11  
*Last reviewed:* 2026-03-11

Store repo utilities and bootstrap helpers here.

Current scripts:
- `bootstrap_new_project.py` resets template identity and task scaffolding using a
  cross-platform Python entrypoint.
- `bootstrap_new_project.ps1` resets the template's project name, changelog, task queue,
  and bootstrap work item for a fresh project (Windows/PowerShell path).
- `run_prompt_evals.py` runs deterministic prompt/eval link and golden-fixture checks.
- `newcomer_smoke_test.py` runs newcomer-readiness structural and eval smoke checks.

Rules:
- prefer idempotent scripts
- document assumptions near the script or in the file header
- keep scripts easy to run from CI or a clean local checkout
- add at least one happy-path test for important scripts

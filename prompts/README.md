# Prompts Directory
*Version:* v0.6  
*Date:* 2026-03-11  
*Last reviewed:* 2026-03-11

Store runtime prompt assets here.

Starter example:
- `PROMPT-001-repo-change-triage.md` (linked to `evals/EVAL-001-repo-change-triage.md`)
- validate linked eval coverage via `python scripts/run_prompt_evals.py`

Rules:
- keep one versioned prompt asset per file when practical
- use `system/templates/prompt_asset.md` for new prompts
- keep stable instructions and reusable examples above highly variable task data
- link every important prompt to eval coverage under `evals/`
- review `docs/MODEL_POLICY.md` when a prompt change depends on model-specific behavior
- use structured outputs when downstream code depends on exact fields
- never store secrets or private customer data in prompt files

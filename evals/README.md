# Evals Directory
*Version:* v0.6  
*Date:* 2026-03-11  
*Last reviewed:* 2026-03-11

Store prompt and agent evaluation assets here.

Starter example:
- `EVAL-001-repo-change-triage.md` (covers `prompts/PROMPT-001-repo-change-triage.md`)

Run deterministic eval checks:
- `python scripts/run_prompt_evals.py`
- fixtures live under `evals/fixtures/`

Rules:
- start with a small representative set of cases
- prefer pass/fail, exact-match, or explicit rubric grading where possible
- use `system/templates/eval_case.md` for new evals
- link eval cases back to the prompt or workflow they cover
- rerun the linked eval set when prompts or model defaults change
- add edge cases when a bug fix or production issue reveals them

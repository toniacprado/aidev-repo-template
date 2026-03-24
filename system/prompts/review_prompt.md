# Review Prompt
*Version:* v0.5  
*Date:* 2026-03-24  
*Last reviewed:* 2026-03-24

Goal: review a change for bugs, regressions, missing tests, prompt drift, model drift,
and contract drift.

Instructions:
- read `docs/CONTEXT_ENGINEERING.md` and load only the smallest relevant context for the
  change under review
- prioritize correctness and risk over style commentary
- cite files and lines when possible
- call out missing tests, missing evals, missing task updates, or missing policy updates
- mention assumptions and residual risk explicitly
- mention missing verification if checks were not run

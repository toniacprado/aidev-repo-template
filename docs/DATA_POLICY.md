# Data Policy
*Version:* v0.4  
*Date:* 2026-03-11  
*Last reviewed:* 2026-03-11

Document the rules for sensitive information, generated artifacts, logs, and third-
party services.

## Minimum questions to answer
- What data is sensitive?
- What must never be committed to Git?
- What can be logged?
- What can be sent to external APIs or AI providers?
- What must stay local?

## Default rules
- Never hardcode secrets.
- Use `.env` and `.env.example` for environment variables.
- Do not commit secrets, personal data, or customer data unless explicitly intended.
- Keep generated runtime artifacts out of canonical source-of-truth locations unless
  reviewed.
- Treat prompts as code, but do not include secrets or private customer data inside
  prompt files.
- If external AI providers are used, document what categories of code, content, and
  metadata may be sent to them.
- Align permission and logging choices with `docs/GUARDRAILS.md`.
- When in doubt, prefer redaction or local-only workflows until policy is explicit.

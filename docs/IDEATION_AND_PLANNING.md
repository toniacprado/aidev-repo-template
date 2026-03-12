# Ideation And Planning
*Version:* v0.2  
*Date:* 2026-03-11  
*Last reviewed:* 2026-03-11

Use this document to turn a rough idea into an executable plan before feature work
sprawls.

---

## Step 1: Frame the problem
Write down:
- who has the problem
- what is painful today
- why current tools or workflows are insufficient
- what outcome would actually feel better

## Step 2: Write the manifesto
Create or rewrite `docs/PROJECT_MANIFESTO.md` before implementation.

Why:
- Codex makes better decisions when it understands intent.
- The manifesto protects the repo from drifting into generic feature accumulation.

## Step 3: Create the charter
Define scope, non-goals, users, success metrics, and risks in
`docs/PROJECT_CHARTER.md`.

## Step 4: Pick the thinnest useful slice
Describe one end-to-end workflow that proves the product is real.

Good slices are:
- valuable
- small enough to finish
- easy to verify
- narrow enough to explain in one screen of text

## Step 5: Choose the stack deliberately
Use `docs/TECH_STACK_SELECTION.md` before locking frameworks, runtimes, or hosting.

## Step 6: Plan prompt and eval assets if AI is product-critical
If model behavior matters to the product:
- define the prompt asset boundary
- define the expected output contract
- define the eval cases before prompt tuning spreads across chats

## Step 7: Break work into iterations
Each iteration should answer:
- what behavior will exist after this slice
- which docs or contracts need to change first
- what tests or evals prove it works
- what risks remain

## Suggested Codex planning prompt
> Read `docs/PROJECT_MANIFESTO.md`, `docs/PROJECT_CHARTER.md`, and
> `docs/TECH_STACK_SELECTION.md`. Propose the smallest MVP plan with explicit
> assumptions, risks, prompt or eval implications, and verification needs.

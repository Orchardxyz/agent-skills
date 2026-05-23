---
name: executor-reviews
description: Use when code written by another model or engineer needs to be validated and reviewed, and the results must be written into docs/reviews with findings, evidence, reproduction details, and self-check results.
---

# Executor Reviews

## Overview

Review implementation work produced by an execution model such as DeepSeek. The output must prioritize findings, cite evidence from the current code or command results, and be written as a reusable review document in `docs/reviews/`.

## When to Use

Use this skill when:

- the user asks for a review document in `docs/reviews/`
- another model or engineer has already implemented a change
- the task is to validate behavior, find issues, and recommend follow-up work
- self-check commands need to be run and documented

Do not use this skill for pre-implementation planning. Use `executor-plans` for that.

## Required Workflow

1. Inspect the current diff or changed files first.
2. Read the relevant code paths, not just the patch summary.
3. Run the narrowest meaningful verification commands.
4. Separate real issues from unrelated existing warnings or repo noise.
5. Write the review into `docs/reviews/YYYY-MM-DD-<topic>-review.md`.

## Review Standard

Findings come first.

Each real finding should include:

- severity level such as `P1`, `P2`, or `P3`
- impact
- evidence with file references, commands, or observable behavior
- a concrete recommendation

If there are no findings, say that explicitly.

## Required Sections

Include:

- Date
- Scope
- Overall assessment
- Findings
- Self-check
- Suggested next-step bundle when follow-up work is needed
- Bottom line

## Self-Check Rules

The review must document which commands were actually run and what happened.

Examples:

- `typecheck`
- targeted `eslint`
- relevant tests
- build or smoke commands when they matter

If a command could not be run, record the reason exactly.

## Writing Rules

- Prioritize bugs, regressions, broken workflows, and unsafe design choices.
- Keep summaries short and evidence specific.
- Distinguish new issues from pre-existing unrelated warnings.
- Do not pad the review with praise when findings exist.
- Do not claim validation that was not actually performed.

## Common Mistakes

- Writing a changelog instead of a review
- Listing observations without impact
- Reporting issues without evidence
- Skipping command validation
- Treating unrelated existing warnings as regressions from the current change

## Output Target

Write the final artifact into `docs/reviews/` so the executor can use it as a direct follow-up task list.

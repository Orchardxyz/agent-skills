---
name: executor-plans
description: Use when implementation work will be handed off to another model or engineer, and a decision-complete execution plan needs to be written into docs/plans for them to follow without making key product or technical decisions.
---

# Executor Plans

## Overview

Write implementation plans for an execution model such as DeepSeek. The output must be directly actionable, grounded in the current repository, and complete enough that the executor does not need to invent important decisions.

## When to Use

Use this skill when:

- the user wants a plan written into `docs/plans/`
- another model or engineer will implement the work
- code has not been implemented yet, or implementation should be guided by a written spec first
- the task needs clear scope, sequencing, validation, and success criteria

Do not use this skill for post-implementation review. Use `executor-reviews` for that.

## Required Workflow

1. Explore the current repo state before writing anything.
2. Read the relevant code, config, docs, and recent diffs or commits.
3. Resolve discoverable facts locally instead of asking the user.
4. Decide the exact plan shape: goals, non-goals, target files or subsystems, validation, and acceptance criteria.
5. Write the plan into `docs/plans/YYYY-MM-DD-<topic>-design.md`.

## Plan Standard

Every plan must be written for execution handoff, not brainstorming.

Include:

- Summary
- Goals
- Non-Goals
- Current constraints or repo facts that matter
- Recommended approach
- Concrete implementation areas or files when needed
- Validation commands
- Success criteria
- Assumptions and defaults chosen for the executor

The plan must:

- make the important decisions up front
- avoid vague advice like “consider”, “maybe”, or “if needed” unless a real branch is intentional
- tell the executor what not to change when boundaries matter
- prefer behavior-level guidance over giant file inventories

## Writing Rules

- Ground the plan in the actual repository, not generic best practices.
- Keep it concise but decision-complete.
- Optimize for execution safety, not exhaustive explanation.
- If dependency changes are proposed, state why existing tools are insufficient.
- If validation cannot be run yet, say exactly what the executor must run after implementation.

## Validation Section

Always end with concrete validation commands that the executor should run.

Typical examples:

- package-level `typecheck`
- targeted `eslint`
- focused test commands
- smoke checks relevant to the changed area

Only include commands that make sense for the task.

## Common Mistakes

- Writing a design discussion instead of an execution plan
- Leaving key tradeoffs unresolved
- Omitting non-goals, causing scope creep
- Forgetting validation commands
- Repeating repository facts without telling the executor what to do with them

## Output Target

Write the final artifact into `docs/plans/` and make it ready to hand to the executor without extra interpretation.

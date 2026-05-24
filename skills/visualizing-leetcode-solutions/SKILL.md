---
name: visualizing-leetcode-solutions
description: Use when turning a LeetCode problem and one chosen solution into a step-by-step HTML walkthrough, especially when code alone is hard to follow and the user would benefit from frame-by-frame visualization.
---

# Visualizing LeetCode Solutions

## Overview

Turn one LeetCode problem and one chosen solution into a compact, single-file HTML walkthrough.

This skill uses one fixed visual shell derived from the rotate-array example. Do not redesign the page for each problem. Replace the content layer, frame data, and only the minimum visualization details required by the data structure.

## When to Use

- The user wants a LeetCode problem explained visually instead of only reading code
- The user wants a simple HTML artifact with playback controls
- The user provides a LeetCode link, title, problem text, code, or some combination of them

Do not use this skill for:

- Comparing multiple algorithms for the same problem
- Designing a new frontend product or plugin shell
- Building a heavy animation system before the explanation structure is clear

## Required References

Before generating or revising a page, inspect:

- `assets/shell/base-layout.html`
- `assets/shell/ui-contract.md`
- `scripts/player-template.js`
- `scripts/code-panel-template.js`

Use them as the default shell and behavior source.

## Non-Negotiables

- Reuse the canonical rotate-array shell. Do not invent a brand-new page layout for each problem.
- Produce one single-file HTML document.
- Keep the shell stable: header, theme toggle, core idea card, two-column desktop layout, left visualization, right code panel, bottom controls.
- Default to light mode and provide a visible dark-mode toggle.
- Keep the page one-screen-first. Long visualization content and long code should scroll inside their own panels.
- Preserve code indentation exactly. Render code from source lines with a whitespace-preserving container or line-by-line `textContent`.
- Use one fixed page title format: `LeetCode <problem-number> — <problem-title-cn> · <solution-keyword>`.
- If the user provided code, explain that code instead of silently switching algorithms.
- The right panel should support two modes: real code and pseudocode. Default to real code.
- Do not dynamically synchronize code-line highlighting during playback unless the user explicitly asks for it.

## Input Rules

- If the user gives a LeetCode link, first try to fetch or read that exact URL with the tools available in the current environment.
- If a `leetcode.cn` URL fails to fetch, try the corresponding non-`cn` LeetCode problem URL before giving up.
- If direct fetching still fails, extract the problem slug from the URL and try a web search using `leetcode <problem-slug>` before giving up.
- If fetching is unavailable or incomplete after those attempts, ask for the core problem statement, constraints, and examples.
- If the user does not give code and the session supports back-and-forth interaction, ask which language the code panel should use.
- If the user does not give code and the request is effectively single-turn, explicitly state the fallback language before showing generated code.
- If the user does not give code, choose one reasonable solution path and stay with it.
- If sample input/output is missing, create 1 to 3 small examples that reveal the algorithm's state changes.
- Do not silently rely on memory when link fetching failed. Only continue from known problem knowledge after making that fallback explicit.

## Output Contract

The page must include:

- Problem title and short summary
- Core idea in 2 to 5 sentences
- Left panel for state visualization
- Right panel for code
- Code mode toggle for `真实代码` and `伪代码`
- Step explanation tied to the current frame
- Controls for play, pause, previous, next, restart, and speed
- Frame indicator such as `Step 3 / 12`

Use `slow`, `normal`, and `fast` speed controls.

## Visualization Rules

- Treat the data structure as the body and the algorithm as the motion.
- Each frame should make clear: what is visible now, what operation is happening, which code lines matter, and why the step moves the solution forward.
- Choose the simplest template that matches the dominant structure: arrays/strings, linked lists, stacks/queues, trees, heaps, graphs, or hash tables.
- Start with one primary view. Add a second synchronized view only when it truly clarifies the algorithm.

## Code Rules

- Prefer descriptive variable names such as `left`, `right`, `windowStart`, `currentNode`, or `nextNode`.
- Avoid cryptic abbreviations such as `lo`, `hi`, or `tmp` unless they are clearly standard and still readable.
- Keep generated reference implementations short and explanation-friendly.
- Provide a short pseudocode view that mirrors the real solution path without language-specific syntax noise.

## Workflow

1. Gather the problem and chosen solution.
2. Load the standard shell references before inventing any new structure.
3. Identify the dominant data structure and choose the simplest matching visualization template.
4. Derive the smallest example that reveals the algorithm's state changes.
5. Break the solution into frames and map each frame to state, summary, and code highlights.
6. Fill the standard shell instead of redesigning the page.
7. Generate a single-file HTML walkthrough.

## Common Mistakes

- Rebuilding the UI for each problem instead of reusing the canonical shell
- Letting code overflow break the layout instead of making the code panel scroll internally
- Losing indentation when generating code
- Skipping language confirmation in an interactive session
- Explaining a different algorithm than the user's code

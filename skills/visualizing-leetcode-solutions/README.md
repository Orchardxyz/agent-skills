# Visualizing LeetCode Solutions

Generate a compact, single-file HTML walkthrough for one LeetCode problem and one chosen solution so the solving process is easier to understand step by step.

## Installation

```bash
npx skills add https://github.com/Orchardxyz/agent-skills --skill visualizing-leetcode-solutions
```

## Purpose

This skill is for explanation-first visualization:

- Input a LeetCode problem by link, title, or pasted statement
- Optionally provide one solution implementation
- Output one self-contained HTML page
- Keep the page focused on one solution path rather than comparing alternatives
- Reuse one fixed visual shell instead of redesigning the page for each problem

## Structure

```text
visualizing-leetcode-solutions/
├── SKILL.md
├── README.md
├── assets/
│   └── shell/
│       ├── base-layout.html
│       └── ui-contract.md
└── scripts/
    ├── code-panel-template.js
    └── player-template.js
```

The visual baseline is derived from the rotate-array example. Future pages should preserve that shell and mainly replace the content area, frame data, and structure-specific rendering details.

Recommended page title format:

`LeetCode <problem-number> — <problem-title-cn> · <solution-keyword>`

## Output Shape

The default artifact is a single HTML file with:

- A short problem summary
- A page title that follows one fixed naming format
- A left-side state visualization
- A right-side code panel
- A code-mode toggle with real code and pseudocode
- Frame-by-frame step explanations
- Autoplay and manual stepping controls
- Light mode by default with a dark-mode toggle
- A full-screen-first layout with internal scrolling for long content

## Expected Inputs

- Required: a LeetCode problem
- Optional: one solution implementation
- Optional: sample input and output
- Optional: concepts to emphasize

If a link is provided, the skill should try to fetch the problem with the tools available in the current environment. If fetching is unavailable, the user should provide the problem statement directly.

For LeetCode links, prefer this fallback order:

1. Fetch the original URL
2. If a `leetcode.cn` URL fails, retry with the equivalent non-`cn` LeetCode problem URL
3. If that still fails, extract the problem slug from the URL and search the web with `leetcode <problem-slug>`
4. If that still fails, ask the user for the core problem statement
5. Only fall back to known problem knowledge after stating that fallback explicitly

If the user does not provide code:

- In an interactive session, the skill should ask which language to use before generating the code panel.
- In a single-turn flow, the skill should explicitly state the fallback language before showing generated code.

## Design Bias

- Prefer teaching clarity over animation complexity
- Prefer one dominant visualization template per problem
- Prefer minimal JavaScript and Tailwind via CDN
- Prefer proactive sample construction when the user omitted examples
- Prefer readable variable names in generated code when the user did not provide an implementation
- Prefer a stable reusable shell over one-off page redesigns

## Dependencies

- A capable agent environment
- Optional web fetching or page-reading tools when the user provides a LeetCode link
- No frontend build tool is required for the default output

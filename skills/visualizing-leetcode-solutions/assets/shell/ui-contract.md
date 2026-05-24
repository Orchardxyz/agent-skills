# UI Contract

This skill uses one fixed shell for all LeetCode walkthrough pages.

## Canonical Baseline

The visual baseline is the rotate-array page in:

- `/Users/orchard/code/personal/agent-skills/playground/visualizations/rotate-array-189.html`

That page defines the expected product feel. Future pages should look like variations within the same family, not brand-new designs.

## Stable Regions

These regions should stay consistent across problems:

- Page title format
- Header with title, subtitle, and theme toggle
- Core idea card
- Two-column desktop layout
- Visualization panel on the left
- Code panel on the right
- Code-mode toggle with real code and pseudocode
- Playback control bar at the bottom
- Dark/light theme behavior
- Slow/normal/fast speed controls

## Replaceable Regions

These regions are expected to change per problem:

- Problem title and summary
- Core idea wording
- Visualization content inside the left panel
- Code panel contents
- Frame data
- Small render helpers for the chosen data structure

## Layout Rules

- Prefer a one-screen application layout
- Let inner panels scroll instead of the whole page growing vertically without bound
- The code panel must allow horizontal scrolling for long lines
- Keep controls visible and easy to reach
- Mobile should stack cleanly while preserving scrollable sub-panels

## Code Rendering Rules

- Preserve indentation exactly
- Render code from source lines, not from collapsed prose
- Use `<pre><code>` or equivalent line-by-line rendering with `textContent`
- Default to a two-mode panel: real code and pseudocode
- Default to real code mode
- Do not require line-by-line dynamic highlighting during playback

## Theme Rules

- Default to light mode
- Always provide a visible theme toggle
- Preserve the same color logic across pages even if the visualization content changes

## Page Title Rule

Use this format for the HTML `<title>`:

`LeetCode <problem-number> — <problem-title-cn> · <solution-keyword>`

Keep the format stable across problems. Only replace the problem number, title, and short algorithm label.

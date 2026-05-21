---
name: one-page-visual
description: Build single-screen "one-map/one-pager" static HTML+CSS pages (poster-style) with Tailwind CDN. Always confirm visual style options, layout, palette, typography, content, and assets with the user first. Default to producing separate static HTML files per theme (light/dark) and split HTML/CSS outputs—no runtime theme toggle. Use whenever a user asks for a one-screen visual/landing/poster built with HTML+CSS (Tailwind CDN allowed).
---

# One-Page Visual Builder

## When to use this skill
- The user wants a single-screen visual/landing/poster-like page built with HTML+CSS.
- They allow Tailwind via CDN and want a quick static deliverable (no build tooling).
- They expect a clean handoff: separate HTML and CSS files, optional dual themes.

Hard constraint: In all one-pagers, do not place copy like “light version”, “dark theme”, or style labels on the visual itself. Theme/style labels are allowed only on an optional external portal page.

Always converse with the user in their language; this document stays in English.

## Pre-flight questionnaire (ask before designing)
Gather concise answers; propose options if the user is unsure.
1) Goal & audience: purpose, target viewers, primary CTA.
2) Content inventory: headline, subhead, bullets/features, CTAs, metrics, contact info, legal/footer.
3) Visual style menu (allow multi-select; offer multiple picks):
   - Minimal/white-space
   - Magazine/editorial grid
   - Tech/neon/cyberpunk
   - Product hero (device mock/hero + feature chips)
   - Ecommerce/product grid
   - Event/announcement poster
   - Data/insight dashboard poster
   - Illustration/flat/collage
   - Brutalist/high-contrast blocks
   - Glassmorphism/blurred cards
   - Retro/vaporwave
   - Serif newspaper/classic print
   - Hand-drawn/scribble accents
   - Custom mix (let them describe)
   - If multiple styles are desired, note the count and intended differences.
4) Layout preference: single column hero, split hero+visual, stacked sections, grid cards, timeline/steps, comparison blocks.
5) Color direction: user palette; if none, propose 2–3 palettes with accent/neutral (e.g., teal+slate, amber+stone, violet+zinc) and confirm.
6) Typography: sans (clean), serif (editorial), mono (techy), display (accent). Offer 2–3 pairings; confirm Google Fonts if desired.
7) Imagery assets: logo, hero image, icons/illustrations, whether placeholders are acceptable.
8) Interactions: no in-page theme toggles; allow hover depth, subtle gradients/textures, gentle motion. If needed, only the optional portal page may link to theme/style variants.
9) Output format: confirm separate files (`index.html`, `style.css`), Tailwind CDN usage, and whether to inline small custom CSS tokens.

## Defaults if unspecified
- Style: Minimal hero + feature grid (single style), but support multi-style variants if requested.
- Palette: teal + slate with accessible contrast; add soft gradient for hero.
- Typography: clean sans for body, display or semi-bold sans for headings.
- Themes: deliver two static HTML files (light and dark), each baked with its theme—no runtime toggles. Optionally include a tiny router page that links to each theme/style variant if helpful.
- Assets: use placeholders for images/icons if none provided.

## Build approach
1) Confirm and restate the agreed spec (style(s), palette, layout, typography, assets, themes, file split, variant count) before coding.
2) Generate files:
   - For each requested style, emit separate HTML files per theme (e.g., `style-a-light.html`, `style-a-dark.html`, `style-b-light.html`). No runtime theme toggles inside the one-pagers.
   - Optionally add a lightweight index/portal HTML that links to each variant (allowed to have navigation only; keep one-pagers themselves non-interactive except links/CTAs).
   - `style.css`: shared custom tokens (CSS variables) for light/dark, and any bespoke effects (textures, gradients, fine-grain layout tweaks). Keep utility-first; only add bespoke CSS where Tailwind utilities are insufficient.
3) Structure (adapt as needed):
   - `<main>` with hero (headline, subhead, CTA, optional badge/eyebrow, key metric) and a visual (image/gradient card/mock).
   - Supporting sections: feature grid/cards, highlights/steps/timeline, testimonial or stat strip, CTA/footer.
4) Theme strategy:
   - Define CSS variables for colors/gradients in `:root[data-theme="light"]` and `:root[data-theme="dark"]` inside `style.css`; bake the desired `data-theme` on `<html>` in each per-theme HTML file.
   - Apply Tailwind classes using `text-[color:var(--...)]`/`bg-[color:var(--...)]` patterns when needed, or use standard Tailwind shades that suit both themes.
   - Avoid theme toggles within the one-pager outputs; each file is a finished static visual. Do not include any theme/style labels in-page.
5) Accessibility & quality:
   - Maintain WCAG-friendly contrast for text on both themes.
   - Use semantic tags and meaningful aria labels for buttons/links.
   - Prefer clamp() for responsive text where helpful; ensure mobile-friendly spacing.
   - Limit motion; use gentle transitions only.

## Output expectations
- Deliver code blocks for all files. Example format:
  - `style-a-light.html`, `style-a-dark.html` (and additional style variants if requested)
  - Optional `index.html` portal linking to all variants
  - `style.css`
- No in-page theme toggles for the one-pagers; each HTML is a fixed-theme snapshot.
- Do not place theme/style labels or “current version” text inside the visuals.
- If the user asks for file creation, create the folder `skills/one-page-visual/` or a user-specified path and place the files accordingly.
- Keep copy concise unless the user provides long-form text; avoid lorem ipsum—write context-aware placeholder copy.

## Reference style & briefing helpers (for faster user alignment)

### I. Style keywords (multi-select allowed)
| Style | Description | Ideal use cases |
| --- | --- | --- |
| Minimalism | Generous whitespace, restrained palette | Portfolios, brand sites |
| Glassmorphism | Frosted blur, translucency, soft bg | Dashboards, cards |
| Neumorphism | Soft shadows, embossed, monochrome | Control panels, toggles |
| Cyberpunk | Neon, glitch, high-tech vibe | Games, music, street |
| Brutalism | Raw, bold, irregular | Art, experimental |
| Editorial/Magazine | Grid, oversized headings | Blogs, fashion, news |
| Dark Tech | Dark bg, glowing borders | Tech, data viz |
| Natural/Organic | Curves, earthy palette | Wellness, sustainability |
| Retro/Vintage | Textures, nostalgic palette | Cafés, heritage |

Description example: ✅ “Dark tech with neon cyan accents and subtle glow”; ❌ “Make it nicer.”

### II. Layout terminology
| Term | Explanation |
| --- | --- |
| Hero section | First screen with headline + CTA |
| Above the fold | Content visible without scroll |
| Card layout | Grid of cards for products/articles |
| Split layout | Left/right or top/bottom contrast |
| Grid system | 12/24-col grid for order |
| Masonry | Staggered variable-height cards |
| Full-screen immersive | 100vh, minimal scroll |

Patterns: F-pattern (reading-heavy), Z-pattern (conversion), single-column (mobile), asymmetrical (tension).

### III. Color description
Palette types: monochromatic, analogous, complementary, triadic, split-complementary.
How to describe: “Primary deep navy (#0A192F) with mint (#64FFDA) accents”, “Warm amber hero, creamy white background”, “Morandi muted palette”, “High-contrast black + punchy yellow”.
Keywords: high contrast, low saturation/Morandi, neon, earth tones, monochrome gradient, multicolor gradient.

### IV. Typography & typesetting
| Type | Traits | Best for |
| --- | --- | --- |
| Serif | Decorative terminals | Editorial, luxury |
| Sans | Clean strokes | Tech, modern |
| Mono | Equal width | Code/tech vibe |
| Script | Handwritten | Personal, artistic |
| Display | Decorative titles | Posters |

Tips: set hierarchy with size/weight/color; use line-height 1.5–1.8; adjust letter spacing on big titles; state weights (light/regular/medium/bold/black).

### V. Motion & interaction (keep subtle)
Types: entrance, hover lift, scroll-trigger, parallax, micro-interactions, particle, typing, number counter.
Adjectives: fluid, elastic, fade-in, slide-in, scale.
Example: “Fade-in on load, cards lift on hover, buttons have elastic click feedback.”

### VI. Mood & atmosphere
Map emotion to direction: professional/trustworthy (stable palette, whitespace, serif), energetic/youthful (high saturation, irregular layout), premium/luxurious (dark, metallic sheen), tech/futuristic (dark + neon, monospace), warm/friendly (warm hues, rounded shapes), fresh/natural (light tones, organic curves).

### VII. Full description template (prompt aide)
```
[Style] e.g., Dark tech with cyberpunk accents
[Colors] Primary deep black (#0D0D0D), accent neon cyan (#00FFF5), secondary magenta (#FF0080)
[Layout]
  - Hero: Full-screen immersive, headline left + animated particle background right
  - Content: Three-column card grid with glassmorphism cards
  - Footer: Simple single column
[Typography] Bold sans for headings, light sans for body
[Motion] Sequential fade-in; cards glow on hover; slow gradient flares in bg
[Mood] High-tech, cutting-edge, mysterious
```

## Optional accelerators
- Provide 2–3 quick palette/font combos the user can pick.
- If the user is undecided on layout, share 2 sketch options (bulleted) before coding.
- Offer to include a printable-friendly variant (A4) only if requested.

## Example theme token scaffold (for `style.css`)
```css
:root[data-theme="light"] {
  --bg: #f8fafc;
  --panel: #ffffff;
  --text: #0f172a;
  --muted: #475569;
  --accent: #0ea5e9;
  --accent-strong: #0284c7;
  --border: #e2e8f0;
  --glow: radial-gradient(circle at 20% 20%, rgba(14,165,233,0.12), transparent 40%),
          radial-gradient(circle at 80% 0%, rgba(94,234,212,0.16), transparent 45%);
}
:root[data-theme="dark"] {
  --bg: #0b1220;
  --panel: #0f172a;
  --text: #e2e8f0;
  --muted: #94a3b8;
  --accent: #22d3ee;
  --accent-strong: #06b6d4;
  --border: #1e293b;
  --glow: radial-gradient(circle at 20% 20%, rgba(34,211,238,0.12), transparent 40%),
          radial-gradient(circle at 80% 0%, rgba(94,234,212,0.16), transparent 45%);
}
```

## Example minimal HTML skeleton (adapt during generation)
```html
<!doctype html>
<html lang="en" data-theme="light" class="scroll-smooth">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>One-Page Visual</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="style.css" />
</head>
<body class="min-h-screen bg-[var(--bg)] text-[var(--text)]" style="font-family: 'Space Grotesk', sans-serif;">
  <div class="absolute inset-0 -z-10" aria-hidden="true" style="background: var(--glow);"></div>
  <header class="mx-auto max-w-6xl px-6 pt-12 flex items-center justify-between">
    <div class="text-sm uppercase tracking-[0.2em] text-[var(--muted)]">Brand</div>
  </header>
  <main class="mx-auto max-w-6xl px-6 py-12 grid gap-12 lg:grid-cols-2 items-center">
    <section class="space-y-6">
      <div class="inline-flex items-center gap-2 rounded-full border border-[var(--border)] px-3 py-1 text-xs text-[var(--muted)]">Badge</div>
      <h1 class="text-4xl sm:text-5xl font-semibold leading-tight">Hero headline</h1>
      <p class="text-lg text-[var(--muted)]">Supportive subheadline that explains the value.</p>
      <div class="flex flex-wrap gap-3">
        <a class="rounded-full bg-[var(--accent)] text-white px-5 py-3 font-medium shadow" href="#">Primary CTA</a>
        <a class="rounded-full border border-[var(--border)] px-5 py-3 font-medium text-[var(--text)]" href="#">Secondary</a>
      </div>
      <div class="grid grid-cols-3 gap-4 text-sm text-[var(--muted)]">
        <div><div class="text-2xl font-semibold text-[var(--text)]">24k</div>Active users</div>
        <div><div class="text-2xl font-semibold text-[var(--text)]">99.9%</div>Uptime</div>
        <div><div class="text-2xl font-semibold text-[var(--text)]">4.9★</div>Rating</div>
      </div>
    </section>
    <section class="relative">
      <div class="rounded-3xl border border-[var(--border)] bg-[var(--panel)]/80 backdrop-blur shadow-xl p-6 h-full flex items-center justify-center">
        <div class="aspect-[4/3] w-full rounded-2xl bg-gradient-to-br from-[var(--accent)]/20 to-[var(--accent-strong)]/10 border border-[var(--border)]"></div>
      </div>
    </section>
  </main>
  <section class="mx-auto max-w-6xl px-6 pb-16 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
    <article class="rounded-2xl border border-[var(--border)] bg-[var(--panel)] p-6 space-y-3">
      <div class="h-10 w-10 rounded-full bg-[var(--accent)]/15 border border-[var(--border)]"></div>
      <h3 class="text-xl font-semibold">Feature title</h3>
      <p class="text-[var(--muted)] text-sm">Short supportive copy.</p>
    </article>
    <!-- Repeat cards as needed -->
  </section>
</body>
</html>
```

Follow the agreed design brief closely and keep HTML/CSS tidy and minimal.

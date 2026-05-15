---
name: make-slide
description: "Generate single-file HTML presentations with 10 professional themes and speaker notes. Use this skill whenever the user mentions presentations, slides, deck, talk, keynote, pitch, slideshow, or wants to turn any content into a visual presentation — even if they don't explicitly say 'slide'. Also triggers for requests like 'make a talk about', 'create a pitch for', 'turn this into slides', or any request to visualize content for an audience."
---

# make-slide — AI Presentation Skill

## Overview

Generate single-file HTML presentations with speaker notes. The output is always a standalone `.html` file with all CSS and JS inlined — no build step, no framework, no dependencies beyond font CDNs.

**Repository**: [github.com/kuneosu/make-slide](https://github.com/kuneosu/make-slide)
**Theme Gallery**: [make-slide.vercel.app](https://make-slide.vercel.app)

---

## When to Use

Activate this skill when the user's request matches any of these patterns:

- "Make a presentation about..."
- "Create slides for..."
- "Build a slide deck..."
- "Turn this into a presentation"
- "Make a talk about..."
- "Create a pitch deck for..."
- "Generate presentation slides..."
- Any request involving: **presentation**, **slides**, **deck**, **talk**, **keynote**, **pitch**, **slideshow**
- Any request to visualize or structure content for an audience, even without explicit "slide" mention

---

## Input Modes

Determine which mode applies based on the user's input:

### Mode A: Topic Only
The user provides a topic and optionally a duration or audience.
```
"Make a 15-min talk about AI trends"
"Create a presentation on microservices architecture"
```
→ Design the structure, content, and speaker notes from scratch.

### Mode B: Content/Material Provided
The user provides source material (documents, notes, data, articles).
```
"Turn this document into a presentation"
"Create slides based on these meeting notes"
```
→ Organize and distill the material into slides + speaker notes.

### Mode C: Script Provided
The user provides a written speech or speaking script.
```
"Create slides for this speech script"
"Make a visual deck that accompanies this talk"
```
→ Analyze the script's structure and create matching visual slides. The script becomes the speaker notes.

---

## Workflow

Follow these steps in order:

### Step 0: Check Project Conventions
Before generating any file, check for project-level instructions that override skill defaults:

- Read `CLAUDE.md` (or `AGENTS.md` / project README) at the project root if present
- Note any documented file-naming conventions (e.g., `[slug]-deck.html` suffix, specific output directory)
- Note any documented design tokens, font rules, or layout conventions
- Project-level rules ALWAYS override skill defaults

### Step 1: Analyze Input
- Determine the input mode (A, B, or C)
- Estimate the appropriate number of slides:
  - 5-min talk → 8–12 slides
  - 10-min talk → 12–18 slides
  - 15-min talk → 18–25 slides
  - 20-min talk → 25–30 slides
  - 30-min talk → 30–40 slides
- Identify the target audience and tone (technical, business, casual, academic)
- Detect the user's language from the conversation — generate content in that language
- Ask the user about the desired output format (always ask, do not skip):
  > **Which output format would you like?**
  > - **HTML** — Interactive single-file presentation you can open in a browser (navigation, animations, speaker notes built-in)
  > - **PPTX** — PowerPoint file for Office, Google Slides, or Keynote

  - If the user already mentioned "PowerPoint", "pptx", "PPT", ".pptx", "Google Slides", or "Keynote" in their request → skip the question and use PPTX mode
  - Otherwise, always ask explicitly before proceeding

### Step 2: Choose a Theme
Present the user with the theme gallery link for browsing:
> **Browse themes here**: https://make-slide.vercel.app

Read `references/themes.md` for the full theme list with GitHub raw URLs and recommendations by context.

If the user doesn't choose a theme, recommend one based on context:
- Tech/developer talk → `minimal-dark` or `neon-terminal`
- Business/corporate → `corporate` or `minimal-light`
- Startup pitch → `gradient-pop` or `keynote-apple`
- Data/analytics → `data-focus`
- Education/workshop → `paper` or `playful`
- Design/creative → `magazine`
- Product launch → `keynote-apple`
- Casual/team event → `playful`

### Step 2.5: Choose a Layout
Ask the user which layout style they prefer:

> **Which layout style would you like?**
> Browse layouts here: https://make-slide.vercel.app (Layouts section)
>
> - **Centered** (default) — Classic centered content, clean and balanced
> - **Wide** — Full-width content, great for data-heavy slides
> - **Split** — Two-column with text + visuals side by side
> - **Editorial** — Magazine-style asymmetric, dramatic typography

If the user doesn't choose, default to **centered**.

Read `references/layouts.md` for layout descriptions and `layouts/{name}/reference.html` for the layout reference code.

When generating HTML, combine the chosen **theme** (colors, fonts, design) with the chosen **layout** (content positioning, spacing, structure).

### Step 3: Image Options
Ask the user which image approach they prefer:

> **How would you like to handle images in your slides?**
>
> **A) No images** — Use styled CSS placeholders (emoji, icons, shapes) that match the theme. Clean and lightweight.
>
> **B) I'll provide URLs** — I'll mark image positions in the outline, and you provide the image URLs.
>
> **C) Auto-search** — I'll search the web for relevant, high-quality images and place them automatically.

- **Option A** → Use CSS placeholders matching the theme (emoji, SVG icons, CSS shapes)
- **Option B** → Mark image positions in the outline, ask user for URLs, use `<img src>` with `loading="lazy"` and descriptive `alt` text
- **Option C** → Automatically search and place images, but be selective:
  1. NOT every slide needs an image. Only add images to slides where a visual genuinely enhances understanding (e.g., concept slides, example slides, section dividers). Skip images for quote slides, code slides, data/chart slides, comparison slides, and agenda slides.
  2. Aim for roughly 30-40% of slides having images — not all of them.
  3. Determine a relevant English search keyword based on the slide content.
  4. Use Unsplash direct photo URLs: `https://images.unsplash.com/photo-{PHOTO_ID}?w=800&h=600&fit=crop`
     - To find valid photo IDs, search the web for `site:unsplash.com {keyword}` and extract the photo ID from the URL.
     - NEVER guess or fabricate Unsplash photo IDs — every URL must come from an actual search result.
  5. After collecting image URLs, verify each one actually returns an image (HTTP 200) before inserting. Replace any 404 URLs with CSS placeholders.
  6. Insert as `<img src="URL" alt="description" loading="lazy">`
  7. Inform the user that images are from Unsplash (Unsplash License, free for commercial use).

### Step 4: Generate Outline
Create a slide-by-slide outline with:
- Slide number
- Slide type (from slide types reference)
- Title
- Key points / content summary
- Image placement (if applicable)

Read `references/slide-types.md` for the 12 available slide type patterns.

Present the outline to the user for confirmation. Wait for approval or modifications before proceeding.

### Step 5: Fetch Theme Reference
Fetch the chosen theme's reference files from GitHub:

1. **reference.html** — The complete example presentation with all slide types, styles, navigation, and interactive features. This is the primary template.
2. **README.md** — Design guidelines including color palette, typography, spacing rules, and design philosophy.

Use the raw GitHub URLs listed in `references/themes.md`.

### Step 6: Generate HTML
Using the theme's reference.html and the layout's reference.html as templates:
- Use the **theme's** reference.html for visual styling (colors, fonts, design elements)
- Use the **layout's** reference.html for content structure and positioning
- Replace the demo content with the user's actual content
- Keep all interactive features (navigation, fullscreen, speaker notes, etc.)
- Match the theme's typography, colors, spacing, and animations
- Ensure all slide types used match the patterns in the reference

Read `references/core-features.md` and use the exact JavaScript code provided for navigation, fullscreen, speaker notes popup, progress bar, and slide counter. Do not rewrite these features — copy the code directly. This ensures consistent behavior across all AI models.

Read `references/html-spec.md` for the full HTML requirements including navigation, fullscreen, PDF export, CDN dependencies, image handling, and code blocks.

**Critical CSS rules** — see `## Responsive Design` and `## Interactive Elements & Click Routing` sections below for required patterns (responsive architecture, chart flex-shrink, popup positioning, click/wheel handlers, modals).

### Step 7: Generate Speaker Notes
Add speaker notes as `data-notes` attributes on each slide's `<div>`:
```html
<div class="slide" data-notes="Welcome everyone. Today I'll be talking about...">
```
- Notes should be conversational and natural
- Include timing cues where helpful (e.g., "[PAUSE]", "[2 min]")
- Expand on the slide text — don't just repeat it
- Include transitions between slides (e.g., "Now let's move on to...")

**Speaker Notes Panel must be a separate popup window** using `window.open()`. Do NOT render notes inline at the bottom of the slide — this breaks the slide layout. The `S` key should toggle a popup window that shows the current slide's notes and auto-updates on slide change. See `references/html-spec.md` for the implementation pattern.

### Step 8: Generate Script (Mode A and B only)
For Mode A and B, also generate a separate `script.md` file containing:
- Full speaking script organized by slide
- Timing estimates per section
- Audience interaction cues
- Key points to emphasize

For Mode C, the user already has a script — skip this step.

### Step 9: Save and Deliver
- Save the presentation as `index.html` by default, unless project rules (Step 0) specify otherwise
- Save the script as `script.md` (if generated)
- Tell the user they can open the HTML file directly in their browser — no server needed
- The file is fully self-contained (all CSS/JS inlined), so it works by simply double-clicking the file or dragging it into a browser

---

## PPTX Output Mode

When the user selects PPTX output, follow this modified workflow:

### PPTX Step 1: Generate HTML Slides (PPTX-Compatible)
Follow the standard HTML generation workflow (Steps 1-7) but with these constraints from the PPTX spec. Read `references/pptx-spec.md` for the complete PPTX conversion rules before generating HTML.

### PPTX Step 2: Convert HTML to PPTX
Use the screenshot-based conversion pipeline with Puppeteer + PptxGenJS:
1. Install dependencies if not present: `npm install pptxgenjs puppeteer`
2. Write a conversion script that:
   - Opens the HTML file in a headless browser with viewport 1280×720 (16:9)
   - For EACH slide:
     a. Navigate to that slide (set it as active, remove active class from others)
     b. **Disable animations and force visibility** — inject CSS to disable all animations/transitions AND force `.a` elements visible: `* { animation: none !important; transition: none !important; } .slide.active .a, .a { opacity: 1 !important; transform: none !important; }`. Also wait for font loading with `document.fonts.ready`.
     c. **Hide all other slides completely** — ensure only the current slide is visible (opacity:1, display:flex) and all others are hidden (opacity:0, display:none). This prevents ghost/residue from previous slides.
     d. Take a full-page screenshot of the viewport at **2x resolution** (deviceScaleFactor: 2) for crisp text
   - Insert each screenshot into PPTX as a **full-slide image** covering the entire slide area (x:0, y:0, w:'100%', h:'100%')
   - Do NOT add margins or padding around the image — it should fill the entire slide
3. Save as `.pptx`

**Critical: Preventing ghost slides and small content**
```javascript
// Before each screenshot, inject CSS to disable animations AND force animated elements visible
await page.addStyleTag({ content: '*, *::before, *::after { animation: none !important; transition: none !important; animation-delay: 0s !important; } .slide.active .a, .a { opacity: 1 !important; transform: none !important; }' });

// Wait for fonts to load
await page.evaluateHandle('document.fonts.ready');

// Hide all slides, then show only current
await page.evaluate((idx) => {
  document.querySelectorAll('.slide').forEach((s, i) => {
    s.style.display = i === idx ? 'flex' : 'none';
    s.style.opacity = i === idx ? '1' : '0';
    s.classList.toggle('active', i === idx);
  });
}, slideIndex);

// Wait for layout to settle
await new Promise(r => setTimeout(r, 500));

// Screenshot at 2x for crisp text
await page.screenshot({ path: outputPath, type: 'png' });
```

### PPTX Step 3: Validate and Deliver
- Verify the PPTX opens correctly and content fills each slide without excess margins
- Save as `presentation.pptx` (or user-specified filename)
- Offer to also generate the HTML version for preview

---

## Output Rules

1. Always output a single `.html` file with all CSS and JS inlined
2. Only allowed external dependencies: **Font CDN (Pretendard only — see "Typography & Multilingual" below)** + Prism.js CDN (conditional, for code highlighting). DO NOT include JetBrains Mono, Fira Code, or any Latin-only monospace web font, even if the theme reference includes it — strip those `<link>` tags.
3. Speaker notes embedded as `data-notes` attributes on each slide `<div>`
4. Optionally output `script.md` for full speaking script (Mode A and B)
5. Generate content in the user's language — detect from the conversation context
6. Filename: `index.html` by default, or as specified by the user / project rules
7. Vanilla JS only — no JavaScript frameworks
8. Vanilla CSS only — no CSS frameworks

---

## Typography & Multilingual

Decks must read cleanly across all target languages, including CJK (Korean, Japanese, Chinese).

### Font rule — Pretendard only

- **Use Pretendard** (`'Pretendard Variable', Pretendard, -apple-system, BlinkMacSystemFont, system-ui, 'Apple SD Gothic Neo', 'Noto Sans KR', sans-serif`) as the **sole** typeface for the entire deck — body text, headings, UI, captions, slide counter, numeric stats, everything.
- **DO NOT use** `JetBrains Mono`, `Fira Code`, `Source Code Pro`, or any Latin-only monospace web font. They lack proper Hangul/Kana/Hanzi glyphs and the browser falls back to a mismatched system font, producing visibly ugly mixed-script rendering.
- If a CSS variable `--font-mono` exists in the theme reference, redefine it to alias the body font: `--font-mono: var(--font-body);`. Do not remove the variable name (other rules may reference it), just redirect it.
- Remove ANY `@import url('...JetBrains+Mono...')` or `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono...">` from the theme reference before generating.

### Numeric alignment without monospace

When numbers need to align in columns (chart values, stats, slide counters, tabular data), use OpenType tabular figures:
```css
.chart-value, .stat-number, .slide-counter, .src-meta {
  font-variant-numeric: tabular-nums;
}
```
Pretendard supports tabular-nums and renders properly aligned numerals at proportional widths.

### Reuse for theme overrides

When the theme's reference.html has hardcoded `font-family: 'JetBrains Mono', monospace` rules, replace each with `font-family: inherit; font-variant-numeric: tabular-nums;`. This preserves layout intent while routing to Pretendard.

---

## Responsive Design

A web-native deck must read across viewports from 4K presentation displays down to mobile portrait. Use a **two-architecture model**, switched by media query — not by CSS scale-transform, which renders text as scaled pixels and breaks selection/accessibility.

### Wide viewport (≥1024px) — "deck mode"

One slide per viewport, fade between slides. Body content centered in remaining space below the title.

```css
.slide { position: absolute; inset: 0; display: flex; flex-direction: column; padding: 50px 60px; opacity: 0; visibility: hidden; overflow-y: auto; }
.slide.active { opacity: 1; visibility: visible; }

/* Content slides: title fixed at top, body safely centered */
.slide:not(:has(.slide-title)):not(:has(.slide-quote)):not(:has(.slide-closing)) {
  justify-content: safe center;
  padding-top: 210px;
}
.slide:not(:has(.slide-title)):not(:has(.slide-quote)):not(:has(.slide-closing)) h2 {
  position: absolute; top: 110px; left: 60px; right: 60px;
  margin: 0 !important; text-align: center !important; z-index: 1;
}
```

**Critical: `justify-content: safe center`** — NOT plain `center`. The `safe` keyword makes flexbox fall back to `flex-start` when content overflows the container. Without `safe`, centered content extends BOTH above and below the container, causing tall body content to overlap an absolute-positioned title at the top of the slide. This was a real production bug.

### Narrow viewport (<1024px) — "web reflow mode"

Only the active slide is in flow; body scrolls vertically; multi-column layouts collapse.

```css
@media (max-width: 1023px) {
  body { overflow-x: hidden; overflow-y: auto; height: auto; min-height: 100vh; }
  .deck { height: auto; min-height: 100vh; }
  .slide {
    position: relative; height: auto; min-height: 100vh; width: 100%;
    padding: 44px 24px; opacity: 1; visibility: visible; transition: none;
    overflow: visible; display: none;
  }
  .slide.active { display: flex; }
  .slide.active .a { animation: none; opacity: 1; transform: none; }

  /* h2 to normal flow */
  .slide:not(:has(.slide-title)):not(:has(.slide-quote)):not(:has(.slide-closing)) {
    justify-content: flex-start !important;
    padding-top: 44px !important;
  }
  .slide:not(:has(.slide-title)):not(:has(.slide-quote)):not(:has(.slide-closing)) h2 {
    position: static !important;
    margin: 0 auto 20px !important;
    text-align: center !important;
  }

  /* Multi-column to single column */
  .comparison, .cards { grid-template-columns: 1fr; gap: 16px; }
  .steps { flex-direction: column; gap: 12px; }
  .step-arrow { transform: rotate(90deg); }
}
```

Add finer breakpoints at 768px and 480px for tablet/mobile, with proportional reduction of BOTH heading AND body font sizes (preserves hierarchy — never reduce only one).

### Animations on narrow
Disable entrance stagger animations in narrow mode (`.slide.active .a { animation: none; opacity: 1; transform: none; }`). They look awkward when slides reflow naturally and slow down scroll.

### Touch / no-hover devices

```css
@media (hover: none) {
  .chart-bar-group.has-popup .chart-bar-popup,
  .chart-bar-group.has-popup:hover .chart-bar-popup {
    opacity: 0; pointer-events: none;
  }
  .chart-bar-group.has-popup.tapped .chart-bar-popup {
    opacity: 1; pointer-events: auto;
  }
}
```

JS toggles `.tapped` on bar tap, untaps siblings, dismisses on document click outside.

---

## Chart-Specific Rules

CSS-only bar charts have several non-obvious failure modes. Apply these defaults:

### Prevent flex-shrink collapse

```css
.chart {
  display: flex;
  align-items: flex-end;
  gap: 60px;
  height: 380px;
  flex-shrink: 0;    /* CRITICAL — without this, the slide's flex parent compresses
                        the chart and percentage-based bar heights collapse to 0,
                        making bars invisible in mid-width viewports */
  width: 100%;
  max-width: 1180px;
  padding: 0 24px;
}
```

### Muted bars: use background alpha, not opacity

```css
.chart-bar.muted {
  background: rgba(75, 85, 99, 0.45);   /* OK — only the bar fades */
  /* NOT: opacity: 0.45 — element opacity cascades to child popups/labels,
     making the popups look faded too */
}
```

### Narrow-viewport chart sizing

Percentage-based bar heights require an explicit parent height. In narrow viewports, set chart height explicitly per breakpoint:
```css
@media (max-width: 1023px) { .chart { height: 300px; } .chart-bar { width: 72px; } }
@media (max-width: 768px)  { .chart { height: 260px; } .chart-bar { width: 60px; } }
@media (max-width: 480px)  { .chart { height: 220px; } .chart-bar { width: 50px; } }
.chart-bar-group { height: 100%; }   /* explicit so % bars resolve */
```

Also add `overflow-x: auto` to `.chart` in narrow mode so 4+ bars don't squeeze unreadably.

### Hover popups anchored to bar top

Place the popup as a child of `.chart-bar` (NOT as a child of `.chart-bar-group`), with `position: relative` on `.chart-bar`. Position the popup with `bottom: calc(100% + 36px)` so it sits just above the bar's actual rendered top — regardless of bar height (4% bars and 92% bars both get the popup at the right spot).

```html
<div class="chart-bar-group has-popup">
  <div class="chart-value">+195%</div>
  <div class="chart-bar gold" style="height: 88%;">
    <div class="chart-bar-popup">…popup content…
      <div class="chart-bar-popup-bridge"></div>   <!-- transparent hit-zone to prevent flicker -->
    </div>
  </div>
  <div class="chart-label">$30 ~ $50</div>
</div>
```

```css
.chart-bar { position: relative; }
.chart-bar-popup {
  position: absolute; bottom: calc(100% + 36px);
  left: 50%; transform: translateX(-50%);
  opacity: 0; pointer-events: none;
  transition: opacity 0.18s ease, transform 0.18s ease;
}
.chart-bar-group.has-popup:hover .chart-bar-popup,
.chart-bar-popup:hover {   /* second selector keeps it open when cursor crosses gap */
  opacity: 1; pointer-events: auto;
}
.chart-bar-popup-bridge {
  position: absolute; top: 100%; left: 50%; transform: translateX(-50%);
  width: 90%; height: 50px; pointer-events: none;
}
.chart-bar-popup:hover .chart-bar-popup-bridge { pointer-events: auto; }
```

For "edge" bars (leftmost / rightmost), add a `popup-left` / `popup-right` class to offset the popup inward so it doesn't extend off-slide.

### Default-shown popup on slide entry

If you want one bar's popup visible by default when the user lands on the slide (e.g., a hero callout), add a `.default-shown` class to that bar-group on slide activation, and remove it on first chart hover. CSS:

```css
.slide.active .chart-bar-group.default-shown .chart-bar-popup {
  opacity: 1; pointer-events: auto; transform: translateX(-50%) translateY(0);
}
```

JS uses MutationObserver on the slide's `class` to re-add `.default-shown` whenever the slide becomes active again.

---

## Interactive Elements & Click Routing

The deck's default click and wheel handlers can swallow events on interactive widgets unless properly scoped. Apply these patterns when adding sliders, toggles, hover popups, or modals.

### Click navigation allowlist

The deck-level click handler (left third → prev, right two-thirds → next) lives on `.deck`. Add interactive widget classes to its allowlist:

```js
document.querySelector('.deck').addEventListener('click', function (e) {
  if (e.target.closest(
    'a, button, input, label, summary, details, ' +
    '.card, .step, .toc-list li, ' +
    '.your-widget-class, .chart-bar-group.has-popup, .source-btn, .source-modal'
  )) return;
  // … prev/next based on click X position
});
```

If you forget to add a widget class, clicking the widget triggers slide navigation. Always test interactive elements after adding them.

### Wheel handler — edge-aware (option 1: scroll within slide, navigate at edge)

Recommended default. Lets users scroll long content naturally; navigation triggers only when scrolling past slide edges.

```js
document.addEventListener('wheel', function (e) {
  if (Math.abs(e.deltaY) < 30) return;
  if (wheelLocked) return;
  var narrow = window.matchMedia('(max-width: 1023px)').matches;
  var container = narrow
    ? (document.scrollingElement || document.documentElement)
    : document.querySelector('.slide.active');
  if (!container) return;
  var scrollable = container.scrollHeight > container.clientHeight + 1;
  var atTop = container.scrollTop <= 1;
  var atBottom = container.scrollTop + container.clientHeight >= container.scrollHeight - 1;
  if (scrollable) {
    if (e.deltaY > 0 && !atBottom) return;
    if (e.deltaY < 0 && !atTop) return;
  }
  wheelLocked = true;
  if (e.deltaY > 0) next(); else prev();
  setTimeout(function () { wheelLocked = false; }, 350);
}, { passive: true });
```

Inside `goTo(index)`, reset scroll so the new slide starts at its top:
```js
if (window.matchMedia('(max-width: 1023px)').matches) {
  window.scrollTo({ top: 0, behavior: 'auto' });
} else if (slides[current].scrollTop) {
  slides[current].scrollTop = 0;
}
```

### Source citations / detail panels — use overlay modal, NOT inline `<details>`

For citations, references, or expandable content (which is common in data-heavy decks), use a **fixed overlay modal** rendered outside `.deck`. Inline `<details>` causes three problems:
1. Opening pushes content down, often beyond the slide viewport (forcing scroll)
2. Mouse wheel during scroll triggers the deck's wheel handler → unintended slide change
3. Layout shifts can break carefully tuned typography spacing

Pattern:
```html
<!-- On each slide that needs a source citation -->
<button class="source-btn" data-source="slide-4">출처 정보</button>
<div class="source-data" data-source-id="slide-4" data-title="가격대 변화 — 출처">
  <div class="src-section">
    <span class="src-title">Newzoo 2026 Market Report</span>
    <a class="src-link" href="https://newzoo.com" target="_blank" rel="noopener">newzoo.com</a>
    <p class="src-quote">"…"</p>
    <p class="src-meta">Newzoo · 2026</p>
  </div>
</div>

<!-- Single shared modal at end of body, OUTSIDE .deck -->
<div class="source-modal" id="source-modal" aria-hidden="true">
  <div class="source-modal-backdrop" data-modal-close></div>
  <div class="source-modal-card">
    <button class="source-modal-close" data-modal-close aria-label="닫기">&times;</button>
    <h3 id="source-modal-title"></h3>
    <div class="source-modal-content"></div>
  </div>
</div>
```

```css
.source-data { display: none; }
.source-modal {
  position: fixed; inset: 0; z-index: 3000;
  display: flex; align-items: center; justify-content: center;
  opacity: 0; pointer-events: none;
  transition: opacity 0.22s ease;
}
.source-modal.open { opacity: 1; pointer-events: auto; }
.source-modal-backdrop { position: absolute; inset: 0; background: rgba(12,22,38,0.55); backdrop-filter: blur(4px); }
.source-modal-card { position: relative; background: #fff; border-radius: 12px; max-width: 720px; width: calc(100% - 60px); max-height: calc(100vh - 80px); overflow-y: auto; padding: 26px 32px; }
```

JS: on button click, clone `.source-data` content into `.source-modal-content`, add `.open` class. On close (× button, backdrop click, ESC key), remove `.open`. While modal is open, intercept Escape and arrow keys in capture phase with `stopImmediatePropagation()` so the deck doesn't navigate.

### Slider / range input widgets

Range inputs work natively but need to be excluded from the deck's keyboard navigation. The existing keyboard handler at document level should early-return when `e.target.tagName === 'INPUT'`:
```js
document.addEventListener('keydown', function (e) {
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
  // … arrow key navigation
});
```
This lets arrow keys adjust the slider when focused, instead of jumping slides.

### Toggle / tab widgets

For binary toggles (e.g., "Before / After" comparison), use two radio-styled buttons + JS to swap content panels. Add the toggle button container class (e.g., `.model-toggle-tabs`) to the click navigation allowlist.

---

## Backup before destructive edits

When iterating on a deck that already has content, save a backup with `_bak` suffix before large refactors:
```
steam-marketing-strategy-deck.html  →  steam-marketing-strategy-deck_bak.html
```
This gives a single-step rollback if a refactor breaks something subtle.

---

## Tips for Best Results

### Content
- Keep slides concise: max 6–8 bullet points per slide
- One core idea per slide
- Use short phrases, not full sentences, on slides
- Save detailed explanations for speaker notes

### Design
- Use the theme's accent color for emphasis and key terms
- Match typography hierarchy exactly from the reference.html
- Maintain consistent spacing and padding throughout
- Work within the theme's design system — don't override its core design

### Speaker Notes
- Write notes in a conversational tone
- Expand, explain, give examples — don't just repeat slide text
- Include timing hints: "[This section: ~3 minutes]"
- Add transition phrases: "Now let's look at...", "Building on that..."
- Mark audience interaction points: "[ASK AUDIENCE]", "[DEMO]", "[PAUSE]"

### Data Visualization
- Use CSS-only charts when possible (bar charts, progress bars, donut charts)
- Apply `flex-shrink: 0` on chart containers (see Chart-Specific Rules)
- Keep numbers round and memorable (say "nearly 50%" not "49.7%")
- Highlight the most important metric with size or color

### Performance
- Keep total HTML file size under 200KB ideally
- Use `loading="lazy"` on images
- Minimize complex CSS animations on slides with heavy content

### Accessibility
- Maintain sufficient color contrast ratios
- Include `alt` text on all images
- Ensure keyboard navigation works for all interactive elements
- Use semantic HTML where appropriate

---

## Quick Start Example

If the user says: *"Make a 10-minute presentation about Python best practices"*

1. **Step 0**: Check for project-level CLAUDE.md / conventions
2. **Mode**: A (Topic only)
3. **Slides**: ~15 slides
4. **Theme recommendation**: `minimal-dark` or `neon-terminal` (developer topic)
5. **Ask**: Theme preference + image needs
6. **Generate outline** → Get confirmation
7. **Fetch**: `minimal-dark/reference.html` + `minimal-dark/README.md`
8. **Strip JetBrains Mono import** from theme reference; route `--font-mono` to Pretendard
9. **Apply** Responsive Design + Chart + Click Routing patterns
10. **Generate**: `index.html` + `script.md`
11. **Offer**: Local file preview

---

*Skill version: 2.1 | Repository: [kuneosu/make-slide](https://github.com/kuneosu/make-slide) | Gallery: [make-slide.vercel.app](https://make-slide.vercel.app)*
*Changelog v2.1: Pretendard-only font rule (no JetBrains Mono); two-architecture responsive model with `safe center`; chart flex-shrink + alpha-bg patterns; hover popup anchored to bar top; tap-to-show on no-hover devices; click/wheel/modal patterns; project conventions step.*

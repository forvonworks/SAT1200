# Book Design Spec — Fonts, Sizes, Colors, Page Structure

**Status: locked baseline, v2 — corrected against the real book.** §§2-5 and 9
below were originally guessed from a from-scratch prototype and were **wrong**
— they didn't match the actual existing Canva book (`White and Black Modern
Book Cover A4`, design ID `DAHSYbGKTZo`). This version replaces those sections
with values pulled directly from that design's element data (exact hex colors,
positions, and font sizes, converted from Canva's 794×1123px page canvas to
real mm/pt via a 210mm/794px position scale and a 0.75pt/px font scale — Canva
canvas is 96dpi, print is 72dpi, hence the 0.75 factor). Treat §§2-5 and 9 as
ground truth; don't re-guess from thumbnails again.

Fonts (§6 Libertinus Serif/Sans/Math) and the content-block pattern (§10 —
Definition → Model → Your-turn → Common Mistake → Vocabulary) are a
**deliberate upgrade** over the old book's plain bullet-list format, grounded
in the worked-example/split-attention pedagogy research, and were not part of
the user's complaint — kept as-is. Everything about brand chrome (colors,
header, watermark, footer) is now pixel-matched to the real book instead.

Derived from: live element-data read of design `DAHSYbGKTZo` pages 1 (cover)
and 5-7 (Lesson 1 content + practice), `06-concept-explanation-pedagogy.md`,
`08-concept-explanation-style-guide.md`.

---

## 1. Why LaTeX/XeLaTeX instead of Canva

Canva could not hold a consistent look across pages in practice: font/size drift
page to page, a DPI-halving bug, pixel-color-detection workarounds just to locate
text, image corruption on resize, and a matplotlib bug that force-bolded text
containing an apostrophe. None of that is a one-off — it's structural: Canva is a
freeform visual editor, not a template-driven typesetting system, so nothing
enforces consistency between pages.

XeLaTeX fixes this at the root: every page is generated from the same `.tex`
template with the same macros (`\pageheader`, `\pagefooter`, content-block
commands), so font, size, color, and spacing are identical everywhere by
construction, not by careful manual matching. Math renders natively (no
image/DPI pipeline). Fonts are controlled via `fontspec`/`unicode-math`.

## 2. Fonts

**Chosen family: Libertinus** (Serif + Sans + Math), not bundled with the system
TeX install — fetched manually from
`https://github.com/alerque/libertinus/releases/download/v7.040/Libertinus-7.040.zip`,
`.otf` files copied to `~/.fonts/`, registered with `fc-cache -f ~/.fonts`.

```latex
\setmainfont{Libertinus Serif}   % body text, Uzbek + English prose
\setsansfont{Libertinus Sans}    % headers, labels, UI chrome (header bar, footer, box titles)
\setmathfont{Libertinus Math}    % all math — matches the serif body visually
```

Compared against: Latin Modern Roman, EB Garamond, Linux Libertine O, Gentium,
Caladea, Carlito. Libertinus won on: full Cyrillic/Uzbek Latin-extended glyph
coverage with no missing-glyph boxes (EB Garamond bold dropped an en-dash glyph;
Gentium had no real bold shape and LaTeX faked one), a math font that's a true
visual match to the body serif (not just "a math font that exists"), and a sans
companion in the same family for headers — avoids the mismatched-pairing look.

**Do not substitute fonts per-page.** One family, three roles (serif body / sans
chrome / math), everywhere.

## 3. Type sizes (corrected, matches real book)

Body/bullet text: **18pt** (`fontSize: 24` in Canva's px-equivalent units ×
0.75pt/px). This is much larger than our original 11pt guess — the real book
is written at this size throughout. Concept pages built with the boxed
Model/Your-turn pattern (denser than the old plain-bullet format) should use
11-12pt within those boxes to actually fit the extra pedagogical content on
one page — bullet-style content (vocabulary, short definitions, practice
numbers) should use the true 18pt to match.

| Role | Size | Style |
|---|---|---|
| Header "Lesson N" badge text | sans, 28pt, bold | white, on `badge`-fill pill |
| Header topic title | sans, 19pt, bold | `accent`, centered |
| Header Uzbek subtitle | sans, 14.5pt, bold | `badge` color, centered |
| Section label ("Concepts:") | serif, 19pt, bold italic | black, centered |
| Body bullet text | serif, 18pt | black (`#000000`, not `ink`) |
| Example/"ex:" lines within bullets | serif, 18pt | `accent` |
| Vocabulary list | serif, 18pt (or smaller if tight) | black |
| Practice set heading ("Set N") | serif, italic, centered | black |
| Footer handle / page number | sans, italic, 14pt | `accent` |

## 4. Colors (corrected — one color added)

| Token | Hex | Use |
|---|---|---|
| `accent` | `#F46530` | Title text, example lines, footer, dividers, emphasis |
| `badge` | `#FFBDA5` | Header pill/circle fill, Uzbek subtitle text — **new, was missing entirely from v1** |
| `ink` | `#2A2E30` | Watermark text color only (not body text) |
| black | `#000000` | Body bullet text, "Concepts:" label — real book uses pure black here, not `ink` |

`accentlight` (`#FFEEE8`) from v1 is **not used anywhere in the real book** —
drop it. No full-bleed colored header band exists; the header is white with a
pill badge on it, not a colored band.

## 5. Page geometry (corrected — pixel-matched)

All positions below are converted from the real Canva design (`DAHSYbGKTZo`,
pages 1/5-7) at 210mm/794px for positions and 0.75pt/px for font sizes (Canva
canvas is 96dpi, print is 72dpi).

- **A4, zero page margin**, absolute-positioned `textblock*` (`textpos`),
  same as v1 — this part was right.
- **Background: white**, not a colored band. The "light red" the user saw is
  the header pill + subtitle color (`badge`), not a page band.
- **Watermark** (every page, behind content): two large bold "sat / 1200+"
  text blocks, serif... no — **sans**, bold, 81pt, color `ink` tinted to ~7%
  opacity (approximate with `ink!7` — mixing with white, since true alpha
  isn't needed against a white background), centered at (112.8mm, 111.9mm)
  rotated 12.16°, and a second copy centered at (97.1mm, 185.0mm) rotated
  -167.84° (i.e. the same block mirrored/flipped to the opposite corner —
  together they form a diamond-ish watermark, not true circular text as the
  thumbnail suggested). Plus "math" centered at (105.0mm, 148.4mm), 114pt,
  bold, `accent` tinted to ~14% opacity (`accent!14`), no rotation.
- **Header pill badge:** rounded rectangle, fill `badge`, from
  roughly x=-12.9mm to x=56.7mm (bleeds off the left page edge), y=10.5mm,
  height=12.5mm, rounded corners on the visible (right) end only — achieved
  in the original via a rectangle + overlapping circle, but a plain
  `rounded corners` rect reproduces the same look. Contains "Lesson N" in
  white 28pt bold, centered in that pill.
- **Header title:** "LESSON TOPIC NAME" in `accent`, 19pt bold, centered,
  box starting x=72.0mm, y=11.5mm, width=128.9mm.
- **Header subtitle:** Uzbek translation of the topic, `badge` color, 14.5pt
  bold, centered, box starting x=109.5mm, y=19.3mm, width=59.8mm (sits
  directly under the title, narrower, right-of-center).
- **"Concepts:" section label:** bold italic serif, 19pt, **black** (not
  accent), centered, at roughly x=92.7mm, y=34.9mm.
- **Body content area:** starts x=5.5mm, y=48.6mm, width=199mm (nearly full
  page width minus small margins), bullet-point format.
- **Footer:** solid `accent` bar, full width (202mm), at y=286.4mm. Below it:
  `@sat1200plus` handle at x=-5.8mm (bleeds slightly off left edge, text
  box is wide enough that visible text starts near the true margin),
  page number at x=198.6mm (right edge) — both y=288.3mm, 14pt italic accent.
- **Page style:** `\pagestyle{empty}`, header/footer/watermark drawn by
  macros on every page, same as v1.

**Simplification kept from v1, not from the real book:** the real header also
has two small decorative accent-colored "elbowed" swoosh lines near the pill
badge and a thin accent divider line specific to one lesson's diagram layout.
These are minor and content-specific — not reproduced. Flag to the user if an
exact match including these becomes important later.

## 6. Content block pattern (per concept page)

From the pedagogy research (worked-example effect, split-attention effect — see
`06-concept-explanation-pedagogy.md`), every concept page follows this fixed
sequence, no exceptions:

1. **Definition + notation** — native Uzbek definition first (term-first,
   verb-last structure per `07`/`08`), terse English gloss second, in muted
   `ink!70` small text below it. Math notation inline where relevant.
2. **Model example ("N-misol")** — solid accent-bordered rounded box. Fully
   worked, fully reasoned ("I do"). Problem statement → labeled **Yechish:**
   reasoning → **Javob:** boxed answer.
3. **Your-turn example ("O'zingiz bajaring")** — dashed muted-border box, same
   visual family as the model box but visually distinct as "incomplete" (dashed,
   `ink!40`). Same problem shape as the model example, blanks via
   `\makebox[Nmm]{\dotfill}` for the student to fill in by hand.
4. *(Conditional, only when the topic has a documented common error — see
   `04-common-student-mistakes.md`)* — a common-mistake box pairing the wrong
   approach with the correct one.
5. **Vocabulary** — two-column mini-glossary (`minipage` pair), English term —
   Uzbek term, small serif, directly below the worked examples.
6. *(Not shown in the prototype — still needed per-lesson)* **Practice set** —
   this is the **second file per lesson** (problems file), not inline on the
   concept page itself, per the agreed two-file workflow.

Labels/diagrams are always integrated directly into the example box they
explain — never a separate "see figure below" reference (split-attention
effect: forcing the eye to jump between text and a separate diagram measurably
hurts learning).

## 7. Reference artifacts

- `fontcompare.tex` — 6-font + 4-size comparison sheet (not yet committed to
  repo; was a scratch comparison, superseded by the decision above).
- `prototype.tex` — full A4 mockup of a Concepts page in final fonts/colors,
  demonstrating the pattern in §6, topic "Fractions" (Lesson 2 placeholder, not
  necessarily Book 1's actual Lesson 2 — see annotated TOC for real lesson
  order). Both were reviewed and approved as the direction to build on.

## 8. Known gotcha — multi-page documents with `textpos`

**`\usepackage[absolute,overlay]{textpos}` silently merges every page onto
page 1 in a multi-page document.** The `overlay` option makes textblocks
contribute zero real content to the page, so when a lesson's content is
*entirely* absolute-positioned boxes (as every page here is), TeX never
finds a real breakpoint and dumps everything into one final shipout —
`\newpage`/`\clearpage` between pages gets silently ignored, with no error.

**Fix, both required:**
1. Drop `overlay` from the package options — use `\usepackage[absolute]{textpos}` only.
2. Put `\mbox{}` as the first thing after each page's `\pageheader{...}{...}`
   call, before any `textblock*` content — this gives TeX one real (invisible)
   box per page so `\clearpage` has actual material to break on.

Without both of these, a multi-page lesson compiles cleanly (no LaTeX errors)
but silently produces a 1-page PDF with every page's content stacked
illegibly on top of each other — always render and visually check page count
after adding pages, don't just check for compile errors.

## 9. Practice-set page layout (corrected — matches real book)

v1 used a single-column numbered list, 11pt, minimal spacing — wrong on two
counts the user flagged directly: wasted space (cost matters, these get
printed and sold) and wrong column structure. Real book pattern:

- **Two columns**, divided by a single thin vertical rule down the page
  center — not two independent blocks, one shared rule between them.
- **"Set N" heading**, italic serif, centered, directly above the two
  columns, with a one-line italic instruction below it ("Add the Positive
  Integers:", etc.).
- **Each problem is terse** ("3+4=") with **generous vertical space after
  it** for the student to write the answer by hand directly on the page —
  this is deliberate blank space *for writing*, not wasted space; the v1
  mistake was leaving blank space from under-filling the page, not from
  write-in room.
- Fill the page: pack as many sets/problems as fit using the write-in
  spacing above, rather than one short set per page. Cost-per-page is real
  money once printed — density matters.

## 10. What's still open

- Multi-page concept lessons (when one topic needs more than one page) —
  pattern not yet tested at scale.
- Cover/front-matter/table-of-contents page design — out of scope until Book 1
  content is further along.
- The decorative elbow-swoosh lines and content-specific dividers noted in
  §5 — not reproduced, revisit if the user wants an exact match.

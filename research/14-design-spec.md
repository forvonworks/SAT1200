# Book Design Spec — Fonts, Sizes, Colors, Page Structure

**Status: locked baseline.** This is the single source of truth for how every book
page is typeset. Every Book 1/2/3 lesson page should follow this spec exactly —
that consistency is the whole point of moving off Canva. If something here needs
to change, change it here first, then re-derive the pages — never drift a single
page off-spec by hand.

Derived from: `01-official-sat-math-spec.md`, `06-concept-explanation-pedagogy.md`,
`08-concept-explanation-style-guide.md`, plus two compiled prototypes built and
reviewed earlier in this project (font comparison sheet + full mockup page).

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

## 3. Type sizes

Body text: **11pt / 15pt leading** (`\fontsize{11}{15}\selectfont`). Tested
9/10/11/12pt at matching leading on a full A4 page with real Uzbek+English+math
content; 11pt was the chosen balance — 9–10pt read cramped at normal reading
distance for a dense bilingual page, 12pt wasted space given how much every
concept page needs to hold (native definition, English gloss, worked example,
practice prompt, vocabulary). This matches typical printed-textbook body size
(most printed A4 textbooks run 10–12pt body).

| Role | Size | Leading | Style |
|---|---|---|---|
| Page header lesson label ("LESSON 2") | sans, `\large`, bold | — | accent color |
| Page header topic title ("FRACTIONS") | sans, `\large`, bold | — | accent color, right-aligned |
| Section label ("Concepts") | sans, `\Large`, bold italic | — | ink, centered |
| Body text (definitions, prose) | serif, 11pt | 15pt | ink |
| Secondary/gloss text (English translation line) | serif, `\small`, 70% ink | — | ink!70 |
| Box titles ("1-misol", "O'zingiz bajaring") | sans, bold | — | accent / ink!70 |
| Vocabulary list | serif, `\small` | — | ink |
| Footer handle / page number | sans, italic/`\small` | — | accent |

## 4. Colors

Brand palette, fixed:

| Token | Hex | Use |
|---|---|---|
| `accent` | `#F46530` | Headers, box titles, footer rule, emphasis |
| `accentlight` | `#FFEEE8` | Header bar background (full-bleed band) |
| `ink` | `#2A2E30` | Body text (near-black, not pure black) |

No other colors. Tints of `ink` (e.g. `ink!70`, `ink!40`) are allowed for
secondary text and muted borders — no new hues.

## 5. Page geometry

- **A4, zero page margin** (`geometry: margin=0mm`) — all layout is done via
  absolute-positioned `textblock*` blocks (`textpos` package), not LaTeX's normal
  flowing margins. This gives exact, repeatable pixel-level placement instead of
  "roughly consistent" flow layout.
- **Header band:** full-bleed `accentlight` rectangle, 0–14mm from top. Lesson
  label at left (12mm from left edge), topic title at right, both 4mm from top,
  sans bold accent.
- **Footer:** thin `accent` rule at 186mm width, 12mm from left edge, y=280mm.
  Below it: handle (`@sat1200plus`) at left, page number at right, both sans,
  accent color, 283mm from top.
- **Content area:** 170mm wide, starting 20mm from left, 22mm from top (section
  label), body content starts ~34mm from top. Effective content column leaves
  ~20mm margin left/right within the un-printed header/footer bands.
- **Page style:** `\pagestyle{empty}` — no running LaTeX page numbers; header/
  footer are hand-drawn via the macros above, same on every page.

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

## 9. What's still open

- Practice-set page layout (problems file → typeset page) is not yet
  specified — only the concepts page pattern above has a built prototype.
  Will design this when the first lesson's problems file is written.
- Multi-page concept lessons (when one topic needs more than one page) —
  pattern not yet tested at scale.
- Cover/front-matter/table-of-contents page design — out of scope until Book 1
  content is further along.

#!/usr/bin/env python3
"""Generator for Book 3 Lesson 4 rules-sheet.tex (cards laid out automatically from the card list below).
Usage: python3 gen_rules.py ; then xelatex rules-sheet.tex (twice)."""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PREAMBLE = r"""\documentclass[a4paper]{article}
\usepackage[a4paper,margin=0mm]{geometry}
\usepackage{fontspec}
\usepackage{unicode-math}
\usepackage{tikz}
\usetikzlibrary{fit,calc,positioning,arrows.meta}
\usepackage[table]{xcolor}
\usepackage[absolute]{textpos}
\usepackage{array}

\setmainfont{Libertinus Serif}
\setsansfont{Libertinus Sans}
\setmathfont{Libertinus Math}

\definecolor{accent}{HTML}{0F6A52}
\definecolor{badge}{HTML}{A9CFC2}
\definecolor{ink}{HTML}{2A2E30}

\setlength{\TPHorizModule}{1mm}
\setlength{\TPVertModule}{1mm}
\setlength{\parindent}{0pt}
\pagestyle{empty}

\newcommand{\topicheader}[2]{%
\begin{textblock*}{194mm}(16mm,10mm)
\begin{tikzpicture}
\node[fill=accent,text=white,font=\sffamily\bfseries\fontsize{13}{13}\selectfont,
      minimum width=9mm,minimum height=9mm,inner sep=0pt] at (4.5mm,-4.5mm) {#1};
\node[font=\sffamily\bfseries\fontsize{15}{16}\selectfont,text=ink,anchor=west] at (12mm,-4.5mm) {#2};
\end{tikzpicture}
\end{textblock*}
\begin{textblock*}{194mm}(16mm,22.5mm)
\begin{tikzpicture}
\fill[accent] (0,0) rectangle (194mm,0.5mm);
\end{tikzpicture}
\end{textblock*}
}

\newcommand{\pagekicker}[1]{%
\begin{textblock*}{100mm}(16mm,25.5mm)
\begin{tikzpicture}
\node[fill=ink,text=white,font=\sffamily\bfseries\fontsize{8}{8}\selectfont,
      inner sep=2.2pt,rounded corners=1pt] {\MakeUppercase{#1}};
\end{tikzpicture}
\end{textblock*}
}

\newcommand{\videobanner}[1]{%
\begin{textblock*}{178mm}(16mm,25.5mm)
\begin{tikzpicture}
\fill[accent] (0,0) rectangle (178mm,-10mm);
\draw[white,line width=0.6pt] (3mm,-1.7mm) rectangle (11.5mm,-8.3mm);
\node[white,font=\sffamily\fontsize{4}{4.4}\selectfont,align=center] at (7.25mm,-5mm) {QR\\CODE};
\node[white,font=\sffamily\bfseries\fontsize{9.5}{11}\selectfont,anchor=west] at (16mm,-5.6mm) {WATCH THE VIDEO BEFORE YOU SOLVE};
\node[white,font=\sffamily\fontsize{7.5}{8}\selectfont,anchor=east] at (174mm,-5.6mm) {YouTube ~\textbullet~ #1};
\end{tikzpicture}
\end{textblock*}
}

\newcommand{\pagefooter}[1]{%
\begin{textblock*}{194mm}(8mm,286.41mm)
  \begin{tikzpicture}
    \fill[accent] (0,0) rectangle (194mm,0.6mm);
  \end{tikzpicture}
\end{textblock*}
\begin{textblock*}{63.59mm}(8mm,288.27mm)
  {\sffamily\bfseries\color{accent}\fontsize{13}{16}\selectfont SAT 1200+}
\end{textblock*}
\begin{textblock*}{10mm}(188mm,288.27mm)
  \centering{\sffamily\color{accent}\fontsize{14}{16}\selectfont #1}
\end{textblock*}
}

\newcommand{\cardbg}[4]{%
\begin{textblock*}{#3mm}(#1mm,#2mm)
\begin{tikzpicture}
\fill[badge!22,rounded corners=3mm] (0,0) rectangle (#3mm,-#4mm);
\end{tikzpicture}
\end{textblock*}%
}

\newcommand{\pill}[3]{%
\begin{textblock*}{160mm}(#1mm,#2mm)
\begin{tikzpicture}
\node[fill=accent,text=white,anchor=north west,font=\sffamily\bfseries\fontsize{10}{10}\selectfont,
      rounded corners=8pt,inner xsep=5mm,inner ysep=1.8mm] at (0,0) {RULE ~\textperiodcentered~ #3};
\end{tikzpicture}
\end{textblock*}%
}

\newcommand{\pillw}[3]{%
\begin{textblock*}{160mm}(#1mm,#2mm)
\begin{tikzpicture}
\node[fill=accent,text=white,anchor=north west,font=\sffamily\bfseries\fontsize{10}{10}\selectfont,
      rounded corners=8pt,inner xsep=5mm,inner ysep=1.8mm] at (0,0) {#3};
\end{tikzpicture}
\end{textblock*}%
}

\arrayrulecolor{accent}
\setlength{\arrayrulewidth}{0.7pt}
\renewcommand{\arraystretch}{1.5}

"""

GAP = 6.0
# line kinds: big (15pt), mid (13pt), note (11pt italic).  frac=True -> taller line
CARDS = [
 # ------------------------------------------------------------------ page 1
 [("The discriminant",
   [("big", r"$ax^2+bx+c=0$: \ $D=b^2-4ac$ \qquad $D>0$: two \ \ $D=0$: one \ \ $D<0$: none", False),
    ("mid", r"$x^2+bx+49=0$ has exactly one solution $\Rightarrow b^2-196=0$, so $b=\pm14$", False),
    ("note", r"Move everything to one side first. Only real solutions count: ``no real solutions'' means $D<0$.", False)]),
  ("Discriminant backward: a parameter",
   [("big", r"exactly one: \ $D=0$ \qquad no real solution: \ $D<0$ \qquad two: \ $D>0$", False),
    ("mid", r"$D=0$ is often itself a quadratic in $k$, so it may give \textbf{two} values of $k$", False),
    ("mid", r"$3x^2-6x=k$: \ $D=36+12k<0\Rightarrow k<-3$ \quad ($k=-3$ gives one solution, not none)", False),
    ("note", r"Equality is the trap: ``at least one'' is $D\ge0$, ``two'' is $D>0$, ``greatest integer $k$'' needs the boundary check.", False)]),
  ("Line meets parabola or circle",
   [("big", r"set equal $\Rightarrow$ quadratic: \ $D>0$ two points \ $D=0$ tangent \ $D<0$ none", False),
    ("mid", r"$y=2x+1$ and $y=x^2-2x+5$: \ $x^2-4x+4=0$, $D=0$, so tangent (one point)", False),
    ("mid", r"horizontal line $y=k$ and a parabola: compare $k$ with the vertex $y$-value", False),
    ("note", r"Line through a given point: write $y=mx+b$ with that point, then set $D=0$ for the slope $m$.", False)]),
  ("When the parameter hides in $a$",
   [("big", r"$(k-2)x^2+6x+3=0$: \ if $k=2$ it is \textbf{not} a quadratic", False),
    ("mid", r"$kx^2+4x+k=0$: \ $D=0$ gives $k=\pm2$, and $k=0$ gives $4x=0$ (also one solution)", False),
    ("note", r"Check what happens when the leading coefficient is $0$ before you trust $D$.", False)]),
 ],
 # ------------------------------------------------------------------ page 2
 [("Quadratic hidden in a system",
   [("big", r"solve the linear equation for one letter, then substitute", False),
    ("mid", r"$x-y=2$, $xy=15$: \ $x(x-2)=15\Rightarrow x=5$ or $-3$ \quad (read the condition, e.g. $x>0$)", False),
    ("note", r"Parabola with a circle: replace $x^2$ by $y+4$ and solve for $y$ first, then count the $x$-values for each $y$.", False)]),
  ("Radical equations: always check",
   [("big", r"isolate the radical $\Rightarrow$ square both sides $\Rightarrow$ solve $\Rightarrow$ \textbf{test every answer}", False),
    ("mid", r"$\sqrt{3x+4}=x\Rightarrow x^2-3x-4=0$: \ $x=4$ works, $x=-1$ is extraneous", False),
    ("note", r"A square root is never negative, so the other side must be $\ge0$. Two radicals: isolate one, square, repeat.", False)]),
  ("Rational equations: excluded values",
   [("big", r"multiply by the LCD, solve, \textbf{discard} values that make a denominator $0$", False),
    ("mid", r"$\dfrac{3}{x-2}-\dfrac{12}{x^2-4}=1\Rightarrow x^2-3x+2=0$: \ $x=1$ only ($x=2$ excluded)", True),
    ("note", r"$\dfrac{x^2-x}{x-1}=k$ simplifies to $x=k$ for $x\ne1$, so $k=1$ has no solution.", True)]),
  ("Quadratic form: u-substitution",
   [("big", r"spot a pattern $\Rightarrow$ let $u$ = the repeated piece $\Rightarrow$ solve $\Rightarrow$ go back to $x$", False),
    ("mid", r"$x^4-5x^2-36=0$: \ $u=x^2=9$ or $-4$, and $x^2=-4$ is impossible, so $x=\pm3$", False),
    ("mid", r"$u=x^{1/3},\ \ 3^x,\ \ \sqrt x,\ \ \dfrac1x,\ \ x^2-5x$ \quad ($2^x>0$ and $\sqrt x\ge0$: reject negative $u$)", True),
    ("note", r"Check every $u$ for real $x$-values: each positive $u=x^2$ gives two, $u=0$ gives one. $9^x=(3^x)^2$.", False)]),
 ],
 # ------------------------------------------------------------------ page 3
 [("Word problems that become quadratics",
   [("big", r"area, border, consecutive, work, shared cost $\Rightarrow$ one equation", False),
    ("mid", r"border $x$ on all four sides: \ $(20+2x)(30+2x)$ \qquad work: \ $\dfrac1t+\dfrac1{t+3}=\dfrac12$", True),
    ("mid", r"$\dfrac{24}{v}-\dfrac{24}{v+2}=1\Rightarrow v^2+2v-48=0$ \quad reject the negative root", True),
    ("note", r"Height $h(t)$ above a level: solve $h=$ level to get two times, then subtract.", False)]),
  ("Completing the square",
   [("big", r"$x^2+bx\ \to\ \left(x+\dfrac b2\right)^2-\dfrac{b^2}{4}$ \qquad circle: \ $(x-h)^2+(y-k)^2=r^2$", True),
    ("mid", r"$x^2+y^2-6x+10y+18=0\Rightarrow(x-3)^2+(y+5)^2=16$: \ center $(3,-5)$, $r=4$", False),
    ("note", r"If the right side is $0$ the ``circle'' is a single point; if negative, no points. Divide by $a$ before completing.", False)]),
  ("Factoring higher degree and hidden structure",
   [("big", r"$a^2-b^2=(a-b)(a+b)$ \qquad $a^3\pm b^3=(a\pm b)(a^2\mp ab+b^2)$", False),
    ("mid", r"$x^4-13x^2+36=(x^2-4)(x^2-9)$ \qquad $x^4+x^2+1=(x^2+1)^2-x^2$", False),
    ("mid", r"grouping: $2x^3-3x^2-8x+12=(2x-3)(x^2-4)$ \qquad $\sqrt{(x-3)^2}=|x-3|$", False),
    ("note", r"A factor must give remainder $0$. $x^2+4$ never factors over the reals.", False)]),
  ("Division and rational expressions",
   [("big", r"$\dfrac{P(x)}{ax-b}$: \ quotient $+\dfrac{\text{remainder}}{ax-b}$ \qquad remainder $=P\!\left(\dfrac ba\right)$", True),
    ("mid", r"$\dfrac{6x^2+x-12}{2x-3}=3x+5+\dfrac{3}{2x-3}$ \quad (use $\tfrac32$, not $3$)", True),
    ("mid", r"cancel only \textbf{factors}: \ $\dfrac{x^3-27}{x-3}=x^2+3x+9$ \qquad match numerators for $\dfrac A{x-2}+\dfrac B{x+1}$", True)]),
  ("Exponent rules",
   [("big", r"$x^ax^b=x^{a+b}$ \quad $(x^a)^b=x^{ab}$ \quad $x^{1/n}=\sqrt[n]{x}$ \quad $4^x=2^{2x}$", False),
    ("mid", r"$\sqrt[3]{x^2}\cdot\sqrt x=x^{2/3+1/2}=x^{7/6}$ \qquad $4\cdot4^x=4^{x+1}$ \quad (same base first)", False)]),
 ],
]


# page assignment by card title (keeps the card definitions above in reading order)
_flat = {c[0]: c for page in CARDS for c in page}
_layout = [
 ["The discriminant", "Discriminant backward: a parameter", "Line meets parabola or circle", "When the parameter hides in $a$", "Completing the square"],
 ["Quadratic hidden in a system", "Radical equations: always check", "Rational equations: excluded values", "Quadratic form: u-substitution", "Word problems that become quadratics"],
 ["Factoring higher degree and hidden structure", "Division and rational expressions", "Exponent rules"],
]
CARDS = [[_flat[t] for t in page] for page in _layout]

NEWWORDS = [
 ("discriminant", "diskriminant"),
 ("real solution", "haqiqiy yechim"),
 ("tangent", "urinma"),
 ("intersection point", "kesishish nuqtasi"),
 ("extraneous solution", "chet yechim"),
 ("excluded value", "taqiqlangan qiymat"),
 ("radical equation", "ildizli tenglama"),
 ("substitution", "almashtirish"),
 ("quadratic form", "kvadrat ko'rinish"),
 ("completing the square", "to'liq kvadrat ajratish"),
 ("vertex", "parabola uchi"),
 ("leading coefficient", "bosh koeffitsiyent"),
 ("remainder", "qoldiq"),
 ("denominator", "maxraj"),
]

def line_adv(kind, frac):
    return {"big": 13.5 if frac else 9.0, "mid": 12.0 if frac else 8.0, "note": 8.0}[kind]

def last_h(kind, frac):
    return {"big": 9.0 if frac else 7.0, "mid": 9.0 if frac else 6.0, "note": 5.0}[kind]

FONT = {"big": r"\fontsize{15}{18}\selectfont", "mid": r"\fontsize{13}{16}\selectfont",
        "note": r"\itshape\color{black!70}\fontsize{11}{14}\selectfont"}

def card_tex(y, title, lines):
    out = []
    off = 12.0 if (lines[0][2] and lines[0][0] == "big") else 10.5
    ys = []
    for i, (kind, tex, frac) in enumerate(lines):
        ys.append(off)
        off += line_adv(kind, frac)
    kind, tex, frac = lines[-1]
    h = ys[-1] + last_h(kind, frac) + 6
    out.append(r"%% ---- %s (y=%.1f h=%.1f end %.1f)" % (title, y, h, y + h))
    out.append(r"\cardbg{16}{%.1f}{178}{%.1f}" % (y, h))
    out.append(r"\pill{26}{%.1f}{%s}" % (y + 3, title))
    for (kind, tex, frac), o in zip(lines, ys):
        out.append(r"\begin{textblock*}{158mm}(26mm,%.1fmm)" % (y + o))
        out.append(r"{%s %s}" % (FONT[kind], tex))
        out.append(r"\end{textblock*}")
    return "\n".join(out), h

def newwords_tex(y):
    half = (len(NEWWORDS) + 1) // 2
    cols = [NEWWORDS[:half], NEWWORDS[half:]]
    rows = half + 1
    h = 12.5 + rows * 7.0 + 4
    out = [r"%% ---- New words (y=%.1f h=%.1f)" % (y, h), r"\cardbg{16}{%.1f}{178}{%.1f}" % (y, h),
           r"\pillw{26}{%.1f}{NEW WORDS ~\textperiodcentered~ YANGI SO'ZLAR}" % (y + 3)]
    for ci, col in enumerate(cols):
        x = 26 if ci == 0 else 108
        out.append(r"\begin{textblock*}{80mm}(%dmm,%.1fmm)" % (x, y + 12.5))
        out.append(r"{\fontsize{10.5}{12}\selectfont")
        out.append(r"\begin{tabular}{@{}>{\bfseries}p{37mm}p{36mm}@{}}")
        out.append(r"\cellcolor{accent}\textcolor{white}{\sffamily English} & \cellcolor{accent}\textcolor{white}{\sffamily O'zbekcha}\\")
        for i, (en, uz) in enumerate(col):
            bg = r"\rowcolor{badge!45}" if i % 2 == 0 else r"\rowcolor{white}"
            out.append(r"%s %s & {\itshape %s}\\" % (bg, en, uz))
        out.append(r"\end{tabular}}")
        out.append(r"\end{textblock*}")
    return "\n".join(out), h

def main():
    out = [PREAMBLE, r"\begin{document}"]
    npages = len(CARDS)
    for pi, page in enumerate(CARDS):
        out.append(r"\topicheader{4}{Discriminant \& Disguised Quadratics}")
        if pi == 0:
            out.append(r"\videobanner{Lesson 4}")
            y = 40.0
        else:
            out.append(r"\pagekicker{Rules sheet -- %d/%d}" % (pi + 1, npages))
            y = 33.0
        out.append(r"\pagefooter{%d}" % (pi + 1))
        out.append(r"\mbox{}%")
        for title, lines in page:
            t, h = card_tex(y, title, lines)
            out.append(t)
            y += h + GAP
        if pi == npages - 1:
            t, h = newwords_tex(y)
            out.append(t)
            y += h
        print("page %d ends at y=%.1f" % (pi + 1, y - GAP))
        if pi < npages - 1:
            out.append(r"\clearpage")
    out.append(r"\end{document}")
    open("rules-sheet.tex", "w").write("\n".join(out) + "\n")

main()

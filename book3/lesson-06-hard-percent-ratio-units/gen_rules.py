#!/usr/bin/env python3
"""Generator for Book 3 Lesson 2 rules-sheet.tex (cards laid out automatically from the card list below).
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
 [("Forms of a line",
   [("big", r"$y=mx+b$ \qquad $Ax+By=C$: \ slope $-\dfrac AB$", True),
    ("mid", r"$y$-intercept $\dfrac CB$ \qquad $x$-intercept $\dfrac CA$ \qquad point-slope: $y-y_1=m(x-x_1)$", True),
    ("mid", r"$3x+4y=12$: \ slope $-\tfrac34$, \ $y$-intercept $3$, \ $x$-intercept $4$", False)]),
  ("Slope, parallel, perpendicular",
   [("big", r"$m=\dfrac{y_2-y_1}{x_2-x_1}$ \qquad parallel: $m_1=m_2$ \qquad perpendicular: $m_1m_2=-1$", True),
    ("mid", r"slope $-\tfrac23$ $\Rightarrow$ perpendicular slope $\tfrac32$ \ (flip the fraction, change the sign)", False),
    ("note", r"Standard form: $Ax+By=C$ and $Ax+By=D$ are parallel; $Bx-Ay=D$ is perpendicular to the first.", False)]),
  ("Number of solutions: the $a:b:c$ ratio test",
   [("big", r"$a_1x+b_1y=c_1$ and $a_2x+b_2y=c_2$: \ $\dfrac{a_1}{a_2}\ne\dfrac{b_1}{b_2}\Rightarrow$ exactly one", True),
    ("mid", r"no solution: $\dfrac{a_1}{a_2}=\dfrac{b_1}{b_2}\ne\dfrac{c_1}{c_2}$ \qquad infinitely many: all three ratios equal", True),
    ("mid", r"$kx+12y=9$ and $5x+4y=7$: \ $\dfrac k5=\dfrac{12}4\Rightarrow k=15$, \ and $9\ne3\cdot7$, so no solution", True),
    ("note", r"Slope form: same slope and different intercept = no solution; the same line = infinitely many.", False)]),
  ("A parameter in a system",
   [("big", r"ratios equal $\Rightarrow$ solve for $k$ $\Rightarrow$ \textbf{check the constants} for each $k$", False),
    ("mid", r"$\dfrac k4=\dfrac9k\Rightarrow k=\pm6$: \ one value gives infinitely many solutions, the other none", True),
    ("note", r"\textit{Which could be the second equation?} Same $x,y$-ratio as the given one, different constant.", False)]),
 ],
 # ------------------------------------------------------------------ page 2
 [("Solve for the combination, not the unknowns",
   [("big", r"find $\lambda,\mu$ with $\lambda(\text{eq}_1)+\mu(\text{eq}_2)=$ the expression asked", False),
    ("mid", r"$5a+2b=34$, $3a-4b=10$: \ $a+3b=\tfrac12(34)-\tfrac12(10)=12$", True),
    ("note", r"Add for $x+y$-type sums, subtract for $x-y$-type differences; stop as soon as the asked expression appears.", False)]),
  ("One variable: identity or contradiction",
   [("big", r"$ax+b=cx+d$: \ $a\ne c$ \ $\Rightarrow$ \ exactly one solution", False),
    ("mid", r"$a=c$ and $b=d$: infinitely many \qquad $a=c$ and $b\ne d$: no solution", False),
    ("mid", r"$3(2x-k)+x=7x+12\Rightarrow 7x-3k=7x+12$, so $k=-4$ gives infinitely many", False),
    ("note", r"Variables cancel and a true statement is left: infinitely many; a false statement: no solution.", False)]),
  ("Interpreting a linear model",
   [("big", r"$y=mx+b$: \ $m$ = change in $y$ per 1 unit of $x$ \quad $b$ = value at $x=0$", False),
    ("mid", r"$Ax+By=C$: \ $x$-intercept $\dfrac CA$ (all of one item), \ each $+1$ in $x$ changes $y$ by $-\dfrac AB$", True),
    ("mid", r"$3x+5y=600$: \ the point $(0,120)$ means 0 of the first item and 120 of the second", False)]),
  ("Linear function from two points or a table",
   [("big", r"$m=\dfrac{\Delta y}{\Delta x}$ \qquad $f(x)=f(x_1)+m(x-x_1)$", True),
    ("mid", r"equal steps in $x$ give equal changes in $y$: \ $f(a+3)-f(a)=12\Rightarrow f(a+10)-f(a)=40$", False),
    ("note", r"Shift right $h$: $f(x-h)$. Shift up $k$: $f(x)+k$. Reading a table: compute $\Delta y\div\Delta x$ first.", False)]),
  ("Means and totals",
   [("big", r"mean $=\dfrac{\text{total}}{\text{count}}$ \qquad combined mean $=\dfrac{n_1\bar x_1+n_2\bar x_2}{n_1+n_2}$", True),
    ("mid", r"missing group: \ $24(78)+36m=60(84)\Rightarrow m=88$ \quad (work with totals)", False),
    ("note", r"Two means can be averaged directly only when the groups have the same size.", False)]),
 ],
 # ------------------------------------------------------------------ page 3
 [("Two items, two totals: mixture and rate",
   [("big", r"define two unknowns $\Rightarrow$ one equation for each fact \ (count, cost, amount)", False),
    ("mid", r"mixture: \ $p_1a_1+p_2a_2=p_{\text{final}}(a_1+a_2)$ \qquad distance $=$ rate $\times$ time", False),
    ("mid", r"boat: $v-c=\dfrac{\text{up}}{\text{time}}$, \ $v+c=\dfrac{\text{down}}{\text{time}}$ \quad 36 km in 3 h up, 2 h down: $c=3$", True),
    ("note", r"$p$ = concentration as a decimal. Check the units (minutes or hours) and what the last sentence asks for.", False)]),
  ("Linear inequalities and systems",
   [("big", r"multiply or divide by a negative $\Rightarrow$ \textbf{flip the sign}", False),
    ("mid", r"$-3x<12\Rightarrow x>-4$ \qquad system: the solution is the overlap of all the inequalities", False),
    ("note", r"Strict $<$ excludes the boundary (greatest integer with $x<12$ is $11$). Test a point in every inequality.", False)]),
  ("Absolute value",
   [("big", r"$|u|=k\ (k\ge0)\Rightarrow u=k$ or $u=-k$ \qquad $|u|<k\Rightarrow -k<u<k$", False),
    ("mid", r"$|u|>k\Rightarrow u<-k$ or $u>k$ \qquad $|x-c|\le r$: center $c$, half-width $r$", False),
    ("mid", r"$|4x-6|=14$: \ $x=5$ or $x=-2$", False),
    ("note", r"If $x$ also appears outside the bars ($|x-4|=2x-5$), check each answer in the original equation.", False)]),
 ],
]

NEWWORDS = [
 ("system of equations", "tenglamalar sistemasi"),
 ("no solution", "yechimi yo'q"),
 ("infinite solutions", "cheksiz ko'p yechim"),
 ("parallel lines", "parallel chiziqlar"),
 ("perpendicular", "perpendikulyar"),
 ("slope", "qiyalik"),
 ("intercept", "o'qni kesish joyi"),
 ("coefficient", "koeffitsiyent"),
 ("constant term", "ozod had"),
 ("identity", "ayniyat"),
 ("contradiction", "ziddiyat"),
 ("inequality", "tengsizlik"),
 ("absolute value", "modul"),
 ("rate of change", "o'zgarish tezligi"),
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
        out.append(r"\topicheader{2}{Hard Linear Systems}")
        if pi == 0:
            out.append(r"\videobanner{Lesson 2}")
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

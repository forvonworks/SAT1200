#!/usr/bin/env python3
"""Generator for Book 3 Lesson 9 rules-sheet.tex (cards laid out automatically from the card list below).
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
 [("Right-triangle ratios (SOH-CAH-TOA)",
   [("big", r"$\sin A=\dfrac{\text{opp}}{\text{hyp}}$ \qquad $\cos A=\dfrac{\text{adj}}{\text{hyp}}$ \qquad $\tan A=\dfrac{\text{opp}}{\text{adj}}$", True),
    ("mid", r"legs $5,12$, hyp $13$: \ $\sin A=\dfrac5{13}$, $\cos A=\dfrac{12}{13}$, $\tan A=\dfrac5{12}$", True)]),
  ("Complementary angles",
   [("big", r"$\sin x=\cos(90^\circ-x)$ \qquad $\tan x=\dfrac1{\tan(90^\circ-x)}$", True),
    ("mid", r"$\sin P=\cos Q$ (acute) $\Rightarrow P+Q=90^\circ$ \quad solve for $x$, reject impossible roots", False)]),
  ("From a ratio to the sides: scale with $k$",
   [("big", r"$\tan\theta=\dfrac ab\Rightarrow$ legs $ak,\ bk$, hyp $=k\sqrt{a^2+b^2}$", True),
    ("mid", r"$\tan\theta=\dfrac{24}7$, hyp $50$: \ $7k,24k,25k$ with $25k=50$, $k=2$, area $=\dfrac12(14)(48)=336$", True)]),
  ("Special right triangles",
   [("big", r"$45^\circ$-$45^\circ$-$90^\circ$: $\ 1:1:\sqrt2$ \qquad $30^\circ$-$60^\circ$-$90^\circ$: $\ 1:\sqrt3:2$", False),
    ("mid", r"hyp $12$ isosceles right: leg $6\sqrt2$ \qquad $30^\circ$ with hyp $14$: legs $7$ and $7\sqrt3$", False)]),
  ("Pythagorean triples (and their multiples)",
   [("big", r"$3,4,5\quad5,12,13\quad8,15,17\quad7,24,25\quad9,40,41\quad20,21,29$", False),
    ("mid", r"$a^2+b^2=c^2$ \quad $x,\,x+7,\,x+8$ is a right triangle $\Rightarrow x=5$: \ $5,12,13$", False)]),
  ("Altitude to the hypotenuse",
   [("big", r"$h^2=p\,q$ \qquad $a^2=p\,c$ \qquad $b^2=q\,c$ \qquad $h=\dfrac{ab}{c}$ \qquad three similar triangles", True),
    ("mid", r"$p=4$, $q=9$: \ $h=6$, $c=13$, area $39$ \qquad $\angle ABD=\angle C$ (small angles repeat)", True)]),
 ],
 # ------------------------------------------------------------------ page 2
 [
  ("Similar triangles",
   [("big", r"sides $\times k$ \qquad perimeter $\times k$ \qquad area $\times k^2$ \qquad $DE\parallel BC\Rightarrow\triangle ADE\sim\triangle ABC$", True),
    ("mid", r"$AD=9$, $AB=15$, $DE=12$: \ $BC=12\cdot\dfrac{15}9=20$ \qquad areas $18$ and $98$: $k=\dfrac37$", True)]),
  ("Midsegment and centroid",
   [("big", r"midsegment $=\dfrac12$ third side, parallel to it \qquad centroid splits a median $2:1$", True),
    ("mid", r"$MN=2x+3=\dfrac12(5x-3)\Rightarrow x=9$ \qquad $AG=2\,GD$, so $AD=3\,GD$", True)]),
  ("Triangle angle facts",
   [("big", r"sum $180^\circ$ \qquad exterior $=$ far interior angles \qquad isosceles: equal base angles", False),
    ("mid", r"third side: $|a-b|<c<a+b$ \qquad $9,12,14$: $81+144>196$, so the largest angle is \textbf{acute}", False)]),
  ("Parallel lines and polygons",
   [("big", r"alternate, corresponding: equal \qquad same-side interior: sum $180^\circ$", False),
    ("mid", r"polygon interior sum $(n-2)180^\circ$ \quad regular: exterior $=\dfrac{360^\circ}{n}$, interior $=180^\circ-$exterior", True)]),
  ("Equilateral and isosceles triangles",
   [("big", r"equilateral: $h=\dfrac{\sqrt3}2\,s$ \qquad area $=\dfrac{\sqrt3}4\,s^2$ \qquad isosceles: $h=\sqrt{\text{leg}^2-\left(\tfrac{\text{base}}2\right)^2}$", True),
    ("mid", r"legs $10$, base $16$: \ $h=6$, area $=48$ \qquad height $15$ equilateral: $s=10\sqrt3$, area $75\sqrt3$", True)]),
 ],
 # ------------------------------------------------------------------ page 3
 [  ("Angle of elevation and depression",
   [("big", r"elevation $=$ depression \qquad two points, one height: $d=h(\cot a-\cot b)$", True),
    ("mid", r"$45^\circ$ and $30^\circ$, $d=40$: \ $h\,(\sqrt3-1)=40$, so $h=20(\sqrt3+1)$", False)]),
  ("Coordinate chains",
   [("big", r"distance $\sqrt{(\Delta x)^2+(\Delta y)^2}$ \qquad midpoint $\left(\tfrac{x_1+x_2}2,\tfrac{y_1+y_2}2\right)$ \qquad $m_1m_2=-1$", True),
    ("mid", r"right angle at $Q$: $\overrightarrow{QP}\cdot\overrightarrow{QR}=0$ \qquad equidistant from $A,B$: set $PA^2=PB^2$ (linear in $x$)", False)]),
  ("Area toolkit and composites",
   [("big", r"triangle $\dfrac12bh$ \quad trapezoid $\dfrac12(a+b)h$ \quad height $h=s\sin\theta$", True),
    ("mid", r"hidden height first (Pythagoras); \textbf{subtract} corner pieces from a bounding box", False)]),
  ("Chain rule for hard geometry",
   [("big", r"name the \textbf{shared} side, angle or $x$ \ $\to$ \ rule 1 \ $\to$ \ rule 2", False),
    ("mid", r"two right triangles, one shared leg: \ $c_1^2-a^2=c_2^2-b^2$ \qquad do not trust a picture", False)]),
 ],
]

NEWWORDS = [
 ("hypotenuse", "gipotenuza"),
 ("leg (of a right triangle)", "katet"),
 ("altitude (height)", "balandlik"),
 ("median", "mediana"),
 ("centroid", "og'irlik markazi"),
 ("midsegment", "o'rta chiziq"),
 ("similar triangles", "o'xshash uchburchaklar"),
 ("scale factor", "o'xshashlik koeffitsiyenti"),
 ("exterior angle", "tashqi burchak"),
 ("complementary angles", "to'ldiruvchi burchaklar"),
 ("transversal", "kesuvchi to'g'ri chiziq"),
 ("angle of elevation", "ko'tarilish burchagi"),
 ("angle of depression", "pasayish burchagi"),
 ("polygon", "ko'pburchak"),
 ("perpendicular", "perpendikulyar"),
]

def line_adv(kind, frac):
    return {"big": 12.5 if frac else 8.5, "mid": 11.0 if frac else 7.5, "note": 8.0}[kind]

def last_h(kind, frac):
    return {"big": 8.5 if frac else 7.0, "mid": 8.5 if frac else 6.0, "note": 5.0}[kind]

FONT = {"big": r"\fontsize{15}{18}\selectfont", "mid": r"\fontsize{13}{16}\selectfont",
        "note": r"\itshape\color{black!70}\fontsize{11}{14}\selectfont"}

def card_tex(y, title, lines):
    out = []
    off = 11.5 if (lines[0][2] and lines[0][0] == "big") else 11.0
    ys = []
    for i, (kind, tex, frac) in enumerate(lines):
        ys.append(off)
        off += line_adv(kind, frac)
    kind, tex, frac = lines[-1]
    h = ys[-1] + last_h(kind, frac) + 4.5
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
        out.append(r"\topicheader{9}{Hard Triangles \& Chained Geometry}")
        if pi == 0:
            out.append(r"\videobanner{Lesson 9}")
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

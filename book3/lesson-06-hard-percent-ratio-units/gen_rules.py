#!/usr/bin/env python3
"""Generator for Book 3 Lesson 6 rules-sheet.tex (cards laid out automatically from the card list below).
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
 [("Percent as a multiplier",
   [("big", r"$p\%$ of $N=\dfrac p{100}\,N$ \qquad new $=N\left(1\pm\dfrac p{100}\right)$", True),
    ("mid", r"$+15\%\Rightarrow\times1.15$ \qquad $-15\%\Rightarrow\times0.85$ \qquad $+150\%\Rightarrow\times2.5$", False)]),
  ("Percent change",
   [("big", r"$\%\text{ change}=\dfrac{\text{new}-\text{old}}{\text{old}}\times100\%$ \quad (the base is the \textbf{old} value)", True),
    ("mid", r"$40\to46$: \ $\dfrac{6}{40}=15\%$ \qquad $12\to9$: \ $-\dfrac{3}{12}=-25\%$", True)]),
  ("Percent change vs percentage points",
   [("big", r"points $=$ rate$_2-$rate$_1$ \qquad percent change $=\dfrac{\text{points}}{\text{rate}_1}$", True),
    ("mid", r"$40\%\to46\%$: \ $+6$ percentage points, which is a $+15\%$ change", False)]),
  ("Successive changes: multiply, never add",
   [("big", r"factor $=f_1\cdot f_2\cdots$ \qquad up $x\%$ then down $x\%$: $1-\left(\dfrac{x}{100}\right)^2$", True),
    ("mid", r"$+20\%$ then $-20\%$: \ $1.2\times0.8=0.96$, a net $-4\%$ (not $0$)", False)]),
  ("Reverse percent: divide by the factor",
   [("big", r"original $=\dfrac{\text{final}}{\text{factor}}$ \qquad to undo $\times f$ multiply by $\dfrac1f$", True),
    ("mid", r"final \$102 after $-15\%$: \ $102\div0.85=120$ \qquad undo $+60\%$: \ $1-\dfrac1{1.6}=37.5\%$ off", True)]),
  ("``$n\%$ more'' vs ``$n$ times as much''",
   [("big", r"$n\%$ more $=\times\left(1+\dfrac n{100}\right)$ \qquad $n$ times as much $=\times n$", True),
    ("mid", r"$150\%$ more $=2.5$ times \qquad $150\%$ of $=1.5$ times \qquad $40\%$ less $=\times0.6$", False)]),
 ],
 # ------------------------------------------------------------------ page 2
 [("Discount, markup, tax, tip",
   [("big", r"stacked changes multiply \qquad profit $\%=\dfrac{\text{price}-\text{cost}}{\text{cost}}$", True),
    ("mid", r"cost \$80, $+60\%$, then $25\%$ off: \ $80(1.6)(0.75)=96$, profit $\dfrac{16}{80}=20\%$", True)]),
  ("Simple vs compound interest",
   [("big", r"simple: $A=P(1+rt)$ \qquad compound: $A=P(1+r)^t$ \qquad $P\left(1+\dfrac rm\right)^{mt}$", True),
    ("mid", r"$12\%$ compounded monthly: \ $P(1.01)^{12t}$ \qquad $1.5\%$ a month $\Rightarrow1.015^{12}-1\approx19.6\%$ a year", False)]),
  ("Mixtures and concentration",
   [("big", r"amount $=$ concentration $\times$ volume \qquad amount in $=$ amount out", False),
    ("mid", r"$0.40(6)+0.10x=0.30(6+x)\Rightarrow x=3$ \qquad water or evaporation: \textbf{solute stays fixed}", False)]),
  ("Weighted average and composition",
   [("big", r"mean $=\dfrac{\sum n_ix_i}{\sum n_i}$ \qquad fraction of group 2: $f=\dfrac{\text{mean}-x_1}{x_2-x_1}$", True),
    ("mid", r"$20\%$ and $50\%$ mixed to $38\%$: \ $f=\dfrac{18}{30}=0.6$ \qquad table: pick the \textbf{row or column} as base", True)]),
  ("Ratios: part-to-part vs part-to-whole",
   [("big", r"$a:b\Rightarrow\dfrac a{a+b}$ of the whole \qquad write $a=ak$, $b=bk$ and solve", True),
    ("mid", r"$3:5$ of $96$: $36$ and $60$ \qquad $3k:7k$, remove $8$ red $\to3:5$: \ $\dfrac{3k}{7k-8}=\dfrac35$", True)]),
  ("Percent error and relative change",
   [("big", r"percent error $=\dfrac{|\text{measured}-\text{true}|}{\text{true}}\times100\%$ \qquad base $=$ true value", True),
    ("mid", r"radius $+5\%\Rightarrow$ area $\times1.05^2=1.1025$, so $+10.25\%$ \qquad measured $4\%$ low: true $=\dfrac m{0.96}$", True)]),
 ],
 # ------------------------------------------------------------------ page 3
 [("Rates, work, flow and average speed",
   [("big", r"distance $=$ rate $\times$ time \qquad work together: \textbf{add rates} $\dfrac1a+\dfrac1b$", True),
    ("mid", r"fills in 6 h and 12 h, drains in 9 h: \ $\dfrac16+\dfrac1{12}-\dfrac19=\dfrac5{36}$, so $7.2$ h", True),
    ("mid", r"average speed $=\dfrac{\text{total distance}}{\text{total time}}$ \qquad equal distances $a$, $b$: $\dfrac{2ab}{a+b}$ ($12,24\to16$)", True)]),
  ("Unit conversion chains",
   [("big", r"units$^2$: \textbf{square} the factor \qquad units$^3$: \textbf{cube} the factor", False),
    ("mid", r"$1\text{ m}^2=10^4\text{ cm}^2$ \quad $1\text{ m}^3=10^6\text{ cm}^3=1000\text{ L}$ \quad $72\text{ km/h}=20\text{ m/s}$", False)]),
  ("Similar figures, scale drawings, density",
   [("big", r"length $\times k$ \qquad area $\times k^2$ \qquad volume $\times k^3$ \qquad $k=\sqrt{\dfrac{A_2}{A_1}}$", True),
    ("mid", r"map $1$ cm $=3.2$ km $\Rightarrow1\text{ cm}^2=10.24\text{ km}^2$ \qquad $k=3$: area $\times9$, volume $\times27$", False),
    ("mid", r"density $=\dfrac{\text{mass}}{\text{volume}}$ \qquad same material: mass $\propto k^3$ \qquad $2.7\text{ g/cm}^3=2700\text{ kg/m}^3$", True)]),
 ],
]

NEWWORDS = [
 ("percent change", "foiz o'zgarishi"),
 ("percentage point", "foiz punkti"),
 ("multiplier", "ko'paytuvchi"),
 ("discount", "chegirma"),
 ("markup", "ustama narx"),
 ("simple interest", "oddiy foiz"),
 ("compound interest", "murakkab foiz"),
 ("ratio", "nisbat"),
 ("rate", "tezlik, me'yor"),
 ("concentration", "konsentratsiya"),
 ("mixture", "aralashma"),
 ("weighted average", "vaznli o'rtacha"),
 ("scale factor", "o'xshashlik koeffitsiyenti"),
 ("density", "zichlik"),
 ("unit conversion", "birlik almashtirish"),
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
        out.append(r"\topicheader{6}{Hard Percent, Ratio \& Units}")
        if pi == 0:
            out.append(r"\videobanner{Lesson 6}")
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

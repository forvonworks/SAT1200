#!/usr/bin/env python3
"""Generator for Book 3 Lesson 8 rules-sheet.tex (cards laid out automatically from the card list below).
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
 [("Equation of a circle",
   [("big", r"$(x-h)^2+(y-k)^2=r^2$ \qquad center $(h,k)$, radius $r$", False),
    ("mid", r"$x^2+y^2-6x+10y+18=0\ \Rightarrow\ (x-3)^2+(y+5)^2=16$", False),
    ("mid", r"center $(3,-5)$, $r=4$ \qquad $x^2+y^2+Dx+Ey+F=0$: \ $r^2=\dfrac{D^2+E^2}4-F$", True)]),
  ("Point inside, on or outside",
   [("big", r"$d^2=(x-h)^2+(y-k)^2$ \quad $<r^2$ inside \quad $=r^2$ on \quad $>r^2$ outside", False),
    ("mid", r"center $(1,-2)$, $r=5$: \ $(4,2)\to9+16=25$, so it is \textbf{on} the circle", False),
    ("mid", r"diameter endpoints: center $=$ midpoint, \ $r=\dfrac12(\text{distance between them})$", True)]),
  ("Tangent line and tangent length",
   [("big", r"tangent $\perp$ radius \qquad $m_{\text{tan}}=-\dfrac1{m_{\text{radius}}}$", True),
    ("mid", r"radius slope $\dfrac43\Rightarrow$ tangent slope $-\dfrac34$ \qquad two tangents from one point are equal", True),
    ("mid", r"tangent length from an outside point: \ $t=\sqrt{d^2-r^2}$ \quad ($13,5\to12$)", False)]),
  ("Distance from the center to a line",
   [("big", r"$d=\dfrac{|Ax_0+By_0+C|}{\sqrt{A^2+B^2}}$ \qquad tangent $\iff d=r$", True),
    ("mid", r"$x^2+y^2=k$ tangent to $3x-4y=40$: \ $d=\dfrac{40}5=8$, so $k=r^2=64$", True)]),
  ("Chords",
   [("big", r"$r^2=d^2+\left(\dfrac c2\right)^2$ \qquad sagitta $=r-d$", True),
    ("mid", r"the perpendicular from the center bisects the chord \quad $r=17$, $c=30$: $d=8$, sagitta $9$", False)]),
 ],
 # ------------------------------------------------------------------ page 2
 [("Angles in a circle",
   [("big", r"inscribed $=\tfrac12$ central \qquad angle in a semicircle $=90^\circ$", False),
    ("mid", r"central $100^\circ\Rightarrow$ inscribed $50^\circ$ (on the major arc), $130^\circ$ (on the minor arc)", False),
    ("mid", r"two chords crossing: angle $=\tfrac12(\text{arc}+\text{opposite arc})$", False)]),
  ("Arc length, sector, segment (degrees)",
   [("big", r"arc $=\dfrac{\theta}{360}\cdot2\pi r$ \qquad sector $=\dfrac{\theta}{360}\cdot\pi r^2$", True),
    ("mid", r"$r=9$, $80^\circ$: \ $\frac29$ of the circle, arc $4\pi$, sector $18\pi$", True),
    ("mid", r"segment $=$ sector $-$ triangle \qquad $60^\circ$, $r=6$: \ $6\pi-9\sqrt3$", True)]),
  ("Radians",
   [("big", r"$\pi\text{ rad}=180^\circ$ \quad $s=r\theta$ \quad $A=\tfrac12r^2\theta=\tfrac12rs$", False),
    ("mid", r"$\dfrac{5\pi}6=150^\circ$ \qquad $r=9$: \ $A=\tfrac12(81)\dfrac{5\pi}6=\dfrac{135\pi}4$", True)]),
  ("Inscribed and circumscribed circles",
   [("big", r"square, side $s$: \ in-circle $r=\dfrac s2$ \quad circum-circle $r=\dfrac{s\sqrt2}2$", True),
    ("mid", r"right triangle: $r_{\text{in}}=\dfrac{a+b-c}2$, \ $R=\dfrac c2$ \qquad equilateral: $R=\dfrac a{\sqrt3}$", True),
    ("mid", r"rectangle or square in a circle: \textbf{diagonal $=$ diameter}", False)]),
  ("Rings and composite areas",
   [("big", r"ring $=\pi(R^2-r^2)$ \qquad shaded $=$ whole $-$ parts", False),
    ("mid", r"chord $c$ of the big circle tangent to the small one: \ ring $=\pi\left(\dfrac c2\right)^2$", True),
    ("mid", r"semicircle $\tfrac12\pi r^2$ \qquad regular hexagon: $R=s$, area $6\cdot\dfrac{\sqrt3}4s^2$", True)]),
 ],
 # ------------------------------------------------------------------ page 3
 [("Volumes and surface areas",
   [("big", r"cylinder $\pi r^2h$ \quad cone $\tfrac13\pi r^2h$ \quad sphere $\tfrac43\pi r^3$ \quad prism $Bh$ \quad pyramid $\tfrac13Bh$", True),
    ("mid", r"cylinder $2\pi r^2+2\pi rh$ \quad sphere $4\pi r^2$ \quad cone side $\pi r\ell$, \ $\ell=\sqrt{r^2+h^2}$", False),
    ("mid", r"square pyramid: base $+\ \tfrac12(\text{perimeter})\ell$, \quad $\ell=\sqrt{h^2+(s/2)^2}$", True)]),
  ("Scaling, similar cuts, rolled sectors",
   [("big", r"length $\times k$ \quad area $\times k^2$ \quad volume $\times k^3$ \quad $k=\sqrt{A_2/A_1}$", False),
    ("mid", r"edge $+10\%$: area $\times1.21$, volume $\times1.331$ \quad area $\times2.25\Rightarrow k=1.5$, volume $\times3.375$", False),
    ("mid", r"cut parallel to the base: similar solid, \ $h=9$ cut at $3$: $k=\dfrac23$, area $\times\dfrac49$", True),
    ("mid", r"sector rolled into a cone: arc $=2\pi r_{\text{base}}$, \ sector radius $=\ell$ (slant height)", False)]),
  ("Filling, recasting, units",
   [("big", r"rise $=\dfrac{\text{volume added}}{\text{base area}}$ \qquad volume is conserved", True),
    ("mid", r"melt into $n$ pieces: $n=V_{\text{big}}/V_{\text{piece}}$ \quad an object displaces its own volume once covered", False),
    ("mid", r"$1\text{ m}^2=10^4\text{ cm}^2$ \quad $1\text{ m}^3=10^6\text{ cm}^3=1000\text{ L}$ \quad $1\text{ L}=1000\text{ cm}^3$", False),
    ("mid", r"convert the \textbf{lengths} first, then square or cube \quad $240$ cm $=2.4$ m", False)]),
 ],
]

NEWWORDS = [
 ("chord", "vatar"),
 ("tangent", "urinma"),
 ("arc", "yoy"),
 ("sector", "sektor"),
 ("central angle", "markaziy burchak"),
 ("inscribed angle", "ichki chizilgan burchak"),
 ("ring (annulus)", "halqa"),
 ("radian", "radian"),
 ("cylinder", "silindr"),
 ("cone", "konus"),
 ("sphere", "shar"),
 ("pyramid", "piramida"),
 ("volume", "hajm"),
 ("surface area", "sirt yuzi"),
 ("scale factor", "o'xshashlik koeffitsiyenti"),
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
        out.append(r"\topicheader{8}{Hard Circles, Area \& Volume}")
        if pi == 0:
            out.append(r"\videobanner{Lesson 8}")
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

#!/usr/bin/env python3
"""Generator for Book 3 Lesson 7 rules-sheet.tex (cards laid out automatically from the card list below).
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


% Bar graph (histogram of counts). #1 counts, #2 slot width mm, #3 mm per count,
% #4 number of bars, #5 total picture height mm, #6 mean (x position), #7 top of mean line (count units)
\newcommand{\bargraph}[7]{%
\pgfmathsetmacro{\bgW}{#4*#2}%
\pgfmathsetmacro{\bgS}{#5-5}%
\begin{tikzpicture}[x=#2mm,y=#3mm]
\useasboundingbox (0mm,-#5mm) rectangle (\bgW mm,0mm);
\begin{scope}[shift={(0mm,-\bgS mm)}]
\draw[ink!55,line width=0.5pt] (0.3,0) -- ({#4+0.7},0);
\foreach \c [count=\i] in {#1} {%
  \ifnum\c>0 \fill[accent] ({\i-0.42},0) rectangle ({\i+0.42},\c);\fi
  \node[below,font=\sffamily\fontsize{6}{6}\selectfont,text=ink!80,inner sep=1pt] at (\i,0) {\i};
}
\draw[dashed,ink!70,line width=0.45pt] (#6,-0.2) -- (#6,#7);
\node[above,font=\sffamily\fontsize{5.5}{6}\selectfont,text=ink!80,inner sep=1pt] at (#6,#7) {mean};
\end{scope}
\end{tikzpicture}}
"""

GAP = 5.5
TOP1, TOP2, BOTTOM = 40.0, 33.0, 283.0
TOTAL_PAGES_PLACEHOLDER = None

def tab(header, rows, widths, fs=10.5):
    spec = "|" + "|".join("p{%dmm}" % w for w in widths) + "|"
    t = [r"{\fontsize{%s}{13}\selectfont\renewcommand{\arraystretch}{1.25}" % fs, r"\begin{tabular}{%s}\hline" % spec,
         " & ".join(r"\cellcolor{accent}\textcolor{white}{\bfseries %s}" % h for h in header) + r"\\ \hline"]
    for r in rows:
        t.append(" & ".join(r) + r"\\ \hline")
    t.append(r"\end{tabular}}")
    return "\n".join(t)

def shapes_fig(y):
    """three true-scale bar graphs (skyrocket, double top, flat); y = top of the picture area"""
    out = []
    specs = [("0,2,4,14,4,2,0", "skyrocket"), ("7,3,1,0,1,3,7", "double top"), ("3,3,3,3,3,3,3", "flat")]
    for i, (c, name) in enumerate(specs):
        x = 26 + i * 54
        out.append(r"\begin{textblock*}{50mm}(%dmm,%.1fmm)" % (x, y))
        out.append(r"\bargraph{%s}{5.4}{1.7}{7}{34}{4}{15.5}" % c)
        out.append(r"\end{textblock*}")
        out.append(r"\begin{textblock*}{50mm}(%dmm,%.1fmm)" % (x, y + 34.5))
        out.append(r"{\sffamily\bfseries\fontsize{9}{10}\selectfont\color{ink} %s}" % name.upper())
        out.append(r"\end{textblock*}")
    return "\n".join(out)

def box_fig_rules(y):
    u = 1.75
    X = lambda v: v * u
    s = [r"\begin{textblock*}{150mm}(26mm,%.1fmm)" % y, r"\begin{tikzpicture}[font=\sffamily\fontsize{7}{8}\selectfont]"]
    mn, q1, md, q3, mx = 10, 20, 25, 40, 50
    yy = -9
    s.append(r"\useasboundingbox (-2mm,-20mm) rectangle (112mm,0mm);")
    s.append(r"\draw[ink,line width=0.6pt] (%.2fmm,%dmm) -- (%.2fmm,%dmm);" % (X(mn), yy, X(q1), yy))
    s.append(r"\draw[ink,line width=0.6pt] (%.2fmm,%dmm) -- (%.2fmm,%dmm);" % (X(q3), yy, X(mx), yy))
    for v in (mn, mx):
        s.append(r"\draw[ink,line width=0.6pt] (%.2fmm,%dmm) -- (%.2fmm,%dmm);" % (X(v), yy - 2, X(v), yy + 2))
    s.append(r"\draw[ink,fill=white,line width=0.6pt] (%.2fmm,%dmm) rectangle (%.2fmm,%dmm);" % (X(q1), yy - 3.4, X(q3), yy + 3.4))
    s.append(r"\draw[ink,line width=1pt] (%.2fmm,%dmm) -- (%.2fmm,%dmm);" % (X(md), yy - 3.4, X(md), yy + 3.4))
    for v, lab in ((mn, "min"), (q1, "Q1"), (md, "median"), (q3, "Q3"), (mx, "max")):
        s.append(r"\node[above,inner sep=0pt,text=accent] at (%.2fmm,%.1fmm) {\bfseries %s};" % (X(v), yy + 4.8, lab))
    s.append(r"\draw[ink,line width=0.5pt] (0mm,%dmm) -- (%.2fmm,%dmm);" % (yy - 6.5, X(60), yy - 6.5))
    for v in range(0, 61, 10):
        s.append(r"\draw[ink,line width=0.4pt] (%.2fmm,%.1fmm) -- (%.2fmm,%.1fmm);" % (X(v), yy - 6.5, X(v), yy - 7.9))
        s.append(r"\node[below,inner sep=1pt] at (%.2fmm,%.1fmm) {%d};" % (X(v), yy - 7.8, v))
    s.append(r"\end{tikzpicture}")
    s.append(r"\end{textblock*}")
    return "\n".join(s)

CARDS = [
 ("Mean, median, mode", [
   ("big", r"mean $=\dfrac{\text{total}}{\text{count}}$ \quad median $=$ middle value \quad mode $=$ most frequent", True, 1),
   ("mid", r"even count: median $=$ average of the two middle values", False, 1),
   ("mid", r"mean of 5 is $30$, mean of the other 4 is $28$: \ removed $=5(30)-4(28)=38$", False, 1),
   ("note", r"Work with totals, not means.", False, 1)]),
 ("Add, remove or change a value", [
   ("big", r"extreme value: mean and range move; median barely; mode not", False, 1),
   ("mid", r"$3,5,5,8$ plus $30$: \ mean $5.25\to10.2$, \ median $5\to5$, \ mode $5\to5$, \ range $5\to27$", False, 1),
   ("note", r"An even count makes the median the average of two middle values, so it can move. Compare totals before and after.", False, 1)]),
 ("Weighted mean and combined means", [
   ("big", r"mean $=\dfrac{\sum(\text{value}\times\text{frequency})}{\text{total frequency}}$ \qquad combined: $\dfrac{n_1m_1+n_2m_2}{n_1+n_2}$", True, 1),
   ("mid", r"15 students (mean 60) and 25 students (mean 80): \ $\dfrac{900+2000}{40}=72.5$", True, 1),
   ("note", r"Missing value: needed $=$ (target mean $\times$ new count) $-$ (current total). Never average two means without weights.", False, 1)]),
 ("Standard deviation: read the graph, no formula", [
   ("mid", r"SD $=$ how far values typically sit from the mean. \textbf{More spread $\Rightarrow$ bigger SD.}", False, 1),
   ("raw", ("fig_shapes", 38.0)),
   ("mid", r"skyrocket bar near the mean $\Rightarrow$ \textbf{small SD} \quad double top at the ends $\Rightarrow$ \textbf{large SD}", False, 1),
   ("note", r"All three graphs have the same mean. Judge spread by where the tall bars sit, not by the range alone.", False, 1)]),
 ("What changes when every value changes", [
   ("tab", (["Change to the data", "Mean", "SD", "Range, IQR"],
            [[r"add $c$ to every value", r"$+c$", "same", "same"],
             [r"multiply every value by $k$", r"$\times k$", r"$\times|k|$", r"$\times|k|$"],
             [r"add a far-away outlier", "pulled", "jumps up", "range jumps"],
             [r"add a value equal to the mean", "same", "smaller", "same"]], [57, 25, 26, 30]), 4 * 7.3 + 8.0)]),
 ("Range, IQR and SD", [
   ("big", r"range $=\max-\min$ \qquad IQR $=Q_3-Q_1$ (the middle half)", False, 1),
   ("mid", r"SD $=$ typical distance from the mean \qquad median and IQR resist outliers", False, 1),
   ("mid", r"two clumps far apart: the combined data have a larger SD than either clump alone", False, 1),
   ("note", r"Split into halves to find $Q_1$ and $Q_3$ (medians of the lower and upper half). Range and IQR can disagree.", False, 1)]),
 ("Box plots, histograms, dot plots", [
   ("mid", r"box plot = five numbers: each quarter of the data lies between neighbors. \textbf{No mean.}", False, 1),
   ("raw", ("fig_box", 22.0)),
   ("mid", r"histogram: height $=$ frequency; median bar $=$ where the running total hits half", False, 1),
   ("note", r"A long tail on the right: mode $<$ median $<$ mean. Symmetric: mean $=$ median.", False, 1)]),
 ("Grouped data: least and greatest possible", [
   ("big", r"least mean: every value at the \textbf{bottom} of its class; greatest: at the \textbf{top}", False, 1),
   ("mid", r"integer classes $0$--$9$ and $10$--$19$ (5 values each): least mean $5$, greatest $14$, difference $9$", False, 1),
   ("note", r"For the median, find the two middle positions first (even count), then bound each. Midpoints give an estimate, not a bound.", False, 1)]),
 ("Scatterplots and the line of best fit", [
   ("big", r"$y=mx+b$: \ slope $=$ change in $y$ per \textbf{one} unit of $x$", False, 1),
   ("mid", r"$b=$ predicted $y$ at $x=0$ \qquad residual $=$ actual $-$ predicted", False, 1),
   ("mid", r"$y=1.5x+8$, point $(12,30)$: \ residual $30-26=+4$ \quad ($+$ means above the line)", False, 1),
   ("note", r"Inside the data range: prediction. Far outside it: extrapolation, unreliable. Check the intercept at $x=0$, not the left edge.", False, 1)]),
 ("Reading a model from a graph", [
   ("big", r"slope from two far-apart points: $\dfrac{y_2-y_1}{x_2-x_1}$ \qquad point $(x_0,y_0)$: $b=y_0-mx_0$", True, 1),
   ("mid", r"exponential $y=ab^x$: equal steps in $x$ multiply $y$ by $b$ \quad $4,\,6,\,9,\,13.5\Rightarrow b=1.5$, $a=4$", False, 1),
   ("note", r"A far-away point tilts the line toward itself; removing it moves the slope and the intercept in opposite ways.", False, 1)]),
 ("Two-way tables: conditional probability", [
   ("big", r"$P(A\mid B)=\dfrac{\text{count}(A\text{ and }B)}{\text{count}(B)}$ \quad the ``given'' group is the denominator", True, 1),
   ("mid", r"40 like tea, 10 of them under 30: \ $P(\text{under }30\mid\text{tea})=\dfrac{10}{40}$ \qquad $P(\text{tea}\mid\text{under }30)\ne$ that", True, 1),
   ("note", r"Reverse conditionals: with percents, build both parts (\,$0.55\cdot0.30$ and $0.45\cdot0.60$\,) and divide by the total of the group asked about.", False, 1)]),
 ("Independence", [
   ("big", r"independent $\iff P(A\mid B)=P(A)\iff P(A\text{ and }B)=P(A)\,P(B)$", False, 1),
   ("mid", r"in a table: the rate is the same in every row, e.g. $\dfrac{12}{40}=\dfrac{60}{200}=0.3$ \ $\Rightarrow$ independent", True, 1),
   ("note", r"A parameter in the table: set the two rates equal and solve.", False, 1)]),
 ("At least one; with and without replacement", [
   ("big", r"$P(\text{at least one})=1-P(\text{none})$ \qquad independent: multiply", False, 1),
   ("mid", r"$4$ items, each defective with probability $0.05$: \ $1-0.95^4$", False, 1),
   ("mid", r"without replacement the pool shrinks: \ $5$ red, $3$ blue: $P(\text{both red})=\dfrac58\cdot\dfrac47$", True, 1),
   ("note", r"Add the disjoint cases (e.g. both red, both blue). For ``least $n$ so that\,\ldots'' try values.", False, 1)]),
 ("Expected counts and subgroup percents", [
   ("big", r"expected count $=$ proportion $\times$ population", False, 1),
   ("mid", r"36 of 200 sampled $=18\%$; town of $5000$: \ $0.18\cdot5000=900$", False, 1),
   ("note", r"Chain the proportions by multiplying. Percent of a subgroup: part $\div$ that subgroup's total, not the grand total.", False, 1)]),
 ("Margin of error and intervals", [
   ("big", r"estimate $\pm$ margin of error $=$ \textbf{plausible} values for the population", False, 1),
   ("mid", r"$62\%$ with margin of error $3$ points: \ plausible $59\%$ to $65\%$ (not exactly $62\%$)", False, 1),
   ("note", r"4 times the sample size halves the margin. Overlapping intervals: no difference shown. It is not a chance of error.", False, 1)]),
 ("Study design: what can be concluded", [
   ("tab", (["Study design", "Conclusion allowed"],
            [[r"random sample \textbf{and} random assignment", r"cause for the whole population"],
             [r"random sample, no random assignment", r"association for the population (no cause)"],
             [r"random assignment of volunteers", r"cause, for people like the volunteers"],
             [r"neither (self-selected, convenience)", r"association in the sample; biased"]], [66, 74]), 4 * 7.3 + 8.0),
   ("note", r"Generalize only to the population the sample was drawn from. A flawed sampling method cannot be fixed by a larger sample.", False, 1)]),
]

NEWWORDS = [
 ("mean", "o'rtacha qiymat"),
 ("median", "mediana"),
 ("mode", "moda"),
 ("range", "variatsiya oralig'i"),
 ("standard deviation", "standart og'ish"),
 ("outlier", "chetga chiqqan qiymat"),
 ("quartile", "kvartil"),
 ("line of best fit", "eng mos to'g'ri chiziq"),
 ("residual", "qoldiq (chetlanish)"),
 ("conditional probability", "shartli ehtimollik"),
 ("independent events", "erkli hodisalar"),
 ("sample / population", "tanlanma / bosh to'plam"),
 ("margin of error", "xatolik chegarasi"),
 ("bias", "tarafkashlik"),
]

FONT = {"big": r"\fontsize{15}{18}\selectfont", "mid": r"\fontsize{13}{16}\selectfont",
        "note": r"\itshape\color{black!70}\fontsize{11}{14}\selectfont"}
MM = 2.845275590551181
HT = {}

def measure_all():
    import subprocess, hashlib
    items = {}
    for c in CARDS:
        for ln in c[1]:
            if ln[0] in ("big", "mid", "note"):
                items[ln[1]] = (ln[0], ln[1])
            elif ln[0] == "tab":
                hdr, rows, widths = ln[1]
                items[("T", tuple(hdr))] = ("tab", tab(hdr, rows, widths))
    lines = [PREAMBLE, r"\newwrite\mw \immediate\openout\mw=meas.txt", r"\begin{document}"]
    keys = {}
    for i, (k, (kind, tex)) in enumerate(items.items()):
        keys[i] = k
        if kind == "tab":
            body = tex
        else:
            body = r"{%s %s}" % (FONT[kind], tex)
        lines.append(r"\setbox0=\vbox{\hsize=158mm\noindent %s\par}\immediate\write\mw{%d \the\dimexpr\ht0+\dp0\relax}" % (body, i))
    lines += [r"\immediate\closeout\mw", r"\end{document}"]
    open("measure.tex", "w").write("\n".join(lines))
    subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", "measure.tex"], stdout=subprocess.DEVNULL, check=True)
    for ln in open("meas.txt"):
        i, v = ln.split()
        HT[keys[int(i)]] = float(v.replace("pt", "")) / MM

def card(y, title, lines):
    out, off = [], 12.5
    GAPL = 2.2
    for ln in lines:
        kind = ln[0]
        if kind in ("big", "mid", "note"):
            h = HT[ln[1]]
            out.append((kind, ln[1], off))
            off += h + GAPL
        elif kind == "raw":
            name, h = ln[1]
            out.append(("raw", name, off))
            off += h + GAPL
        elif kind == "tab":
            hdr, rows, widths = ln[1]
            h = HT[("T", tuple(hdr))]
            out.append(("tab", tab(hdr, rows, widths), off))
            off += h + GAPL
    h = off - GAPL + 5.0
    tex = [r"%% ---- %s (y=%.1f h=%.1f end %.1f)" % (title, y, h, y + h),
           r"\cardbg{16}{%.1f}{178}{%.1f}" % (y, h), r"\pill{26}{%.1f}{%s}" % (y + 3, title)]
    for kind, t, o in out:
        if kind == "raw":
            tex.append(shapes_fig(y + o) if t == "fig_shapes" else box_fig_rules(y + o))
            continue
        tex.append(r"\begin{textblock*}{158mm}(26mm,%.1fmm)" % (y + o))
        if kind == "tab":
            tex.append(t)
        else:
            tex.append(r"{%s %s}" % (FONT[kind], t))
        tex.append(r"\end{textblock*}")
    return "\n".join(tex), h

def newwords(y):
    half = (len(NEWWORDS) + 1) // 2
    cols = [NEWWORDS[:half], NEWWORDS[half:]]
    h = 12.5 + (half + 1) * 6.5 + 4
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
    measure_all()
    pages, cur, y, top = [], [], TOP1, TOP1
    items = [("card", c) for c in CARDS] + [("nw", None)]
    for kind, c in items:
        if kind == "card":
            t, h = card(0, c[0], c[1])
        else:
            t, h = newwords(0)
        if y + h > BOTTOM:
            pages.append(cur)
            cur, y = [], TOP2
        cur.append((kind, c, y, h))
        y += h + GAP
    pages.append(cur)
    n = len(pages)
    out = [PREAMBLE, r"\begin{document}"]
    for pi, pg in enumerate(pages):
        out.append(r"\topicheader{7}{Data Analysis Edge Cases}")
        out.append(r"\videobanner{Lesson 7}" if pi == 0 else r"\pagekicker{Rules sheet -- %d/%d}" % (pi + 1, n))
        out.append(r"\pagefooter{%d}" % (pi + 1))
        out.append(r"\mbox{}%")
        for kind, c, yy, h in pg:
            t, _ = card(yy, c[0], c[1]) if kind == "card" else newwords(yy)
            out.append(t)
        print("page %d ends at y=%.1f" % (pi + 1, pg[-1][2] + pg[-1][3]))
        if pi < n - 1:
            out.append(r"\clearpage")
    out.append(r"\end{document}")
    open("rules-sheet.tex", "w").write("\n".join(out) + "\n")

main()

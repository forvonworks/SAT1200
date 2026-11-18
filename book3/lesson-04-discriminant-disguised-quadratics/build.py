#!/usr/bin/env python3
"""Generator for Book 3 Lesson 4: writes problems.md and lesson04-typeset.tex from verify.py's problem bank.
Usage: python3 build.py            (writes problems.md + lesson04-typeset.tex; measure pass uses xelatex)
Page-packing: every problem is measured in a first LaTeX pass (measure.tex), then packed into 2 columns per page.
"""
import os, re, subprocess, sys
import verify

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

NUM, TITLE = 4, "Discriminant \\& Disguised Quadratics"

PREAMBLE = r"""\documentclass[a4paper]{article}
\usepackage[a4paper,margin=0mm]{geometry}
\usepackage{fontspec}
\usepackage{unicode-math}
\usepackage{tikz}
\usepackage[table]{xcolor}
\usepackage[absolute]{textpos}
\usepackage{array}
\usepackage{multirow}

\setmainfont{Libertinus Serif}
\setsansfont{Libertinus Sans}
\setmathfont{Libertinus Math}

\definecolor{accent}{HTML}{0F6A52}
\definecolor{badge}{HTML}{A9CFC2}
\definecolor{ink}{HTML}{2A2E30}

\setlength{\TPHorizModule}{1mm}
\setlength{\TPVertModule}{1mm}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\emergencystretch=3em
\abovedisplayskip=4pt plus 2pt minus 2pt \belowdisplayskip=4pt plus 2pt minus 2pt \abovedisplayshortskip=2pt \belowdisplayshortskip=2pt
\pagestyle{empty}

\newcommand{\LCOL}{16mm}
\newcommand{\RCOL}{111mm}
\newcommand{\COLW}{83mm}

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

\newcommand{\colrule}[2]{%
\begin{textblock*}{1mm}(105mm,#1mm)
\begin{tikzpicture}
\draw[black!65,line width=0.5pt] (0,0) -- (0,#2mm);
\end{tikzpicture}
\end{textblock*}
}

\newcommand{\setkicker}[2]{%
{\sffamily\bfseries\fontsize{12}{14}\selectfont #1.}\ {\itshape\fontsize{11}{14}\selectfont\color{black!75} #2}\par\vspace{2mm}%
}

\setlength{\fboxsep}{1.4pt}
\setlength{\fboxrule}{0.5pt}
\newcommand{\pnum}[1]{\fcolorbox{ink}{white}{\sffamily\bfseries\fontsize{8}{8}\selectfont #1}~}

% ---- SAT-style multiple-choice block (2x2 grid of short choices) ----
\newcommand{\satq}[6]{%
\noindent\pnum{#1} #2\par\nobreak\vspace{2mm}%
\noindent\hspace*{7mm}\begin{tabular}[t]{@{}p{32mm}p{32mm}@{}}
(A) #3 & (B) #4 \\[2mm]
(C) #5 & (D) #6 \\
\end{tabular}\par\vspace{5.5mm}%
}

% ---- stacked choices for long ones ----
\newcommand{\satqw}[6]{%
\noindent\pnum{#1} #2\par\nobreak\vspace{2mm}%
\noindent\hspace*{7mm}(A) #3\par\vspace{1.6mm}%
\noindent\hspace*{7mm}(B) #4\par\vspace{1.6mm}%
\noindent\hspace*{7mm}(C) #5\par\vspace{1.6mm}%
\noindent\hspace*{7mm}(D) #6\par\vspace{5.5mm}%
}

% ---- student-produced response (grid-in) ----
\newcommand{\satg}[2]{%
\noindent\pnum{#1} {\sffamily\bfseries\fontsize{7}{8}\selectfont\color{accent}GRID-IN}\ #2\par\nobreak\vspace{2.5mm}%
\noindent\hspace*{7mm}{\sffamily\fontsize{8.5}{10}\selectfont Answer:}\ \rule[-1.2mm]{28mm}{0.4pt}\par\vspace{5.5mm}%
}

% ---- worked-solution entry ----
\newcommand{\solitem}[4]{%
\noindent\pnum{#1} {\bfseries #2}\ —\ #3\ {\itshape\color{accent}[#4]}\par\vspace{2.1mm}%
}

\arrayrulecolor{accent}
\setlength{\arrayrulewidth}{0.7pt}
\renewcommand{\arraystretch}{1.3}

\usepackage{multicol}
\usepackage{fancyhdr}
\usepackage{needspace}
\newcommand{\pgoff}{0}
\renewcommand{\solitem}[4]{\noindent\parbox[t]{\linewidth}{\raggedright\pnum{#1} {\bfseries #2}\ ---\ #3\ {\itshape\color{accent}[#4]}}\par\vspace{3.6mm}}
\newcommand{\solkicker}[2]{\Needspace{38mm}\vspace{1.5mm}{\sffamily\bfseries\fontsize{12.5}{15}\selectfont #1.}\ {\itshape\fontsize{11}{14}\selectfont\color{black!75} #2}\par\vspace{3mm}}
\renewcommand{\satqw}[6]{%
\noindent\pnum{#1} #2\par\nobreak\vspace{2mm}%
\noindent\hangindent=13mm\hangafter=1\hspace*{7mm}(A)~#3\par\vspace{1.6mm}%
\noindent\hangindent=13mm\hangafter=1\hspace*{7mm}(B)~#4\par\vspace{1.6mm}%
\noindent\hangindent=13mm\hangafter=1\hspace*{7mm}(C)~#5\par\vspace{1.6mm}%
\noindent\hangindent=13mm\hangafter=1\hspace*{7mm}(D)~#6\par\vspace{5.5mm}%
}
\newcommand{\solkitem}[5]{\noindent\parbox[t]{\linewidth}{\vspace{1.5mm}{\sffamily\bfseries\fontsize{12.5}{15}\selectfont #1.}\ {\itshape\fontsize{11}{14}\selectfont\color{black!75} Worked solutions}\par\vspace{3mm}\raggedright\pnum{#2} {\bfseries #3}\ ---\ #4\ {\itshape\color{accent}[#5]}}\par\vspace{3.6mm}}
\fancypagestyle{solstyle}{\fancyhf{}\renewcommand{\headrulewidth}{0pt}\renewcommand{\footrulewidth}{0pt}%
 \fancyhead[L]{\topicheader{4}{Discriminant \& Disguised Quadratics}}%
 \fancyfoot[L]{\pagefooter{\the\numexpr\value{page}+\pgoff\relax}}}
"""

KICK = {
    1: ("Bridge: the core moves, one problem each.", "Bridge"),
    2: ("The discriminant backward: tangents, intersections and parameters.", "Discriminant"),
    3: ("Equations that become quadratics: radicals, fractions, quadratic form, word problems.", "Disguised quadratics"),
    4: ("Equivalent expressions and completing the square.", "Expressions"),
    5: ("Summit: the hardest mixed problems.", "Summit"),
}
KEYTITLE = {
    1: "Bridge: the core moves",
    2: "The discriminant backward",
    3: "Equations that become quadratics",
    4: "Equivalent expressions and completing the square",
    5: "Summit: the hardest mixed problems",
}

def visible(t):
    t = re.sub(r"\\[a-zA-Z]+", "X", t)
    return re.sub(r"[\$\{\}\\]", "", t)

def short_choice(t):
    """Choice text for the answer key (None if too long)."""
    t = t.strip()
    if len(visible(t)) > 30:
        return None
    return t.rstrip(".")

def answer_label(p, tex=True):
    if p["kind"] == "gi":
        a = p["ans_tex"]
        return "Ans. " + (a.replace("-", "−") if tex else a)
    sc = short_choice(p["choices"][p["pos"]][0])
    if sc and sc.startswith("$("):
        return p["letter"] + " " + sc
    return p["letter"] + (" (%s)" % sc if sc else "")

def item_tex(p):
    n = p["n"]
    if p["kind"] == "gi":
        return r"\satg{%d}{%s}" % (n, p["stem"])
    ch = [c[0] for c in p["choices"]]
    longest = max(len(visible(c)) for c in ch)
    macro = r"\satqw" if (longest > 11 or any(("\\dfrac" in c_ and len(visible(c_)) > 8) for c_ in ch)) else r"\satq"
    return macro + "{%d}{%s}{%s}{%s}{%s}{%s}" % ((n, p["stem"]) + tuple(ch))

# ------------------------------------------------------------------ problems.md
def write_md():
    out = []
    out.append("# Book 3 — Lesson %d: %s — Problem Sets\n" % (NUM, TITLE.replace("\\&", "&")))
    out.append("All problems are original. Every answer and every worked solution below is recomputed by `verify.py` "
               "(sympy and brute-force checks), which prints OK/FAIL for each item. The digital SAT has a built-in Desmos graphing "
               "calculator, so a calculator is allowed on every problem. **Grid-in** = student-produced response: write a number "
               "(fractions and decimals are accepted; negative answers are allowed).\n")
    out.append("---\n")
    for sn in range(1, 6):
        name, title, diff = verify.SET_TITLES[sn]
        out.append("## %s — %s  (%s)\n" % (name, title, diff.replace(" and ", " / ")))
        for p in [q for q in verify.PROBLEMS if q["set"] == sn]:
            d = "Medium" if p["diff"] == "M" else "Hard"
            gi = "**Grid-in.** " if p["kind"] == "gi" else ""
            out.append("%d. *(%s)* %s%s\n" % (p["n"], d, gi, p["stem"]))
            if p["kind"] == "mc":
                for i, c in enumerate(p["choices"]):
                    out.append("   - (%s) %s" % ("ABCD"[i], c[0]))
                out.append("")
        out.append("---\n")
    out.append("## Answer Key\n")
    out.append("Each entry: answer, a short worked solution, and the trick used.\n")
    for sn in range(1, 6):
        name, title, diff = verify.SET_TITLES[sn]
        out.append("### %s — %s\n" % (name, title))
        for p in [q for q in verify.PROBLEMS if q["set"] == sn]:
            out.append("%d. **%s** — %s  *Trick: %s*\n" % (p["n"], answer_label(p, tex=False), p["sol"], p["trick"]))
    open("problems.md", "w").write("\n".join(out) + "\n")

# ------------------------------------------------------------------ measurement
def measure(items):
    """items: dict id -> tex. Returns id -> height in pt."""
    lines = [PREAMBLE, r"\newwrite\mw \immediate\openout\mw=meas.txt",
             r"\newcommand{\meas}[2]{\setbox0=\vbox{\hsize=83mm\fontsize{10}{12.5}\selectfont\noindent #2}\immediate\write\mw{#1 \the\dimexpr\ht0+\dp0\relax}}",
             r"\begin{document}"]
    for k, v in items.items():
        lines.append(r"\meas{%s}{%s}" % (k, v))
    lines.append(r"\immediate\closeout\mw")
    lines.append(r"\end{document}")
    open("measure.tex", "w").write("\n".join(lines))
    subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", "measure.tex"],
                   stdout=subprocess.DEVNULL, check=True)
    h = {}
    for ln in open("meas.txt"):
        k, v = ln.split()
        h[k] = float(v.replace("pt", ""))
    return h

MM = 2.845275590551181  # pt per mm

def build_tex():
    P = verify.PROBLEMS
    items = {}
    for p in P:
        items["S%d.%d" % (p["set"], p["n"])] = item_tex(p)
    items["K"] = r"\setkicker{Set 3}{Equations that become quadratics: radicals, fractions, quadratic form, word problems.}"
    hts = measure(items)
    H = 240 * MM
    cols = [[]]
    used = 0.0
    kh = hts["K"]
    def newcol():
        nonlocal used
        cols.append([])
        used = 0.0
    for sn in range(1, 6):
        ps = [q for q in P if q["set"] == sn]
        full, short = KICK[sn]
        name = verify.SET_TITLES[sn][0]
        first_h = hts["S%d.%d" % (sn, 1)]
        gap = 3 * MM if cols[-1] else 0
        if used + gap + kh + first_h > H:
            newcol()
            gap = 0
        if gap:
            cols[-1].append(r"\vspace{3mm}")
            used += gap
        cols[-1].append(r"\setkicker{%s}{%s}" % (name, full))
        used += kh
        for p in ps:
            h = hts["S%d.%d" % (sn, p["n"])]
            if used + h > H:
                newcol()
                cols[-1].append(r"\setkicker{%s (cont.)}{%s}" % (name, short))
                used += kh
            cols[-1].append(item_tex(p))
            used += h
    # pages
    out = [PREAMBLE, r"\begin{document}"]
    npages = 0
    for i in range(0, len(cols), 2):
        npages += 1
        out.append(r"\topicheader{%d}{%s}" % (NUM, TITLE))
        out.append(r"\pagefooter{%d}" % npages)
        out.append(r"\colrule{32}{238}")
        out.append(r"\mbox{}%")
        for j, c in enumerate(cols[i:i + 2]):
            x = r"\LCOL" if j == 0 else r"\RCOL"
            out.append(r"\begin{textblock*}{\COLW}(%s,32mm)" % x)
            out.append(r"{\fontsize{10}{12.5}\selectfont")
            out.extend(c)
            out.append("}")
            out.append(r"\end{textblock*}")
        out.append(r"\clearpage")
    # answer key page
    npages += 1
    out.append(r"\topicheader{%d}{%s}" % (NUM, TITLE))
    out.append(r"\pagefooter{%d}" % npages)
    out.append(r"\mbox{}%")
    out.append(r"\begin{textblock*}{178mm}(16mm,30mm)")
    out.append(r"{\bfseries\itshape\color{accent}\fontsize{19}{21}\selectfont\centering Answer Key\par}")
    out.append(r"\end{textblock*}")
    out.append(r"\begin{textblock*}{178mm}(16mm,41mm)")
    out.append(r"{\fontsize{9.5}{12}\selectfont\color{black!70}\centering Multiple choice: the letter. Grid-in: the number to enter. Worked solutions follow on the next pages.\par}")
    out.append(r"\end{textblock*}")
    out.append(r"\begin{textblock*}{178mm}(16mm,52mm)")
    out.append(r"{\fontsize{10}{13}\selectfont")
    out.append(r"\centering")
    out.append(r"\setlength{\tabcolsep}{2pt}\renewcommand{\arraystretch}{1.3}")
    for sn in range(1, 6):
        name = verify.SET_TITLES[sn][0]
        out.append(r"{\sffamily\bfseries\color{accent}\fontsize{11}{13}\selectfont %s \ \textmd{\itshape\small %s}}\\[1.3mm]" % (name, KEYTITLE[sn]))
        ps = [q for q in P if q["set"] == sn]
        for r0 in range(0, len(ps), 10):
            row = ps[r0:r0 + 10]
            spec = "|" + "|".join([r">{\centering\arraybackslash}p{16mm}"] * len(row)) + "|"
            out.append(r"\begin{tabular}{%s}" % spec)
            out.append(r"\hline")
            out.append(" & ".join(r"\cellcolor{badge!55}\textbf{%d}" % q["n"] for q in row) + r"\\")
            out.append(r"\hline")
            cells = []
            for q in row:
                if q["kind"] == "mc":
                    cells.append(r"\textbf{%s}" % q["letter"])
                else:
                    cells.append(q["ans_tex"].replace("-", "−"))
            out.append(" & ".join(cells) + r"\\")
            out.append(r"\hline")
            out.append(r"\end{tabular}\\[1.5mm]")
        out.append(r"\vspace{3.5mm}")
    out.append("}")
    out.append(r"\end{textblock*}")
    # solutions (auto-flowing two columns, as in the reference lesson)
    out.append(r"\clearpage")
    out.append(r"%%AUTOFLOW-SOLUTIONS")
    out.append(r"\newgeometry{top=34mm,bottom=24mm,left=16mm,right=16mm}")
    out.append(r"\pagestyle{solstyle}")
    out.append(r"\setlength{\columnsep}{14mm}\setlength{\columnseprule}{0.4pt}")
    out.append(r"{\fontsize{10}{13.6}\selectfont")
    out.append(r"\begin{multicols}{2}")
    for sn in range(1, 6):
        name = verify.SET_TITLES[sn][0]
        for q in [q for q in P if q["set"] == sn]:
            if q["n"] == 1:
                out.append(r"\solkitem{%s}{%d}{%s}{%s}{%s}" % (name, q["n"], answer_label(q), q["sol"], q["trick"]))
            else:
                out.append(r"\solitem{%d}{%s}{%s}{%s}" % (q["n"], answer_label(q), q["sol"], q["trick"]))
    out.append(r"\end{multicols}}")
    out.append(r"\end{document}")
    s = "\n".join(out) + "\n"
    s = s.replace(r"\newcommand{\pgoff}{0}", r"\newcommand{\pgoff}{0}")
    open("lesson%02d-typeset.tex" % NUM, "w").write(s)
    return npages, len(cols)

if __name__ == "__main__":
    verify.prepare()
    bad = [(p["set"], p["n"]) for p in verify.PROBLEMS if not verify.check(p)[0]]
    if bad:
        print("verify failures:", bad)
        sys.exit(1)
    write_md()
    np_, nc = build_tex()
    print("problem pages (incl. answer key):", np_, " columns:", nc)

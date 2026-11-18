#!/usr/bin/env python3
"""Generator for Book 3 Lesson 1: writes problems.md and lesson01-typeset.tex from the bank in verify.py.

  python3 build.py            # writes problems.md + lesson01-typeset.tex (measures item heights with xelatex)
Pagination is automatic: every item's height is measured by TeX, then items are poured into the two
columns of each page without splitting an item.  Run xelatex twice on lesson01-typeset.tex afterwards.
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import verify as V

V.prepare()
P = V.PROBLEMS
LESSON, TITLE = 1, "Disguised Word Problems"
SHORT = {1: "Bridge", 2: "Hidden information", 3: "Multi-step chains", 4: "Notation and models", 5: "Summit"}
KICK = {1: "Bridge: read the last sentence first.",
        2: "Translate sentence by sentence.",
        3: "Rates, work, mixtures, units.",
        4: "Notation, models, meaning.",
        5: "Summit: the hardest mixed problems."}
LONGLBL = 46          # choices longer than this (visible chars) are shown by letter only in the key


# ------------------------------------------------------------------ helpers
def vis(tex):
    t = re.sub(r"\\[a-zA-Z]+", "", tex)
    t = re.sub(r"[\$\{\}\\]", "", t)
    return t

def minus(s):
    return s.replace("-", "−") if re.fullmatch(r"-?[0-9./]+", s) else s

TIKZ_CUBIC = r"""\begin{tikzpicture}[x=8mm,y=3.5mm]
\clip (-4.6,-7.6) rectangle (3.5,7.4);
\draw[black!15,line width=0.3pt] (-4,-7) grid (3,7);
\draw[->,ink,line width=0.6pt] (-4.5,0) -- (3.4,0) node[below left,font=\sffamily\fontsize{7}{8}\selectfont]{$x$};
\draw[->,ink,line width=0.6pt] (0,-7.4) -- (0,7.2) node[left,font=\sffamily\fontsize{7}{8}\selectfont]{$y$};
\foreach \u in {-4,-3,-2,-1,1,2,3}{\draw[ink,line width=0.4pt] (\u,-0.25) -- (\u,0.25); \node[font=\sffamily\fontsize{6.5}{7}\selectfont,below] at (\u+0.0,-0.35){$\u$};}
\foreach \v in {-6,-4,-2,2,4,6}{\draw[ink,line width=0.4pt] (-0.1,\v) -- (0.1,\v); \node[font=\sffamily\fontsize{6.5}{7}\selectfont,left] at (-0.15,\v){$\v$};}
\draw[accent,line width=1.1pt,domain=-4.2:3.2,samples=90,smooth,variable=\xx] plot ({\xx},{-0.25*(\xx+3)*(\xx-1)*(\xx-1)});
\fill[ink] (-1,-2) circle (0.09); \node[font=\sffamily\fontsize{7}{8}\selectfont,anchor=north] at (-1,-2.4){$(-1,-2)$};
\fill[ink] (-3,0) circle (0.09); \fill[ink] (1,0) circle (0.09);
\end{tikzpicture}"""
FIGS = {'cubic': (TIKZ_CUBIC, "*(Figure: the graph of the cubic $y=p(x)$ on a grid; it crosses the $x$-axis at $x=-3$, touches the $x$-axis at $x=1$, and passes through $(-1,-2)$. The left end rises and the right end falls.)*")}

def md_table(tb):
    rows = tb
    out = ["| " + " | ".join(rows[0]) + " |", "|" + "---|"*len(rows[0])]
    for r_ in rows[1:]:
        out.append("| " + " | ".join(r_) + " |")
    return "\n".join("   " + l for l in out)

def tex_table(tb):
    n = len(tb[0])
    lines = [r"\begin{tabular}{|" + "c|"*n + "}", r"\hline"]
    for i, r_ in enumerate(tb):
        cells = [r"\cellcolor{badge!55}\textbf{%s}" % r_[0]] + r_[1:]
        lines.append(" & ".join(cells) + r"\\ \hline")
    lines.append(r"\end{tabular}")
    return "\n".join(lines)

def difficulty_word(d):
    return {"M": "Medium", "H": "Hard"}[d]


# ------------------------------------------------------------------ problems.md
def disp_md(stem):
    return re.sub(r"\[\[D:(.*?):D\]\]", lambda m: "\n\n   $$" + m.group(1) + "$$\n\n   ", stem, flags=re.S)

def disp_tex(stem):
    return re.sub(r"\[\[D:(.*?):D\]\]", lambda m: r"\par\vspace{1mm}\centerline{$\displaystyle " + m.group(1) + r"$}\vspace{1mm}\par ", stem, flags=re.S)

def md_stem(p):
    stem = disp_md(p['stem'])
    parts = stem.split("\n")
    head, rest = parts[0], parts[1:]
    if '[[TABLE]]' in head:
        head = head.replace('[[TABLE]]', "\n\n" + md_table(p['table']) + "\n\n   ")
    if '[[FIG]]' in head:
        head = head.replace('[[FIG]]', FIGS[p['fig']][1] + "\n\n   ")
    s = head
    for r_ in rest:
        s += "  \n   " + r_
    return s

def write_md():
    L = []
    L.append("# Book 3 — Lesson 1: Disguised Word Problems — Problem Sets\n")
    L.append("All problems are original. Every answer below is recomputed independently by `verify.py` (sympy), which prints OK/FAIL for each item, checks that exactly one choice is correct, and balances the correct letters. The digital SAT has a built-in Desmos graphing calculator, so a calculator is allowed on every problem. **Grid-in** = student-produced response: write a number (fractions and decimals are accepted; negative answers are allowed).\n")
    for sn in range(1, 6):
        ttl = V.SET_TITLES[sn]
        L.append("---\n")
        L.append("## %s — %s  (%s)\n" % (ttl[0], ttl[1], ttl[2]))
        for p in [q for q in P if q['set'] == sn]:
            tag = "*(%s)* " % difficulty_word(p['diff'])
            if p['kind'] == 'gi':
                L.append("%d. %s**Grid-in.** %s\n" % (p['n'], tag, md_stem(p)))
            else:
                L.append("%d. %s%s\n" % (p['n'], tag, md_stem(p)))
                for i, (tx, _) in enumerate(p['choices']):
                    L.append("   - (%s) %s" % ("ABCD"[i], tx))
                L.append("")
    L.append("---\n")
    L.append("## Answer Key\n")
    L.append("Each entry: the answer, a short worked solution that uses the shortcut, and the trick used.\n")
    for sn in range(1, 6):
        ttl = V.SET_TITLES[sn]
        L.append("### %s — %s\n" % (ttl[0], ttl[1]))
        for p in [q for q in P if q['set'] == sn]:
            L.append("%d. %s — %s  *Trick: %s*\n" % (p['n'], key_label_md(p), p['sol'], p['trick']))
    with open(os.path.join(HERE, "problems.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")

def key_label_md(p):
    if p['kind'] == 'gi':
        return "**%s**" % p['ans_tex']
    tx = p['choices'][p['pos']][0]
    if len(vis(tx)) > LONGLBL:
        return "**%s**" % p['letter']
    if tx.startswith("$("):
        return "**%s %s**" % (p['letter'], tx)
    return "**%s (%s)**" % (p['letter'], tx)

def key_label_tex(p):
    if p['kind'] == 'gi':
        return "Ans. " + minus(p['ans_tex'])
    tx = p['choices'][p['pos']][0]
    if len(vis(tx)) > LONGLBL:
        return p['letter']
    if tx.startswith("$("):
        return "%s %s" % (p['letter'], tx)
    return "%s (%s)" % (p['letter'], tx)


# ------------------------------------------------------------------ TeX
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
\binoppenalty=10000

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
\end{tabular}\par\vspace{4.2mm}%
}

% ---- stacked choices for long ones ----
\newcommand{\satqw}[6]{%
\noindent\pnum{#1} #2\par\nobreak\vspace{2mm}%
\noindent\hspace*{7mm}(A) #3\par\vspace{1.6mm}%
\noindent\hspace*{7mm}(B) #4\par\vspace{1.6mm}%
\noindent\hspace*{7mm}(C) #5\par\vspace{1.6mm}%
\noindent\hspace*{7mm}(D) #6\par\vspace{4.2mm}%
}

% ---- automatic choice: 2x2 grid when every choice is short, stacked otherwise ----
\newsavebox{\chA}\newsavebox{\chB}\newsavebox{\chC}\newsavebox{\chD}
\newcommand{\satqa}[6]{%
\sbox{\chA}{#3}\sbox{\chB}{#4}\sbox{\chC}{#5}\sbox{\chD}{#6}%
\ifdim\wd\chA>26mm \satqw{#1}{#2}{#3}{#4}{#5}{#6}\else
\ifdim\wd\chB>26mm \satqw{#1}{#2}{#3}{#4}{#5}{#6}\else
\ifdim\wd\chC>26mm \satqw{#1}{#2}{#3}{#4}{#5}{#6}\else
\ifdim\wd\chD>26mm \satqw{#1}{#2}{#3}{#4}{#5}{#6}\else
\satq{#1}{#2}{#3}{#4}{#5}{#6}\fi\fi\fi\fi}

% ---- student-produced response (grid-in) ----
\newcommand{\satg}[2]{%
\noindent\pnum{#1} {\sffamily\bfseries\fontsize{7}{8}\selectfont\color{accent}GRID-IN}\ #2\par\nobreak\vspace{2.5mm}%
\noindent\hspace*{7mm}{\sffamily\fontsize{8.5}{10}\selectfont Answer:}\ \rule[-1.2mm]{28mm}{0.4pt}\par\vspace{4.2mm}%
}

% ---- worked-solution entry ----
\newcommand{\solitem}[4]{%
\noindent\pnum{#1} {\bfseries #2}\ —\ #3\ {\itshape\color{accent}[#4]}\par\vspace{2.1mm}%
}

% ---- centered table / figure inside a stem ----
\newcommand{\figwrap}[1]{\par\vspace{2mm}\centerline{{\arrayrulecolor{ink}\setlength{\arrayrulewidth}{0.5pt}\renewcommand{\arraystretch}{1.3}\setlength{\tabcolsep}{5pt}#1}}\vspace{1mm}}

\arrayrulecolor{accent}
\setlength{\arrayrulewidth}{0.7pt}
\renewcommand{\arraystretch}{1.3}
"""

def tex_stem(p):
    stem = disp_tex(p['stem'])
    parts = stem.split("\n")
    head, rest = parts[0], parts[1:]
    if '[[TABLE]]' in head:
        head = head.replace('[[TABLE]]', r"\figwrap{%s}" % tex_table(p['table']))
    if '[[FIG]]' in head:
        head = head.replace('[[FIG]]', r"\figwrap{%s}" % FIGS[p['fig']][0])
    s = head
    for r_ in rest:
        s += r"\par\vspace{0.8mm}\hspace*{5mm}" + r_
    return s

def tex_problem(p):
    st = tex_stem(p)
    if p['kind'] == 'gi':
        return r"\satg{%d}{%s}" % (p['n'], st)
    ch = [c[0] for c in p['choices']]
    return r"\satqa{%d}{%s}{%s}{%s}{%s}{%s}" % ((p['n'], st) + tuple(ch))

def tex_sol(p):
    return r"\solitem{%d}{%s}{%s}{%s}" % (p['n'], key_label_tex(p), p['sol'], p['trick'].replace("--", "-"))

def kicker(sn, cont, suffix=""):
    ttl = V.SET_TITLES[sn][0]
    if suffix:
        return r"\setkicker{%s%s}{%s}" % (ttl, " (cont.)" if cont else "", suffix)
    if cont:
        return r"\setkicker{%s (cont.)}{%s}" % (ttl, SHORT[sn])
    return r"\setkicker{%s}{%s}" % (ttl, KICK[sn])

def measure(items, fontspec):
    """items: list of tex strings; returns heights in mm (TeX measured)."""
    body = [PREAMBLE, r"\begin{document}"]
    for i, it in enumerate(items):
        body.append(r"\setbox1\vbox{\begin{minipage}{83mm}{%s \strut\par}\end{minipage}}\setbox0\vbox{\begin{minipage}{83mm}{%s \strut\par %s}\end{minipage}}\typeout{@@%d|\the\dimexpr\ht0+\dp0-\ht1-\dp1\relax}" % (fontspec, fontspec, it, i))
    body.append(r"\end{document}")
    path = os.path.join(HERE, "_measure.tex")
    open(path, "w", encoding="utf-8").write("\n".join(body))
    r_ = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", "_measure.tex"], cwd=HERE,
                        capture_output=True, text=True)
    out = r_.stdout
    hs = {}
    for m in re.finditer(r"@@(\d+)\|([0-9.]+)pt", out):
        hs[int(m.group(1))] = float(m.group(2)) * 25.4 / 72.27
    if len(hs) != len(items):
        print(out[-3000:])
        raise SystemExit("measurement failed")
    for ext in (".aux", ".log", ".pdf"):
        try:
            os.remove(os.path.join(HERE, "_measure" + ext))
        except OSError:
            pass
    os.remove(path)
    return [hs[i] for i in range(len(items))]

COLTOP, COLCAP = 32.0, 238.0 + 4.5     # a little of the trailing item space may hang into the margin
GAP = 3.0

def pour(entries, kick_h):
    """entries: list of (set, text, height). Returns list of pages -> [col0, col1]; each col = list of tex strings.
    A set kicker (or continuation kicker) is added in front of the first item of a set / top of a column."""
    pages = [[[], []]]
    col = 0
    used = 0.0
    last_set = None
    def new_col():
        nonlocal col, used
        if col == 0:
            col = 1
        else:
            pages.append([[], []])
            col = 0
        used = 0.0
    for (sn, txt, hgt) in entries:
        starts_set = (sn != last_set)
        while True:
            top = (used == 0.0)
            head = ""
            hh = 0.0
            if top:
                head = kicker(sn, not starts_set) if not starts_set else kicker(sn, False)
                hh = kick_h
            elif starts_set:
                head = r"\vspace{3mm}" + kicker(sn, False)
                hh = GAP + kick_h
            if used + hh + hgt <= COLCAP:
                if head:
                    pages[-1][col].append(head)
                pages[-1][col].append(txt)
                used += hh + hgt
                break
            if top:
                raise SystemExit("item taller than a column")
            new_col()
        last_set = sn
    return pages

def pour_sol(entries, kick_h):
    pages = [[[], []]]
    col = 0
    used = 0.0
    last = None
    def new_col():
        nonlocal col, used
        if col == 0:
            col = 1
        else:
            pages.append([[], []])
            col = 0
        used = 0.0
    for (sn, txt, hgt) in entries:
        starts = (sn != last)
        while True:
            top = (used == 0.0)
            if top:
                head = r"\setkicker{%s%s}{Worked solutions}" % (V.SET_TITLES[sn][0], "" if starts else " (cont.)"); hh = kick_h
            elif starts:
                head = r"\vspace{3mm}\setkicker{%s}{Worked solutions}" % V.SET_TITLES[sn][0]; hh = GAP + kick_h
            else:
                head, hh = "", 0.0
            if used + hh + hgt <= COLCAP - 6:
                if head:
                    pages[-1][col].append(head)
                pages[-1][col].append(txt)
                used += hh + hgt
                break
            if top:
                raise SystemExit("solution taller than a column")
            new_col()
        last = sn
    return pages

def page_tex(num, cols, fs, with_rule=True):
    s = [r"\clearpage" if num > 1 else "",
         r"\topicheader{%d}{%s}" % (LESSON, TITLE), r"\pagefooter{%d}" % num]
    if with_rule:
        s.append(r"\colrule{32}{238}")
    s.append(r"\mbox{}%")
    for ci, items in enumerate(cols):
        if not items:
            continue
        s.append(r"\begin{textblock*}{\COLW}(%s,32mm)" % (r"\LCOL" if ci == 0 else r"\RCOL"))
        s.append(r"{%s" % fs)
        s.extend(items)
        s.append("}")
        s.append(r"\end{textblock*}")
    return "\n".join(s)

def key_page(num):
    s = [r"\clearpage", r"\topicheader{%d}{%s}" % (LESSON, TITLE), r"\pagefooter{%d}" % num, r"\mbox{}%",
         r"\begin{textblock*}{178mm}(16mm,30mm)",
         r"{\bfseries\itshape\color{accent}\fontsize{19}{21}\selectfont\centering Answer Key\par}",
         r"\end{textblock*}",
         r"\begin{textblock*}{178mm}(16mm,41mm)",
         r"{\fontsize{9.5}{12}\selectfont\color{black!70}\centering Multiple choice: the letter. Grid-in: the number to enter. Worked solutions follow on the next pages.\par}",
         r"\end{textblock*}",
         r"\begin{textblock*}{178mm}(16mm,52mm)",
         r"{\fontsize{10}{13}\selectfont", r"\centering", r"\setlength{\tabcolsep}{2pt}\renewcommand{\arraystretch}{1.3}"]
    for sn in range(1, 6):
        ps = [q for q in P if q['set'] == sn]
        ttl = V.SET_TITLES[sn]
        s.append(r"{\sffamily\bfseries\color{accent}\fontsize{11}{13}\selectfont %s \ \textmd{\itshape\small %s}}\\[1.3mm]" % (ttl[0], ttl[1]))
        for i in range(0, len(ps), 10):
            chunk = ps[i:i + 10]
            colspec = "|" + "|".join([r">{\centering\arraybackslash}p{16mm}"] * len(chunk)) + "|"
            s.append(r"\begin{tabular}{%s}" % colspec)
            s.append(r"\hline")
            s.append(" & ".join(r"\cellcolor{badge!55}\textbf{%d}" % q['n'] for q in chunk) + r"\\")
            s.append(r"\hline")
            cells = []
            for q in chunk:
                if q['kind'] == 'mc':
                    cells.append(r"\textbf{%s}" % q['letter'])
                else:
                    cells.append(minus(q['ans_tex']))
            s.append(" & ".join(cells) + r"\\")
            s.append(r"\hline")
            s.append(r"\end{tabular}\\[1.5mm]")
        s.append(r"\vspace{3.5mm}")
    s.append("}")
    s.append(r"\end{textblock*}")
    return "\n".join(s)

def write_tex():
    fs_prob = r"\fontsize{9.8}{11.7}\selectfont"
    fs_sol = r"\fontsize{8.6}{10.5}\selectfont"
    # --- measure problems
    ptex = [tex_problem(p) for p in P]
    hs = measure(ptex, fs_prob)
    kick_h = measure([r"\setkicker{Set 1}{Bridge}"], fs_prob)[0]
    entries = [(p['set'], t, h) for p, t, h in zip(P, ptex, hs)]
    pages = pour(entries, kick_h)
    stex = [tex_sol(p) for p in P]
    shs = measure(stex, fs_sol)
    skick = measure([r"\setkicker{Set 1}{Worked solutions}"], fs_prob)[0]
    sentries = [(p['set'], t, h) for p, t, h in zip(P, stex, shs)]
    spages = pour_sol(sentries, skick)
    out = [PREAMBLE, r"\begin{document}"]
    num = 0
    for cols in pages:
        num += 1
        out.append(page_tex(num, cols, fs_prob))
    num += 1
    out.append(key_page(num))
    for cols in spages:
        num += 1
        out.append(page_tex(num, cols, fs_sol))
    out.append(r"\end{document}")
    txt = "\n".join(out)
    # normalise worked-solution kickers: one per set, at the set's first item (respace_solutions.py re-flows them)
    txt = re.sub(r"^\\setkicker\{Set \d \(cont\.\)\}\{Worked solutions\}\n", "", txt, flags=re.M)
    txt = re.sub(r"^\\vspace\{3mm\}(\\setkicker\{Set \d\}\{Worked solutions\})$", r"\1", txt, flags=re.M)
    out = [txt]
    open(os.path.join(HERE, "lesson01-typeset.tex"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("problem pages:", len(pages), " solution pages:", len(spages), " total pages:", num)


if __name__ == "__main__":
    write_md()
    write_tex()

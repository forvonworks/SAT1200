#!/usr/bin/env python3
"""Rewrite the 'Worked solutions' pages of a Book 3 lesson typeset into comfortably spaced,
automatically flowing two-column pages (multicol + fancyhdr). Usage: respace_solutions.py lessonNN-typeset.tex
Idempotent: if the file already contains the marker %%AUTOFLOW-SOLUTIONS it does nothing."""
import re, sys
p = sys.argv[1]
t = open(p).read()
if '%%AUTOFLOW-SOLUTIONS' in t:
    sys.exit(0)
i = t.index(r'\setkicker{Set 1}{Worked solutions}')
start = t.rfind(r'\clearpage', 0, i)
end = t.rindex(r'\end{document}')
section = t[start:end]
m = re.search(r'\\topicheader\{(\d+)\}\{(.*?)\}', t)
num, title = m.group(1), m.group(2)
items = re.findall(r'^(\\setkicker\{[^\n]*\}\{Worked solutions\}|\\solitem\{.*\})\s*$', section, re.M)
body = '\n'.join(items)
body = re.sub(r'(\\setkicker\{)', r'\\solkicker{', body)
body = body.replace(r'{Worked solutions}', r'{Worked solutions}')
new = r'''\clearpage
%%AUTOFLOW-SOLUTIONS
\usepackage{multicol}
'''
# preamble additions must go before \begin{document}
pre = r'''\usepackage{multicol}
\usepackage{fancyhdr}
\usepackage{needspace}
\newcommand{\pgoff}{0}
\renewcommand{\solitem}[4]{\noindent\parbox[t]{\linewidth}{\raggedright\pnum{#1} {\bfseries #2}\ ---\ #3\ {\itshape\color{accent}[#4]}}\par\vspace{3.6mm}}
\newcommand{\solkicker}[2]{\Needspace{38mm}\vspace{1.5mm}{\sffamily\bfseries\fontsize{12.5}{15}\selectfont #1.}\ {\itshape\fontsize{11}{14}\selectfont\color{black!75} #2}\par\vspace{3mm}}
\fancypagestyle{solstyle}{\fancyhf{}\renewcommand{\headrulewidth}{0pt}\renewcommand{\footrulewidth}{0pt}%
 \fancyhead[L]{\topicheader{'''+num+r'''}{'''+title+r'''}}%
 \fancyfoot[L]{\pagefooter{\the\numexpr\value{page}+\pgoff\relax}}}
'''
t2 = t[:start] + r'''\clearpage
%%AUTOFLOW-SOLUTIONS
\newgeometry{top=34mm,bottom=24mm,left=16mm,right=16mm}
\pagestyle{solstyle}
\setlength{\columnsep}{14mm}\setlength{\columnseprule}{0.4pt}
{\fontsize{10}{13.6}\selectfont
\begin{multicols}{2}
''' + body + r'''
\end{multicols}}
''' + t[end:]
t2 = t2.replace(r'\begin{document}', pre + r'\begin{document}', 1)
open(p, 'w').write(t2)

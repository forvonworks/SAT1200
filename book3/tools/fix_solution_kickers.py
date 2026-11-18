#!/usr/bin/env python3
"""Normalise the set kickers inside the multicol worked-solutions block: remove every \\solkicker (stray '(cont.)'
ones included) and put '\\solkicker{Set k}{Worked solutions}' before each \\solitem{1}. Idempotent."""
import re, sys
p = sys.argv[1]; t = open(p).read()
a = t.index(r'\begin{multicols}{2}'); b = t.index(r'\end{multicols}', a)
body = t[a + len(r'\begin{multicols}{2}'):b]
lines = [l for l in body.split('\n') if not l.startswith(r'\solkicker{')]
out = []; k = 0
for l in lines:
    if re.match(r'\\solitem\{1\}\{', l):
        k += 1; out.append(r'\solkicker{Set %d}{Worked solutions}' % k)
    out.append(l)
t = t[:a + len(r'\begin{multicols}{2}')] + '\n'.join(out) + t[b:]
open(p, 'w').write(t)
print(p, 'sets', k)

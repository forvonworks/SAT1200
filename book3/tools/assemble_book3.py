#!/usr/bin/env python3
"""Assemble Book3-Complete.pdf: renumber footers, compile, splice notes pages, merge, verify paging.
Usage: assemble_book3.py [--partial]   (--partial allows missing lessons/mocks, for dry runs)"""
import re, glob, subprocess, os, sys, json
from concurrent.futures import ThreadPoolExecutor
B = os.environ.get('B3ROOT', '/home/user/SAT1200/book3')
os.chdir(B)
PARTIAL = '--partial' in sys.argv
TMP = os.environ.get('B3TMP', '/tmp/b3asm'); os.makedirs(TMP, exist_ok=True)

def pages(p):
    return int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', p], capture_output=True, text=True).stdout).group(1))
def ptext(p, i):
    return subprocess.run(['pdftotext', '-f', str(i), '-l', str(i), p, '-'], capture_output=True, text=True).stdout
def xe(texpath):
    d, f = os.path.split(texpath)
    for _ in range(2):
        subprocess.run(['xelatex', '-interaction=nonstopmode', f], cwd=d or '.', capture_output=True)
    log = open(texpath[:-4] + '.log', errors='ignore').read()
    ok = not re.search(r'^!', log, re.M)
    for e in ('aux', 'log', 'out'):
        try: os.remove(texpath[:-4] + '.' + e)
        except FileNotFoundError: pass
    if not ok: print('COMPILE ERROR', texpath)
    return ok
def renumber_literal(tex, start, skip_from=None):
    """Replace \pagefooter{N} literals sequentially from `start`; if skip_from, skip one number from occurrence index skip_from on."""
    cnt = [0]
    def rep(m):
        cnt[0] += 1; i = cnt[0]
        return '\\pagefooter{%d}' % (start + i - 1 + (1 if skip_from and i >= skip_from else 0))
    return re.sub(r'\\pagefooter\{\d+\}', rep, tex), cnt[0]

lessons = []
for d in sorted(glob.glob('lesson-0*-*')):
    n = d[7:9]
    need = [f'{d}/rules-sheet.pdf', f'{d}/lesson{n}-typeset.pdf', f'{d}/notes-page.pdf']
    if all(os.path.exists(x) for x in need): lessons.append((d, n))
    elif not PARTIAL: sys.exit('missing lesson files in ' + d)
if not PARTIAL and len(lessons) != 9: sys.exit('need 9 lessons, have %d' % len(lessons))
mocks = []
for i in range(1, 11):
    d = f'mocks/mock-{i:02d}'
    need = [f'{d}/mock{i:02d}-typeset.pdf', f'{d}/mock{i:02d}-answer-sheet.pdf']
    if all(os.path.exists(x) for x in need): mocks.append(i)
    elif not PARTIAL: sys.exit('missing mock %d' % i)

cur = 7
plan = []; toc = []; jobs = []; parts_after = {}
for d, n in lessons:
    rs, ts, nt = f'{d}/rules-sheet', f'{d}/lesson{n}-typeset', f'{d}/notes-page'
    title = re.search(r'\\topicheader\{\d+\}\{(.*?)\}\s*$', open(rs + '.tex').read(), re.M).group(1)
    toc.append((int(n), title, cur, d))
    # rules sheet
    t = open(rs + '.tex').read(); rp = pages(rs + '.pdf')
    t2, c = renumber_literal(t, cur); assert c == rp, (rs, c, rp)
    open(rs + '.tex', 'w').write(t2); jobs.append(rs + '.tex'); cur += rp
    # typeset
    pc = pages(ts + '.pdf')
    k = next(i for i in range(1, pc + 1) if 'Answer Key' in ptext(ts + '.pdf', i))
    t = open(ts + '.tex').read()
    t2, c = renumber_literal(t, cur, skip_from=k)
    t2 = re.sub(r'\\newcommand\{\\pgoff\}\{\d+\}', r'\\newcommand{\\pgoff}{%d}' % cur, t2)
    open(ts + '.tex', 'w').write(t2); jobs.append(ts + '.tex')
    notes_no = cur + k - 1
    nt_t = open(nt + '.tex').read()
    nt_t = re.sub(r'\\pagefooter\{\d+\}', '\\\\pagefooter{%d}' % notes_no, nt_t, count=1)
    open(nt + '.tex', 'w').write(nt_t); jobs.append(nt + '.tex')
    plan.append(dict(d=d, n=n, ts=ts, rs=rs, nt=nt, k=k, pc=pc, start=cur - rp, notes_no=notes_no))
    cur += pc + 1
mock_open = cur; cur += 1
mock_start = {}
for i in mocks:
    p = f'mocks/mock-{i:02d}/mock{i:02d}-typeset'
    pc = pages(p + '.pdf'); t = open(p + '.tex').read()
    t2, c = renumber_literal(t, cur); assert c == pc, (p, c, pc)
    open(p + '.tex', 'w').write(t2); jobs.append(p + '.tex'); mock_start[i] = cur; cur += pc
ans_open = cur; cur += 1
ans_start = {}
for i in mocks:
    p = f'mocks/mock-{i:02d}/mock{i:02d}-answer-sheet'
    t = open(p + '.tex').read()
    t2, c = renumber_literal(t, cur); assert c == 1, (p, c)
    open(p + '.tex', 'w').write(t2); jobs.append(p + '.tex'); ans_start[i] = cur; cur += 1
# static pages
for name, page in (('mocks-opener', mock_open), ('answers-opener', ans_open)):
    src = open(f'{name}.tex').read().replace('@@PAGE@@', str(page))
    open(f'{TMP}/{name}.tex', 'w').write(src)
    for ex in glob.glob('*.sty'): pass
# toc
t = open('../book2/toc.tex').read().replace('602785', '0F6A52').replace('B8A0C8', 'A9CFC2')
a = t.index(r'\tocrow{1}'); b = t.index(r'\end{textblock*}', a)
rows = ''.join('\\tocrow{%d}{%s}{%d}\n' % (n, ti, p) for n, ti, p, _ in toc)
rows += '\n\\vspace{3mm}\n\\tocrowB{Mock Tests 1--10}{%d}\n\\tocrowB{Answer Sheets (Mock 1--10)}{%d}\n' % (mock_open, ans_open)
open('toc.tex', 'w').write(t[:a] + rows + t[b:])
# compile all
with ThreadPoolExecutor(4) as ex:
    res = list(ex.map(xe, [os.path.join(B, j) for j in jobs]))
xe(f'{TMP}/mocks-opener.tex'); xe(f'{TMP}/answers-opener.tex')
for f in ('toc', 'front-matter', 'back-cover', 'dedication-page'): xe(f'{B}/{f}.tex')
# splice
parts = [f'{B}/cover.pdf', '/tmp/blank2.pdf', f'{B}/front-matter.pdf', f'{B}/toc.pdf']
if not os.path.exists('/tmp/blank2.pdf'):
    subprocess.run(['pdfseparate', '-f', '1', '-l', '1', f'{B}/../book2/frontmatter.pdf', '/tmp/blank2.pdf'], check=True)
def gs_range(src, a, b, out):
    """Extract pages a..b with poppler (pdfseparate+pdfunite): keeps the original embedded fonts (Ghostscript re-embedding broke glyphs in some phone viewers)."""
    import tempfile, glob as _g
    d = tempfile.mkdtemp(dir=TMP)
    subprocess.run(['pdfseparate', '-f', str(a), '-l', str(b), src, os.path.join(d, 'p%04d.pdf')], check=True)
    files = sorted(_g.glob(os.path.join(d, 'p*.pdf')))
    if len(files) == 1:
        import shutil; shutil.copy(files[0], out)
    else:
        subprocess.run(['pdfunite'] + files + [out], check=True)
for p in plan:
    n, k, pc = p['n'], p['k'], p['pc']
    a_, b_ = f'{TMP}/ts{n}a.pdf', f'{TMP}/ts{n}b.pdf'
    gs_range(p['ts'] + '.pdf', 1, k - 1, a_); gs_range(p['ts'] + '.pdf', k, pc, b_)
    parts += [p['rs'] + '.pdf', a_, p['nt'] + '.pdf', b_]
parts.append(f'{TMP}/mocks-opener.pdf')
for i in mocks: parts.append(f'mocks/mock-{i:02d}/mock{i:02d}-typeset.pdf')
parts.append(f'{TMP}/answers-opener.pdf')
for i in mocks: parts.append(f'mocks/mock-{i:02d}/mock{i:02d}-answer-sheet.pdf')
parts += [f'{B}/dedication-page.pdf', f'{B}/back-cover.pdf']
out = f'{B}/Book3-Complete.pdf'
subprocess.run(['pdfunite'] + parts + [out], check=True)
tot = pages(out); print('total pages', tot, 'expected', cur + 1)
bad = []
for pgn in range(7, cur):
    t = ptext(out, pgn)
    nums = [l.strip() for l in t.split('\n') if re.fullmatch(r'\d{1,3}', l.strip())]
    if str(pgn) not in nums[-3:]: bad.append((pgn, nums[-3:]))
print('footer mismatches:', len(bad), bad[:10])
json.dump(dict(toc=toc, mock_open=mock_open, ans_open=ans_open, total=tot), open(f'{TMP}/plan.json', 'w'))

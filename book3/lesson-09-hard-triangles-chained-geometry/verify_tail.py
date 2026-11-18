# ================================================================== verification
LETTERS = "ABCD"

def _num(v):
    try:
        return float(sympify(v)) if not isinstance(v, (tuple, str)) and not callable(v) else None
    except Exception:
        return None

def arrange_all():
    """Choose the print order of every MC problem and balance the correct letter globally.
    Numeric choices are normally printed in ascending or descending order; when a letter is already
    used more than its share, the right answer is instead placed first/last with the wrong choices sorted."""
    glob = [0, 0, 0, 0]
    perset = {}
    total_mc = sum(1 for p_ in PROBLEMS if p_['kind'] == 'mc')
    cap = -(-total_mc // 4)
    for p_ in PROBLEMS:
        if p_['kind'] != 'mc':
            continue
        ps = perset.setdefault(p_['set'], [0, 0, 0, 0])
        items = [p_['right']] + list(p_['wrongs'])
        numeric = all(_num(it[1]) is not None for it in items)
        order = p_['order']
        if isinstance(order, int):
            pos = order
            wr = list(p_['wrongs'])
            out = wr[:pos] + [p_['right']] + wr[pos:]
        elif order in ('a', 'd') or (order == 'auto' and numeric):
            asc = sorted(items, key=lambda it: float(sympify(it[1])))
            wsort = sorted(p_['wrongs'], key=lambda it: float(sympify(it[1])))
            pa = [i for i, it in enumerate(asc) if it is p_['right']][0]
            if order == 'a':
                pos, out = pa, asc
            elif order == 'd':
                pos, out = 3 - pa, asc[::-1]
            else:
                cands = []
                for out_, pos_, unsorted in ((asc, pa, 0), (asc[::-1], 3 - pa, 0),
                                              ([p_['right']] + wsort, 0, 1), (wsort + [p_['right']], 3, 1),
                                              ([p_['right']] + wsort[::-1], 0, 1), (wsort[::-1] + [p_['right']], 3, 1)):
                    over = 20 if glob[pos_] >= cap else 0
                    cands.append((over + unsorted * 2 + glob[pos_] * 0.5 + ps[pos_] * 0.3, pos_, out_))
                _, pos, out = min(cands, key=lambda c: c[0])
        else:  # free: wrongs keep listed order, right goes to the least used letter
            wr = list(p_['wrongs'])
            pos = min(range(4), key=lambda i: (glob[i], ps[i], i))
            out = wr[:pos] + [p_['right']] + wr[pos:]
        p_['choices'], p_['pos'] = out, pos
        p_['letter'] = LETTERS[pos]
        p_['answer'] = p_['letter']
        glob[pos] += 1
        ps[pos] += 1

def prepare():
    for i, p_ in enumerate(PROBLEMS):
        p_['n'] = sum(1 for q_ in PROBLEMS[:i] if q_['set'] == p_['set']) + 1
        if p_['kind'] == 'gi':
            p_['answer'] = p_['ans_tex']
    arrange_all()

def check(p_):
    if p_['kind'] == 'gi':
        got = p_['calc']()
        return (got is not None and same(got, p_['ans_val'])), got
    vals = [c_[1] for c_ in p_['choices']]
    distinct = all(not same(vals[i], vals[j]) for i in range(4) for j in range(i + 1, 4))
    if len(p_['choices']) != 4:
        return False, 'not 4 choices'
    if p_.get('each') is not None:
        truth = [bool(p_['each'](v)) for v in vals]
        ok = sum(truth) == 1 and truth[p_['pos']] and distinct
        return ok, p_['choices'][truth.index(True)][0] if any(truth) else 'none'
    got = p_['calc']()
    if isinstance(got, list):
        got = got[0] if len(got) == 1 else tuple(got)
    n_correct = sum(1 for v in vals if same(got, v))
    ok = same(got, p_['right'][1]) and n_correct == 1 and distinct and p_['choices'][p_['pos']][1] is p_['right'][1]
    return ok, got

def main():
    from collections import Counter
    prepare()
    fails = 0
    for p_ in PROBLEMS:
        ok, got = check(p_)
        tag = "S%d.%-2d" % (p_['set'], p_['n'])
        shown = p_['answer'] if p_['kind'] == 'gi' else "%s = %s" % (p_['letter'], p_['right'][0])
        print("%s %-4s %s   (recomputed: %s)" % (tag, "OK" if ok else "FAIL", shown, got))
        if not ok:
            fails += 1
    print()
    print("problems:", len(PROBLEMS), " FAIL:", fails)
    for sn in range(1, 6):
        ps = [p_ for p_ in PROBLEMS if p_['set'] == sn]
        mcs = [p_ for p_ in ps if p_['kind'] == 'mc']
        print("Set %d: %d problems (%d MC, %d grid-in); correct-letter counts %s; difficulty %s" %
              (sn, len(ps), len(mcs), len(ps) - len(mcs),
               dict(sorted(Counter(p_['letter'] for p_ in mcs).items())),
               dict(Counter(p_['diff'] for p_ in ps))))
    allmc = [p_ for p_ in PROBLEMS if p_['kind'] == 'mc']
    print("All MC letter counts:", dict(sorted(Counter(p_['letter'] for p_ in allmc).items())))
    gcount = len(PROBLEMS) - len(allmc)
    print("grid-ins: %d of %d (%.0f%%)" % (gcount, len(PROBLEMS), 100.0*gcount/len(PROBLEMS)))
    print("ALL OK" if not fails else "SOME FAILED")
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())

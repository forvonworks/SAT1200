#!/usr/bin/env python3
"""List page numbers in Materials/SAT MATH.pdf matching a skill + difficulty.

Usage: python3 tools/qbank_find.py "Circles" Hard [--limit 4]
Then render a page:  pdftoppm -png -r 150 -f N -l N "Materials/SAT MATH.pdf" /tmp/q
"""
import argparse, os, random, re, subprocess, sys

PDF = os.path.join(os.path.dirname(__file__), "..", "Materials", "SAT MATH.pdf")
CACHE = "/tmp/satmath_pages.txt"

def pages():
    if not os.path.exists(CACHE):
        subprocess.run(["pdftotext", "-layout", PDF, CACHE], check=True)
    with open(CACHE, encoding="utf-8", errors="ignore") as f:
        return f.read().split("\f")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("skill", help="substring of the official skill name, case-insensitive")
    ap.add_argument("difficulty", choices=["Easy", "Medium", "Hard"])
    ap.add_argument("--limit", type=int, default=4)
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    skill = re.sub(r"\s+", " ", a.skill.lower())
    hits = []
    for i, txt in enumerate(pages(), start=1):
        head = re.sub(r"\s+", " ", txt[:900].lower())
        if "question id" in head and skill in head and a.difficulty.lower() in head:
            hits.append(i)
    random.Random(a.seed).shuffle(hits)
    print(f"{len(hits)} matching pages; sample: {sorted(hits[:a.limit])}")

if __name__ == "__main__":
    sys.exit(main())

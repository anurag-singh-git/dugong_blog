#!/usr/bin/env python3
"""Recompute the dispatch count and the date range printed on every hub and
author page from the dispatches those pages actually link, and rewrite them.
The daily run updates the card lists and the counts but has repeatedly left
the 'FIRST -> LAST' range line behind."""
import re, glob, html, sys, calendar
DRY = "--dry" in sys.argv

disp = {}
for f in sorted(glob.glob("*.html")):
    s = open(f, encoding="utf-8").read()
    if 'http-equiv="refresh"' in s: continue
    m = re.search(r'article:published_time" content="([0-9-]+)"', s)
    if m: disp[f] = m.group(1)

MON = {i: calendar.month_abbr[i].upper() for i in range(1, 13)}
def fmt(d, with_year):
    y, m, dd = d.split("-")
    return f"{MON[int(m)]} {dd}" + (f" {y}" if with_year else "")

hubs = sorted(glob.glob("shopify-*.html")) + ["priya-singh.html"]
for f in hubs:
    s = open(f, encoding="utf-8").read()
    orig = s
    linked = sorted(set(re.findall(r'href="([a-z0-9-]+\.html)"', s)) & set(disp))
    if not linked: continue
    dates = sorted(disp[x] for x in linked)
    n = len(linked)

    # count: "<N> DISPATCHES" in the visible meta line and section heading
    counts = set(re.findall(r'(\d+) DISPATCHES', s))
    for c in counts:
        if int(c) != n:
            s = s.replace(f"{c} DISPATCHES", f"{n} DISPATCHES")
            s = s.replace(f"across {c} Dugong field dispatches", f"across {n} Dugong field dispatches")

    # range: "MON DD[ YYYY] &rarr; MON DD[ YYYY]"
    rng = re.compile(r'([A-Z]{3} \d{2})( 20\d{2})? &rarr; ([A-Z]{3} \d{2})( 20\d{2})?')
    def repl(m):
        first_year = bool(m.group(2)); last_year = bool(m.group(4))
        return fmt(dates[0], first_year) + " &rarr; " + fmt(dates[-1], last_year)
    s = rng.sub(repl, s)

    if s != orig:
        print(f"{f}: n={n} range={dates[0]}..{dates[-1]}")
        for a, b in zip(re.findall(r'[A-Z]{3} \d{2}(?: 20\d{2})? &rarr; [A-Z]{3} \d{2}(?: 20\d{2})?', orig),
                        re.findall(r'[A-Z]{3} \d{2}(?: 20\d{2})? &rarr; [A-Z]{3} \d{2}(?: 20\d{2})?', s)):
            if a != b: print(f"    range  {a}  ->  {b}")
        oc = sorted(set(re.findall(r'\d+ DISPATCHES', orig))); nc = sorted(set(re.findall(r'\d+ DISPATCHES', s)))
        if oc != nc: print(f"    count  {oc}  ->  {nc}")
        if not DRY: open(f, "w", encoding="utf-8").write(s)

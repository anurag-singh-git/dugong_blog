#!/usr/bin/env python3
"""Two repairs the 2026-10-18 publishing run left behind.

1. The new dispatch shipped a 198-character meta description; the house
   invariant is 70-165 and og:/twitter: must carry the same string.
2. Four pages gained the new dispatch in their card lists, so the run moved
   their sitemap lastmod to 2026-10-18 and left dateModified where it was.
   The page's own dateModified is the first one in its @graph.
"""
import re, sys
DRY = "--dry" in sys.argv

OLD_DESC = ("You cancelled the order and refunded the customer, and the label you bought that "
            "morning is still paid for. The AI playbook that finds every unused Shopify label "
            "before the 30 day void window shuts.")
NEW_DESC = ("You cancelled the order and refunded the customer, and the label is still paid for. "
            "The AI playbook that voids every unused Shopify label before day 30.")
assert 70 <= len(NEW_DESC) <= 165, len(NEW_DESC)

f = "how-to-catch-shopify-shipping-labels-you-never-used.html"
s = open(f, encoding="utf-8").read()
n = s.count(OLD_DESC)
if n:
    s2 = s.replace(OLD_DESC, NEW_DESC)
    print(f"{f}: description {len(OLD_DESC)} -> {len(NEW_DESC)} chars, {n} occurrence(s)")
    if not DRY: open(f, "w", encoding="utf-8").write(s2)

for f, want in [("index.html", "2026-10-18"), ("priya-singh.html", "2026-10-18"),
                ("shopify-automation-questions.html", "2026-10-18"),
                ("shopify-shipping-and-fulfillment-automation.html", "2026-10-18")]:
    s = open(f, encoding="utf-8").read()
    m = re.search(r'"dateModified":\s*"([0-9-]+)"', s)
    if not m or m.group(1)[:10] == want: continue
    s2 = s[:m.start()] + f'"dateModified": "{want}"' + s[m.end():]
    print(f"{f}: dateModified {m.group(1)} -> {want}")
    if not DRY: open(f, "w", encoding="utf-8").write(s2)

# SEO / GEO report - 2026-10-19 (second pass)

Scheduled autonomous run. This run's trigger fired at **2026-10-15 16:14 UTC** and its session was
suspended before it could write anything; it resumed and executed at **2026-10-19 17:43 UTC**, twenty
minutes after the regular 10-19 pass finished at 17:23. So this is a second pass over the same day's
tree, not a missed Oct 15 pass.

The first thing it did was read `SEO-GEO-report-2026-10-19.md` rather than start auditing, because
duplicating a pass that had just run would have been the main risk here. Everything that report
claims was verified and holds: `_tools/seo-check.py` reports **PASS** on the tree as found (99
rendered pages, 82 stubs, 86 dispatches, 98 sitemap URLs, 86 feed items), and the 10-19 work is not
merely local - `HEAD` is `bce95c5`, identical to `origin/main`, so the author page, the grounded hub
entities, the llms.txt repairs and the visible dek links are all being served. **Carried item 1 of
the 10-19 report, commit and push, is closed.** Nothing in the 10-19 report needed redoing.

That left the carried items. This pass took the two nobody had been able to close, because both were
blocked on a file-deletion permission that no previous unattended run could obtain, and this run
obtained it.

## Part 1 - 108 MB of working snapshots were tracked in a repo that serves its own root

Carried item 2 from 10-17, 10-18 and 10-19, and the back half of carried item 11.

`.gitignore` was added on 10-19 and stopped new snapshots entering the index, but gitignoring a path
does not untrack what is already committed. Measured on the tree as found:

| Tracked path | Files | Bytes |
|---|---|---|
| `_qa_tmp/` | 50 | 94,263,426 |
| `_to_delete/` | 14 | 14,332,062 |
| `__deltest.tmp` | 1 | 0 |
| **total** | **65** | **~108 MB** |

Why this is an SEO problem and not just repo hygiene: the site is GitHub Pages with `.nojekyll`, which
is precisely the switch that makes underscore-prefixed directories publicly fetchable. The repo's own
`robots.txt` comment says so in as many words, and adds that the rule only asks crawlers not to fetch
those paths and does not make them private. `_qa_tmp/` holds whole-site tarballs: `before` and `after`
snapshots of **every page on the site**, roughly fifty times over. Any crawler that does not honour
robots.txt - which is most of the AI crawlers the site is explicitly courting, and robots.txt names
about 35 of them - can fetch a complete, stale, duplicate copy of the entire site from a URL the
sitemap never mentions.

`__deltest.tmp` deserves a note: it is a two-byte probe file that **this run's own 10-15 session
created** while testing whether deletion was permitted, and the owner's commit that day swept it into
the repo. It had its own `Disallow` line in robots.txt. Cleaning it up was this run cleaning up after
itself.

All 65 paths are now **untracked and left on disk**:

```
git rm -r --cached _qa_tmp __deltest.tmp _to_delete
```

673 tracked files to 608. Nothing was deleted from the working tree - `_qa_tmp/` still holds its 43
entries and `_to_delete/` its 9, so no snapshot or history is lost locally. `__deltest.tmp` is gone
from disk as well as the index, because it was never anything but this routine's litter.

Disk deletion was deliberately **not** done for the rest, despite the permission now existing. GitHub
Pages serves the repository, not the disk, so once the untracking is pushed those files stop being
reachable whether or not they exist locally. Deleting them would buy no additional SEO benefit and
would be irreversible, so the conservative half of the fix is the whole fix.

Two checks on the staged state, because the owner commits with `git add -A` and a re-add would have
silently undone this:

| Verified | Result |
|---|---|
| `git add -A --dry-run` re-adds any of the 65 | **no** - `.gitignore` lines 4 and 8 hold |
| `git check-ignore -v` on a tarball and a lock file | both attributed to `.gitignore`, as intended |
| staged changes touching site content | **none** - `git diff --cached` is exactly 65 deletions |
| `index.html`, `sitemap.xml`, `robots.txt`, `llms.txt`, `llms-full.txt`, `feed.xml`, `.nojekyll`, `CNAME` | all unchanged |
| `_tools/seo-check.py` after the change | **PASS**, same 99 / 82 / 86 / 98 / 86 counts |

The history still carries the 108 MB after this lands. That is the separate and larger decision the
10-19 report flagged, and it is still open; see Part 3.

## Part 2 - 98 orphaned git objects, the residue of the blocked-delete era

Not previously reported, found while measuring Part 1. `git count-objects -vH` emitted 98 warnings:

```
warning: garbage found: .git/objects/01/tmp_obj_yhXwYE
... 97 more
size-garbage: 2,870,512 bytes
```

These are half-written object files left behind when a git operation was interrupted, which is exactly
what happened repeatedly on this machine while deletion was forbidden: git replaces tracked files by
deleting them and removes its own lock files, so every blocked commit left debris. The dates confirm
the story - 4 from June, 2 from 19 June, 3 from 10 July, **78 from 20 September** and 5 from 27
September, the period the `_to_delete/git-index.lock-stale-*` files also come from. None newer than
three weeks.

Removed, after confirming no git process was running. `git fsck` exits clean, `size-garbage` is now 0
bytes, and `HEAD` still matches `origin/main`. The dangling blobs fsck reports are normal unreferenced
objects, not damage. This has no ranking effect; it removes a standing hazard that made every future
`git gc` and `count-objects` on this repo noisy and ambiguous.

The `.git/index` was backed up before any of this, to `/tmp/git-index-backup-<epoch>` on the desktop
VM.

## Part 3 - Not changed, needs a decision

Items 3 through 13 of the 10-19 report are all carried unchanged; this pass closed only its items 1
(already done by the owner), 2 and 11. Repeating only what moved or is new:

1. **The 65 untracked paths are staged but not committed.** The tree now holds exactly 65 staged
   deletions and no other change. This pass did not commit, for the same reason every pass since
   10-12 has not: the commit history here is hand-written and the owner has been committing daily.
   Verified safe either way - `git commit` alone lands them because they are already staged, and
   `git add -A && git commit` does not re-add them. Nothing is live until it happens, and until then
   the tarballs remain fetchable.
2. **235 operational markdown files are tracked and served from the site root.** New this pass, and
   arguably a larger exposure than the tarballs: 84 `SEO-GEO-report-*.md`, 69 `blog-run-*.md` and 82
   `QA-report-*.md`, about 1.5 MB. They carry no underscore prefix, so GitHub Pages serves them
   unconditionally. They are correctly absent from `sitemap.xml`, `llms.txt`, `llms-full.txt` and
   `feed.xml` - 0 references in all four - and robots.txt disallows all three prefixes, so compliant
   crawlers will not fetch them. Non-compliant ones will, and these files are this site's complete
   internal record: every defect found, every editorial judgement, every count the reports argue
   should or should not be trusted. **Not touched**, because unlike the tarballs these are records the
   owner may well want versioned, and relocating 235 files is a structural change with an editorial
   decision inside it. The options are to move them under an underscore-prefixed directory, where
   `.nojekyll` still serves them but at least the existing `_`-rules cover them, or out of the
   published tree entirely.
3. **robots.txt still carries `Disallow` lines for `_qa_tmp/`, `_to_delete/` and `__deltest.tmp`.**
   Left in place on purpose: they are still load-bearing until the Part 1 untracking is pushed. Once
   it is, they describe paths that no longer exist, which is harmless but worth tidying on a later
   pass.
4. **Live-site verification was not possible this run.** Both shells and `WebFetch` were refused:
   the two proxies return 403 on `blog.dugong.live` outright, and `WebFetch` correctly honours the
   site's own robots.txt, which disallows `/_qa_tmp/` - so the one URL worth testing is the one URL
   that cannot be tested from here. The 10-19 pass did reach the live site, so this is intermittent
   rather than a new block. The exposure in Part 1 is established from the mechanism (`.nojekyll`,
   plus the file being in the served commit) rather than from a fetch.
5. **Two routines still share one tree and one minute.** Carried item 3 from 10-19, and this run is a
   second instance of the same class of problem from a different direction: a trigger that fired on
   10-15 executed on 10-19 against a tree four days and five commits ahead of the one it was scheduled
   against. It read the day's report first and so cost nothing, but a pass that had started editing on
   its stale assumptions would have fought the 10-19 work. **Worth having every pass read the newest
   `SEO-GEO-report-*.md` before it audits anything**, which costs one file read and makes a late or
   duplicated run safe by construction.

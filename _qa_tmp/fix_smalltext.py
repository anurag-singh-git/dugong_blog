import glob,re
BLOCK = """
/* QA 2026-10-11: 12px legibility floor for micro-labels on phones (desktop unchanged) */
@media (max-width: 560px) {
  .tag { font-size: 12px; letter-spacing: 0.05em; }
  .post-meta { font-size: 12px; }
  .post-read { font-size: 12px; }
  .card-foot { font-size: 12px; }
  .card-date, .card-author { font-size: 12px; }
  .byline-avatar { font-size: 12px; }
  .callout-mark { font-size: 12px; }
  .cta-fine { font-size: 12px; }
  .foot-h { font-size: 12px; }
  .stat-label { font-size: 12px; }
  .pb-status, .pb-tag, .pb-node-sub, .pb-branch-arm { font-size: 12px; }
}
@media (max-width: 360px) {
  .nav-cta { font-size: 12px; padding: 7px 9px; }
}
"""
n=0; skipped=[]
for f in sorted(glob.glob('*.html')):
    raw=open(f,encoding='utf-8').read()
    if 'QA 2026-10-11' in raw: continue
    if '</style>' not in raw: skipped.append(f); continue
    i=raw.rindex('</style>')
    raw=raw[:i]+BLOCK+raw[i:]
    open(f,'w',encoding='utf-8').write(raw); n+=1
print('files patched:',n)
print('no <style> (stubs):',len(skipped))

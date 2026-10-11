import glob
ADD = """  .foot-bot, .foot-bot span, .foot-bot a { font-size: 12px; }
  .art-coord { font-size: 12px; }
  .signup-label { font-size: 12px; }
  .signup-fine { font-size: 12px; }
  .arch-date { font-size: 12px; }
  .author-role { font-size: 12px; }
"""
MARK = "  .pb-status, .pb-tag, .pb-node-sub, .pb-branch-arm { font-size: 12px; }\n"
n=0
for f in sorted(glob.glob('*.html')):
    raw=open(f,encoding='utf-8').read()
    if MARK not in raw or '.foot-bot, .foot-bot span' in raw: continue
    raw=raw.replace(MARK, MARK+ADD, 1)
    open(f,'w',encoding='utf-8').write(raw); n+=1
print('files patched:',n)

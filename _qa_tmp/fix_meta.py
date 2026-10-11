import glob,re,html
from bs4 import BeautifulSoup
changed=[]
for f in sorted(glob.glob('*.html')):
    raw=open(f,encoding='utf-8').read()
    if 'noindex' in raw and len(raw)<20000 and f!='404.html': continue
    s=BeautifulSoup(raw,'lxml')
    og=s.find('meta',attrs={'property':'og:description'})
    tw=s.find('meta',attrs={'name':'twitter:description'})
    if not og: continue
    want=og['content'].strip()
    if tw is None: continue
    cur=tw['content'].strip()
    if cur==want: continue
    # replace only the twitter:description tag's content, byte-exact in source
    m=re.search(r'<meta\s+name="twitter:description"\s+content="(.*?)"\s*/?>',raw,re.S)
    if not m:
        print('  !! tag not matched in source:',f); continue
    esc=html.escape(want,quote=True).replace('&#x27;',"'")
    new=raw[:m.start()]+'<meta name="twitter:description" content="%s" />'%esc+raw[m.end():]
    open(f,'w',encoding='utf-8').write(new)
    changed.append((f,len(cur),len(want)))
print('twitter:description mirrored on',len(changed),'pages')
for f,a,b in changed[:60]: print('  %-66s %d -> %d'%(f[:66],a,b))

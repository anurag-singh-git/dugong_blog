import re,html
from bs4 import BeautifulSoup
# 1) Pages whose og:description exceeds the 165-char ceiling: mirror the canonical meta description
for f in ['best-shopify-automations-to-set-up.html',
          'how-to-reduce-where-is-my-order-wismo-tickets-on-shopify.html',
          'how-to-validate-shipping-addresses-on-shopify.html']:
    raw=open(f,encoding='utf-8').read()
    s=BeautifulSoup(raw,'lxml')
    want=s.find('meta',attrs={'name':'description'})['content'].strip()
    esc=html.escape(want,quote=True).replace('&#x27;',"'")
    for pat,repl in (
        (r'<meta\s+property="og:description"\s+content="(.*?)"\s*/?>','<meta property="og:description" content="%s" />'%esc),
        (r'<meta\s+name="twitter:description"\s+content="(.*?)"\s*/?>','<meta name="twitter:description" content="%s" />'%esc)):
        raw,n=re.subn(pat,lambda m: repl,raw,count=1,flags=re.S)
        assert n==1,(f,pat)
    open(f,'w',encoding='utf-8').write(raw)
    print('mirrored meta->og/twitter:',f,len(want))

# 2) 404.html: trim meta description to the 165 ceiling, add the twitter card block the other 79 pages carry
raw=open('404.html',encoding='utf-8').read()
old='That page is not here. Dugong Field Notes publishes field research on Shopify and ecommerce workflow automation. Start from the latest dispatches or the full archive.'
new='That page is not here. Dugong Field Notes publishes field research on Shopify and ecommerce workflow automation. Start from the latest dispatches or the archive.'
assert old in raw and len(new)<=165, (len(old),len(new))
raw=raw.replace(old,new)
print('404 meta description',len(old),'->',len(new))
if 'twitter:card' not in raw:
    anchor='<meta property="og:image" content="https://blog.dugong.live/og-image.png" />'
    assert anchor in raw
    blk=(anchor+'\n'
         '<meta name="twitter:card" content="summary_large_image" />\n'
         '<meta name="twitter:title" content="Page not found" />\n'
         '<meta name="twitter:description" content="That page is not here. Start from the latest dispatches or the full archive." />\n'
         '<meta name="twitter:image" content="https://blog.dugong.live/og-image.png" />')
    raw=raw.replace(anchor,blk,1)
    print('404: twitter card tags added')
open('404.html','w',encoding='utf-8').write(raw)

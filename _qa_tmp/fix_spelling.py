import glob,re,sys
# US-English normalisation. Word-boundary, case-preserving for first letter.
PAIRS=[('grey','gray'),('Grey','Gray'),
       ('fulfilment','fulfillment'),('Fulfilment','Fulfillment'),
       ('colour','color'),('Colour','Color'),('colours','colors'),
       ('defence','defense'),('Defence','Defense'),
       ('apologise','apologize'),('apologised','apologized'),('Apologise','Apologize'),
       ('programme','program'),('Programme','Program'),
       ('labelled','labeled'),('Labelled','Labeled')]
targets=sorted(glob.glob('*.html'))+['feed.xml','llms.txt','llms-full.txt','sitemap.xml']
total=0; changed=[]
for f in targets:
    try: raw=open(f,encoding='utf-8').read()
    except FileNotFoundError: continue
    orig=raw; n=0
    for a,b in PAIRS:
        new,k=re.subn(r'\b'+a+r'\b',b,raw)
        raw=new; n+=k
    if raw!=orig:
        open(f,'w',encoding='utf-8').write(raw); changed.append((f,n)); total+=n
print('replacements:',total)
for f,n in changed: print('  %-64s %d'%(f[:64],n))

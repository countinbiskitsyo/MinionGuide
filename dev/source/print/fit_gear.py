import re
from weasyprint import HTML
from pypdf import PdfReader, PdfWriter
src=open('gear_targets.html').read()
head,body=src.split('<body>',1); body=body.split('</body>')[0]
pre=body[:body.find('<div class="slot">')]
foot=body[body.rfind('<div class="foot">'):]
blocks=re.findall(r'<div class="slot">.*?</table>(?:<div class="note">.*?</div>)*</div>',body,re.S)
print('blocks',len(blocks))
def sc(s,f): return re.sub(r'(\d+(?:\.\d+)?)pt',lambda m:f"{float(m.group(1))*f:.2f}pt",s)
def doc(inner): return head+'<body>'+inner+'</body></html>'
def fit(inner,tag):
    lo,hi=0.6,1.5
    for _ in range(11):
        m=(lo+hi)/2; HTML(string=sc(doc(inner),m)).write_pdf(tag+'.pdf')
        if len(PdfReader(tag+'.pdf').pages)==1: lo=m
        else: hi=m
    f=round(lo-0.003,3); HTML(string=sc(doc(inner),f)).write_pdf(tag+'.pdf'); return f
best=None
for k in range(4,len(blocks)-2):
    f1=fit(pre+''.join(blocks[:k]),'a'); f2=fit(''.join(blocks[k:])+foot,'b')
    print(k,f1,f2)
    if best is None or min(f1,f2)>min(best[1],best[2]): best=(k,f1,f2)
k,f1,f2=best; print('chosen',best)
fit(pre+''.join(blocks[:k]),'a'); fit(''.join(blocks[k:])+foot,'b')
w=PdfWriter(); w.add_page(PdfReader('a.pdf').pages[0]); w.add_page(PdfReader('b.pdf').pages[0]); w.write('MinionGuide_print_gear_targets.pdf')
open('split_choice.txt','w').write(str(best))

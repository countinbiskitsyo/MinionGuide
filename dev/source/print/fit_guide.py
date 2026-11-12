import re,sys
from weasyprint import HTML
from pypdf import PdfReader,PdfWriter
def sc(s,f): return re.sub(r'(\d+(?:\.\d+)?)pt',lambda m:f"{float(m.group(1))*f:.2f}pt",s)
def fit(src,tag):
    lo,hi=0.6,1.6
    for _ in range(12):
        m=(lo+hi)/2; HTML(string=sc(src,m)).write_pdf(tag+'.pdf')
        if len(PdfReader(tag+'.pdf').pages)==1: lo=m
        else: hi=m
    f=round(lo-0.004,3); HTML(string=sc(src,f)).write_pdf(tag+'.pdf'); return f
def setw(src,wl): return re.sub(r'colL" style="width:[0-9.]*%',f'colL" style="width:{wl}%',re.sub(r'colR" style="width:[0-9.]*%',f'colR" style="width:{97.2-wl:.1f}%',src,1),1)
front=open('guide_front.html').read()
best=None
for wl in [float(x) for x in sys.argv[1:]] or [52.0]:
    s=fit(setw(front,wl),'f'); print('WL',wl,s)
    if not best or s>best[1]: best=(wl,s)
open('guide_front.html','w').write(setw(front,best[0])); f1=fit(open('guide_front.html').read(),'f'); f2=fit(open('guide_back.html').read(),'b')
w=PdfWriter(); w.add_page(PdfReader('f.pdf').pages[0]); w.add_page(PdfReader('b.pdf').pages[0]); w.write('MinionGuide_print_guide.pdf'); print('final',best,f1,f2)

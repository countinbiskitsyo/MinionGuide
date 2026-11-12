"""Build ../../index.html (the live page) from the template + data. Run from the repo root:
   python3 dev/source/build_index.py
For each release, edit the version in checklist_template.html (<title> and the hero 'vX.Y · date · PoB code vA.B')."""
import json, os
H=os.path.dirname(os.path.abspath(__file__))
t=open(os.path.join(H,'checklist_template.html'),encoding='utf-8').read()
d=json.load(open(os.path.join(H,'checklist_data.json'),encoding='utf-8'))
d['gearTargets']=open(os.path.join(H,'gear_targets_fragment.html'),encoding='utf-8').read()
d['pob']=open(os.path.join(H,'..','PoB_code.txt'),encoding='utf-8').read().strip()
out=t.replace('__DATA__',json.dumps(d,ensure_ascii=False).replace('</','<\\/'))
open(os.path.join(H,'..','..','index.html'),'w',encoding='utf-8').write(out)
print('index.html written',len(out))

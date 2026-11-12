"""Build index.html (the live page) from the template + data. Run from the repo root:
   python3 dev/source/build_index.py
For each release, edit the version in checklist_template.html (<title> and the hero '.ver' line)."""
import json, os, re
H=os.path.dirname(os.path.abspath(__file__))
rd=lambda *p: open(os.path.join(H,*p),encoding='utf-8').read()
t=rd('checklist_template.html')
d=json.loads(rd('checklist_data.json'))
d['gems']=json.loads(rd('gems.json'))                      # structured gem loadout (keys must stay stable)
frag=rd('gear_targets_fragment.html')
i=frag.find('<div class="slot">')
d['gearTargets']=frag[:i]+'<div class="slots">'+frag[i:]+'</div>'
gn=[n for n in re.findall(r'<div class="note[^"]*">.*?</div>',d['gear'],re.S) if 'While levelling' not in n]
d['gearNotes']='<div class="notes" style="margin-top:0;margin-bottom:12px">'+''.join(gn)+'</div>'
d['pob']=rd('..','PoB_code.txt').strip()
out=t.replace('__DATA__',json.dumps(d,ensure_ascii=False).replace('</','<\\/'))
open(os.path.join(H,'..','..','index.html'),'w',encoding='utf-8').write(out)
print('index.html written',len(out))

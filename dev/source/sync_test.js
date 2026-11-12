const {JSDOM}=require(process.env.JSDOM||'jsdom'); const fs=require('fs');
const html=fs.readFileSync(require('path').join(__dirname,'..','..','index.html'),'utf8');
const GOOD='ghp_test123'; let gists={}, nid=1, calls=[];
function mkFetch(){ return async (url,opts={})=>{
  const h=opts.headers||{}; const method=(opts.method||'GET'); calls.push(method+' '+url.replace('https://api.github.com',''));
  const res=(status,obj)=>({ok:status<300,status,json:async()=>obj,text:async()=>JSON.stringify(obj)});
  if(h.Authorization!=='Bearer '+GOOD) return res(401,{message:'Bad credentials'});
  const u=new URL(url); const p=u.pathname;
  if(p==='/gists'&&method==='GET') return res(200,Object.values(gists).map(g=>({id:g.id,files:{[Object.keys(g.files)[0]]:{filename:Object.keys(g.files)[0]}}})));
  if(p==='/gists'&&method==='POST'){ const b=JSON.parse(opts.body); const id='g'+(nid++); gists[id]={id,files:{}}; for(const k in b.files) gists[id].files[k]={content:b.files[k].content,truncated:false}; return res(201,gists[id]); }
  const m=p.match(/^\/gists\/(\w+)$/);
  if(m&&method==='GET'){ return gists[m[1]]?res(200,gists[m[1]]):res(404,{}); }
  if(m&&method==='PATCH'){ const b=JSON.parse(opts.body); for(const k in b.files) gists[m[1]].files[k]={content:b.files[k].content,truncated:false}; return res(200,gists[m[1]]); }
  return res(404,{});
};}
function device(name){
  const dom=new JSDOM(html,{runScripts:'dangerously',url:'https://me.github.io/minion-guide/',beforeParse(w){ w.fetch=mkFetch(); if(!w.HTMLDialogElement.prototype.showModal){ w.HTMLDialogElement.prototype.showModal=function(){this.open=true}; w.HTMLDialogElement.prototype.close=function(){this.open=false}; } }});
  return dom.window;
}
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
(async()=>{
  const A=device('A'); await sleep(200);
  const st=w=>w.document.getElementById('status').textContent;
  console.log('A start:',st(A));
  // bad token
  A.document.getElementById('syncBtn').click(); A.document.getElementById('tokIn').value='wrong'; A.document.getElementById('tokSave').click(); await sleep(200);
  console.log('A bad token:',st(A));
  // good token
  A.document.getElementById('tokIn').value=GOOD; A.document.getElementById('tokSave').click(); await sleep(300);
  console.log('A connected:',st(A),'gists:',Object.keys(gists).length);
  // tick 3 things on A
  const boxes=[...A.document.querySelectorAll('[role=checkbox][data-key]')]; boxes[0].click(); boxes[10].click(); boxes[90].click();
  await sleep(1600); console.log('A after ticks:',st(A),'| A total:',A.document.getElementById('totText').textContent);
  // device B
  const B=device('B'); await sleep(200);
  B.document.getElementById('syncBtn').click(); B.document.getElementById('tokIn').value=GOOD; B.document.getElementById('tokSave').click(); await sleep(300);
  console.log('B connected:',st(B),'| B total:',B.document.getElementById('totText').textContent,'gists:',Object.keys(gists).length);
  // untick on B, then A returns to tab
  [...B.document.querySelectorAll('[role=checkbox][data-key]')][10].click(); await sleep(1600);
  Object.defineProperty(A.document,'visibilityState',{value:'visible',configurable:true}); A.document.dispatchEvent(new A.Event('visibilitychange')); await sleep(300);
  console.log('A after B untick:',A.document.getElementById('totText').textContent,'|',st(A));
  console.log('API calls:',calls.length, [...new Set(calls)].join(' , '));
  process.exit(0);
})();

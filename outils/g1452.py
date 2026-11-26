import json,re,difflib,sys
base,out,grid=sys.argv[1],sys.argv[2],sys.argv[3]
src=open(base,encoding='utf-8').read(); orig=src
cfg=json.load(open(sys.argv[4]))  # {"subs":[[chordregex, oldscale, newscale]], "desc":[old,new]}
i=src.index('{id:"%s",'%grid); j=src.index('\n{id:',i+10); A=src[i:j]; B=A
for nm,o,n in cfg["subs"]:
    B,k=re.subn(r'(\{name:"(?:%s)",beats:[\d.]+,voicing:"[^"]+",scale:)"%s"'%(nm,o),r'\1"%s"'%n,B); print(nm,o,'->',n,k)
o,n=cfg["desc"]; assert B.count(o)==1; B=B.replace(o,n)
src=src[:i]+B+src[j:]
sm=difflib.SequenceMatcher(None,A,B,autojunk=False); ops=[x for x in sm.get_opcodes() if x[0]!='equal']
a1,a2=ops[0][1],ops[-1][2]; b1,b2=ops[0][3],ops[-1][4]; c=30
while orig.count(A[max(0,a1-c):a2+c])!=1: c+=20
E=[{"old_text":A[max(0,a1-c):a2+c],"new_text":A[max(0,a1-c):a1]+B[b1:b2]+A[a2:a2+c]}]
x=orig.replace(E[0]["old_text"],E[0]["new_text"]); print('ok',x==src, len(E[0]["old_text"]))
open(out,'w',encoding='utf-8').write(src); json.dump(E,open(out.replace('.html','.json').replace('/v','/e'),'w'),ensure_ascii=False)

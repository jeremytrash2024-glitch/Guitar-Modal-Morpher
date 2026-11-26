import json,re,difflib
src=open('/tmp/t/v1450.html',encoding='utf-8').read(); orig=src; E=[]
def bloc(g):
    i=src.index('{id:"%s",'%g); j=src.index('\n{id:',i+10); return i,j
MAP={"jz-harris-sixte-dim":[('scale:"C:symmetric:0"','scale:"C:bebop:1"'),('scale:"C:0"','scale:"C:bebop:1"')],
     "jz-harris-sixte-min":[('scale:"C:symmetric:0"','scale:"C:bebop:3"'),('scale:"C:melodicMinor:0"','scale:"C:bebop:3"')],
     "jz-ii-v-i-maj":[('{name:"Dm7",','DM'),]}
DESC={"jz-harris-sixte-dim":("Pour improviser : Do majeur sur les Do 6, ajoute le Lab sur les diminués.","Pour improviser : la gamme bebop majeure de Do partout ; sur les Do 6 comme sur les diminués, c'est la même gamme."),
      "jz-harris-sixte-min":("Pour improviser : Do mineur mélodique sur les Do m6, ajoute le Lab sur les diminués.","Pour improviser : la gamme bebop mineure mélodique de Do partout, sur les Do m6 comme sur les diminués."),
      "jz-ii-v-i-maj":("Pour improviser : Do majeur partout, sauf Lab, Sib et Mib sur Fa m7, Lab et Sib sur Sib 7, Do# et Fa# sur La 7.","Pour improviser : les gammes bebop sur la cadence, dorienne sur Ré m7, dominante sur Sol 7, majeure sur Do maj7 ; ailleurs Do majeur, sauf Fa m7 (bebop dorienne de Fa), Sib 7 (Lab et Sib) et La 7 (bebop dominante de La).")}
for g in ["jz-harris-sixte-dim","jz-harris-sixte-min","jz-ii-v-i-maj"]:
    i,j=bloc(g); A=src[i:j]; B=A
    if g=="jz-ii-v-i-maj":
        B=re.sub(r'(\{name:"Dm7",beats:\d+,voicing:"[^"]+",scale:)"D:1"',r'\1"D:bebop:2"',B)
        B=re.sub(r'(\{name:"G7",beats:\d+,voicing:"[^"]+",scale:)"G:4"',r'\1"G:bebop:0"',B)
        B=re.sub(r'(\{name:"Cmaj7",beats:\d+,voicing:"[^"]+",scale:)"C:0"',r'\1"C:bebop:1"',B)
        B=re.sub(r'(\{name:"Fm7",beats:\d+,voicing:"[^"]+",scale:)"F:1"',r'\1"F:bebop:2"',B)
        B=re.sub(r'(\{name:"A7",beats:\d+,voicing:"[^"]+",scale:)"A:4"',r'\1"A:bebop:0"',B)
    else:
        for o,n in MAP[g]: B=B.replace(o,n)
    o,n=DESC[g]; assert B.count(o)==1,g; B=B.replace(o,n)
    print(g, len(re.findall(r'bebop:\d',B)))
    src=src[:i]+B+src[j:]
    sm=difflib.SequenceMatcher(None,A,B,autojunk=False); ops=[x for x in sm.get_opcodes() if x[0]!='equal']
    for op,a1,a2,b1,b2 in ops:
        c=30
        while orig.count(A[max(0,a1-c):a2+c])!=1: c+=20
        E.append({"old_text":A[max(0,a1-c):a2+c],"new_text":A[max(0,a1-c):a1]+B[b1:b2]+A[a2:a2+c]})
# fusion des éditions qui se chevauchent : appliquer séquentiellement et vérifier
x=orig; ok=True
for d in E:
    if x.count(d["old_text"])!=1: ok=False; break
    x=x.replace(d["old_text"],d["new_text"])
print('éditions',len(E),'ok',ok and x==src)
open('/tmp/t/v1451.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1451.json','w'),ensure_ascii=False)

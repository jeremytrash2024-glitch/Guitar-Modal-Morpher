import sys,json; sys.path.insert(0,'/tmp/t'); from lib import *
src=open('/tmp/t/v1476.html',encoding='utf-8').read(); E=[]
def rep(o,n):
    global src
    assert src.count(o)==1,(src.count(o),o[:80]); src=src.replace(o,n); E.append({"old_text":o,"new_text":n})
O=[40,45,50,55,59,64]
def ref(v):
    m=min(O[i]+int(f) for i,f in enumerate(v.split('-')) if f!='x')-12
    while m>45: m-=12
    return m
SH=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
FL=["C","Db","D","Eb","E","F","Gb","G","Ab","A","Bb","B"]
def nm(m): return SH[m%12]+str(m//12-1)
def bas(pc):  # registre de contrebasse 29..40
    m=29+((pc-5)%12); return m
keys=[0,5,10,3,8,1,6,11,4,9,2,7]; TON=["C","F","Bb","Eb","Ab","Db","Gb","B","E","A","D","G"]
CH=[]
for k,t in enumerate(keys):
    s=t if t<=10 else t-12
    ii,V,I=(t+2)%12,(t+7)%12,t
    v_ii="x-%d-%d-%d-%d-x"%(5+s,3+s,5+s,5+s)
    v_V="%d-x-%d-%d-%d-x"%(3+s,3+s,4+s,5+s)
    v_I="x-%d-%d-%d-%d-x"%(3+s,2+s,4+s,3+s)
    nt=(keys[(k+1)%12]+2)%12   # ii suivant = quinte de la tonalité
    bi,bv,bI=bas(ii),bas(V),bas(I)
    L_ii=[[0,bi,2],[2,bi+7 if bi+7<=43 else bi-5,2]]
    L_V=[[0,bv,2],[2,bv+7 if bv+7<=43 else bv-5,1],[3,bas((I+2)%12),1]]
    L_I=[[0,bI,2],[2,bI+7 if bI+7<=43 else bI-5,2],[4,bI,2],[6,bI+4 if bI+4<=43 else bI-8,1],[7,bas((I+9)%12),1]]
    for nmC,beats,v,sc,L in ((FL[ii]+"m9",4,v_ii,SH[ii]+":bebop:2",L_ii),(FL[V]+"13",4,v_V,SH[V]+":bebop:0",L_V),(FL[I]+"maj9",8,v_I,SH[I]+":bebop:1",L_I)):
        fr=[int(x) for x in v.split('-') if x!='x']; assert min(fr)>=1 and max(fr)<=15,(nmC,v)
        CH.append('{name:"%s",beats:%d,voicing:"%s",ton:"%s",scale:"%s",basseLigne:%s}'%(nmC,beats,v,TON[k],sc,J([[b,m-ref(v),d] for b,m,d in L])))
gid="jz-douze-visages"
i0=src.index('{id:"%s",'%gid); i1=src.index('\n{id:',i0+10); old=src[i0:i1]
assert old.endswith(']},'),old[-30:]
desc=("Le geste : les trois mêmes formes dans les douze tonalités, par quartes. ii en m9 (fondamentale sur la corde de La), V en 13 (fondamentale sur le Mi grave), I en maj9 (corde de La) : les trois tiennent dans quatre cases, et c'est la même main qui se déplace d'une tonalité à l'autre. "
 "La contrebasse joue fondamentale et quinte ; sa dernière note mène au ii suivant, qui est toujours la quinte de la tonalité qu'on quitte. Sib, La et Lab se jouent haut (jusqu'à la case 15) pour garder les mêmes formes sans corde à vide. "
 "Pour improviser : bebop dorienne sur le ii, bebop dominante sur le V, bebop majeure sur le I, dans chaque tonalité.")
new=('{id:"%s", lecons:{pentatoniques:2, voicings:3, cadences:2}, basseSon:"uprightReel", basseDb:12, basseHarmoniques:-4, rythmeDb:6, preset:"ballade", root:"C", scale:"C:0",   /* v1477 : exercice ; une seule forme par fonction transposée dans les douze tonalités, 96 bpm, contrebasse */\n'
     'name:"Les douze visages — trois formes, douze tonalités", tempo:96, groove:"jazz",\ndesc:"%s",\nchords:[\n'%(gid,desc)+",\n".join(CH)+"\n]},")
rep(old,new)
rep('const NOUVEAUTES=[\n["jz-rhythm-changes-pont","remix v1476"],','const NOUVEAUTES=[\n["jz-douze-visages","remix v1477"],   // v1477 — exercice : trois formes, douze tonalités, contrebasse\n["jz-rhythm-changes-pont","remix v1476"],')
if src.count('["jz-douze-visages",{feel:"shuffle"}],\n'): rep('["jz-douze-visages",{feel:"shuffle"}],\n','')
open('/tmp/t/v1477.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1477.json','w'),ensure_ascii=False)
print("ok",len(E))

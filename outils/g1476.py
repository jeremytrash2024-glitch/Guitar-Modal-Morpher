import sys,json; sys.path.insert(0,'/tmp/t'); from lib import *
src=open('/tmp/t/v1475.html',encoding='utf-8').read(); E=[]
def rep(o,n):
    global src
    assert src.count(o)==1,(src.count(o),o[:80]); src=src.replace(o,n); E.append({"old_text":o,"new_text":n})
O=[40,45,50,55,59,64]
def ref(v):
    m=min(O[i]+int(f) for i,f in enumerate(v.split('-')) if f!='x')-12
    while m>45: m-=12
    return m
PC2={'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11}
def nom(m): return [k for k,v in PC2.items() if v==m%12][0]+str(m//12-1)
S={"bb":[10,0,2,3,5,7,9],"ga":[7,9,10,0,2,3,5],"cd":[0,2,3,5,7,9,10],"fm":[5,7,9,10,0,2,3],"gp":[7,8,11,0,2,3,5],"dm":[2,4,6,7,9,11,0],"gm":[7,9,11,0,2,4,5],"cm":[0,2,4,5,7,9,10]}
C=[("Bbmaj7","x-1-3-2-3-x","A#:bebop:1",S["bb"]),("Gm7","3-x-3-3-3-x","G:5",S["ga"]),("Cm7","x-3-5-3-4-x","C:bebop:2",S["cd"]),("F7","1-x-1-2-1-x","F:bebop:0",S["fm"]),
   ("Bb6","6-x-5-7-6-x","A#:bebop:1",S["bb"]),("G7b9","x-x-3-4-3-4","G:harmonicMinor:4",S["gp"]),("Cm7","x-3-5-3-4-x","C:bebop:2",S["cd"]),("F13","1-x-1-2-3-x","F:bebop:0",S["fm"]),
   ("D9","x-5-4-5-5-x","D:bebop:0",S["dm"]),("D9","x-5-4-5-5-x","D:bebop:0",S["dm"]),("G7","3-x-3-4-3-x","G:bebop:0",S["gm"]),("G7","3-x-3-4-3-x","G:bebop:0",S["gm"]),
   ("C9","x-3-2-3-3-x","C:bebop:0",S["cm"]),("C9","x-3-2-3-3-x","C:bebop:0",S["cm"]),("F7","1-x-1-2-1-x","F:bebop:0",S["fm"]),("F7","1-x-1-2-1-x","F:bebop:0",S["fm"])]
R=["A#1","G1","C2","F1","A#1","G1","C2","F1","D2","D2","G1","G1","C2","C2","F1","F1"]
Q=["F2","D2","G1","C2","F2","D2","G1","C2","A1","A1","D2","D2","G1","G1","C2","C2"]
M=[[[0,"D5",2.5,"vib"],[3,"C5",.5],[3.5,"A#4",.5]],
   [[0,"A#4",1],[1,"A4",.5],[1.5,"G4",.5],[2,"D5",1.5]],
   [[0,"D#5",2.5,"vib"],[3,"D5",.5],[3.5,"C5",.5]],
   [[0,"A4",1],[1,"C5",.5],[1.5,"D#5",.5],[2,"D5",1.5]],
   [[0,"D5",2.5,"vib"],[3,"F5",.5],[3.5,"D5",.5]],
   [[0,"B4",1],[1,"D5",.5],[1.5,"F5",.5],[2,"D5",1.5]],
   [[0,"D#5",2.5,"vib"],[3,"D5",.5],[3.5,"C5",.5]],
   [[0,"A4",1],[1,"C5",.5],[1.5,"D5",.5],[2,"C5",1.5]],
   [[0,"C5",2.5,"vib"],[3,"A4",.5],[3.5,"B4",.5]],
   [[0,"C5",1],[1,"A4",.5],[1.5,"F#4",.5],[2,"C5",1.5]],
   [[0,"B4",2.5,"vib"],[3,"D5",.5],[3.5,"E5",.5]],
   [[0,"F5",1],[1,"D5",.5],[1.5,"B4",.5],[2,"F5",1.5]],
   [[0,"E5",2.5,"vib"],[3,"D5",.5],[3.5,"C5",.5]],
   [[0,"A#4",1],[1,"G4",.5],[1.5,"E4",.5],[2,"A#4",1.5]],
   [[0,"A4",2.5,"vib"],[3,"C5",.5],[3.5,"D5",.5]],
   [[0,"D#5",1],[1,"C5",.5],[1.5,"A4",.5],[2,"D#5",1.5]]]
Rp=[[[1.5,"F4",.5],[2,"A4",.5],[2.5,"A#4",.5]],[[3,"F4",.5],[3.5,"G4",.5]],
    [[1.5,"G4",.5],[2,"A#4",.5],[2.5,"G4",.5]],[[3,"A4",.5],[3.5,"F4",.5]],
    [[1.5,"F4",.5],[2,"G4",.5],[2.5,"A#4",.5]],[[3,"G#4",.5],[3.5,"F4",.5]],
    [[1.5,"C4",.5],[2,"G4",.5],[2.5,"A#4",.5]],[[3,"F4",.5],[3.5,"A4",.5]],
    [[1.5,"F#4",.5],[2,"A4",.5],[2.5,"E4",.5]],[[3,"F#4",.5],[3.5,"A4",.5]],
    [[1.5,"F4",.5],[2,"D4",.5],[2.5,"G4",.5]],[[3,"B4",.5],[3.5,"G4",.5]],
    [[1.5,"A#4",.5],[2,"G4",.5],[2.5,"D5",.5]],[[3,"G4",.5],[3.5,"E4",.5]],
    [[1.5,"F4",.5],[2,"C4",.5],[2.5,"D#4",.5]],[[3,"A4",.5],[3.5,"C5",.5]]]
for i in range(16):
    for b,n,d,*_ in M[i]+Rp[i]: assert midi(n)%12 in C[i][3],(i,n)
A=[]
for i in range(16):
    nxt=midi(R[(i+1)%16]); sol=[midi(n) for b,n,d,*_ in M[i]+Rp[i] if b<4 and b+d>3]
    best=None
    for dlt in (2,-2,1,-1):
        c=nxt+dlt
        if c%12 in C[i][3] and not any(abs(c-x)%12 in (1,11) for x in sol) and c!=midi(Q[i]): best=c; break
    A.append(nom(best) if best else Q[i])
print(A)
BL=[[[0,R[i],2],[2,Q[i],1],[3,A[i],1]] for i in range(16)]
on=[0]*256
for i in range(16):
    for b,n,d,*_ in M[i]+Rp[i]+BL[i]: assert b+d<=4
    for b,n,d,*_ in M[i]+Rp[i]:
        for k in range(int((4*i+b)*4),int((4*i+b+d)*4)): on[k]=1
assert on.count(0)==0,[k/4 for k,x in enumerate(on) if not x]
P1=[[n,4*i+b,d] for i in range(16) for b,n,d,*_ in M[i]]
P2=[[n,4*i+b,d] for i in range(16) for b,n,d,*_ in Rp[i]]
gid="jz-rhythm-changes-pont"
i0=src.index('{id:"%s",'%gid); i1=src.index('\n{id:',i0+10); old=src[i0:i1]
assert old.endswith('}]},'),old[-30:]
desc=("Le geste : huit mesures chez Sib (I, vi, ii, V, deux fois), où l'oreille se pose ; puis le pont, quatre dominantes par quartes, deux mesures chacune : Ré 9, Sol 7, Do 9, Fa 7. "
 "Sur le pont, la septième de chaque dominante glisse d'un demi-ton et devient la tierce de la suivante : Do vers Si, Fa vers Mi, Sib vers La, et le Mib final retombe sur le Ré de Sib. Le sax tient chaque note, puis la fait glisser ; la main descend le manche. "
 "Pour improviser : bebop majeure sur Sib, Sol éolien, bebop dorienne sur Do m, mixolydien b9 b13 sur Sol 7b9, bebop dominante sur toutes les dominantes du pont.")
new=('{id:"%s", soloAuto:true, phrase:%s, phrase2:%s,   /* v1476 : ballade à 72 bpm, rythme droit, 16 mesures ; A en Sib (I vi ii V deux fois), pont de quatre dominantes par quartes, la septième glisse vers la tierce suivante ; contrebasse */ '
     'phraseAuto:true, phraseDb:-1, soloDb:7, basseSon:"uprightReel", basseDb:12, basseHarmoniques:-4, rythmeDb:6, preset:"ballade", lecons:{cadences:2, voicings:2, dominantes:2}, root:"A#", scale:"A#:0",\n'
     'name:"Le pont en ballade — rhythm changes en Sib", tempo:72, groove:"jazz",\ndesc:"%s",\nchords:[\n'%(gid,J(P1),J(P2),desc)
     + ",\n".join('{name:"%s",beats:4,voicing:"%s",scale:"%s",basseLigne:%s,soloEcrit:%s,soloEcrit2:%s}'%(n,v,sc,J([[bb,midi(x)-ref(v),d] for bb,x,d in BL[i]]),J(Rp[i]),J(M[i])) for i,(n,v,sc,_) in enumerate(C))
     + "\n]},")
rep(old,new)
rep('const NOUVEAUTES=[\n["jz-substitution-triton","remix v1475"],','const NOUVEAUTES=[\n["jz-rhythm-changes-pont","remix v1476"],   // v1476 — ballade, rhythm changes en Sib : la septième glisse vers la tierce suivante\n["jz-substitution-triton","remix v1475"],')
if src.count('["jz-rhythm-changes-pont",{feel:"shuffle"}],\n'): rep('["jz-rhythm-changes-pont",{feel:"shuffle"}],\n','')
open('/tmp/t/v1476.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1476.json','w'),ensure_ascii=False)
print("ok",len(E))

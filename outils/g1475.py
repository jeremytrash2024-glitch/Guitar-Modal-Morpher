import sys,json; sys.path.insert(0,'/tmp/t'); from lib import *
src=open('/tmp/t/v1474.html',encoding='utf-8').read(); E=[]
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
S={"dd":[2,4,5,7,9,11,0],"gm":[7,9,11,0,2,4,5],"c":[0,2,4,5,7,9,11],"dl":[1,3,5,7,8,10,11],"ep":[4,5,7,9,11,0,2],"el":[3,5,7,9,10,0,1]}
DM=("Dm7","x-5-3-5-6-x","D:bebop:2",S["dd"]); CM=("Cmaj9","x-3-2-4-3-x","C:bebop:1",S["c"]); C6=("C6/9","x-3-2-2-3-3","C:bebop:1",S["c"])
DB=("Db9","x-4-3-4-4-x","C#:melodicMinor:3",S["dl"]); EM=("Em7","x-7-9-7-8-x","E:2",S["ep"]); EB=("Eb9","x-6-5-6-6-x","D#:melodicMinor:3",S["el"])
C=[DM,("G7","3-x-3-4-3-x","G:bebop:0",S["gm"]),CM,C6, DM,DB,CM,C6, EM,EB,DM,DB, CM,C6,EM,EB]
R=["D2","G1","C2","C2","D2","C#2","C2","C2","E2","D#2","D2","C#2","C2","C2","E2","D#2"]
Q=["A1","D2","G1","G1","A1","G#1","G1","G1","B1","A#1","A1","G#1","G1","G1","B1","A#1"]
ii=[[0,"A4",1],[1,"G4",.5],[1.5,"E4",.5],[2,"F4",2,"vib"]]
V=[[0,"F4",3,"vib"],[3,"G4",.5],[3.5,"F4",.5]]
I1=[[0,"E4",2,"vib"],[2,"G4",.5],[2.5,"B4",.5],[3,"D5",1]]
I2=[[0,"C5",2,"vib"],[2,"B4",.5],[2.5,"A4",.5],[3,"A4",1]]
iii=[[0,"B4",1],[1,"A4",.5],[1.5,"E4",.5],[2,"G4",2,"vib"]]
VI=[[0,"G4",3,"vib"],[3,"A4",.5],[3.5,"G4",.5]]
M=[ii,V,I1,I2, ii,V,I1,I2, iii,VI,ii,V, I1,I2,iii,VI]
rii=[[2.5,"D4",.5],[3,"C4",.5],[3.5,"A3",.5]]; rG=[[1,"B3",.5],[1.5,"D4",.5],[2,"G3",1]]; rDb=[[1,"B3",.5],[1.5,"D#4",.5],[2,"G#3",1]]
rC=[[1,"G3",.5],[1.5,"C4",.5]]; rC6=[[1,"E4",.5],[1.5,"G4",.5]]; rE=[[2.5,"E4",.5],[3,"D4",.5],[3.5,"B3",.5]]; rEb=[[1,"A#3",.5],[1.5,"C#4",.5],[2,"D#4",1]]
Rp=[rii,rG,rC,rC6, rii,rDb,rC,rC6, rE,rEb,rii,rDb, rC,rC6,rE,rEb]
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
gid="jz-substitution-triton"
i0=src.index('{id:"%s",'%gid); i1=src.index('\n{id:',i0+10); old=src[i0:i1]
assert old.endswith('}]},'),old[-30:]
desc=("Le geste : la même cadence entendue deux fois en Do. D'abord Ré m7, Sol 7, Do ; puis Ré m7, Réb 9, Do : les deux doigts du milieu (cordes de Ré et de Sol) ne bougent pas, seule la basse change, et elle descend par demi-tons au lieu de sauter. "
 "Le sax garde le même Fa sur Sol 7 comme sur Réb 9, puis le pose sur le Mi de Do. En B, Mib 9 remplace La 7 : la basse descend Mi, Mib, Ré, Réb, Do, et la mélodie la suit (Sol, Sol, Fa, Fa, Mi). L'oreille se pose sur Do quatre fois. "
 "Pour improviser : bebop dorienne sur Ré m7, bebop dominante sur Sol 7, lydien dominant sur Réb 9 et Mib 9, bebop majeure sur Do, Mi phrygien sur Mi m7.")
new=('{id:"%s", soloAuto:true, phrase:%s, phrase2:%s,   /* v1475 : ballade à 72 bpm, rythme droit, 16 mesures en Do ; la cadence avec Sol 13 puis avec Réb 9 (mêmes doigts au milieu, basse chromatique), B Mib 9 pour La 7 ; contrebasse */ '
     'phraseAuto:true, phraseDb:-1, soloDb:7, basseSon:"uprightReel", basseDb:12, basseHarmoniques:-4, rythmeDb:6, preset:"ballade", lecons:{dominantes:4, cadences:4, voicings:3}, root:"C", scale:"C:0",\n'
     'name:"La substitution tritonique — même cadence, autre basse", tempo:72, groove:"jazz",\ndesc:"%s",\nchords:[\n'%(gid,J(P1),J(P2),desc)
     + ",\n".join('{name:"%s",beats:4,voicing:"%s",scale:"%s",basseLigne:%s,soloEcrit:%s,soloEcrit2:%s}'%(n,v,sc,J([[bb,midi(x)-ref(v),d] for bb,x,d in BL[i]]),J(Rp[i]),J(M[i])) for i,(n,v,sc,_) in enumerate(C))
     + "\n]},")
rep(old,new)
rep('const NOUVEAUTES=[\n["jz-modulations-tierces","remix v1474"],','const NOUVEAUTES=[\n["jz-substitution-triton","remix v1475"],   // v1475 — ballade, même cadence, autre basse : la substitution tritonique en Do\n["jz-modulations-tierces","remix v1474"],')
if src.count('["jz-substitution-triton",{feel:"shuffle"}],\n'): rep('["jz-substitution-triton",{feel:"shuffle"}],\n','')
open('/tmp/t/v1475.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1475.json','w'),ensure_ascii=False)
print("ok",len(E))

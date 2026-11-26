import sys,json; sys.path.insert(0,'/tmp/t'); from lib import *
src=open('/tmp/t/v1459.html',encoding='utf-8').read(); E=[]
def rep(o,n):
    global src
    assert src.count(o)==1,(src.count(o),o[:80]); src=src.replace(o,n); E.append({"old_text":o,"new_text":n})
O=[40,45,50,55,59,64]
def ref(v):
    m=min(O[i]+int(f) for i,f in enumerate(v.split('-')) if f!='x')-12
    while m>45: m-=12
    return m
C=[("Fm7","x-8-10-8-9-x","F:bebop:2"),("Bb7","6-x-6-7-6-x","A#:bebop:0"),("Ebmaj7","x-6-8-7-8-x","D#:bebop:1"),("Abmaj7","4-x-5-5-4-x","G#:bebop:1"),
   ("Dm7b5","x-5-6-5-6-x","D:6"),("G7alt","3-x-3-4-4-x","G:melodicMinor:6"),("Cm7","x-3-5-3-4-x","C:bebop:2"),("F7","1-x-1-2-1-x","F:bebop:0"),
   ("Bbm7","6-x-6-6-6-x","A#:bebop:2"),("Eb7","x-6-8-6-8-x","D#:bebop:0"),("Abmaj7","4-x-5-5-4-x","G#:bebop:1"),("Dbmaj7","x-4-6-5-6-x","C#:3"),
   ("Gm7b5","3-x-3-3-2-x","G:6"),("C7#9","x-3-2-3-4-x","C:melodicMinor:6"),("Fm7","1-x-1-1-1-x","F:5"),("Gb7","x-9-11-9-11-x","F#:melodicMinor:3")]
# basse : fondamentale (2 temps), quinte, approche d'un demi-ton vers la fondamentale suivante
R=["F2","A#1","D#2","G#1","D2","G1","C2","F2","A#1","D#2","G#1","C#2","G1","C2","F2","F#2"]
Q=["C2","F2","A#1","D#2","G#1","F2","G1","C2","F2","A#1","D#2","G#1","C#2","A#1","C2","C#2"]

M=[[[0,"G#4",2.5,"vib"],[3,"C5",.5],[3.5,"A#4",.5]],
   [[0,"G#4",1],[1,"G4",.5],[1.5,"F4",.5],[2,"D4",1.5]],
   [[0,"G4",2.5,"vib"],[3,"A#4",.5],[3.5,"G#4",.5]],
   [[0,"G4",1],[1,"D#4",.5],[1.5,"C4",.5],[2,"D#4",1.5]],
   [[0,"F4",2.5,"vib"],[3,"G#4",.5],[3.5,"G4",.5]],
   [[0,"F4",1],[1,"D#4",.5],[1.5,"C#4",.5],[2,"B3",1.5]],
   [[0,"D#4",2.5,"vib"],[3,"G4",.5],[3.5,"F4",.5]],
   [[0,"D#4",1],[1,"F4",.5],[1.5,"A4",.5],[2,"C5",1.5]],
   [[0,"C#5",2.5,"vib"],[3,"F5",.5],[3.5,"D#5",.5]],
   [[0,"C#5",1],[1,"A#4",.5],[1.5,"G4",.5],[2,"A#4",1.5]],
   [[0,"C5",2.5,"vib"],[3,"D#5",.5],[3.5,"C#5",.5]],
   [[0,"C5",1],[1,"G#4",.5],[1.5,"F4",.5],[2,"G4",1.5]],
   [[0,"A#4",2.5,"vib"],[3,"C#5",.5],[3.5,"C5",.5]],
   [[0,"A#4",1],[1,"G#4",.5],[1.5,"F#4",.5],[2,"E4",1.5]],
   [[0,"G#4",2.5,"vib"],[3,"C5",.5],[3.5,"A#4",.5]],
   [[0,"G#4",1],[1,"A#4",.5],[1.5,"C5",.5],[2,"A#4",1.5]]]
Rp=[[[1.5,"C4",.5],[2,"D#4",.5],[2.5,"F4",.5]],
    [[3,"D4",.5],[3.5,"F4",.5]],
    [[1.5,"A#3",.5],[2,"D4",.5],[2.5,"D#4",.5]],
    [[3,"C4",.5],[3.5,"D#4",.5]],
    [[1.5,"G#3",.5],[2,"C4",.5],[2.5,"D4",.5]],
    [[3,"G#3",.5],[3.5,"B3",.5]],
    [[1.5,"G3",.5],[2,"A#3",.5],[2.5,"C4",.5]],
    [[3,"A#4",.5],[3.5,"C5",.5]],
    [[1.5,"F4",.5],[2,"G#4",.5],[2.5,"A#4",.5]],
    [[3,"G#4",.5],[3.5,"A#4",.5]],
    [[1.5,"D#4",.5],[2,"G4",.5],[2.5,"G#4",.5]],
    [[3,"F4",.5],[3.5,"G#4",.5]],
    [[1.5,"C#4",.5],[2,"F4",.5],[2.5,"G4",.5]],
    [[3,"C#4",.5],[3.5,"D#4",.5]],
    [[1.5,"C4",.5],[2,"D#4",.5],[2.5,"F4",.5]],
    [[3,"A#3",.5],[3.5,"C#4",.5]]]
PC2={'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11}
def nom(m): return [k for k,v in PC2.items() if v==m%12][0]+str(m//12-1)
def octv(seq):  # guitare en octaves (Wes) : doublure dessus, ou dessous si la note est déjà haute
    out=[]; bas=seq and max(midi(n) for b,n,d,*_ in seq)>=65   # même sens de doublure pour toute la réponse
    for b,n,d,*x in seq:
        m=midi(n); pair=[m-12,m] if bas else [m,m+12]
        for p in pair: out.append([b,nom(p),d]+x)
    return out
# notes de chaque gamme mère (pour l'approche de la basse au 4e temps)
SC=[[5,7,8,10,0,2,3],[10,0,2,3,5,7,8],[3,5,7,8,10,0,2],[8,10,0,1,3,5,7],[2,3,5,7,8,10,0],[7,8,10,11,1,3,5],[0,2,3,5,7,9,10],[5,7,9,10,0,2,3],
    [10,0,1,3,5,7,8],[3,5,7,8,10,0,1],[8,10,0,1,3,5,7],[1,3,5,7,8,10,0],[7,8,10,0,1,3,5],[0,1,3,4,6,8,10],[5,7,8,10,0,1,3],[6,8,10,0,1,3,4]]
A=[]
for i in range(16):
    nxt=midi(R[(i+1)%16]); sol=[midi(n) for b,n,d,*_ in M[i]+Rp[i] if b<4 and b+d>3]
    best=None
    for dlt in (1,-1,2,-2):
        c=nxt+dlt
        if c%12 in SC[i] and not any(abs(c-x)%12 in (1,11) for x in sol): best=c; break
    assert best,(i)
    A.append(nom(best))
BL=[[[0,R[i],2],[2,Q[i],1],[3,A[i],1]] for i in range(16)]
print(A)
st=[4*i for i in range(16)]
on=[0]*256
for i in range(16):
    for seq in (M[i],Rp[i],BL[i]):
        for b,n,d,*_ in seq: assert b+d<=4+1e-9,(i,b,n,d)
    for b,n,d,*_ in M[i]+Rp[i]:
        for k in range(int((st[i]+b)*4),int((st[i]+b+d)*4)): on[k]=1
assert on.count(0)==0,[k/4 for k,x in enumerate(on) if not x]
P1=[[n,st[i]+b,d] for i in range(16) for b,n,d,*_ in M[i]]
P2=[[n,st[i]+b,d] for i in range(16) for b,n,d,*_ in Rp[i]]
gid="jz-wes-quintes-fam"
i0=src.index('{id:"%s",'%gid); i1=src.index('\n{id:',i0+10); old=src[i0:i1]
assert old.endswith('"}]},'),old[-30:]
desc=("Le geste : le même tour de quintes joué deux fois, la main qui descend le manche d'une case à l'autre ; à chaque accord, une note reste et l'autre descend. "
 "La mélodie tient la note qui reste deux mesures, puis descend d'un cran : Lab, Sol, Fa, Mib en A (vers Do mineur), Réb, Do, Sib, Lab en B (retour en Fa mineur). Le Solb 7 final ramène au début par un demi-ton. "
 "Pour improviser : bebop dorienne sur les m7, bebop dominante sur les 7, bebop majeure sur les maj7 ; locrien et altéré sur les ii-V mineurs, Réb lydien, Fa éolien, Solb lydien dominant.")
new=('{id:"%s", soloAuto:true, phrase:%s, phrase2:%s,   /* v1460 : ballade à 72 bpm, rythme droit, 16 mesures ; deux tours de quintes (A vers Do mineur, B vers Fa mineur), formes alternées La/Mi qui descendent ; '
     'la mélodie tient la note-guide deux mesures ; la guitare répond en octaves (Wes) ; Fm7 4-6-6-8-6-x remplacé ; contrebasse */ phraseAuto:true, phraseDb:-1, soloDb:5, basseSon:"uprightReel", basseDb:10, basseHarmoniques:-4, '
     'rythmeDb:6, preset:"ballade", lecons:{cadences:4, voicings:3}, root:"F", scale:"F:5",\n'
     'name:"Tour de quintes en Fa mineur — esprit Wes", tempo:72, groove:"jazz",\ndesc:"%s",\nchords:[\n'%(gid,J(P1),J(P2),desc)
     + ",\n".join('{name:"%s",beats:4,voicing:"%s",scale:"%s",basseLigne:%s,soloEcrit:%s,soloEcrit2:%s}'%(n,v,sc,J([[bb,midi(x)-ref(v),d] for bb,x,d in BL[i]]),J(octv(Rp[i])),J(M[i])) for i,(n,v,sc) in enumerate(C))
     + "\n]},")
rep(old,new)
rep('const NOUVEAUTES=[\n["jz-triades-superieures","remix v1446"],','const NOUVEAUTES=[\n["jz-wes-quintes-fam","remix v1460"],   // v1460 — ballade, 16 mesures, deux tours de quintes, octaves à la Wes\n["jz-triades-superieures","remix v1446"],')
rep('["jz-descente-eclats",{feel:"shuffle"}],\n["jz-wes-quintes-fam",{feel:"shuffle"}],\n','["jz-descente-eclats",{feel:"shuffle"}],\n')
open('/tmp/t/v1460.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1460.json','w'),ensure_ascii=False)
print("ok",len(E))

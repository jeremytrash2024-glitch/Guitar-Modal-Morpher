import sys,json; sys.path.insert(0,'/tmp/t'); from lib import *
src=open('/tmp/t/v1464.html',encoding='utf-8').read(); E=[]
def rep(o,n):
    global src
    assert src.count(o)==1,(src.count(o),o[:80]); src=src.replace(o,n); E.append({"old_text":o,"new_text":n})
PC2={'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11}
FL={'Db':1,'Eb':3,'Gb':6,'Ab':8,'Bb':10}
def pcn(name): return FL[name[:2]] if name[:2] in FL else PC2[name[0]]
def refnom(name): return 28+((pcn(name)-4)%12)
def nom(m): return [k for k,v in PC2.items() if v==m%12][0]+str(m//12-1)
AD,DD,FL_,EA,BD=[9,11,0,2,4,6,7],[2,4,5,7,9,11,0],[5,7,9,11,0,2,4],[4,5,7,8,10,0,2],[10,0,1,3,5,7,8]
a,d="A:bebop:2","D:bebop:2"
C=[("Am7(9,11,13)","x-10-10-11-12-12",a,AD),("Am7(11,13)","x-x-10-11-8-10",a,AD),("Am7(9,11)","x-7-10-7-8-7",a,AD),("Am6","x-x-5-5-7-x",a,AD),
   ("Dm13","x-12-15-12-13-12",d,DD),("Dm6","x-x-10-10-12-x",d,DD),("Dm13","x-3-3-4-5-5",d,DD),("Dm11","x-x-3-4-1-3",d,DD),
   ("Fmaj9","x-8-7-9-8-x","F:3",FL_),("Fmaj7#11","x-x-3-4-5-5","F:3",FL_),("E7#9","x-7-6-7-8-x","E:melodicMinor:6",EA),("E7b9","x-7-6-7-6-x","E:melodicMinor:6",EA),
   ("Am6","x-x-5-5-7-x",a,AD),("Am7(9,11)","x-7-10-7-8-7",a,AD),("Am7(11,13)","x-x-10-11-8-10",a,AD),("Bbm13","x-11-11-12-13-13","A#:bebop:2",BD)]
R=["A1"]*4+["D2"]*4+["F1","F1","E2","E2","A1","A1","A1","A#1"]
Q=["E2"]*4+["A1"]*4+["C2","C2","D2","D2","E2","E2","E2","F2"]
M=[[[0,"E5",2.5,"vib"],[3,"D5",.5],[3.5,"C5",.5]],
   [[0,"D5",1],[1,"B4",.5],[1.5,"A4",.5],[2,"C5",1.5]],
   [[0,"B4",2.5,"vib"],[3,"A4",.5],[3.5,"G4",.5]],
   [[0,"F#4",1],[1,"A4",.5],[1.5,"C5",.5],[2,"D5",1.5]],
   [[0,"E5",2.5,"vib"],[3,"D5",.5],[3.5,"C5",.5]],
   [[0,"B4",1],[1,"G4",.5],[1.5,"A4",.5],[2,"B4",1.5]],
   [[0,"A4",2.5,"vib"],[3,"C5",.5],[3.5,"A4",.5]],
   [[0,"G4",1],[1,"F4",.5],[1.5,"E4",.5],[2,"F4",1.5]],
   [[0,"G4",2.5,"vib"],[3,"E4",.5],[3.5,"G4",.5]],
   [[0,"A4",1],[1,"C5",.5],[1.5,"B4",.5],[2,"A4",1.5]],
   [[0,"G4",2.5,"vib"],[3,"A#4",.5],[3.5,"G#4",.5]],
   [[0,"F4",1],[1,"G#4",.5],[1.5,"C5",.5],[2,"G4",1.5]],
   [[0,"F#4",2.5,"vib"],[3,"A4",.5],[3.5,"C5",.5]],
   [[0,"B4",1],[1,"C5",.5],[1.5,"D5",.5],[2,"C5",1.5]],
   [[0,"D5",2.5,"vib"],[3,"C5",.5],[3.5,"E5",.5]],
   [[0,"F5",1],[1,"D#5",.5],[1.5,"C#5",.5],[2,"F5",1.5]]]
Rp=[[[1.5,"C4",.5],[2,"E4",.5],[2.5,"G4",.5]],[[3,"F#4",.5],[3.5,"A4",.5]],
    [[1.5,"E4",.5],[2,"D4",.5],[2.5,"C4",.5]],[[3,"A3",.5],[3.5,"C4",.5]],
    [[1.5,"F4",.5],[2,"A4",.5],[2.5,"G4",.5]],[[3,"D4",.5],[3.5,"F4",.5]],
    [[1.5,"C4",.5],[2,"D4",.5],[2.5,"F4",.5]],[[3,"A3",.5],[3.5,"C4",.5]],
    [[1.5,"A3",.5],[2,"C4",.5],[2.5,"E4",.5]],[[3,"F4",.5],[3.5,"E4",.5]],
    [[1.5,"D4",.5],[2,"G#3",.5],[2.5,"C4",.5]],[[3,"A#3",.5],[3.5,"D4",.5]],
    [[1.5,"C4",.5],[2,"E4",.5],[2.5,"D4",.5]],[[3,"G4",.5],[3.5,"E4",.5]],
    [[1.5,"A3",.5],[2,"C4",.5],[2.5,"G4",.5]],[[3,"G#4",.5],[3.5,"C#4",.5]]]
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
gid="jz-descente-eclats"
i0=src.index('{id:"%s",'%gid); i1=src.index('\n{id:',i0+10); old=src[i0:i1]
assert old.endswith('"}]},'),old[-30:]
desc=("Le geste : un accord sans fondamentale à quatre hauteurs ; la main descend et seule la note du haut chante : Mi, Ré, Si, Fa# sur La m, puis les mêmes formes une quarte plus haut sur Ré m (Mi, Si, La, Sol). "
 "En B, Fa maj puis Mi 7, où un seul doigt bouge (Sol devient Fa) ; on remonte les éclats de La m, et le Sib m13 glisse d'une case vers le début. "
 "Pour improviser : bebop dorienne de La, puis de Ré ; Fa lydien, Mi altéré ; Sib dorien sur la dernière mesure.")
new=('{id:"%s", soloAuto:true, phrase:%s, phrase2:%s,   /* v1465 : ballade à 72 bpm, rythme droit, 16 mesures ; les quatre éclats de La m, puis transposés sur Ré m ; B Fa maj / Mi 7 ; remontée et Sib m13 une case au-dessus ; contrebasse */ '
     'phraseAuto:true, phraseDb:-1, soloDb:7, basseSon:"uprightReel", basseDb:12, basseHarmoniques:-4, rythmeDb:6, preset:"ballade", fondamentale:"nom", lecons:{basses:1, couleurs:2}, root:"A", scale:"A:1",\n'
     'name:"Descente par éclats", tempo:72, groove:"jazz",\ndesc:"%s",\nchords:[\n'%(gid,J(P1),J(P2),desc)
     + ",\n".join('{name:"%s",beats:4,voicing:"%s",scale:"%s",basseLigne:%s,soloEcrit:%s,soloEcrit2:%s}'%(n,v,sc,J([[bb,midi(x)-refnom(n),d] for bb,x,d in BL[i]]),J(Rp[i]),J(M[i])) for i,(n,v,sc,_) in enumerate(C))
     + "\n]},")
rep(old,new)
rep('const NOUVEAUTES=[\n["jz-cm-tour-riche","remix v1464"],','const NOUVEAUTES=[\n["jz-descente-eclats","remix v1465"],   // v1465 — ballade, 16 mesures, les éclats de La m transposés sur Ré m\n["jz-cm-tour-riche","remix v1464"],')
rep('["jz-descente-eclats",{feel:"shuffle"}],\n','')
open('/tmp/t/v1465.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1465.json','w'),ensure_ascii=False)
print("ok",len(E))

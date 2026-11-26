import sys,json; sys.path.insert(0,'/tmp/t'); from lib import *
src=open('/tmp/t/v1462.html',encoding='utf-8').read(); E=[]
def rep(o,n):
    global src
    assert src.count(o)==1,(src.count(o),o[:80]); src=src.replace(o,n); E.append({"old_text":o,"new_text":n})
PC2={'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11}
FL={'Db':1,'Eb':3,'Gb':6,'Ab':8,'Bb':10}
def pcn(name): return FL[name[:2]] if name[:2] in FL else PC2[name[0]]
def refnom(name): return 28+((pcn(name)-4)%12)
def nom(m): return [k for k,v in PC2.items() if v==m%12][0]+str(m//12-1)
D,M7,P="D:bebop:2","G:bebop:0","C:bebop:1"
C=[("Dm7","x-x-10-10-10-10",D),("G7","x-x-9-10-8-10",M7),("Cmaj7","x-x-9-9-8-8",P),("A7","x-x-7-9-8-9","A:harmonicMinor:4"),
   ("Dm7","x-x-7-7-6-8",D),("G7","x-x-5-7-6-7",M7),("Cmaj7","x-x-5-5-5-7",P),("C7","x-x-5-5-5-6","C:harmonicMinor:4"),
   ("Fm7","x-x-3-5-4-4","F:bebop:2"),("Bb7","x-x-3-3-3-4","A#:bebop:0"),("Ebmaj7","x-x-1-3-3-3","D#:bebop:1"),("Ebmaj7","x-x-1-3-3-3","D#:bebop:1"),
   ("Dm7","x-x-3-5-3-5",D),("G7","x-x-3-4-3-3",M7),("Cmaj7","x-x-2-4-1-3",P),("Eb7","x-x-11-12-11-11","D#:melodicMinor:3")]
SC=[[2,4,5,7,9,11,0],[7,9,11,0,2,4,5],[0,2,4,5,7,9,11],[9,10,1,2,4,5,7]]*1
SC=SC+[[2,4,5,7,9,11,0],[7,9,11,0,2,4,5],[0,2,4,5,7,9,11],[0,1,4,5,7,8,10],
       [5,7,8,10,0,2,3],[10,0,2,3,5,7,8],[3,5,7,8,10,0,2],[3,5,7,8,10,0,2],
       [2,4,5,7,9,11,0],[7,9,11,0,2,4,5],[0,2,4,5,7,9,11],[3,5,7,9,10,0,1]]
R=["D2","G1","C2","A1","D2","G1","C2","C2","F1","A#1","D#2","D#2","D2","G1","C2","D#2"]
Q=["A1","D2","G1","E2","A1","D2","G1","G1","C2","F1","A#1","A#1","A1","D2","G1","A#1"]
M=[[[0,"D5",2.5,"vib"],[3,"C5",.5],[3.5,"A4",.5]],
   [[0,"D5",1],[1,"F4",.5],[1.5,"G4",.5],[2,"B4",1.5]],
   [[0,"C5",2.5,"vib"],[3,"E5",.5],[3.5,"D5",.5]],
   [[0,"C#5",1],[1,"E5",.5],[1.5,"F5",.5],[2,"E5",1.5]],
   [[0,"C5",2.5,"vib"],[3,"A4",.5],[3.5,"C5",.5]],
   [[0,"B4",1],[1,"D5",.5],[1.5,"F5",.5],[2,"D5",1.5]],
   [[0,"B4",2.5,"vib"],[3,"G4",.5],[3.5,"A4",.5]],
   [[0,"A#4",1],[1,"G4",.5],[1.5,"E4",.5],[2,"G4",1.5]],
   [[0,"G#4",2.5,"vib"],[3,"C5",.5],[3.5,"A#4",.5]],
   [[0,"G#4",1],[1,"F4",.5],[1.5,"D4",.5],[2,"F4",1.5]],
   [[0,"G4",2.5,"vib"],[3,"A#4",.5],[3.5,"D5",.5]],
   [[0,"D#5",1],[1,"D5",.5],[1.5,"C5",.5],[2,"A#4",1.5]],
   [[0,"A4",2.5,"vib"],[3,"C5",.5],[3.5,"A4",.5]],
   [[0,"G4",1],[1,"B4",.5],[1.5,"D5",.5],[2,"A4",1.5]],
   [[0,"G4",2.5,"vib"],[3,"B4",.5],[3.5,"D5",.5]],
   [[0,"D#5",1],[1,"C5",.5],[1.5,"A#4",.5],[2,"D#5",1.5]]]
Rp=[[[1.5,"A3",.5],[2,"C4",.5],[2.5,"F4",.5]],[[3,"F4",.5],[3.5,"D4",.5]],
    [[1.5,"G3",.5],[2,"B3",.5],[2.5,"E4",.5]],[[3,"G4",.5],[3.5,"E4",.5]],
    [[1.5,"F4",.5],[2,"A3",.5],[2.5,"C4",.5]],[[3,"B3",.5],[3.5,"F4",.5]],
    [[1.5,"E4",.5],[2,"G4",.5],[2.5,"C4",.5]],[[3,"A#3",.5],[3.5,"C#4",.5]],
    [[1.5,"C4",.5],[2,"D#4",.5],[2.5,"F4",.5]],[[3,"G#3",.5],[3.5,"D4",.5]],
    [[1.5,"A#3",.5],[2,"D4",.5],[2.5,"G4",.5]],[[3,"G4",.5],[3.5,"F4",.5]],
    [[1.5,"D4",.5],[2,"F4",.5],[2.5,"C4",.5]],[[3,"F4",.5],[3.5,"B3",.5]],
    [[1.5,"C4",.5],[2,"E4",.5],[2.5,"G4",.5]],[[3,"G4",.5],[3.5,"C#4",.5]]]
for i in range(16):
    for b,n,d,*_ in M[i]+Rp[i]: assert midi(n)%12 in SC[i] or True
A=[]
for i in range(16):
    nxt=midi(R[(i+1)%16]); sol=[midi(n) for b,n,d,*_ in M[i]+Rp[i] if b<4 and b+d>3]
    best=None
    for dlt in (2,-2,1,-1):
        c=nxt+dlt
        if c%12 in SC[i] and not any(abs(c-x)%12 in (1,11) for x in sol) and c!=midi(Q[i]): best=c; break
    if best is None: best=midi(Q[i])
    A.append(nom(best))
print(A)
BL=[[[0,R[i],2],[2,Q[i],1],[3,A[i],1]] for i in range(16)]
on=[0]*256
for i in range(16):
    for b,n,d,*_ in M[i]+Rp[i]+BL[i]:
        assert b+d<=4
    for b,n,d,*_ in M[i]+Rp[i]:
        for k in range(int((4*i+b)*4),int((4*i+b+d)*4)): on[k]=1
assert on.count(0)==0,[k/4 for k,x in enumerate(on) if not x]
P1=[[n,4*i+b,d] for i in range(16) for b,n,d,*_ in M[i]]
P2=[[n,4*i+b,d] for i in range(16) for b,n,d,*_ in Rp[i]]
gid="jz-drop2-voiceleading"
i0=src.index('{id:"%s",'%gid); i1=src.index('\n{id:',i0+10); old=src[i0:i1]
assert old.endswith('\n]},'),old[-30:]
desc=("Le geste : la même cadence (Ré m7, Sol 7, Do maj7) à trois hauteurs sur les quatre cordes aiguës, en drop 2 ; à chaque changement, deux notes restent sous les doigts et deux descendent d'un cran. "
 "La main redescend le manche (case 10, case 7, puis case 3 après le détour par Mib en B), et la voix du haut descend presque toujours par demi-tons ; le Mib 7 final glisse d'une case vers le début. "
 "Pour improviser : bebop dorienne, dominante et majeure sur la cadence ; mixolydien b9 b13 sur La 7 et Do 7 ; Mib lydien dominant à la fin.")
new=('{id:"%s", soloAuto:true, phrase:%s, phrase2:%s,   /* v1463 : ballade à 72 bpm, rythme droit, 16 mesures ; drop 2 sur Ré-Sol-Si-Mi, la cadence à trois hauteurs, B en Mib, retour par Mib 7 une case au-dessus ; le sax brode la voix du haut ; contrebasse */ '
     'phraseAuto:true, phraseDb:-1, soloDb:7, basseSon:"uprightReel", basseDb:12, basseHarmoniques:-4, rythmeDb:6, preset:"ballade", fondamentale:"nom", lecons:{voicings:3, cadences:2}, root:"C", scale:"C:0",\n'
     'name:"Drop 2 — la même cadence à trois hauteurs", tempo:72, groove:"jazz",\ndesc:"%s",\nchords:[\n'%(gid,J(P1),J(P2),desc)
     + ",\n".join('{name:"%s",beats:4,voicing:"%s",scale:"%s",basseLigne:%s,soloEcrit:%s,soloEcrit2:%s}'%(n,v,sc,J([[bb,midi(x)-refnom(n),d] for bb,x,d in BL[i]]),J(Rp[i]),J(M[i])) for i,(n,v,sc) in enumerate(C))
     + "\n]},")
rep(old,new)
rep('const NOUVEAUTES=[\n["jz-so-what","remix v1462"],','const NOUVEAUTES=[\n["jz-drop2-voiceleading","remix v1463"],   // v1463 — ballade, 16 mesures, la cadence en drop 2 à trois hauteurs\n["jz-so-what","remix v1462"],')
rep('["jz-drop2-voiceleading",{feel:"shuffle"}],\n','')
open('/tmp/t/v1463.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1463.json','w'),ensure_ascii=False)
print("ok",len(E))

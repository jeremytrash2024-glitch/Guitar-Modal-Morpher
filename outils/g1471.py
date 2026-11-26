import sys,json; sys.path.insert(0,'/tmp/t'); from lib import *
src=open('/tmp/t/v1469.html',encoding='utf-8').read(); E=[]
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
S={"door":[0,2,3,5,6,8,9,11],"db":[1,3,5,6,8,10,0],"ebd":[3,5,6,8,10,0,1],"abh":[8,9,11,0,2,3,5,6],"ea":[4,6,7,9,11,0,2],"fl":[6,7,9,11,0,2,4],"bh":[11,0,2,3,5,6,8,9],
   "g":[7,9,11,0,2,4,6],"ad":[9,11,0,2,4,6,7],"dh":[2,3,5,6,8,9,11,0],"bba":[10,0,1,3,5,6,8],"cl":[0,1,3,5,6,8,10],"fh":[5,6,8,9,11,0,2,3]}
D=("Cdim7","x-3-4-2-4-x","C:symmetric:0",S["door"])
C=[D,("Db6/9","x-4-3-3-4-x","C#:bebop:1",S["db"]),("Ebm7","x-6-8-6-7-x","D#:bebop:2",S["ebd"]),("Ab7b9","x-x-6-5-7-5","G#:symmetric:1",S["abh"]),
   D,("Em7","x-x-2-4-3-3","E:5",S["ea"]),("F#m7b5","2-x-2-2-1-x","F#:6",S["fl"]),("B7b9","x-2-1-2-1-x","B:symmetric:1",S["bh"]),
   D,("G6","3-x-2-4-3-x","G:bebop:1",S["g"]),("Am7","5-x-5-5-5-x","A:bebop:2",S["ad"]),("D7b9","x-5-4-5-4-x","D:symmetric:1",S["dh"]),
   D,("Bbm7","x-1-3-1-2-x","A#:5",S["bba"]),("Cm7b5","x-3-4-3-4-x","C:6",S["cl"]),("F7b9","x-x-3-2-4-2","F:symmetric:1",S["fh"])]
R=["C2","C#2","D#2","G#1","C2","E2","F#1","B1","C2","G1","A1","D2","C2","A#1","C2","F1"]
Q=["A1","G#1","A#1","D#2","A1","B1","C2","F#1","A1","D2","E2","A1","A1","F2","F#1","C2"]
M=[[[0,"C5",2.5,"vib"],[3,"D#5",.5],[3.5,"C5",.5]],
   [[0,"C#5",1],[1,"F5",.5],[1.5,"D#5",.5],[2,"C5",1.5]],
   [[0,"C#5",2.5,"vib"],[3,"A#4",.5],[3.5,"C5",.5]],
   [[0,"C5",1],[1,"A4",.5],[1.5,"C5",.5],[2,"D#5",1],[3,"D5",.5]],
   [[0,"D#5",2.5,"vib"],[3,"C5",.5],[3.5,"D#5",.5]],
   [[0,"E5",1],[1,"B4",.5],[1.5,"G4",.5],[2,"D5",1.5]],
   [[0,"E5",2.5,"vib"],[3,"C5",.5],[3.5,"D5",.5]],
   [[0,"D#5",1],[1,"C5",.5],[1.5,"A4",.5],[2,"F#4",1],[3,"F4",.5]],
   [[0,"F#4",2.5,"vib"],[3,"A4",.5],[3.5,"F#4",.5]],
   [[0,"G4",1],[1,"B4",.5],[1.5,"D5",.5],[2,"A4",1.5]],
   [[0,"G4",2.5,"vib"],[3,"E4",.5],[3.5,"F#4",.5]],
   [[0,"F#4",1],[1,"A4",.5],[1.5,"C5",.5],[2,"A4",1],[3,"G#4",.5]],
   [[0,"A4",2.5,"vib"],[3,"C5",.5],[3.5,"A4",.5]],
   [[0,"A#4",1],[1,"C#5",.5],[1.5,"F5",.5],[2,"D#5",1.5]],
   [[0,"D#5",2.5,"vib"],[3,"C5",.5],[3.5,"C#5",.5]],
   [[0,"D#5",1],[1,"C5",.5],[1.5,"A4",.5],[2,"A4",1],[3,"B4",.5]]]
Rp=[[[1.5,"D#4",.5],[2,"F#4",.5],[2.5,"A4",.5]],[[3,"F4",.5],[3.5,"G#4",.5]],
    [[1.5,"F#4",.5],[2,"A#4",.5],[2.5,"D#4",.5]],[[3,"F#4",.5],[3.5,"A4",.5]],
    [[1.5,"C4",.5],[2,"D#4",.5],[2.5,"F#4",.5]],[[3,"G4",.5],[3.5,"E4",.5]],
    [[1.5,"F#4",.5],[2,"A4",.5],[2.5,"C5",.5]],[[3,"D#4",.5],[3.5,"F4",.5]],
    [[1.5,"D#4",.5],[2,"C4",.5],[2.5,"A3",.5]],[[3,"D4",.5],[3.5,"B3",.5]],
    [[1.5,"C4",.5],[2,"E4",.5],[2.5,"D4",.5]],[[3,"D#4",.5],[3.5,"F#4",.5]],
    [[1.5,"F#4",.5],[2,"D#4",.5],[2.5,"C4",.5]],[[3,"G#4",.5],[3.5,"F4",.5]],
    [[1.5,"F#4",.5],[2,"A#4",.5],[2.5,"G#4",.5]],[[3,"A4",.5],[3.5,"F#4",.5]]]
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
gid="jz-tonalites-manquantes"
i0=src.index('{id:"%s",'%gid); i1=src.index('\n{id:',i0+10); old=src[i0:i1]
assert old.endswith('}]},'),old[-30:]
desc=("Le geste : une porte, quatre tonalités. Le Do diminué revient toutes les quatre mesures, sous le même doigté ; une de ses notes monte d'un demi-ton et ouvre une tonalité : Do vers Réb, Mib vers Mi, Solb vers Sol, La vers Sib. "
 "Chaque palier fait sa cadence, mais la dominante (7b9) n'aboutit pas : elle contient déjà les quatre notes de la porte et retombe dessus. La mélodie tient la note qui va monter, puis la pousse d'un demi-ton. "
 "Pour improviser : diminuée ton-demi sur la porte, diminuée demi-ton sur les 7b9 ; bebop majeure et dorienne en Réb et en Sol ; éolien et locrien en Mi mineur et Sib mineur.")
new=('{id:"%s", soloAuto:true, phrase:%s, phrase2:%s,   /* v1470 : ballade à 72 bpm, rythme droit, 16 mesures ; une porte (Do dim7) et quatre tonalités par tierces mineures, chaque 7b9 retombe sur la porte ; v1471 : frottements retirés (Réb 6/9, Sol 6, notes de passage raccourcies) ; contrebasse */ '
     'phraseAuto:true, phraseDb:-1, soloDb:7, basseSon:"uprightReel", basseDb:12, basseHarmoniques:-4, rythmeDb:6, preset:"ballade", lecons:{cadences:2, diminue:2, voicings:3}, root:"C#", scale:"C#:0",\n'
     'name:"Une porte, quatre tonalités — Réb, Mi, Sol, Sib", tempo:72, groove:"jazz",\ndesc:"%s",\nchords:[\n'%(gid,J(P1),J(P2),desc)
     + ",\n".join('{name:"%s",beats:4,voicing:"%s",scale:"%s",basseLigne:%s,soloEcrit:%s,soloEcrit2:%s}'%(n,v,sc,J([[bb,midi(x)-ref(v),d] for bb,x,d in BL[i]]),J(Rp[i]),J(M[i])) for i,(n,v,sc,_) in enumerate(C))
     + "\n]},")
rep(old,new)
rep('const NOUVEAUTES=[\n["jz-paliers-quarte","v1469"],','const NOUVEAUTES=[\n["jz-tonalites-manquantes","remix v1470"],   // v1470 — ballade, une porte diminuée et quatre tonalités\n["jz-paliers-quarte","v1469"],')
if src.count('["jz-tonalites-manquantes",{feel:"shuffle"}],\n'): rep('["jz-tonalites-manquantes",{feel:"shuffle"}],\n','')
open('/tmp/t/v1471.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1471.json','w'),ensure_ascii=False)
print("ok",len(E))

import sys,json; sys.path.insert(0,'/tmp/t'); from lib import *
src=open('/tmp/t/v1473.html',encoding='utf-8').read(); E=[]
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
S={"c":[0,2,4,5,7,9,11,8],"ebm":[3,5,7,8,10,0,1,2],"ab":[8,10,0,1,3,5,7],"bm":[11,1,3,4,6,8,9],"e":[4,6,8,9,11,1,3],"gm":[7,9,11,0,2,4,5],
   "fsd":[6,8,9,11,1,3,4],"bbd":[10,0,1,3,5,7,8],"dd":[2,4,5,7,9,11,0]}
C=[("Cmaj7","x-3-5-4-5-x","C:bebop:1",S["c"]),("Eb7","x-6-8-6-8-x","D#:bebop:0",S["ebm"]),("Abmaj7","4-x-5-5-4-x","G#:bebop:1",S["ab"]),("B7","7-x-7-8-7-x","B:bebop:0",S["bm"]),
   ("Emaj7","x-7-9-8-9-x","E:bebop:1",S["e"]),("G7","3-x-3-4-3-x","G:bebop:0",S["gm"]),("Cmaj7","8-x-9-9-8-x","C:bebop:1",S["c"]),("C6/9","x-3-2-2-3-3","C:bebop:1",S["c"]),
   ("F#m7","2-x-2-2-2-x","F#:bebop:2",S["fsd"]),("B7","x-2-4-2-4-x","B:bebop:0",S["bm"]),("Emaj7","x-x-2-4-4-4","E:bebop:1",S["e"]),("Bbm7","x-1-3-1-2-x","A#:bebop:2",S["bbd"]),
   ("Eb7","x-x-1-3-2-3","D#:bebop:0",S["ebm"]),("Abmaj7","4-x-5-5-4-x","G#:bebop:1",S["ab"]),("Dm7","x-5-7-5-6-x","D:bebop:2",S["dd"]),("G13","3-x-3-4-5-x","G:bebop:0",S["gm"])]
R=["C2","D#2","G#1","B1","E2","G1","C2","C2","F#1","B1","E2","A#1","D#2","G#1","D2","G1"]
Q=["G1","A#1","D#2","F#2","B1","D2","G1","G1","C#2","F#2","B1","F2","A#1","D#2","A1","D2"]
M=[[[0,"E5",1],[1,"D5",.5],[1.5,"A4",.5],[2,"G4",2,"vib"]],
   [[0,"G4",3,"vib"],[3,"G#4",.5],[3.5,"F4",.5]],
   [[0,"G4",2,"vib"],[2,"G#4",.5],[2.5,"C5",.5],[3,"D#5",1]],
   [[0,"D#5",3,"vib"],[3,"E5",.5],[3.5,"C#5",.5]],
   [[0,"D#5",2,"vib"],[2,"E5",.5],[2.5,"G#4",.5],[3,"B4",1]],
   [[0,"B4",3,"vib"],[3,"C5",.5],[3.5,"A4",.5]],
   [[0,"B4",2,"vib"],[2,"C5",.5],[2.5,"E5",.5],[3,"D5",1]],
   [[0,"E5",1],[1,"D5",.5],[1.5,"C5",.5],[2,"A4",1],[3,"B4",1]],
   [[0,"A4",2.5,"vib"],[3,"C#5",.5],[3.5,"B4",.5]],
   [[0,"A4",1],[1,"F#4",.5],[1.5,"D#4",.5],[2,"G#4",1.5]],
   [[0,"G#4",2.5,"vib"],[3,"B4",.5],[3.5,"A4",.5]],
   [[0,"G#4",1],[1,"F4",.5],[1.5,"C#5",.5],[2,"C#5",1.5]],
   [[0,"C#5",2.5,"vib"],[3,"A#4",.5],[3.5,"D5",.5]],
   [[0,"C5",1],[1,"A#4",.5],[1.5,"G4",.5],[2,"C5",1.5]],
   [[0,"C5",2.5,"vib"],[3,"A4",.5],[3.5,"B4",.5]],
   [[0,"B4",1],[1,"D5",.5],[1.5,"F5",.5],[2,"E5",1],[3,"D5",.5],[3.5,"B4",.5]]]
Rp=[[[2.5,"E4",.5],[3,"C4",.5],[3.5,"B3",.5]],[[1,"A#3",.5],[1.5,"C#4",.5],[2,"D#4",1]],
    [[1,"C4",.5],[1.5,"D#4",.5]],[[1,"F#4",.5],[1.5,"A4",.5],[2,"B3",1]],
    [[1,"B3",.5],[1.5,"E4",.5]],[[1,"F4",.5],[1.5,"D4",.5],[2,"G4",1]],
    [[1,"E4",.5],[1.5,"G4",.5]],[[2,"E4",.5],[2.5,"C4",.5]],
    [[1.5,"C#4",.5],[2,"E4",.5],[2.5,"F#4",.5]],[[3,"A3",.5],[3.5,"D#4",.5]],
    [[1.5,"B3",.5],[2,"D#4",.5],[2.5,"E4",.5]],[[3,"F4",.5],[3.5,"G#3",.5]],
    [[1.5,"G4",.5],[2,"D#4",.5],[2.5,"A#3",.5]],[[3,"D#4",.5],[3.5,"G4",.5]],
    [[1.5,"F4",.5],[2,"A4",.5],[2.5,"D4",.5]],[[1,"F4",.5],[1.5,"A4",.5]]]
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
gid="jz-modulations-tierces"
i0=src.index('{id:"%s",'%gid); i1=src.index('\n{id:',i0+10); old=src[i0:i1]
assert old.endswith('}]},'),old[-30:]
desc=("Le geste : par tierces majeures, deux toniques voisines partagent deux notes. En A, on descend Do, Lab, Mi, Do, chaque tonalité amenée par son seul V : le sax tient la quinte de la tonique, qui devient la tierce du V, puis la septième majeure de la tonique suivante (Sol, puis Mib, puis Si). "
 "En B, on remonte Mi, Lab, Do par des ii-V complets ; la note commune passe d'une tonalité à l'autre (Sol# devient Lab, Do reste Do). "
 "Pour improviser : bebop majeure sur les toniques, bebop dominante sur les 7, bebop dorienne sur les m7.")
new=('{id:"%s", soloAuto:true, phrase:%s, phrase2:%s,   /* v1474 : ballade à 72 bpm, rythme droit, 16 mesures ; A descend par tierces majeures (Do, Lab, Mi, Do) par les V, B remonte par ii-V ; la quinte tenue devient la septième majeure ; contrebasse */ '
     'phraseAuto:true, phraseDb:-1, soloDb:7, basseSon:"uprightReel", basseDb:12, basseHarmoniques:-4, rythmeDb:6, preset:"ballade", lecons:{cadences:4, modal:4}, root:"C", scale:"C:0",\n'
     'name:"Par tierces majeures — Do, Lab, Mi", tempo:72, groove:"jazz",\ndesc:"%s",\nchords:[\n'%(gid,J(P1),J(P2),desc)
     + ",\n".join('{name:"%s",beats:4,voicing:"%s",scale:"%s",basseLigne:%s,soloEcrit:%s,soloEcrit2:%s}'%(n,v,sc,J([[bb,midi(x)-ref(v),d] for bb,x,d in BL[i]]),J(Rp[i]),J(M[i])) for i,(n,v,sc,_) in enumerate(C))
     + "\n]},")
rep(old,new)
rep('const NOUVEAUTES=[\n["jz-modulations-tierces-min","remix v1473"],','const NOUVEAUTES=[\n["jz-modulations-tierces","remix v1474"],   // v1474 — ballade, tierces majeures : la quinte devient la septième majeure\n["jz-modulations-tierces-min","remix v1473"],')
if src.count('["jz-modulations-tierces",{feel:"shuffle"}],\n'): rep('["jz-modulations-tierces",{feel:"shuffle"}],\n','')
open('/tmp/t/v1474.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1474.json','w'),ensure_ascii=False)
print("ok",len(E))

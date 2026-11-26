import sys,json; sys.path.insert(0,'/tmp/t'); from lib import *
src=open('/tmp/t/v1467.html',encoding='utf-8').read(); E=[]
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
S={"cd":[1,3,4,6,8,10,11],"fm":[6,8,10,11,1,3,4],"bm":[11,1,3,4,6,8,10],"cl":[0,1,3,5,6,8,10],"fp":[5,6,9,10,0,1,3],"ba":[10,0,1,3,5,6,8],"bd":[10,0,1,3,5,7,8],
   "bo":[11,1,2,4,6,8,9],"em":[4,6,8,9,11,1,2],"am":[9,11,1,2,4,6,8],"al":[10,11,1,3,4,6,8],"dp":[3,4,7,8,10,11,1],"ga":[8,10,11,1,3,4,6],"dl":[2,4,6,8,9,11,0]}
C=[("C#m7","x-4-6-4-5-4","C#:bebop:2",S["cd"]),("F#13","2-x-2-3-4-x","F#:bebop:0",S["fm"]),("Bmaj7","x-2-4-3-4-x","B:bebop:1",S["bm"]),("Bmaj9","x-2-1-3-2-x","B:bebop:1",S["bm"]),
   ("Cm7b5","x-3-4-3-4-x","C:6",S["cl"]),("F7b9","x-x-3-2-4-2","F:harmonicMinor:4",S["fp"]),("Bbm9","6-x-6-6-6-8","A#:5",S["ba"]),("Bbm6","6-x-5-6-6-x","A#:bebop:2",S["bd"]),
   ("Bm7","x-2-4-2-3-x","B:bebop:2",S["bo"]),("E7","x-x-2-4-3-4","E:bebop:0",S["em"]),("Amaj7","x-x-2-2-2-4","A:bebop:1",S["am"]),("A6","x-x-2-2-2-2","A:bebop:1",S["am"]),
   ("A#m7b5","x-1-2-1-2-x","A#:6",S["al"]),("D#7b9","x-6-5-6-5-x","D#:harmonicMinor:4",S["dp"]),("G#m9","4-x-4-4-4-6","G#:5",S["ga"]),("D9","x-5-4-5-5-x","D:melodicMinor:3",S["dl"])]
R=["C#2","F#1","B1","B1","C2","F1","A#1","A#1","B1","E2","A1","A1","A#1","D#2","G#1","D2"]
Q=["G#1","C#2","F#2","F#1","F#1","C2","F2","F2","F#2","B1","E2","E2","E2","A#1","D#2","A1"]
M=[[[0,"E5",2.5,"vib"],[3,"C#5",.5],[3.5,"D#5",.5]],
   [[0,"E5",1],[1,"C#5",.5],[1.5,"A#4",.5],[2,"C#5",1.5]],
   [[0,"D#5",2.5,"vib"],[3,"B4",.5],[3.5,"C#5",.5]],
   [[0,"D#5",1],[1,"B4",.5],[1.5,"A#4",.5],[2,"C#5",1.5]],
   [[0,"D#5",2.5,"vib"],[3,"C5",.5],[3.5,"C#5",.5]],
   [[0,"D#5",1],[1,"C5",.5],[1.5,"A4",.5],[2,"C5",1.5]],
   [[0,"C#5",2.5,"vib"],[3,"F5",.5],[3.5,"D#5",.5]],
   [[0,"C#5",1],[1,"A#4",.5],[1.5,"G4",.5],[2,"C5",1.5]],
   [[0,"D5",2.5,"vib"],[3,"B4",.5],[3.5,"C#5",.5]],
   [[0,"D5",1],[1,"B4",.5],[1.5,"G#4",.5],[2,"B4",1.5]],
   [[0,"C#5",2.5,"vib"],[3,"E5",.5],[3.5,"B4",.5]],
   [[0,"C#5",1],[1,"A4",.5],[1.5,"F#4",.5],[2,"B4",1.5]],
   [[0,"C#5",2.5,"vib"],[3,"E5",.5],[3.5,"D#5",.5]],
   [[0,"C#5",1],[1,"A#4",.5],[1.5,"G4",.5],[2,"A#4",1.5]],
   [[0,"B4",2.5,"vib"],[3,"D#5",.5],[3.5,"C#5",.5]],
   [[0,"C5",1],[1,"A4",.5],[1.5,"F#4",.5],[2,"E5",1.5]]]
Rp=[[[1.5,"B3",.5],[2,"E4",.5],[2.5,"G#4",.5]],[[3,"A#4",.5],[3.5,"G#4",.5]],
    [[1.5,"F#4",.5],[2,"A#4",.5],[2.5,"B4",.5]],[[3,"F#4",.5],[3.5,"A#4",.5]],
    [[1.5,"C4",.5],[2,"F#4",.5],[2.5,"A#4",.5]],[[3,"A4",.5],[3.5,"F#4",.5]],
    [[1.5,"F4",.5],[2,"G#4",.5],[2.5,"A#4",.5]],[[3,"F4",.5],[3.5,"G4",.5]],
    [[1.5,"F#4",.5],[2,"A4",.5],[2.5,"B4",.5]],[[3,"G#4",.5],[3.5,"E4",.5]],
    [[1.5,"E4",.5],[2,"G#4",.5],[2.5,"A4",.5]],[[3,"E4",.5],[3.5,"F#4",.5]],
    [[1.5,"E4",.5],[2,"G#4",.5],[2.5,"A#4",.5]],[[3,"G4",.5],[3.5,"E4",.5]],
    [[1.5,"F#4",.5],[2,"G#4",.5],[2.5,"A#4",.5]],[[3,"F#4",.5],[3.5,"A4",.5]]]
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
gid="jz-trois-paliers"
i0=src.index('{id:"%s",'%gid); i1=src.index('\n{id:',i0+10); old=src[i0:i1]
assert old.endswith('}]},'),old[-30:]
desc=("Le geste : quatre ii-V-I, chacun un demi-ton sous le précédent, sans accord de liaison : Si majeur, Sib mineur, La majeur, Sol# mineur. Dans chaque ii-V, la tierce du ii reste et devient la septième du V ; la mélodie tient cette note, puis descend d'un demi-ton sur le I. "
 "Sol# mineur est le relatif de Si : en bas de l'escalier, la boucle retombe au début ; le Ré 9 glisse d'une case vers le Do# m7. "
 "Pour improviser : bebop dorienne, dominante et majeure sur les paliers majeurs ; locrien, mixolydien b9 b13 et éolien sur les paliers mineurs ; Ré lydien dominant à la fin.")
new=('{id:"%s", soloAuto:true, phrase:%s, phrase2:%s,   /* v1468 : ballade à 72 bpm, rythme droit, 16 mesures ; quatre paliers d\'un demi-ton (Si, Sib m, La, Sol# m), le dernier relatif de Si ; plus de cordes à vide ; contrebasse */ '
     'phraseAuto:true, phraseDb:-1, soloDb:7, basseSon:"uprightReel", basseDb:12, basseHarmoniques:-4, rythmeDb:6, preset:"ballade", lecons:{cadences:4, modal:4, couleurs:4}, root:"B", scale:"B:0",\n'
     'name:"Quatre paliers qui glissent — Si, Sib, La, Sol#", tempo:72, groove:"jazz",\ndesc:"%s",\nchords:[\n'%(gid,J(P1),J(P2),desc)
     + ",\n".join('{name:"%s",beats:4,voicing:"%s",scale:"%s",basseLigne:%s,soloEcrit:%s,soloEcrit2:%s}'%(n,v,sc,J([[bb,midi(x)-ref(v),d] for bb,x,d in BL[i]]),J(Rp[i]),J(M[i])) for i,(n,v,sc,_) in enumerate(C))
     + "\n]},")
rep(old,new)
rep('const NOUVEAUTES=[\n["jz-mesure-impaire","remix v1467"],','const NOUVEAUTES=[\n["jz-trois-paliers","remix v1468"],   // v1468 — ballade, 16 mesures, quatre paliers d\'un demi-ton\n["jz-mesure-impaire","remix v1467"],')
if src.count('["jz-trois-paliers",{feel:"shuffle"}],\n'): rep('["jz-trois-paliers",{feel:"shuffle"}],\n','')
open('/tmp/t/v1468.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1468.json','w'),ensure_ascii=False)
print("ok",len(E))

import sys,json; sys.path.insert(0,'/tmp/t'); from lib import *
src=open('/tmp/t/v1468.html',encoding='utf-8').read(); E=[]
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
S={"cd":[1,3,4,6,8,10,11],"fm":[6,8,10,11,1,3,4],"bm":[11,1,3,4,6,8,10],"fl":[6,7,9,11,0,2,4],"bp":[11,0,3,4,6,7,9],"ea":[4,6,7,9,11,0,2],"edo":[4,6,7,9,11,1,2],
   "bo":[11,1,2,4,6,8,9],"em":[4,6,8,9,11,1,2],"am":[9,11,1,2,4,6,8],"el":[4,5,7,9,10,0,2],"ad":[9,10,0,1,3,4,6,7],"da":[2,4,5,7,9,10,0],"gp":[8,9,0,1,3,4,6]}
C=[("C#m7","x-4-6-4-5-4","C#:bebop:2",S["cd"]),("F#13","2-x-2-3-4-x","F#:bebop:0",S["fm"]),("Bmaj7","x-2-4-3-4-x","B:bebop:1",S["bm"]),("Bmaj9","x-2-1-3-2-x","B:bebop:1",S["bm"]),
   ("F#m7b5","2-x-2-2-1-x","F#:6",S["fl"]),("B7b9","x-2-1-2-1-x","B:harmonicMinor:4",S["bp"]),("Em9","x-7-5-7-7-x","E:5",S["ea"]),("Em6","x-x-5-6-5-7","E:bebop:2",S["edo"]),
   ("Bm7","x-2-4-2-3-x","B:bebop:2",S["bo"]),("E7","x-x-2-4-3-4","E:bebop:0",S["em"]),("Amaj7","x-x-2-2-2-4","A:bebop:1",S["am"]),("A6","x-x-2-2-2-2","A:bebop:1",S["am"]),
   ("Em7b5","x-7-8-7-8-x","E:6",S["el"]),("A7b9","x-x-7-6-8-6","A:symmetric:1",S["ad"]),("Dm9","x-5-3-5-5-x","D:5",S["da"]),("G#7b13","4-x-4-5-5-x","G#:harmonicMinor:4",S["gp"])]
R=["C#2","F#1","B1","B1","F#1","B1","E2","E2","B1","E2","A1","A1","E2","A1","D2","G#1"]
Q=["G#1","C#2","F#2","F#1","C2","F#1","B1","B1","F#2","B1","E2","E2","A#1","E2","A1","D#2"]
M=[[[0,"E5",2.5,"vib"],[3,"C#5",.5],[3.5,"D#5",.5]],
   [[0,"E5",1],[1,"C#5",.5],[1.5,"A#4",.5],[2,"C#5",1.5]],
   [[0,"D#5",2.5,"vib"],[3,"B4",.5],[3.5,"C#5",.5]],
   [[0,"D#5",1],[1,"B4",.5],[1.5,"A#4",.5],[2,"D#5",1.5]],
   [[0,"E5",2.5,"vib"],[3,"C5",.5],[3.5,"D5",.5]],
   [[0,"D#5",1],[1,"C5",.5],[1.5,"A4",.5],[2,"C5",1.5]],
   [[0,"D5",2.5,"vib"],[3,"E5",.5],[3.5,"C5",.5]],
   [[0,"B4",1],[1,"A4",.5],[1.5,"F#4",.5],[2,"A4",1.5]],
   [[0,"D5",2.5,"vib"],[3,"B4",.5],[3.5,"C#5",.5]],
   [[0,"D5",1],[1,"B4",.5],[1.5,"G#4",.5],[2,"B4",1.5]],
   [[0,"C#5",2.5,"vib"],[3,"E5",.5],[3.5,"B4",.5]],
   [[0,"C#5",1],[1,"A4",.5],[1.5,"E4",.5],[2,"C#5",1.5]],
   [[0,"D5",2.5,"vib"],[3,"A4",.5],[3.5,"C5",.5]],
   [[0,"C#5",1],[1,"A#4",.5],[1.5,"G4",.5],[2,"A#4",1.5]],
   [[0,"C5",2.5,"vib"],[3,"A4",.5],[3.5,"A#4",.5]],
   [[0,"C5",1],[1,"A4",.5],[1.5,"G#4",.5],[2,"D#5",1.5]]]
Rp=[[[1.5,"B3",.5],[2,"E4",.5],[2.5,"G#4",.5]],[[3,"A#4",.5],[3.5,"G#4",.5]],
    [[1.5,"F#4",.5],[2,"A#4",.5],[2.5,"B4",.5]],[[3,"F#4",.5],[3.5,"A#4",.5]],
    [[1.5,"F#4",.5],[2,"A4",.5],[2.5,"C5",.5]],[[3,"A4",.5],[3.5,"F#4",.5]],
    [[1.5,"G4",.5],[2,"B4",.5],[2.5,"F#4",.5]],[[3,"E4",.5],[3.5,"G4",.5]],
    [[1.5,"F#4",.5],[2,"A4",.5],[2.5,"B4",.5]],[[3,"G#4",.5],[3.5,"E4",.5]],
    [[1.5,"E4",.5],[2,"G#4",.5],[2.5,"A4",.5]],[[3,"E4",.5],[3.5,"A4",.5]],
    [[1.5,"G4",.5],[2,"A#4",.5],[2.5,"E4",.5]],[[3,"G4",.5],[3.5,"E4",.5]],
    [[1.5,"F4",.5],[2,"A4",.5],[2.5,"E4",.5]],[[3,"E4",.5],[3.5,"G#4",.5]]]
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
gid="jz-paliers-quarte"
anc='{id:"jz-tonalites-manquantes", root:"B"'
desc=("Le geste : quatre ii-V-I, chacun une quarte au-dessus du précédent : Si majeur, Mi mineur, La majeur, Ré mineur ; la tonalité arrive directement, sans accord de liaison, et chaque palier relance au lieu de glisser. "
 "La mélodie tient la note qui reste dans chaque ii-V, puis descend d'un demi-ton sur le I. Le Sol# 7 final monte lui aussi d'une quarte vers le Do# m7 du début. "
 "Pour improviser : bebop dorienne, dominante et majeure sur les paliers majeurs ; locrien, mixolydien b9 b13 (ou diminuée) et éolien sur les paliers mineurs.")
new=('{id:"%s", soloAuto:true, phrase:%s, phrase2:%s,   /* v1469 : grille sœur de jz-trois-paliers ; ballade à 72 bpm, rythme droit, 16 mesures ; quatre paliers qui montent d\'une quarte (Si, Mi m, La, Ré m), retour par Sol# 7 ; contrebasse */ '
     'phraseAuto:true, phraseDb:-1, soloDb:7, basseSon:"uprightReel", basseDb:12, basseHarmoniques:-4, rythmeDb:6, preset:"ballade", lecons:{cadences:4, couleurs:4}, root:"B", scale:"B:0",\n'
     'name:"Quatre paliers à la quarte — Si, Mi, La, Ré", tempo:72, groove:"jazz",\ndesc:"%s",\nchords:[\n'%(gid,J(P1),J(P2),desc)
     + ",\n".join('{name:"%s",beats:4,voicing:"%s",scale:"%s",basseLigne:%s,soloEcrit:%s,soloEcrit2:%s}'%(n,v,sc,J([[bb,midi(x)-ref(v),d] for bb,x,d in BL[i]]),J(Rp[i]),J(M[i])) for i,(n,v,sc,_) in enumerate(C))
     + "\n]},")
rep(anc, new+"\n"+anc)
rep('const NOUVEAUTES=[\n["jz-trois-paliers","remix v1468"],','const NOUVEAUTES=[\n["jz-paliers-quarte","v1469"],   // v1469 — nouvelle : les paliers qui montent d\'une quarte (grille sœur de jz-trois-paliers)\n["jz-trois-paliers","remix v1468"],')
open('/tmp/t/v1469.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1469.json','w'),ensure_ascii=False)
print("ok",len(E))

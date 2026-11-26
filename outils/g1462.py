import sys,json; sys.path.insert(0,'/tmp/t'); from lib import *
src=open('/tmp/t/v1461.html',encoding='utf-8').read(); E=[]
def rep(o,n):
    global src
    assert src.count(o)==1,(src.count(o),o[:80]); src=src.replace(o,n); E.append({"old_text":o,"new_text":n})
O=[40,45,50,55,59,64]
def vm(v): return [O[i]+int(f) for i,f in enumerate(v.split('-')) if f!='x']
def ref(v):
    m=min(vm(v))-12
    while m>45: m-=12
    return m
PC2={'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11}
def nom(m): return [k for k,v in PC2.items() if v==m%12][0]+str(m//12-1)
S={"D":"x-5-5-5-6-5","E":"x-7-7-7-8-7","F":"x-8-9-9-10-x","G":"x-10-10-10-12-x","C":"x-3-3-4-5-x","Eb":"x-6-6-6-7-6","Fq":"x-8-8-8-9-8"}
N={"D":"Dm11","E":"Em11/D","C":"C/D","F":"Fmaj7#11/D","Eb":"Ebm11","Fq":"Fm11/Eb"}
A_=["D","E","D","C","D","E","F","E","Eb","Fq","Eb","Fq","D","E","D","Eb"]
PRE={"D":"E","E":"F","C":"D","F":"G","Eb":"Fq","Fq":"Eb"}
SCD,SCE="D:bebop:2","D#:bebop:2"
M=[[[0,"A4",1],[1,"G4",.5],[1.5,"F4",.5]],[[0,"E4",1.5],[1.5,"G4",.5]],[[0,"A4",.5],[.5,"C5",.5],[1,"D5",1]],[[0,"B4",1],[1,"A4",.5],[1.5,"E4",.5]],
   [[0,"F4",.5],[.5,"A4",.5],[1,"C5",1]],[[0,"B4",.5],[.5,"A4",.5],[1,"G4",1]],[[0,"A4",.5],[.5,"B4",.5],[1,"E5",1]],[[0,"D5",.5],[.5,"B4",.5],[1,"A4",1]],
   [[0,"A#4",1],[1,"G#4",.5],[1.5,"F#4",.5]],[[0,"F4",1.5],[1.5,"G#4",.5]],[[0,"A#4",.5],[.5,"C#5",.5],[1,"D#5",1]],[[0,"C5",.5],[.5,"A#4",.5],[1,"F4",1]],
   [[0,"A4",1],[1,"G4",.5],[1.5,"F4",.5]],[[0,"E4",1.5],[1.5,"G4",.5]],[[0,"F4",.5],[.5,"A4",.5],[1,"D5",1]],[[0,"C#5",.5],[.5,"A#4",.5],[1,"F#4",1]]]
def amen(sh):   # « so-what » : l'accord du dessus, court, puis celui de la mesure, tenu
    a,b=PRE[sh],sh
    return [[2,nom(m),.5] for m in vm(S[a])]+[[2.5,nom(m),1.5] for m in vm(S[b])]
def top(sh): return [[2,nom(vm(S[PRE[sh]])[-1]),.5],[2.5,nom(vm(S[sh])[-1]),1.5]]
R=[amen(s) for s in A_]; T=[top(s) for s in A_]
BL=[]
for i,s in enumerate(A_):
    P,Q=("D#2","A#1") if s in("Eb","Fq") else ("D2","A1")
    BL.append([[0,P,2],[2,P,1],[3,Q,1]])
# couverture : pas de trou dans les deux voix à la fois
on=[0]*256
for i in range(16):
    for b,n,d,*_ in M[i]+R[i]:
        for k in range(int((4*i+b)*4),int((4*i+b+d)*4)): on[k]=1
        assert b+d<=4
assert on.count(0)==0,[k/4 for k,x in enumerate(on) if not x]
P1=[[n,4*i+b,d] for i in range(16) for b,n,d,*_ in M[i]]
P2=[[n,4*i+b,d] for i in range(16) for b,n,d,*_ in T[i]]
gid="jz-so-what"
i0=src.index('{id:"%s",'%gid); i1=src.index('\n{id:',i0+10); old=src[i0:i1]
assert old.endswith('"}]},'),old[-30:]
desc=("Le geste : la basse ne quitte pas le Ré ; au-dessus, la même forme en quartes glisse dans Ré dorien, et chaque phrase reçoit sa réponse « amen » : l'accord d'au-dessus, court, puis celui de la mesure. "
 "En B, tout monte d'un demi-ton, basse comprise (Mib) ; le Mib m11 de la dernière mesure redescend d'une case vers le début. "
 "Pour improviser : bebop dorienne de Ré, bebop dorienne de Mib en B.")
new=('{id:"%s", soloAuto:true, phrase:%s, phrase2:%s,   /* v1462 : ballade à 72 bpm, rythme droit, 16 mesures A8-B4-A4 ; pédale de Ré (Mib en B), formes en quartes qui glissent dans le mode, réponse « amen » en accords écrits ; contrebasse */ '
     'phraseAuto:true, phraseDb:-1, soloDb:2, basseSon:"uprightReel", basseDb:12, basseHarmoniques:-4, rythmeDb:6, preset:"ballade", lecons:{voicings:2, modal:3}, root:"D", scale:"D:1",\n'
     'name:"So What — la réponse « amen » sur la pédale de Ré", tempo:72, groove:"jazz",\ndesc:"%s",\nchords:[\n'%(gid,J(P1),J(P2),desc)
     + ",\n".join('{name:"%s",beats:4,voicing:"%s",scale:"%s",basseLigne:%s,soloEcrit:%s,soloEcrit2:%s}'%(N[s],S[s],SCE if s in("Eb","Fq") else SCD,J([[bb,midi(x)-ref(S[s]),d] for bb,x,d in BL[i]]),J(R[i]),J(M[i])) for i,s in enumerate(A_))
     + "\n]},")
rep(old,new)
rep('const NOUVEAUTES=[\n["jz-wes-quintes-fam","remix v1460"],','const NOUVEAUTES=[\n["jz-so-what","remix v1462"],   // v1462 — ballade, 16 mesures, pédale de Ré et réponse « amen »\n["jz-wes-quintes-fam","remix v1460"],')
rep('["jz-blues-fa",{feel:"shuffle"}],\n["rock-tierce-hesite-la",{}],\n["jz-so-what",{feel:"shuffle"}],\n','["jz-blues-fa",{feel:"shuffle"}],\n["rock-tierce-hesite-la",{}],\n')
open('/tmp/t/v1462.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1462.json','w'),ensure_ascii=False)
print("ok",len(E))

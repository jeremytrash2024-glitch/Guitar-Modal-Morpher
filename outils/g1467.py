import sys,json; sys.path.insert(0,'/tmp/t'); from lib import *
src=open('/tmp/t/v1466.html',encoding='utf-8').read(); E=[]
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
DD,GD,AA,BL_,EL,AH,CM,FM,EB=[2,4,5,7,9,11,0],[7,9,10,0,2,4,5],[9,10,0,1,3,5,7],[10,0,2,4,5,7,9],[4,5,7,9,10,0,2],[9,10,0,1,3,4,6,7],[0,2,4,5,7,9,10],[5,7,9,10,0,2,4],[3,5,7,9,10,0,2]
d="D:bebop:2"
C=[("Dm7","x-5-7-5-6-x",d,DD,5),("Gm7","3-x-3-3-3-x","G:1",GD,5),("Dm9","x-5-3-5-5-x",d,DD,5),("A7b13","5-x-5-6-6-x","A:melodicMinor:6",AA,5),
   ("Dm7","x-5-7-5-6-x",d,DD,5),("Bbmaj7","6-x-7-7-6-x","A#:3",BL_,5),("Em7b5","x-7-8-7-8-x","E:6",EL,5),("A7b9","x-x-7-6-8-6","A:symmetric:1",AH,5),
   ("Gm9","3-x-3-3-3-5","G:bebop:2",GD,3.5),("C13","8-x-8-9-10-x","C:bebop:0",CM,3.5),("Fmaj7","x-8-10-9-10-x","F:bebop:1",FM,3.5),("A7#9","x-x-7-6-8-8","A:melodicMinor:6",AA,3.5),
   ("Dm9","x-5-3-5-5-x",d,DD,5),("Em7b5","x-7-8-7-8-x","E:6",EL,5),("A7b13","5-x-5-6-6-x","A:melodicMinor:6",AA,5),("Ebmaj7","x-6-8-7-8-x","D#:3",EB,5)]
R=["D2","G1","D2","A1","D2","A#1","E2","A1","G1","C2","F1","A1","D2","E2","A1","D#2"]
Q=["A1","D2","A1","G1","A1","F2","A#1","E2","D2","G1","C2","G1","A1","A#1","G1","A#1"]
M=[[[0,"A4",2.5,"vib"],[3,"C5",.5],[3.5,"B4",.5],[4,"A4",1]],
   [[0,"A#4",1],[1,"A4",.5],[1.5,"F4",1.5]],
   [[0,"E5",2.5,"vib"],[3,"D5",.5],[3.5,"C5",.5],[4,"A4",1]],
   [[0,"G4",1],[1,"A#4",.5],[1.5,"C#5",1.5]],
   [[0,"D5",2.5,"vib"],[3,"F5",.5],[3.5,"E5",.5],[4,"D5",1]],
   [[0,"A4",1],[1,"C5",.5],[1.5,"E5",1.5]],
   [[0,"A#4",2.5,"vib"],[3,"A4",.5],[3.5,"G4",.5],[4,"F4",1]],
   [[0,"G4",1],[1,"A#4",.5],[1.5,"C#5",1.5]],
   [[0,"A4",1.5,"vib"],[2,"A#4",.5],[2.5,"D5",1]],
   [[0,"E5",.5],[.5,"D5",.5],[1,"A#4",1]],
   [[0,"A4",1.5,"vib"],[2,"C5",.5],[2.5,"E5",1]],
   [[0,"C5",.5],[.5,"A#4",.5],[1,"G4",1]],
   [[0,"E5",2.5,"vib"],[3,"D5",.5],[3.5,"B4",.5],[4,"C5",1]],
   [[0,"A#4",1],[1,"G4",.5],[1.5,"E4",1.5]],
   [[0,"C#5",2.5,"vib"],[3,"A#4",.5],[3.5,"G4",.5],[4,"F4",1]],
   [[0,"G4",1],[1,"A4",.5],[1.5,"A#4",1.5]]]
Rp=[[[1.5,"F4",.5],[2,"D4",.5],[2.5,"E4",.5]],[[3,"D4",.5],[3.5,"E4",.5],[4,"F4",1]],
    [[1.5,"F4",.5],[2,"A4",.5],[2.5,"C5",.5]],[[3,"F4",.5],[3.5,"D#4",.5],[4,"C#4",1]],
    [[1.5,"A4",.5],[2,"F4",.5],[2.5,"C5",.5]],[[3,"D5",.5],[3.5,"C5",.5],[4,"A#4",1]],
    [[1.5,"D4",.5],[2,"E4",.5],[2.5,"G4",.5]],[[3,"A#4",.5],[3.5,"G4",.5],[4,"E4",1]],
    [[1,"F4",.5],[1.5,"G4",.5]],[[2,"A4",.5],[2.5,"G4",.5],[3,"E4",.5]],
    [[1,"F4",.5],[1.5,"G4",.5]],[[2,"F4",.5],[2.5,"D#4",.5],[3,"C#4",.5]],
    [[1.5,"A4",.5],[2,"F4",.5],[2.5,"D4",.5]],[[3,"D4",.5],[3.5,"F4",.5],[4,"A4",1]],
    [[1.5,"G4",.5],[2,"F4",.5],[2.5,"D#4",.5]],[[3,"D5",.5],[3.5,"C5",.5],[4,"A#4",1]]]
for i in range(16):
    for b,n,dd,*_ in M[i]+Rp[i]: assert midi(n)%12 in C[i][3],(i,n)
L=[c[4] for c in C]; st=[sum(L[:i]) for i in range(16)]; T=sum(L)
A=[]
for i in range(16):
    l=L[i]; t4=l-1 if l==5 else 2
    nxt=midi(R[(i+1)%16]); sol=[midi(n) for b,n,dd,*_ in M[i]+Rp[i] if b<l and b+dd>t4]
    best=None
    for dlt in (2,-2,1,-1):
        c=nxt+dlt
        if c%12 in C[i][3] and not any(abs(c-x)%12 in (1,11) for x in sol) and c!=midi(Q[i]): best=c; break
    A.append(nom(best) if best else Q[i])
print(A)
BL=[]
for i in range(16):
    if L[i]==5: BL.append([[0,R[i],1.5],[1.5,R[i],1.5],[3,Q[i],1],[4,A[i],1]])
    else: BL.append([[0,R[i],1],[1,Q[i],1],[2,A[i],1.5]])
N=int(T*4); on=[0]*N
for i in range(16):
    for b,n,dd,*_ in M[i]+Rp[i]+BL[i]: assert b+dd<=L[i]+1e-9,(i,b,n)
    for b,n,dd,*_ in M[i]+Rp[i]:
        for k in range(int((st[i]+b)*4),int((st[i]+b+dd)*4)): on[k]=1
assert on.count(0)==0,[k/4 for k,x in enumerate(on) if not x]
P1=[[n,st[i]+b,dd] for i in range(16) for b,n,dd,*_ in M[i]]
P2=[[n,st[i]+b,dd] for i in range(16) for b,n,dd,*_ in Rp[i]]
def fb(x): return ('%g'%x)
gid="jz-mesure-impaire"
i0=src.index('{id:"%s",'%gid); i1=src.index('\n{id:',i0+10); old=src[i0:i1]
assert old.endswith('}]},'),old[-30:]
desc=("Le geste : la mesure raconte, l'harmonie reste simple en Ré mineur. La basse garde le même appui : la fondamentale au début, la quinte au dernier groupe ; 3+2 en 5/4, 2+2+3 en 7/8. "
 "En B, quatre mesures de 7/8 chez Fa majeur (Sol m9, Do 13, Fa maj7), plus courtes d'une croche et demie : la phrase se resserre, puis La 7 ramène au Ré. Le Mib maj7 final redescend d'un cran vers le début. "
 "Pour improviser : bebop dorienne de Ré ; La altéré, Sib lydien, Mi locrien, diminuée sur La 7b9 ; en B, bebop dorienne, dominante et majeure ; Mib lydien à la fin.")
new=('{id:"%s", soloAuto:true, phrase:%s, phrase2:%s,   /* v1467 : ballade à 72 bpm, rythme droit ; A en 5/4 (3+2), B quatre mesures de 7/8 (2+2+3) chez Fa, retour en 5/4 ; plus de cordes à vide ni de changement de tempo ; contrebasse */ '
     'phraseAuto:true, phraseDb:-1, soloDb:7, basseSon:"uprightReel", basseDb:12, basseHarmoniques:-4, rythmeDb:6, preset:"ballade", lecons:{cadences:3, metrique:3}, root:"D", scale:"D:1",\n'
     'name:"Ballade en 5/4 et 7/8", tempo:72, groove:"jazz",\ndesc:"%s",\nchords:[\n'%(gid,J(P1),J(P2),desc)
     + ",\n".join('{name:"%s",beats:%s,sig:%s,voicing:"%s",scale:"%s",basseLigne:%s,soloEcrit:%s,soloEcrit2:%s}'%(n,fb(l),fb(l),v,sc,J([[bb,midi(x)-ref(v),dd] for bb,x,dd in BL[i]]),J(Rp[i]),J(M[i])) for i,(n,v,sc,_,l) in enumerate(C))
     + "\n]},")
rep(old,new)
rep('const NOUVEAUTES=[\n["jz-descente-eclats","remix v1465"],','const NOUVEAUTES=[\n["jz-mesure-impaire","remix v1467"],   // v1467 — ballade, 5/4 et 7/8, la basse garde son appui\n["jz-descente-eclats","remix v1465"],')
c=src.count('["jz-mesure-impaire",{feel:"shuffle"}],\n'); print("shuffle",c)
if c: rep('["jz-mesure-impaire",{feel:"shuffle"}],\n','')
open('/tmp/t/v1467.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1467.json','w'),ensure_ascii=False)
print("ok",len(E),T)

import sys,json; sys.path.insert(0,'/tmp/t'); from lib import *
src=open('/tmp/t/v1472.html',encoding='utf-8').read(); E=[]
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
S={"c":[0,2,4,5,7,9,11],"fd":[5,7,8,10,0,2,3],"bbm":[10,0,2,3,5,7,8],"eb":[3,5,7,8,10,0,2],"gd":[8,10,11,1,3,5,6],"cm":[1,3,5,6,8,10,11],
   "fs":[6,8,10,11,1,3,5],"bd":[11,1,2,4,6,8,9],"em":[4,6,8,9,11,1,2],"a":[9,11,1,2,4,6,8],"dd":[2,4,5,7,9,11,0],"gm":[7,9,11,0,2,4,5]}
C=[("Cmaj7","x-3-5-4-5-x","C:bebop:1",S["c"]),("C6/9","x-3-2-2-3-3","C:bebop:1",S["c"]),("Fm9","1-x-1-1-1-3","F:bebop:2",S["fd"]),("Bb13","6-x-6-7-8-x","A#:bebop:0",S["bbm"]),
   ("Ebmaj7","x-6-8-7-8-x","D#:bebop:1",S["eb"]),("Eb6/9","x-6-5-5-6-6","D#:bebop:1",S["eb"]),("G#m9","4-x-4-4-4-6","G#:bebop:2",S["gd"]),("C#13","9-x-9-10-11-x","C#:bebop:0",S["cm"]),
   ("F#maj7","x-9-11-10-11-x","F#:bebop:1",S["fs"]),("F#6/9","x-9-8-8-9-9","F#:bebop:1",S["fs"]),("Bm9","7-x-7-7-7-9","B:bebop:2",S["bd"]),("E13","12-x-12-13-14-x","E:bebop:0",S["em"]),
   ("Amaj7","x-12-14-13-14-x","A:bebop:1",S["a"]),("A6/9","x-12-11-11-12-12","A:bebop:1",S["a"]),("Dm9","x-5-3-5-5-x","D:bebop:2",S["dd"]),("G13","3-x-3-4-5-x","G:bebop:0",S["gm"])]
R=["C2","C2","F1","A#1","D#2","D#2","G#1","C#2","F#1","F#1","B1","E2","A1","A1","D2","G1"]
Q=["G1","G1","C2","F2","A#1","A#1","D#2","G#1","C#2","C#2","F#1","B1","E2","E2","A1","D2"]
def hold(n,up,lo): return [[0,n,3,"vib"],[3,up,.5],[3.5,lo,.5]]
M=[[[0,"E4",1.5],[1.5,"F4",.5],[2,"G4",2,"vib"]],hold("G4","A4","F4"),hold("G4","G#4","F4"),hold("G4","G#4","F4"),
   [[0,"G4",1.5],[1.5,"G#4",.5],[2,"A#4",2,"vib"]],hold("A#4","C5","G#4"),hold("A#4","B4","G#4"),hold("A#4","B4","G#4"),
   [[0,"A#4",1.5],[1.5,"B4",.5],[2,"C#5",2,"vib"]],hold("C#5","D#5","B4"),hold("C#5","D5","B4"),hold("C#5","D5","B4"),
   [[0,"C#5",1.5],[1.5,"D5",.5],[2,"E5",2,"vib"]],hold("E5","F#5","D5"),hold("E5","F5","D5"),
   [[0,"E5",2,"vib"],[2,"D5",.5],[2.5,"B4",.5],[3,"G4",.5],[3.5,"F4",.5]]]
Rp=[[[3,"C4",.5],[3.5,"E4",.5]],[[1,"E4",.5],[1.5,"D4",.5],[2,"A3",1]],[[1,"G#3",.5],[1.5,"C4",.5],[2,"D#4",1]],[[1,"D4",.5],[1.5,"F4",.5],[2,"G#3",1]],
    [[3,"D4",.5],[3.5,"D#4",.5]],[[1,"G4",.5],[1.5,"F4",.5],[2,"C4",1]],[[1,"B3",.5],[1.5,"D#4",.5],[2,"F#4",1]],[[1,"F4",.5],[1.5,"D#4",.5],[2,"B3",1]],
    [[3,"F4",.5],[3.5,"F#4",.5]],[[1,"A#3",.5],[1.5,"D#4",.5],[2,"G#4",1]],[[1,"D4",.5],[1.5,"F#4",.5],[2,"A4",1]],[[1,"G#4",.5],[1.5,"D4",.5],[2,"B3",1]],
    [[3,"G#4",.5],[3.5,"A4",.5]],[[1,"C#4",.5],[1.5,"F#4",.5],[2,"B4",1]],[[1,"F4",.5],[1.5,"A4",.5],[2,"C5",1]],[[1,"F4",.5],[1.5,"A4",.5]]]
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
gid="jz-modulations-tierces-min"
i0=src.index('{id:"%s",'%gid); i1=src.index('\n{id:',i0+10); old=src[i0:i1]
assert old.endswith('}]},'),old[-30:]
desc=("Le geste : une seule note traverse quatre accords. La quinte de chaque tonique est la 9 du ii suivant, la 13 du V, puis la tierce de la nouvelle tonique : le Sol de Do devient la tierce de Mib, le Sib de Mib celle de Fa#, le Do# de Fa# celle de La, et le Mi de La celle de Do. "
 "Le sax arrive sur la tierce, monte à la quinte et la garde pendant que l'harmonie change trois fois de sens dessous ; la note du haut de la guitare reste la même. Les 6/9, les m9 et les 13 sont chaque fois la même forme, trois cases plus haut. "
 "Pour improviser : bebop majeure sur les toniques, bebop dorienne sur les ii, bebop dominante sur les V.")
new=('{id:"%s", soloAuto:true, phrase:%s, phrase2:%s,   /* v1473 : ballade à 72 bpm, rythme droit, 16 mesures ; quatre tonalités par tierces mineures (Do, Mib, Fa#, La) ; la quinte de chaque tonique tenue sous ii et V devient la tierce de la suivante ; contrebasse */ '
     'phraseAuto:true, phraseDb:-1, soloDb:7, basseSon:"uprightReel", basseDb:12, basseHarmoniques:-4, rythmeDb:6, preset:"ballade", lecons:{cadences:4, modal:4, voicings:3}, root:"C", scale:"C:0",\n'
     'name:"Une note tenue, quatre tonalités — Do, Mib, Fa#, La", tempo:72, groove:"jazz",\ndesc:"%s",\nchords:[\n'%(gid,J(P1),J(P2),desc)
     + ",\n".join('{name:"%s",beats:4,voicing:"%s",scale:"%s",basseLigne:%s,soloEcrit:%s,soloEcrit2:%s}'%(n,v,sc,J([[bb,midi(x)-ref(v),d] for bb,x,d in BL[i]]),J(Rp[i]),J(M[i])) for i,(n,v,sc,_) in enumerate(C))
     + "\n]},")
rep(old,new)
rep('const NOUVEAUTES=[\n["jz-tonalites-manquantes","remix v1470"],','const NOUVEAUTES=[\n["jz-modulations-tierces-min","remix v1473"],   // v1473 — ballade, la note tenue qui traverse quatre tonalités\n["jz-tonalites-manquantes","remix v1470"],')
if src.count('["jz-modulations-tierces-min",{feel:"shuffle"}],\n'): rep('["jz-modulations-tierces-min",{feel:"shuffle"}],\n','')
open('/tmp/t/v1473.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1473.json','w'),ensure_ascii=False)
print("ok",len(E))

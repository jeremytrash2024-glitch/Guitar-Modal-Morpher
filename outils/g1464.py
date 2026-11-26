import sys,json; sys.path.insert(0,'/tmp/t'); from lib import *
src=open('/tmp/t/v1463.html',encoding='utf-8').read(); E=[]
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
AE,LY,BD,LO,PD,DO,MA,HM,DL=[0,2,3,5,7,8,10],[8,10,0,2,3,5,7],[10,0,2,3,5,7,8],[2,3,5,7,8,10,0],[7,8,11,0,2,3,5],[5,7,8,10,0,2,3],[3,5,7,8,10,0,2],[0,2,3,5,7,8,11],[1,3,5,7,8,10,0]
C=[("Cm9","x-3-1-3-3-x","C:5",AE),("Abmaj13","4-x-5-5-6-x","G#:3",LY),("Bb13","6-x-6-7-8-x","A#:bebop:0",BD),("Cm(add9)","x-3-1-0-3-x","C:5",AE),
   ("Abmaj13","4-x-5-5-6-x","G#:3",LY),("Bb13","6-x-6-7-8-x","A#:bebop:0",BD),("Dm7b5","x-5-6-5-6-x","D:6",LO),("G7b13","3-x-3-4-4-x","G:harmonicMinor:4",PD),
   ("Fm9","1-x-1-1-1-3","F:bebop:2",DO),("Bb13","6-x-6-7-8-x","A#:bebop:0",BD),("Ebmaj9","x-6-5-7-6-x","D#:bebop:1",MA),("Abmaj7#11","4-x-5-5-3-x","G#:3",LY),
   ("Dm7b5","x-5-6-5-6-x","D:6",LO),("G7b13","3-x-3-4-4-x","G:harmonicMinor:4",PD),("CmMaj7","x-3-5-4-4-x","C:harmonicMinor:0",HM),("Dbmaj9","x-4-3-5-4-x","C#:3",DL)]
R=["C2","G#1","A#1","C2","G#1","A#1","D2","G1","F2","A#1","D#2","G#1","D2","G1","C2","C#2"]
Q=["G1","D#2","F2","G1","D#2","F2","G#1","D2","C2","F2","A#1","D#2","G#1","D2","G1","G#1"]
M=[[[0,"G4",2.5,"vib"],[3,"A#4",.5],[3.5,"C5",.5]],
   [[0,"C5",1],[1,"D5",.5],[1.5,"D#5",.5],[2,"D5",1.5]],
   [[0,"D5",2.5,"vib"],[3,"C5",.5],[3.5,"G#4",.5]],
   [[0,"G4",1],[1,"A#4",.5],[1.5,"C5",.5],[2,"D5",1.5]],
   [[0,"C5",2.5,"vib"],[3,"D#5",.5],[3.5,"D5",.5]],
   [[0,"D5",1],[1,"C5",.5],[1.5,"A#4",.5],[2,"G#4",1.5]],
   [[0,"G#4",2.5,"vib"],[3,"F4",.5],[3.5,"G#4",.5]],
   [[0,"B4",1],[1,"D5",.5],[1.5,"F5",.5],[2,"D#5",1.5]],
   [[0,"D#5",2.5,"vib"],[3,"C5",.5],[3.5,"D5",.5]],
   [[0,"D5",1],[1,"F5",.5],[1.5,"D#5",.5],[2,"C5",1.5]],
   [[0,"D5",2.5,"vib"],[3,"A#4",.5],[3.5,"C5",.5]],
   [[0,"C5",1],[1,"D5",.5],[1.5,"D#5",.5],[2,"D5",1.5]],
   [[0,"C5",2.5,"vib"],[3,"G#4",.5],[3.5,"F4",.5]],
   [[0,"F4",1],[1,"G4",.5],[1.5,"B4",.5],[2,"G#4",1.5]],
   [[0,"B4",2.5,"vib"],[3,"C5",.5],[3.5,"D5",.5]],
   [[0,"D#5",1],[1,"C5",.5],[1.5,"A#4",.5],[2,"G#4",1.5]]]
Rp=[[[1.5,"C4",.5],[2,"D#4",.5],[2.5,"D4",.5]],[[3,"C4",.5],[3.5,"D#4",.5]],
    [[1.5,"A#3",.5],[2,"D4",.5],[2.5,"F4",.5]],[[3,"G4",.5],[3.5,"D#4",.5]],
    [[1.5,"D#4",.5],[2,"G4",.5],[2.5,"G#4",.5]],[[3,"D4",.5],[3.5,"F4",.5]],
    [[1.5,"D4",.5],[2,"F4",.5],[2.5,"C4",.5]],[[3,"G4",.5],[3.5,"F4",.5]],
    [[1.5,"F4",.5],[2,"G#4",.5],[2.5,"G4",.5]],[[3,"G#4",.5],[3.5,"F4",.5]],
    [[1.5,"G4",.5],[2,"F4",.5],[2.5,"D#4",.5]],[[3,"D#4",.5],[3.5,"G4",.5]],
    [[1.5,"F4",.5],[2,"G#4",.5],[2.5,"D4",.5]],[[3,"D4",.5],[3.5,"D#4",.5]],
    [[1.5,"G4",.5],[2,"D#4",.5],[2.5,"C4",.5]],[[3,"F4",.5],[3.5,"D#4",.5]]]
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
gid="jz-cm-tour-riche"
i0=src.index('{id:"%s",'%gid); i1=src.index('\n{id:',i0+10); old=src[i0:i1]
assert old.endswith('\n]},'),old[-30:]
desc=("Le geste : Lab maj13 et Sib 13 ont la même forme, deux cases plus haut : toute la main monte, les quatre voix avec. En B, on passe chez Mib majeur (Fa m9, Sib 13, Mib maj9), puis la cadence mineure ramène au Do ; du Sol 7 au Do m maj7, le Si et le Mib restent sous les mêmes doigts. Le Réb maj9 final redescend d'une case vers le début. "
 "Pour improviser : Do éolien, Lab lydien, bebop dominante sur Sib 13 ; bebop dorienne et majeure en B ; Ré locrien, Sol mixolydien b9 b13, Do mineur harmonique, Réb lydien.")
new=('{id:"%s", soloAuto:true, phrase:%s, phrase2:%s,   /* v1464 : ballade à 72 bpm, rythme droit, 16 mesures ; Lab et Sib qui montent ensemble, B chez Mib, cadence mineure et Do m maj7, retour par Réb maj9 ; corde de Sol à vide seulement sur Do m(add9) ; Sib 13 et Do m b6 remplacés ; contrebasse */ '
     'phraseAuto:true, phraseDb:-1, soloDb:7, basseSon:"uprightReel", basseDb:12, basseHarmoniques:-4, rythmeDb:6, preset:"ballade", lecons:{cadences:3, harmonique:3}, root:"C", scale:"C:5",\n'
     'name:"Tour en Do mineur — voicings riches", tempo:72, groove:"jazz",\ndesc:"%s",\nchords:[\n'%(gid,J(P1),J(P2),desc)
     + ",\n".join('{name:"%s",beats:4,voicing:"%s",scale:"%s",basseLigne:%s,soloEcrit:%s,soloEcrit2:%s}'%(n,v,sc,J([[bb,midi(x)-ref(v),d] for bb,x,d in BL[i]]),J(Rp[i]),J(M[i])) for i,(n,v,sc,_) in enumerate(C))
     + "\n]},")
rep(old,new)
rep('const NOUVEAUTES=[\n["jz-drop2-voiceleading","remix v1463"],','const NOUVEAUTES=[\n["jz-cm-tour-riche","remix v1464"],   // v1464 — ballade, 16 mesures, Lab et Sib qui montent ensemble, B chez Mib\n["jz-drop2-voiceleading","remix v1463"],')
rep('["jz-cm-tour-riche",{feel:"shuffle"}],\n','')
open('/tmp/t/v1464.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1464.json','w'),ensure_ascii=False)
print("ok",len(E))

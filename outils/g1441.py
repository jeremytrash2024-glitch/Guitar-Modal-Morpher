import sys,json,re; sys.path.insert(0,'/tmp/t'); from lib import *
src=open('/tmp/t/v1440.html',encoding='utf-8').read(); E=[]
def rep(o,n):
    global src
    assert src.count(o)==1,(src.count(o),o[:80]); src=src.replace(o,n); E.append({"old_text":o,"new_text":n})
NOM=re.compile(r'([A-G][b#]?)')
def pc(name):
    r=NOM.match(name).group(1); b=PC[r[0]]
    return (b+(1 if r[1:]=="#" else -1 if r[1:]=="b" else 0))%12
def refnom(name): return 28+((pc(name)-4)%12)
def blv(name,notes): ref=refnom(name); return [[b,midi(x)-ref,d] for b,x,d in notes]

C=[("Dm9",8,"x-3-3-5-5-x","D:1"),("G13",8,"x-5-3-4-5-x","G:4"),("C9",8,"x-5-8-7-5-x","C:4"),("F9",8,"x-8-7-8-8-x","F:4"),
   ("Bb9",8,"x-5-6-5-6-x","A#:4"),("Eb9",8,"x-6-5-6-6-x","D#:4"),("E7b9",8,"x-7-6-7-6-x","E:harmonicMinor:4"),("A7",8,"x-x-5-6-5-x","A:melodicMinor:4")]
BL=[[[0,"D3",2],[2,"A2",2],[4,"D3",2],[6,"A2",2]],
    [[0,"G2",2],[2,"D3",2],[4,"G2",2],[6,"B2",2]],
    [[0,"C3",2],[2,"G2",2],[4,"C3",2],[6,"E3",2]],
    [[0,"F2",2],[2,"C3",2],[4,"F2",2],[6,"A2",2]],
    [[0,"A#2",2],[2,"F2",2],[4,"A#2",2],[6,"F2",2]],
    [[0,"D#3",2],[2,"A#2",2],[4,"D#3",2],[6,"A#2",2]],
    [[0,"E2",2],[2,"B2",2],[4,"E2",2],[6,"G#2",2]],
    [[0,"A2",2],[2,"C#3",2],[4,"A2",2],[6,"C#3",2]]]
M=[[[0,"E4",3.5,"vib"],[4,"A4",.5],[4.5,"G4",.5],[5,"F4",1],[6,"D4",1.5]],
   [[0,"D4",.5],[.5,"F4",.5],[1,"E4",2.5,"vib"],[4,"B4",.5],[4.5,"A4",.5],[5,"G4",1],[6,"F4",1.5]],
   [[0,"G4",.5],[.5,"F4",.5],[1,"E4",2.5,"vib"],[4,"D4",.5],[4.5,"E4",.5],[5,"G4",1],[6,"A#4",1.5]],
   [[0,"F4",.5],[.5,"A4",.5],[1,"G4",2.5,"vib"],[4,"A4",.5],[4.5,"C5",.5],[5,"F4",1],[6,"A4",1.5]],
   [[0,"A#4",.5],[.5,"A4",.5],[1,"G#4",.5],[1.5,"G4",.5],[2,"F4",.5],[2.5,"D#4",.5],[3,"D4",.5],[3.5,"C4",.5],[4,"D4",1.5,"vib"],[6,"F4",.5],[6.5,"A#4",.5],[7,"D5",1]],
   [[0,"D#5",.5],[.5,"D5",.5],[1,"C#5",.5],[1.5,"C5",.5],[2,"A#4",.5],[2.5,"G#4",.5],[3,"G4",.5],[3.5,"F4",.5],[4,"G4",1.5,"vib"],[6,"G4",.5],[6.5,"A#4",.5],[7,"C#5",1]],
   [[0,"D5",.5],[.5,"C5",.5],[1,"B4",.5],[1.5,"A4",.5],[2,"G#4",.5],[2.5,"F4",.5],[3,"E4",.5],[3.5,"D4",.5],[4,"G#4",1.5,"vib"],[6,"B4",.5],[6.5,"D5",.5],[7,"G#4",1]],
   [[0,"A4",.5],[.5,"G#4",.5],[1,"G4",.5],[1.5,"F4",.5],[2,"E4",.5],[2.5,"D4",.5],[3,"C#4",.5],[3.5,"B3",.5],[4,"C#4",1.5,"vib"],[6,"E4",.5],[6.5,"G4",.5],[7,"F4",.5],[7.5,"D#4",.5]]]
R=[[[1,"F3",.5],[1.5,"A3",.5],[2,"C4",2],[6.5,"A3",.5],[7,"C4",1]],
   [[1.5,"G3",.5],[2,"B3",.5],[2.5,"D4",1.5],[6.5,"B3",.5],[7,"D4",1]],
   [[1.5,"C4",.5],[2,"D4",.5],[2.5,"A#3",1.5],[6.5,"E4",.5],[7,"D4",1]],
   [[1.5,"F3",.5],[2,"A3",.5],[2.5,"D#4",1.5],[6.5,"D#4",.5],[7,"F4",1]],
   [[0,"D4",3.5],[4,"G#3",4]],
   [[0,"G4",3.5],[4,"C#4",4]],
   [[0,"G#3",3.5],[4,"D4",4]],
   [[0,"C#4",3.5],[4,"G3",4]]]
st=[];t=0
for c in C: st.append(t); t+=c[1]
assert t==64 and len(M)==len(R)==len(BL)==8
for i,c in enumerate(C):
    for seq in (M[i],R[i],BL[i]):
        for b,n,d,*_ in seq: assert b+d<=c[1]+1e-9,(c[0],b,n,d)
on=[0]*256
for i in range(8):
    for b,n,d,*_ in M[i]+R[i]:
        for k in range(int((st[i]+b)*4),int((st[i]+b+d)*4)): on[k]=1
assert on.count(0)==0,[k/4 for k,x in enumerate(on) if not x]
P1=[[n,st[i]+b,d] for i in range(8) for b,n,d,*_ in M[i]]
P2=[[n,st[i]+b,d] for i in range(8) for b,n,d,*_ in R[i]]
gid="jz-carlton-quartes-sans-fonda"
i0=src.index('{id:"%s",'%gid); i1=src.index('\n{id:',i0+10); old=src[i0:i1]
assert old.endswith('"}]},'),old[-30:]
desc=("Le geste : en A, notes longues ; le Mi reste en haut pendant que la basse avance par quartes, Ré, Sol, Do, Fa. "
 "En B, quatre longues septièmes, et la mélodie se met à courir : une ligne bebop, les notes de l'accord sur les temps, la note de passage entre deux. "
 "Pour improviser : en A, Do majeur, avec Sib sur Do 9, Sib et Mib sur Fa 9. En B, la gamme bebop dominante (mixolydien + 7e majeure de passage) sur Sib 9, Mib 9 et La 7 ; Mi phrygien dominant sur Mi 7b9.")
new=('{id:"%s", soloAuto:true, phrase:%s, phrase2:%s,   /* v1441 : ballade à 70 bpm, 16 mesures ; A, le Mi tenu sur Ré m9, Sol 13, Do 9, puis Fa 9 (x-8-7-8-8-x, le Fa 13 était casse-doigt) ; '
     'B, quatre septièmes de deux mesures (Sib 9, Mib 9, Mi 7b9, La 7) et une ligne bebop en croches, la même phrase transposée de Sib à Mib ; Sib maj9 sans neuvième retiré, contrebasse */ phraseAuto:true, phraseDb:-1, soloDb:5, basseSon:"uprightReel", basseDb:7, basseHarmoniques:-4, '
     'rythmeDb:6, preset:"ballade", fondamentale:"nom", lecons:{voicings:3, dominantes:2}, root:"D", scale:"D:1", '
     'name:"Quartes et ligne bebop — ballade sans fondamentale", tempo:70, groove:"jazz",\ndesc:"%s",\nchords:[\n'%(gid,J(P1),J(P2),desc)
     + ",\n".join('{name:"%s",beats:%d,voicing:"%s",scale:"%s",basseLigne:%s,soloEcrit:%s,soloEcrit2:%s}'%(n,b,v,sc,J(blv(n,BL[i])),J(R[i]),J(M[i])) for i,(n,b,v,sc) in enumerate(C))
     + "\n]},")
rep(old,new)
rep('const NOUVEAUTES=[\n["jz-carlton-broderie-aigues","remix v1437"],','const NOUVEAUTES=[\n["jz-carlton-quartes-sans-fonda","remix v1441"],   // v1441 — ballade, 16 mesures, quartes puis ligne bebop\n["jz-carlton-broderie-aigues","remix v1437"],')
open('/tmp/t/v1441.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1441.json','w'),ensure_ascii=False)
print("ok",len(E))

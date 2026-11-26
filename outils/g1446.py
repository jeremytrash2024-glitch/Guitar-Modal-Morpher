import sys,json; sys.path.insert(0,'/tmp/t'); from lib import *
src=open('/tmp/t/v1445.html',encoding='utf-8').read(); E=[]
def rep(o,n):
    global src
    assert src.count(o)==1,(src.count(o),o[:80]); src=src.replace(o,n); E.append({"old_text":o,"new_text":n})
O=[40,45,50,55,59,64]
def lowv(v): return min(O[i]+int(f) for i,f in enumerate(v.split('-')) if f!='x')
def ref(v):
    m=lowv(v)-12
    while m>45: m-=12
    return m
C=[("C9",8,"x-x-x-7-5-6","C:4"),("Bb/C",8,"x-x-x-7-6-6","C:4"),("D/C",8,"x-x-x-7-7-5","C:melodicMinor:3"),("F#/C",8,"x-x-x-6-7-6","C:melodicMinor:6"),
   ("Fmaj7",8,"x-x-x-5-5-5","F:0"),("Eb/F",4,"x-x-x-3-4-3","F:4"),("G/F",4,"x-x-x-4-3-3","F:melodicMinor:3"),("B/F",8,"x-x-x-4-4-2","F:melodicMinor:6"),("Bbmaj7",8,"x-x-x-2-3-1","A#:3")]
BL=[[[0,"C3",2],[2,"G2",2],[4,"C3",2],[6,"G2",2]],
    [[0,"C3",2],[2,"G2",2],[4,"C3",2],[6,"G2",2]],
    [[0,"C3",2],[2,"E3",2],[4,"C3",2],[6,"E3",2]],
    [[0,"C3",2],[2,"A#2",2],[4,"C3",2],[6,"A#2",2]],
    [[0,"F2",2],[2,"C3",2],[4,"F2",2],[6,"C3",2]],
    [[0,"F2",2],[2,"C3",2]],
    [[0,"F2",2],[2,"A2",2]],
    [[0,"F2",2],[2,"D#3",2],[4,"F2",2],[6,"D#3",2]],
    [[0,"A#2",2],[2,"F2",2],[4,"A#2",2],[6,"C3",2]]]
M=[[[0,"G4",.5],[.5,"A4",.5],[1,"A#4",2.5,"vib"],[4,"C5",.5],[4.5,"A#4",.5],[5,"G4",1],[6,"E4",1.5]],
   [[0,"F4",.5],[.5,"G4",.5],[1,"A#4",2.5,"vib"],[4,"C5",.5],[4.5,"A#4",.5],[5,"F4",1],[6,"D4",1.5]],
   [[0,"F#4",.5],[.5,"E4",.5],[1,"D4",2.5,"vib"],[4,"F#4",.5],[4.5,"A4",.5],[5,"C5",1],[6,"F#4",1.5]],
   [[0,"A#4",.5],[.5,"G#4",.5],[1,"F#4",2.5,"vib"],[4,"A#4",.5],[4.5,"C#5",.5],[5,"A#4",1],[6,"E4",1.5]],
   [[0,"F4",.5],[.5,"G4",.5],[1,"A4",2.5,"vib"],[4,"C5",.5],[4.5,"G4",.5],[5,"A4",1],[6,"G4",1.5]],
   [[0,"G4",2,"vib"],[2.5,"D#4",.5],[3,"A#4",.5],[3.5,"F4",.5]],
   [[0,"G4",2,"vib"],[2.5,"D4",.5],[3,"B4",.5],[3.5,"G4",.5]],
   [[0,"A4",.5],[.5,"G#4",.5],[1,"B4",2.5,"vib"],[4,"A4",.5],[4.5,"F#4",.5],[5,"D#4",1],[6,"C#4",1.5]],
   [[0,"D4",.5],[.5,"F4",.5],[1,"A4",2.5,"vib"],[4,"G4",.5],[4.5,"F4",.5],[5,"D4",1],[6,"C4",1.5]]]
R=[[[1.5,"E4",.5],[2,"D4",.5],[2.5,"E4",1.5],[6.5,"G4",.5],[7,"A#4",1]],
   [[1.5,"D4",.5],[2,"F4",.5],[2.5,"D4",1.5],[6.5,"F4",.5],[7,"G4",1]],
   [[1.5,"F#4",.5],[2,"A4",.5],[2.5,"F#4",1.5],[6.5,"A4",.5],[7,"D4",1]],
   [[1.5,"C#4",.5],[2,"A#3",.5],[2.5,"C#4",1.5],[6.5,"A#3",.5],[7,"C#4",1]],
   [[1.5,"C4",.5],[2,"E4",.5],[2.5,"F4",1.5],[6.5,"E4",.5],[7,"C4",1]],
   [[.5,"A#3",.5],[1,"D#4",.5],[1.5,"A#3",1]],
   [[.5,"B3",.5],[1,"D4",.5],[1.5,"B3",1]],
   [[1.5,"D#4",.5],[2,"F#4",.5],[2.5,"D#4",1.5],[6.5,"B3",.5],[7,"A3",1]],
   [[1.5,"F4",.5],[2,"D4",.5],[2.5,"F4",1.5],[6.5,"A3",.5],[7,"C4",1]]]
st=[];t=0
for c in C: st.append(t); t+=c[1]
assert t==64 and len(M)==len(R)==len(BL)==9
for i,c in enumerate(C):
    for seq in (M[i],R[i],BL[i]):
        for b,n,d,*_ in seq: assert b+d<=c[1]+1e-9,(c[0],b,n,d)
on=[0]*256
for i in range(9):
    for b,n,d,*_ in M[i]+R[i]:
        for k in range(int((st[i]+b)*4),int((st[i]+b+d)*4)): on[k]=1
assert on.count(0)==0,[k/4 for k,x in enumerate(on) if not x]
P1=[[n,st[i]+b,d] for i in range(9) for b,n,d,*_ in M[i]]
P2=[[n,st[i]+b,d] for i in range(9) for b,n,d,*_ in R[i]]
gid="jz-triades-superieures"
i0=src.index('{id:"%s",'%gid); i1=src.index('\n{id:',i0+10); old=src[i0:i1]
assert old.endswith('"}]},'),old[-30:]
desc=("Le geste : une basse qui ne bouge pas, et des triades de trois notes sur les cordes aiguës ; d'une triade à l'autre, une note reste et les deux autres glissent d'un demi-ton. "
 "En A, sur Do : Sib, Ré, puis Fa# ; en B, le même jeu sur Fa, plus vite, puis Sib maj7 qui ramène au Do. "
 "Pour improviser : Do mixolydien, Do lydien dominant sur D/C, Do altéré sur F#/C ; en B, Fa majeur, Fa lydien dominant sur G/F, Fa altéré sur B/F.")
new=('{id:"%s", soloAuto:true, phrase:%s, phrase2:%s,   /* v1446 : ballade à 70 bpm, 16 mesures ; triades sur les trois cordes aiguës, une note reste et deux glissent d\'un demi-ton ; '
     'A sur la pédale de Do, B le même jeu sur Fa puis Sib maj7 ; contrebasse */ phraseAuto:true, phraseDb:-1, soloDb:5, basseSon:"uprightReel", basseDb:13, basseHarmoniques:-4, '
     'rythmeDb:7, preset:"ballade", root:"C", scale:"C:4", lecons:{voicings:2, dominantes:3, couleurs:3},\n'
     'name:"Trois triades sur une seule basse — les structures supérieures", tempo:70, groove:"jazz",\ndesc:"%s",\nchords:[\n'%(gid,J(P1),J(P2),desc)
     + ",\n".join('{name:"%s",beats:%d,voicing:"%s",scale:"%s",basseLigne:%s,soloEcrit:%s,soloEcrit2:%s}'%(n,b,v,sc,J([[bb,midi(x)-ref(v),d] for bb,x,d in BL[i]]),J(R[i]),J(M[i])) for i,(n,b,v,sc) in enumerate(C))
     + "\n]},")
rep(old,new)
rep('const NOUVEAUTES=[\n["jz-diminue-quatre-sorties","remix v1443"],','const NOUVEAUTES=[\n["jz-triades-superieures","remix v1446"],   // v1446 — ballade, 16 mesures, triades qui glissent sur une pédale\n["jz-diminue-quatre-sorties","remix v1443"],')
open('/tmp/t/v1446.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1446.json','w'),ensure_ascii=False)
print("ok",len(E))

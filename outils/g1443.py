import sys,json,re; sys.path.insert(0,'/tmp/t'); from lib import *
src=open('/tmp/t/v1441.html',encoding='utf-8').read(); E=[]
def rep(o,n):
    global src
    assert src.count(o)==1,(src.count(o),o[:80]); src=src.replace(o,n); E.append({"old_text":o,"new_text":n})
NOM=re.compile(r'([A-G][b#]?)')
def pc(name):
    r=NOM.match(name).group(1); b=PC[r[0]]
    return (b+(1 if r[1:]=="#" else -1 if r[1:]=="b" else 0))%12
def refnom(name): return 28+((pc(name)-4)%12)
def blv(name,notes): ref=refnom(name); return [[b,midi(x)-ref,d] for b,x,d in notes]

C=[("Ddim7",4,"x-2-3-1-3-x","D:symmetric:0"),("Ebmaj7",4,"x-5-5-3-4-x","D#:0"),("Fdim7",4,"x-5-6-4-6-x","F:symmetric:0"),("F#maj7",4,"x-8-8-6-7-x","F#:0"),
   ("G#dim7",4,"x-x-3-4-3-4","G#:symmetric:0"),("Amaj7",4,"x-x-6-6-5-5","A:0"),("Bdim7",4,"x-x-6-7-6-7","B:symmetric:0"),("Cmaj7",4,"x-x-9-9-8-8","C:0"),
   ("Cmaj7",4,"x-3-5-4-5-x","C:0"),("C#dim7",4,"x-4-5-3-5-x","C#:symmetric:0"),("Dm7",4,"x-5-7-5-6-x","D:1"),("D#dim7",4,"x-6-7-5-7-x","D#:symmetric:0"),
   ("Em7",4,"x-7-9-7-8-x","E:2"),("Fmaj7",4,"x-8-10-9-10-x","F:3"),("F#dim7",4,"x-9-10-8-10-x","F#:symmetric:0"),("G7",4,"x-10-12-10-12-x","G:4")]
BL=[[[0,"D3",2],[2,"D3",2]],[[0,"D#3",2],[2,"A#2",2]],[[0,"F2",2],[2,"F2",2]],[[0,"F#2",2],[2,"C#3",2]],
    [[0,"G#2",2],[2,"G#2",2]],[[0,"A2",2],[2,"E3",2]],[[0,"B2",2],[2,"B2",2]],[[0,"C3",2],[2,"G2",2]],
    [[0,"C3",2],[2,"G2",2]],[[0,"C#3",2],[2,"C#3",2]],[[0,"D3",2],[2,"A2",2]],[[0,"D#3",2],[2,"D#3",2]],
    [[0,"E3",2],[2,"B2",2]],[[0,"F3",2],[2,"C3",2]],[[0,"F#3",2],[2,"F#3",2]],[[0,"G3",2],[2,"D3",2]]]
M=[[[0,"G#3",.5],[.5,"B3",.5],[1,"D4",2.5,"vib"]],
   [[0,"D#4",2,"vib"],[2.5,"G4",.5],[3,"A#4",.5],[3.5,"G4",.5]],
   [[0,"B3",.5],[.5,"D4",.5],[1,"F4",2.5,"vib"]],
   [[0,"F#4",2,"vib"],[2.5,"A#4",.5],[3,"C#5",.5],[3.5,"A#4",.5]],
   [[0,"D4",.5],[.5,"F4",.5],[1,"G#4",2.5,"vib"]],
   [[0,"A4",2,"vib"],[2.5,"C#5",.5],[3,"G#4",.5],[3.5,"E4",.5]],
   [[0,"F4",.5],[.5,"G#4",.5],[1,"B4",2.5,"vib"]],
   [[0,"C5",2,"vib"],[2.5,"G4",.5],[3,"B4",.5],[3.5,"G4",.5]],
   [[0,"G3",.5],[.5,"C4",.5],[1,"E4",2.5,"vib"]],
   [[0,"G4",.5],[.5,"F#4",.5],[1,"E4",2,"vib"],[3,"A#3",.5],[3.5,"C#4",.5]],
   [[0,"D4",.5],[.5,"E4",.5],[1,"F4",2.5,"vib"]],
   [[0,"A4",.5],[.5,"G#4",.5],[1,"F#4",2,"vib"],[3,"C4",.5],[3.5,"D#4",.5]],
   [[0,"B3",.5],[.5,"D4",.5],[1,"G4",2.5,"vib"]],
   [[0,"F4",.5],[.5,"G4",.5],[1,"A4",2,"vib"],[3,"E4",.5],[3.5,"G4",.5]],
   [[0,"C5",.5],[.5,"B4",.5],[1,"A4",2,"vib"],[3,"D#4",.5],[3.5,"F#4",.5]],
   [[0,"G4",.5],[.5,"A4",.5],[1,"B4",2,"vib"],[3,"A4",.5],[3.5,"F4",.5]]]
R=[[[1.5,"F3",.5],[2,"G#3",.5],[2.5,"B3",1.5]],
   [[.5,"A#3",.5],[1,"G3",.5],[1.5,"A#3",1]],
   [[1.5,"G#3",.5],[2,"B3",.5],[2.5,"D4",1.5]],
   [[.5,"A#3",.5],[1,"C#4",.5],[1.5,"A#3",1]],
   [[1.5,"B3",.5],[2,"D4",.5],[2.5,"F4",1.5]],
   [[.5,"C#4",.5],[1,"E4",.5],[1.5,"C#4",1]],
   [[1.5,"D4",.5],[2,"F4",.5],[2.5,"G#4",1.5]],
   [[.5,"E4",.5],[1,"G4",.5],[1.5,"E4",1]],
   [[1.5,"G3",.5],[2,"B3",.5],[2.5,"C4",1.5]],
   [[1.5,"C#4",.5],[2,"A#3",1]],
   [[1.5,"A3",.5],[2,"C4",.5],[2.5,"D4",1.5]],
   [[1.5,"C4",.5],[2,"A3",1]],
   [[1.5,"B3",.5],[2,"D4",.5],[2.5,"E4",1.5]],
   [[1.5,"C4",.5],[2,"E4",1]],
   [[1.5,"D#4",.5],[2,"C4",1]],
   [[1.5,"D4",.5],[2,"F4",1]]]
st=[];t=0
for c in C: st.append(t); t+=c[1]
assert t==64 and len(M)==len(R)==len(BL)==16
for i,c in enumerate(C):
    for seq in (M[i],R[i],BL[i]):
        for b,n,d,*_ in seq: assert b+d<=c[1]+1e-9,(c[0],b,n,d)
on=[0]*256
for i in range(16):
    for b,n,d,*_ in M[i]+R[i]:
        for k in range(int((st[i]+b)*4),int((st[i]+b+d)*4)): on[k]=1
assert on.count(0)==0,[k/4 for k,x in enumerate(on) if not x]
P1=[[n,st[i]+b,d] for i in range(16) for b,n,d,*_ in M[i]]
P2=[[n,st[i]+b,d] for i in range(16) for b,n,d,*_ in R[i]]
gid="jz-diminue-quatre-sorties"
i0=src.index('{id:"%s",'%gid); i1=src.index('\n{id:',i0+10); old=src[i0:i1]
assert old.rstrip().endswith('atterrissage'),old[-60:]
desc=("Le geste : quatre fois la même paire de formes, un diminué puis un maj7, trois cases plus haut à chaque fois ; en haut, une note monte d'un demi-ton : Ré → Mib, Fa → Fa#, Sol# → La, Si → Do. "
 "En B, les diminués deviennent des marches : la basse monte par demi-tons de Do à Sol, la main et la note du haut montent avec elle, et le Sol 7 ramène au début. "
 "Pour improviser : gamme diminuée ton-demi-ton sur chaque diminué, majeur sur chaque arrivée ; en B, Do majeur entre les diminués.")
new=('{id:"%s", soloAuto:true, phrase:%s, phrase2:%s,   /* v1442 : ballade à 70 bpm, 16 mesures ; A, la paire diminué → maj7 remonte de 3 cases, la note qui monte d\'un demi-ton est en haut, '
     'la basse monte comme une sensible ; v1443 : B refaite, les diminués en marches, basse qui monte par demi-tons de Do à Sol ; contrebasse */ phraseAuto:true, phraseDb:-1, soloDb:5, basseSon:"uprightReel", basseDb:7, basseHarmoniques:-4, '
     'rythmeDb:7, preset:"ballade", fondamentale:"nom", root:"C", scale:"C:0", lecons:{immobile:4, diminue:3, cadences:3, modal:4},\n'
     'name:"Un diminué, quatre sorties", tempo:70, groove:"jazz",\ndesc:"%s",\nchords:[\n'%(gid,J(P1),J(P2),desc)
     + ",\n".join('{name:"%s",beats:%d,voicing:"%s",scale:"%s",basseLigne:%s,soloEcrit:%s,soloEcrit2:%s}'%(n,b,v,sc,J(blv(n,BL[i])),J(R[i]),J(M[i])) for i,(n,b,v,sc) in enumerate(C))
     + "\n]},")
old2=old[:old.index(']},')+3]
rep(old2,new)
rep('const NOUVEAUTES=[\n["jz-carlton-quartes-sans-fonda","remix v1441"],','const NOUVEAUTES=[\n["jz-diminue-quatre-sorties","remix v1443"],   // v1443 — ballade, 16 mesures, quatre sorties puis une montée par demi-tons\n["jz-carlton-quartes-sans-fonda","remix v1441"],')
open('/tmp/t/v1443.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1443.json','w'),ensure_ascii=False)
print("ok",len(E))

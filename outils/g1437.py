import sys,json,re; sys.path.insert(0,'/tmp/t'); from lib import *
src=open('/tmp/t/v1436.html',encoding='utf-8').read(); E=[]
def rep(o,n):
    global src
    assert src.count(o)==1,(src.count(o),o[:80]); src=src.replace(o,n); E.append({"old_text":o,"new_text":n})
NOM=re.compile(r'([A-G][b#]?)')
def pc(name):
    r=NOM.match(name).group(1); b=PC[r[0]]
    return (b+(1 if r[1:]=="#" else -1 if r[1:]=="b" else 0))%12
def refnom(name): return 28+((pc(name)-4)%12)
def blv(name,notes): ref=refnom(name); return [[b,midi(x)-ref,d] for b,x,d in notes]

C=[("Cmaj9",8,"x-x-2-4-3-3","C:0"),("Em9",4,"x-x-2-4-3-2","E:5"),("Am9",4,"x-x-2-4-1-3","A:5"),("Dm9",4,"x-x-3-5-5-5","D:1"),
   ("G7b9",4,"x-x-3-4-3-4","G:harmonicMinor:4"),("Cmaj9",8,"x-x-2-4-3-3","C:0"),
   ("Cm9",8,"x-x-1-3-3-3","C:1"),("Abmaj9",8,"x-x-1-3-1-3","G#:3"),("Fm9",4,"x-x-1-1-1-3","F:1"),
   ("Bb13",4,"x-x-3-1-3-3","A#:4"),("Ebmaj9",4,"x-x-3-3-3-3","D#:0"),("Db7#11",4,"x-x-3-4-4-3","C#:melodicMinor:3")]
BL=[[[0,"C3",2],[2,"G2",2],[4,"C3",2],[6,"D3",2]],
    [[0,"E2",2],[2,"B2",2]],
    [[0,"A2",2],[2,"E3",2]],
    [[0,"D3",2],[2,"A2",2]],
    [[0,"G2",2],[2,"B2",2]],
    [[0,"C3",2],[2,"G2",2],[4,"C3",2],[6,"G2",2]],
    [[0,"C3",2],[2,"G2",2],[4,"C3",2],[6,"A#2",2]],
    [[0,"G#2",2],[2,"D#3",2],[4,"G#2",2],[6,"G2",2]],
    [[0,"F2",2],[2,"C3",2]],
    [[0,"A#2",2],[2,"F2",2]],
    [[0,"D#3",2],[2,"A#2",2]],
    [[0,"C#3",2],[2,"G#2",2]]]
M=[[[0,"E4",1],[1,"G4",2.5,"vib"],[4,"A4",.5],[4.5,"G4",.5],[5,"E4",1],[6,"D4",1.5]],
   [[0,"F#4",2,"vib"],[2.5,"B3",.5],[3,"D4",.5],[3.5,"E4",.5]],
   [[0,"G4",2,"vib"],[2.5,"E4",.5],[3,"G4",.5],[3.5,"B4",.5]],
   [[0,"A4",2,"vib"],[2.5,"F4",.5],[3,"D4",.5],[3.5,"A4",.5]],
   [[0,"G#4",2,"vib"],[2.5,"F4",.5],[3,"D4",.5],[3.5,"F4",.5]],
   [[0,"E4",1],[1,"G4",2.5,"vib"],[4,"B4",.5],[4.5,"A4",.5],[5,"G4",1],[6,"E4",1.5]],
   [[0,"D#4",1],[1,"G4",2.5,"vib"],[4,"A#4",.5],[4.5,"G4",.5],[5,"D#4",1],[6,"D4",1.5]],
   [[0,"C4",.5],[.5,"D#4",.5],[1,"G4",2.5,"vib"],[4,"A#4",.5],[4.5,"G4",.5],[5,"C5",1],[6,"D#4",1.5]],
   [[0,"G4",2,"vib"],[2.5,"C4",.5],[3,"D#4",.5],[3.5,"F4",.5]],
   [[0,"G4",2,"vib"],[2.5,"D4",.5],[3,"F4",.5],[3.5,"A#4",.5]],
   [[0,"G4",2,"vib"],[2.5,"A#3",.5],[3,"D4",.5],[3.5,"F4",.5]],
   [[0,"G4",2,"vib"],[2.5,"C#4",.5],[3,"D#4",.5],[3.5,"F4",.5]]]
R=[[[1.5,"C4",.5],[2,"D4",.5],[2.5,"E4",1.5],[6.5,"A3",.5],[7,"C4",1]],
   [[.5,"B3",.5],[1,"D4",.5],[1.5,"E4",1]],
   [[.5,"A3",.5],[1,"C4",.5],[1.5,"E4",1]],
   [[.5,"D4",.5],[1,"F4",.5],[1.5,"C4",1]],
   [[.5,"B3",.5],[1,"D4",.5],[1.5,"F4",1]],
   [[1.5,"C4",.5],[2,"E4",.5],[2.5,"D4",1.5],[6.5,"C4",.5],[7,"D4",1]],
   [[1.5,"C4",.5],[2,"D#4",.5],[2.5,"A#3",1.5],[6.5,"C4",.5],[7,"A#3",1]],
   [[1.5,"G#3",.5],[2,"C4",.5],[2.5,"D#4",1.5],[6.5,"C4",.5],[7,"A#3",1]],
   [[.5,"G#3",.5],[1,"C4",.5],[1.5,"D#4",1]],
   [[.5,"A#3",.5],[1,"D4",.5],[1.5,"F4",1]],
   [[.5,"A#3",.5],[1,"D4",.5],[1.5,"F4",1]],
   [[.5,"G#3",.5],[1,"B3",.5],[1.5,"F4",1]]]
st=[];t=0
for c in C: st.append(t); t+=c[1]
assert t==64 and len(M)==len(R)==len(BL)==12
for i,c in enumerate(C):
    for seq in (M[i],R[i],BL[i]):
        for b,n,d,*_ in seq: assert b+d<=c[1]+1e-9,(c[0],b,n,d)
on=[0]*256
for i in range(12):
    for b,n,d,*_ in M[i]+R[i]:
        for k in range(int((st[i]+b)*4),int((st[i]+b+d)*4)): on[k]=1
assert on.count(0)==0,[k/4 for k,x in enumerate(on) if not x]
P1=[[n,st[i]+b,d] for i in range(12) for b,n,d,*_ in M[i]]
P2=[[n,st[i]+b,d] for i in range(12) for b,n,d,*_ in R[i]]
gid="jz-carlton-broderie-aigues"
i0=src.index('{id:"%s",'%gid); i1=src.index('\n{id:"jz-carlton-quartes-sans-fonda"',i0); old=src[i0:i1]
assert old.endswith('"}]},'),old[-30:]
desc=("Le geste : des accords sans fondamentale sur les quatre cordes aiguës, entre les cases 1 et 5 ; c'est la contrebasse qui joue la fondamentale. "
 "Partie A : Do maj9 (x-x-2-4-3-3), Mi m9 (x-x-2-4-3-2, seul le petit doigt recule), La m9 (x-x-2-4-1-3), Ré m9 (x-x-3-5-5-5), Sol 7b9 (x-x-3-4-3-4) et le Do maj9. "
 "Partie B : le petit doigt ne quitte plus la case 3 de la corde de Mi, et un ou deux doigts bougent en dessous : Do m9 (x-x-1-3-3-3), Lab maj9 (x-x-1-3-1-3), Fa m9 (x-x-1-1-1-3), "
 "Sib 13 (x-x-3-1-3-3), Mib maj9 (x-x-3-3-3-3) et Réb 7#11 (x-x-3-4-4-3), qui revient au Do maj9 par demi-tons. "
 "À écouter : dans la partie A, la note du haut brode autour du Sol, Sol, Fa#, Sol, La, Sol#, Sol. Dans la partie B, elle ne bouge plus, mais elle change de nom à chaque accord : "
 "quinte du Do m, septième majeure du Lab, neuvième du Fa m, treizième du Sib 7, tierce du Mib, onzième augmentée du Réb 7, et de nouveau quinte du Do. "
 "Entre Do maj9 et Do m9, le Sol ne bouge pas, mais le Mi devient Mib et le Si devient Sib. En dessous, la basse descend : Do, Lab, Fa, Sib, Mib, Réb, Do. "
 "Pour improviser : Do ionien, Mi éolien, La éolien, Ré dorien, Sol phrygien dominant ; dans la partie B, Do dorien, Lab lydien, Fa dorien, Sib mixolydien, Mib ionien et Réb lydien dominant, en gardant le Sol comme repère. "
 "Tout est écrit, en ballade : la mélodie se pose sur la note du haut de chaque accord et la tient, l'autre voix répond pendant ces notes tenues. "
 "Au premier tour le sax chante et la guitare répond ; au second on échange.")
new=('{id:"%s", soloAuto:true, phrase:%s, phrase2:%s,   /* v1437 : ballade à 70 bpm, 16 mesures ; partie A, la broderie autour du Sol ; partie B, le Sol tenu sous le petit doigt '
     'pendant que six accords le renomment ; Do maj9 et La m9 corrigés (il leur manquait la neuvième), contrebasse */ phraseAuto:true, phraseDb:-1, soloDb:5, basseSon:"uprightReel", basseDb:7, basseHarmoniques:-4, '
     'rythmeDb:6, preset:"ballade", fondamentale:"nom", lecons:{voicings:3, melodique:2}, root:"C", scale:"C:0", '
     'name:"La broderie au sommet — ballade, le Sol qui reste", tempo:70, groove:"jazz",\ndesc:"%s",\nchords:[\n'%(gid,J(P1),J(P2),desc)
     + ",\n".join('{name:"%s",beats:%d,voicing:"%s",scale:"%s",basseLigne:%s,soloEcrit:%s,soloEcrit2:%s}'%(n,b,v,sc,J(blv(n,BL[i])),J(R[i]),J(M[i])) for i,(n,b,v,sc) in enumerate(C))
     + "\n]},")
rep(old,new)
rep('const NOUVEAUTES=[\n["jz-ligne-qui-monte","remix v1436"],','const NOUVEAUTES=[\n["jz-carlton-broderie-aigues","remix v1437"],   // v1437 — ballade, 16 mesures, la broderie puis le Sol tenu\n["jz-ligne-qui-monte","remix v1436"],')
open('/tmp/t/v1437.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1437.json','w'),ensure_ascii=False)
print("ok",len(E))

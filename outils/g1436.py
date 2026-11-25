import sys,json,re; sys.path.insert(0,'/tmp/t'); from lib import *
src=open('/tmp/t/v1435.html',encoding='utf-8').read(); E=[]
def rep(o,n):
    global src
    assert src.count(o)==1,(src.count(o),o[:80]); src=src.replace(o,n); E.append({"old_text":o,"new_text":n})
NOM=re.compile(r'([A-G][b#]?)')
def pc(name):
    r=NOM.match(name).group(1); b=PC[r[0]]
    return (b+(1 if r[1:]=="#" else -1 if r[1:]=="b" else 0))%12
def refnom(name): return 28+((pc(name)-4)%12)
def blv(name,notes): ref=refnom(name); return [[b,midi(x)-ref,d] for b,x,d in notes]

C=[("Am11",8,"x-x-5-5-3-3","A:5"),("G9",8,"x-x-3-4-3-5","G:4"),("Cmaj9",8,"x-x-5-7-5-7","C:0"),("E7#5",8,"x-x-6-7-5-8","E:harmonicMinor:4"),
   ("Gm9",8,"x-1-3-2-3-x","G:1"),("G9",8,"x-2-3-2-3-x","G:4"),("C7#9",4,"x-3-2-3-4-x","C:melodicMinor:6"),("Fmaj7",4,"x-x-7-5-5-x","F:3"),
   ("Bm7b5",4,"x-x-7-7-6-x","B:6"),("E9",4,"x-7-6-7-7-x","E:melodicMinor:4")]
BL=[[[0,"A2",2],[2,"E3",2],[4,"A2",2],[6,"G2",2]],
    [[0,"G2",2],[2,"D3",2],[4,"G2",2],[6,"B2",2]],
    [[0,"C3",2],[2,"G2",2],[4,"C3",2],[6,"D3",2]],
    [[0,"E2",2],[2,"G#2",2],[4,"E2",2],[6,"D3",2]],
    [[0,"G2",2],[2,"D3",2],[4,"G2",2],[6,"D3",2]],
    [[0,"G2",2],[2,"D3",2],[4,"G2",2],[6,"B2",2]],
    [[0,"C3",2],[2,"A#2",2]],
    [[0,"F2",2],[2,"C3",2]],
    [[0,"B2",2],[2,"D3",2]],
    [[0,"E2",2],[2,"B2",2]]]
# M : la mélodie, posée sur la note du haut de chaque accord
M=[[[0,"E4",1],[1,"G4",2.5,"vib"],[4,"A4",.5],[4.5,"C5",.5],[5,"B4",1],[6,"G4",1.5]],
   [[0,"F4",.5],[.5,"G4",.5],[1,"A4",2.5,"vib"],[4,"G4",.5],[4.5,"B4",.5],[5,"D5",1],[6,"A4",1.5]],
   [[0,"G4",.5],[.5,"A4",.5],[1,"B4",2.5,"vib"],[4,"D5",.5],[4.5,"A4",.5],[5,"B4",1],[6,"G4",1.5]],
   [[0,"E4",.5],[.5,"G#4",.5],[1,"C5",2.5,"vib"],[4,"D5",.5],[4.5,"C5",.5],[5,"G#4",1],[6,"E4",1.5]],
   [[0,"A#3",.5],[.5,"C4",.5],[1,"D4",2.5,"vib"],[4,"F4",.5],[4.5,"D4",.5],[5,"C4",1],[6,"A#3",1.5]],
   [[0,"A3",.5],[.5,"B3",.5],[1,"D4",2.5,"vib"],[4,"F4",.5],[4.5,"D4",.5],[5,"A3",1],[6,"B3",1.5]],
   [[0,"D#4",2,"vib"],[2.5,"A#3",.5],[3,"C4",.5],[3.5,"D#4",.5]],
   [[0,"E4",2,"vib"],[2.5,"C4",.5],[3,"D4",.5],[3.5,"E4",.5]],
   [[0,"F4",2,"vib"],[2.5,"A3",.5],[3,"D4",.5],[3.5,"F4",.5]],
   [[0,"F#4",2,"vib"],[2.5,"G#4",.5],[3,"F#4",.5],[3.5,"D4",.5]]]
# R : les réponses, dans les notes tenues ; leur dernière note dure jusqu'au retour de la mélodie
R=[[[1.5,"A3",.5],[2,"C4",.5],[2.5,"E4",1.5],[6.5,"C4",.5],[7,"D4",1]],
   [[1.5,"G3",.5],[2,"B3",.5],[2.5,"F4",1.5],[6.5,"D4",.5],[7,"E4",1]],
   [[1.5,"D4",.5],[2,"E4",.5],[2.5,"G4",1.5],[6.5,"E4",.5],[7,"D4",1]],
   [[1.5,"G#3",.5],[2,"D4",.5],[2.5,"E4",1.5],[6.5,"G#3",.5],[7,"D4",1]],
   [[1.5,"G3",.5],[2,"A#3",.5],[2.5,"F4",1.5],[6.5,"D4",.5],[7,"F4",1]],
   [[1.5,"G3",.5],[2,"B3",.5],[2.5,"F4",1.5],[6.5,"D4",.5],[7,"F4",1]],
   [[.5,"A#3",.5],[1,"C4",.5],[1.5,"G#4",1]],
   [[.5,"A3",.5],[1,"C4",.5],[1.5,"A4",1]],
   [[.5,"A3",.5],[1,"B3",.5],[1.5,"D4",1]],
   [[.5,"G#3",.5],[1,"B3",.5],[1.5,"D4",1]]]
st=[];t=0
for c in C: st.append(t); t+=c[1]
assert t==64 and len(M)==len(R)==len(BL)==10
for i,c in enumerate(C):
    for seq in (M[i],R[i],BL[i]):
        for b,n,d,*_ in seq: assert b+d<=c[1]+1e-9,(c[0],b,n,d)
on=[0]*256
for i in range(10):
    for b,n,d,*_ in M[i]+R[i]:
        for k in range(int((st[i]+b)*4),int((st[i]+b+d)*4)): on[k]=1
assert on.count(0)==0,[k/4 for k,x in enumerate(on) if not x]
P1=[[n,st[i]+b,d] for i in range(10) for b,n,d,*_ in M[i]]
P2=[[n,st[i]+b,d] for i in range(10) for b,n,d,*_ in R[i]]
gid="jz-ligne-qui-monte"
i0=src.index('{id:"%s",'%gid); i1=src.index('\n{id:"jz-carlton-broderie-aigues"',i0); old=src[i0:i1]
assert old.endswith('"}]},'),old[-30:]
desc=("Le geste : des accords sans fondamentale, c'est la contrebasse qui la joue. La m11 (x-x-5-5-3-3), Sol 9 (x-x-3-4-3-5), Do maj9 (x-x-5-7-5-7), "
 "puis Mi 7#5 (x-x-6-7-5-8) : du Do maj9 au Mi 7#5, deux doigts avancent d'une case, le Ré et le Mi restent. "
 "La partie B repart d'en bas : Sol m9 (x-1-3-2-3-x), puis Sol 9 (x-2-3-2-3-x) où un seul doigt avance d'une case, Do 7#9 (x-3-2-3-4-x) où toutes les voix bougent d'un demi-ton, "
 "Fa maj7 (x-x-7-5-5-x), Si m7b5 (x-x-7-7-6-x) et Mi 9 (x-7-6-7-7-x) qui ramène au La m11. "
 "À écouter : la note du haut monte. Dans la partie A, elle monte dans la gamme : Sol, La, Si, Do. Dans la partie B, elle monte par demi-tons : Ré, Ré, Ré#, Mi, Fa, Fa#, et le Fa# du Mi 9 monte au Sol du début. "
 "Entre Sol m9 et Sol 9, le Ré du haut ne bouge pas, mais le Sib devient Si : la même phrase revient, éclairée. "
 "Pendant que le haut monte, la basse descend par quartes : Sol, Do, Fa, Si, Mi, La. "
 "Pour improviser : La éolien, Sol mixolydien, Do ionien, puis Mi phrygien dominant sur le Mi 7#5 ; dans la partie B, Sol dorien, Sol mixolydien, Do altéré, Fa lydien, Si locrien et Mi mixolydien b6. "
 "Tout est écrit, en ballade : la mélodie se pose sur la note du haut de chaque accord et la tient, l'autre voix répond pendant ces notes tenues. "
 "Au premier tour le sax chante et la guitare répond ; au second on échange.")
new=('{id:"%s", soloAuto:true, phrase:%s, phrase2:%s,   /* v1436 : ballade à 70 bpm, 16 mesures, partie B où la ligne monte par demi-tons '
     'pendant que la basse descend par quartes ; Mi 7#5 à la place du Mi 7 (sans Fa) nommé 7b9, contrebasse */ phraseAuto:true, phraseDb:-1, soloDb:5, basseSon:"uprightReel", basseDb:7, basseHarmoniques:-4, '
     'rythmeDb:6, preset:"ballade", fondamentale:"nom", lecons:{voicings:3, melodique:2}, root:"A", scale:"A:5", '
     'name:"La ligne qui monte — ballade sans fondamentale", tempo:70, groove:"jazz",\ndesc:"%s",\nchords:[\n'%(gid,J(P1),J(P2),desc)
     + ",\n".join('{name:"%s",beats:%d,voicing:"%s",scale:"%s",basseLigne:%s,soloEcrit:%s,soloEcrit2:%s}'%(n,b,v,sc,J(blv(n,BL[i])),J(R[i]),J(M[i])) for i,(n,b,v,sc) in enumerate(C))
     + "\n]},")
rep(old,new)
rep('const NOUVEAUTES=[\n["jz-ligne-qui-descend","remix v1435"],','const NOUVEAUTES=[\n["jz-ligne-qui-monte","remix v1436"],   // v1436 — ballade, 16 mesures, la ligne par demi-tons, basse par quartes\n["jz-ligne-qui-descend","remix v1435"],')
open('/tmp/t/v1436.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1436.json','w'),ensure_ascii=False)
print("ok",len(E))

import sys,json,re; sys.path.insert(0,'/tmp/t'); from lib import *
src=open('/tmp/t/v1432.html',encoding='utf-8').read(); E=[]
def rep(o,n):
    global src
    assert src.count(o)==1,(src.count(o),o[:80]); src=src.replace(o,n); E.append({"old_text":o,"new_text":n})
NOM=re.compile(r'([A-G][b#]?)')
def pc(name):
    r=NOM.match(name).group(1); b=PC[r[0]]
    return (b+(1 if r[1:]=="#" else -1 if r[1:]=="b" else 0))%12
def refnom(name): return 28+((pc(name)-4)%12)
def blv(name,notes): ref=refnom(name); return [[b,midi(x)-ref,d] for b,x,d in notes]

C=[("Gmaj9",8,"x-x-4-4-3-5","G:0"),("Em9",8,"x-x-4-4-3-3","E:5"),("Am11",8,"x-5-5-5-5-x","A:1"),("D7b9",8,"x-5-4-5-4-x","D:harmonicMinor:4"),
   ("Cmaj9",8,"x-x-2-4-3-3","C:3"),("Cm9",8,"x-x-1-3-3-3","C:1"),("Bm9",4,"x-x-0-2-2-2","B:1"),("E7b9",4,"x-7-6-7-6-x","E:harmonicMinor:4"),
   ("Am11",4,"x-5-5-5-5-x","A:1"),("D7b9",4,"x-5-4-5-4-6","D:harmonicMinor:4")]
BL=[[[0,"G2",2],[2,"D3",2],[4,"G2",2],[6,"F#2",2]],
    [[0,"E2",2],[2,"B2",2],[4,"E2",2],[6,"G2",2]],
    [[0,"A2",2],[2,"E3",2],[4,"A2",2],[6,"C3",2]],
    [[0,"D3",2],[2,"A2",2],[4,"D3",2],[6,"A2",2]],
    [[0,"C3",2],[2,"G2",2],[4,"C3",2],[6,"G2",2]],
    [[0,"C3",2],[2,"G2",2],[4,"C3",2],[6,"G2",2]],
    [[0,"B2",2],[2,"F#2",2]],
    [[0,"E2",2],[2,"B2",2]],
    [[0,"A2",2],[2,"E2",2]],
    [[0,"D3",2],[2,"F#2",2]]]
# M : la mélodie (sax au tour 1, guitare au tour 2) ; elle se pose sur la note du haut de l'accord et la tient
M=[[[0,"B4",1],[1,"A4",2.5,"vib"],[4,"B4",1],[5,"A4",.5],[5.5,"F#4",.5],[6,"D4",1.5]],
   [[0,"B4",.5],[.5,"A4",.5],[1,"G4",2.5,"vib"],[4,"E4",.5],[4.5,"F#4",.5],[5,"G4",.5],[5.5,"B4",1.5,"vib"],[7,"A4",.5],[7.5,"B4",.5]],
   [[0,"G4",.5],[.5,"A4",.5],[1,"E4",2.5,"vib"],[4,"C5",1],[5,"B4",.5],[5.5,"A4",.5],[6,"G4",1.5]],
   [[0,"C4",.5],[.5,"D4",.5],[1,"D#4",2.5,"vib"],[4,"F#4",.5],[4.5,"A4",.5],[5,"C5",1],[6,"A4",1.5,"vib"]],
   [[0,"E4",.5],[.5,"F#4",.5],[1,"G4",2.5,"vib"],[4,"B4",.5],[4.5,"A4",.5],[5,"G4",1],[6,"E4",1.5]],
   [[0,"D#4",.5],[.5,"F4",.5],[1,"G4",2.5,"vib"],[4,"A#4",.5],[4.5,"A4",.5],[5,"G4",1],[6,"D#4",1.5]],
   [[0,"F#4",2,"vib"],[3,"B4",.5],[3.5,"A4",.5]],
   [[0,"F4",2,"vib"],[2.5,"D4",.5],[3,"F4",.5],[3.5,"D4",.5]],
   [[0,"E4",2,"vib"],[2.5,"G4",.5],[3,"A4",.5],[3.5,"E4",.5]],
   [[0,"D#4",2,"vib"],[2.5,"F#4",.5],[3,"A#4",.5],[3.5,"C5",.5]]]
# R : les réponses, glissées dans les notes tenues de la mélodie
R=[[[1.5,"B3",.5],[2,"D4",.5],[2.5,"F#4",1.5],[6.5,"F#4",.5],[7,"A4",1]],
   [[1.5,"E4",.5],[2,"B3",.5],[2.5,"D4",1.5],[6,"E4",.5],[6.5,"G4",.5]],
   [[1.5,"A3",.5],[2,"C4",.5],[2.5,"G4",1.5],[7,"D4",.5],[7.5,"E4",.5]],
   [[1.5,"A3",.5],[2,"C4",.5],[2.5,"F#4",1.5],[6.5,"D4",.5],[7,"F#4",1]],
   [[1.5,"C4",.5],[2,"E4",.5],[2.5,"B4",1.5],[6.5,"G4",.5],[7,"B4",1]],
   [[1.5,"C4",.5],[2,"D#4",.5],[2.5,"A#4",1.5],[6.5,"G4",.5],[7,"A#4",1]],
   [[.5,"B3",.5],[1,"D4",.5],[1.5,"A4",1.5]],
   [[.5,"G#3",.5],[1,"B3",.5],[1.5,"D4",1]],
   [[.5,"A3",.5],[1,"C4",.5],[1.5,"G4",1]],
   [[.5,"A3",.5],[1,"C4",.5],[1.5,"F#4",1]]]
st=[];t=0
for c in C: st.append(t); t+=c[1]
assert t==64 and len(M)==len(R)==len(BL)==10
for i,c in enumerate(C):
    for seq in (M[i],R[i],BL[i]):
        for b,n,d,*_ in seq: assert b+d<=c[1]+1e-9,(c[0],b,n,d)
P1=[[n,st[i]+b,d] for i in range(10) for b,n,d,*_ in M[i]]
P2=[[n,st[i]+b,d] for i in range(10) for b,n,d,*_ in R[i]]
gid="jz-ligne-qui-descend"
i0=src.index('{id:"%s",'%gid); i1=src.index('\n{id:"jz-ligne-qui-monte"',i0); old=src[i0:i1]
assert old.endswith('"}]},'),old[-30:]
desc=("Le geste : quatre accords sans fondamentale, c'est la contrebasse qui la joue. Sol maj9 (x-x-4-4-3-5), puis Mi m9 (x-x-4-4-3-3) : seul le petit doigt bouge. "
 "Ensuite La m11 en un seul barré (x-5-5-5-5-x) et Ré 7b9 (x-5-4-5-4-x). La partie B part vers le Do : Do maj9 (x-x-2-4-3-3), Do m9 (x-x-1-3-3-3), "
 "puis la même forme qui glisse d'une case pour Si m9 (x-x-0-2-2-2), Mi 7b9 (x-7-6-7-6-x), et La m11 et Ré 7b9 qui ramènent au Sol ; sur ce dernier Ré 7b9, le petit doigt ajoute un Sib en case 6 de la corde de Mi (x-5-4-5-4-6). "
 "À écouter : la note du haut descend. Dans la partie A, elle descend dans la gamme : La, Sol, Mi, Ré#. Dans la partie B, elle descend par demi-tons : Sol, Sol, Fa#, Fa, Mi, Ré#. "
 "Entre Do maj9 et Do m9, le Sol du haut ne bouge pas, mais le Mi devient Mib et le Si devient Sib : la même phrase revient, assombrie. "
 "Pour improviser : Sol ionien, Mi éolien, La dorien, puis Ré phrygien dominant sur le Ré 7b9 ; dans la partie B, Do lydien, Do dorien, Si dorien et Mi phrygien dominant. "
 "Tout est écrit, en ballade : la mélodie se pose sur la note du haut de chaque accord et la tient, l'autre voix répond pendant ces notes tenues. "
 "Au retour vers le Sol, chaque voix bouge d'un demi-ton : Sib → La en haut, Mib → Ré, Do → Si, la basse monte Fa# → Sol, et la mélodie descend Do, Si, La. Au premier tour le sax chante et la guitare répond ; au second on échange.")
new=('{id:"%s", soloAuto:true, phrase:%s, phrase2:%s,   /* v1435 : retour vers le Sol par demi-tons (Sib ajouté au dernier Ré 7b9) ; v1434 : réponses prolongées, plus de trous ; v1433 : ballade en Sol (une quarte plus bas, la version en Do était trop aiguë), 16 mesures, '
     'partie B où la ligne descend par demi-tons, contrebasse */ phraseAuto:true, phraseDb:-1, soloDb:5, basseSon:"uprightReel", basseDb:7, basseHarmoniques:-4, '
     'rythmeDb:6, preset:"ballade", fondamentale:"nom", lecons:{voicings:3, melodique:2}, root:"G", scale:"G:0", '
     'name:"La ligne qui descend — ballade sans fondamentale", tempo:70, groove:"jazz",\ndesc:"%s",\nchords:[\n'%(gid,J(P1),J(P2),desc)
     + ",\n".join('{name:"%s",beats:%d,voicing:"%s",scale:"%s",basseLigne:%s,soloEcrit:%s,soloEcrit2:%s}'%(n,b,v,sc,J(blv(n,BL[i])),J(R[i]),J(M[i])) for i,(n,b,v,sc) in enumerate(C))
     + "\n]},")
rep(old,new)
rep('const NOUVEAUTES=[\n["jz-ii-v-i-maj","remix v1432"],','const NOUVEAUTES=[\n["jz-ligne-qui-descend","remix v1435"],   // v1435 — ballade en Sol, 16 mesures, la ligne par demi-tons, retour adouci\n["jz-ii-v-i-maj","remix v1432"],')
open('/tmp/t/v1435.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1435.json','w'),ensure_ascii=False)
print("ok",len(E))

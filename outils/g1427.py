import sys,json,re; sys.path.insert(0,'/tmp/t'); from lib import *
src=open('/home/claude/work7/gmm-v1426.html').read(); E=[]
def rep(o,n):
    global src
    assert src.count(o)==1,(src.count(o),o[:80]); src=src.replace(o,n); E.append({"old_text":o,"new_text":n})
NOMPC={'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11}
def refnom(name):
    r=re.match(r'([A-G][#b]?)',name).group(1).replace('Ab','G#').replace('Eb','D#').replace('Bb','A#'); return 28+((NOMPC[r]-4)%12)
def reg(m):
    while m>45: m-=12
    return m
def blv(v,notes): ref=reg(low(v)-12); return [[b,midi(x)-ref,d] for b,x,d in notes]
def starts(C):
    s=[];t=0
    for c in C: s.append(t); t+=c[1]
    return s,t
def glob(C,cells): st,_=starts(C); return [[n,st[i]+b,d] for i,c in enumerate(cells) for b,n,d,*_ in c]
def build(gid,C,B,S1,S2,P1,P2,nom,cmt,descold,descnew,extra=""):
    global src
    i0=src.index('{id:"%s",'%gid); i1=src.index(']}]},',i0)+5; old=src[i0:i1]; head=old[:old.index('chords:[')]
    head=re.sub(r'phrase:\[.*?\]\], phrase2:\[.*?\]\],',lambda m:'phrase:%s, phrase2:%s,'%(J(P1),J(P2)),head,count=1)
    k=head.index('*/'); head=head[:k]+'; '+cmt+' '+head[k:]
    if extra: head=head.replace('basseDb:-3,',extra,1)
    assert head.count(descold)==1,(gid,descold); head=head.replace(descold,descnew)
    lines=[]
    for i,(n,b,v,sc) in enumerate(C):
        bl=[[bb,midi(x)-refnom(n),d] for bb,x,d in B[i]] if nom else blv(v,B[i])
        lines.append('{name:"%s",beats:%d,voicing:"%s",scale:"%s",basseLigne:%s,soloEcrit:%s,soloEcrit2:%s}'%(n,b,v,sc,J(bl),J(S1[i]),J(S2[i])))
    rep(old, head+"chords:["+",".join(lines)+"]},")
# ---------- Quartal ----------
CQ=[("Am11",4,"5-x-5-5-3-x","A:1"),("Dsus2",4,"x-x-0-2-3-0","A:1"),("Em11",4,"7-x-7-7-8-x","A:1"),("G6/9",4,"3-x-2-2-3-3","A:1"),
    ("Cmaj9#11",4,"x-3-4-4-3-x","A:1"),("Bm7",4,"x-2-4-2-3-2","A:1"),("Am11",4,"5-x-5-5-3-x","A:1"),("Dsus2",4,"x-x-0-2-3-0","A:1")]
BQ=[[[0,n,4]] for n in ["A2","D3","E2","G2","C3","B2","A2","D3"]]
SAX=[[[0,"E4",.5],[.5,"A4",.5],[1,"D5",1]],[[.5,"E4",.5],[1,"A4",.5],[1.5,"D5",1]],[[0,"E4",1],[1,"A4",1],[2,"D5",2,"vib"]],[[0,"E4",.5],[.5,"A4",.5],[1,"D5",3,"vib"]],
     [[0,"D5",.5],[.5,"A4",.5],[1,"E4",1]],[[.5,"D5",.5],[1,"A4",.5],[1.5,"E4",1]],[[0,"D5",1],[1,"A4",1],[2,"E4",2,"vib"]],[[0,"D5",.5],[.5,"A4",.5],[1,"E4",3,"vib"]]]
ECHO=[[[2,"A4",.5],[2.5,"D5",.5],[3,"G5",1,"vib"]],[[2.5,"A4",.5],[3,"D5",.5],[3.5,"G5",.5]],[],[[2,"G5",2,"vib"]],
      [[2,"G4",.5],[2.5,"D4",.5],[3,"A3",1,"vib"]],[[2.5,"G4",.5],[3,"D4",.5],[3.5,"A3",.5]],[],[[2,"A3",2,"vib"]]]
build("jz-quartal-dorien",CQ,BQ,ECHO,SAX,glob(CQ,SAX),glob(CQ,ECHO),True,"v1427 : 8 mesures, la réponse sur Do maj9#11, Si m7, La m11, Ré sus2, le motif à l'envers",
 "Seul son rythme bouge : posé, décalé d'une croche, étiré, puis tenu.",
 "Seul son rythme bouge : posé, décalé d'une croche, étiré, puis tenu. La seconde moitié répond sur Do maj9#11 (x-3-4-4-3-x), Si m7 (x-2-4-2-3-2), La m11 et Ré sus2 : les trois mêmes notes y sont encore toutes, et le motif se joue à l'envers, Ré La Mi, qui descend ; l'écho aussi, Sol Ré La.")
# ---------- ii-V altéré ----------
D=("Dm7b5",2,"x-5-6-5-6-x","D:melodicMinor:5"); G=("G7alt",2,"3-x-3-4-4-4","G:melodicMinor:6"); Cm=("CmMaj7",4,"x-3-1-0-0-x","C:melodicMinor:0")
CA=[D,G,Cm,D,G,Cm,("Abmaj7",4,"4-x-5-5-4-x","G#:3"),("G7alt",4,"3-x-3-4-4-4","G:melodicMinor:6"),D,G,Cm]
BA=[[[0,"D3",2]],[[0,"G2",2]],[[0,"C3",2],[2,"G2",2]],[[0,"D3",2]],[[0,"G2",2]],[[0,"C3",2],[2,"G2",2]],[[0,"G#2",2],[2,"D#3",2]],[[0,"G2",2],[2,"C#3",2]],[[0,"D3",2]],[[0,"G2",2]],[[0,"C3",2],[2,"G2",2]]]
pD=[[0,"F4",.5],[.5,"G#4",.5],[1,"C5",1]]; pG=[[0,"B4",.5],[.5,"G#4",.5],[1,"F4",.5],[1.5,"D#4",.5]]; pC=[[0,"G4",1],[1,"B4",3,"vib"]]
PA=[pD,pG,pC,[[0,"C5",.5],[.5,"G#4",.5],[1,"F4",1]],[[0,"B4",1],[1,"C#5",.5],[1.5,"D#5",.5]],[[0,"B4",4,"vib"]],
    [[0,"C5",1],[1,"G4",3,"vib"]],[[0,"G#4",.5],[.5,"F4",.5],[1,"D#4",.5],[1.5,"C#4",.5],[2,"B3",1.5],[3.5,"D#4",.5]],pD,pG,pC]
HA=[[],[],[[1,"B3",3,"vib"]],[],[],[[1,"B3",3,"vib"]],[[0,"G3",4,"vib"]],[[0,"B3",2,"vib"]],[],[],[[1,"B3",3,"vib"]]]
build("jz-ii-v-altere",CA,BA,HA,PA,glob(CA,PA),glob(CA,HA),False,"v1427 : 8 mesures, pont sur Lab maj7 et Sol 7 altéré tenu",
 "Le geste : Ré m7b5, Sol 7 altéré, puis Do mineur maj7 avec des cordes à vide.",
 "Le geste : Ré m7b5, Sol 7 altéré, puis Do mineur maj7 avec des cordes à vide, deux fois ; puis un pont, Lab maj7 et un long Sol 7 altéré, et la cadence revient.")
rep_ok=True
# ---------- Constant lydien ----------
cC=("Cmaj9#11",4,"x-3-4-4-3-x","C:3"); cF=("Fmaj9#11",4,"x-8-9-9-8-x","F:3"); cBb=("Bbmaj9#11",4,"x-1-2-2-1-x","A#:3"); cEb=("Ebmaj9#11",4,"x-6-7-7-6-x","D#:3")
CL=[cC,cF,cBb,cEb,cEb,cBb,cF,cC]
BL=[[[0,n,2],[2,n,2]] for n in ["C3","F2","A#2","D#2","D#2","A#2","F2","C3"]]
LA=[[[0,"C5",1],[1,"B4",.5],[1.5,"A4",.5],[2,"G4",.5],[2.5,"A4",.5],[3,"F#4",1]],
   [[0,"F4",1],[1,"G4",.5],[1.5,"A4",.5],[2,"C5",.5],[2.5,"A4",.5],[3,"B4",1]],
   [[0,"A#4",1],[1,"C5",.5],[1.5,"A4",.5],[2,"G4",.5],[2.5,"F4",.5],[3,"E4",1]],
   [[0,"D#4",1],[1,"F4",.5],[1.5,"G4",.5],[2,"A#4",.5],[2.5,"G4",.5],[3,"A4",1]],
   [[0,"A4",1],[1,"G4",.5],[1.5,"F4",.5],[2,"G4",.5],[2.5,"F4",.5],[3,"D#4",1]],
   [[0,"E4",1],[1,"F4",.5],[1.5,"G4",.5],[2,"C5",.5],[2.5,"A4",.5],[3,"A#4",1]],
   [[0,"B4",1],[1,"A4",.5],[1.5,"G4",.5],[2,"E4",.5],[2.5,"G4",.5],[3,"F4",1]],
   [[0,"F#4",1],[1,"G4",.5],[1.5,"A4",.5],[2,"B4",.5],[2.5,"A4",.5],[3,"C5",1]]]
HL=[[[0,"D5",4,"vib"]]]*8
build("jz-constant-lydien",CL,BL,HL,LA,glob(CL,LA),glob(CL,[[[0,"D5",4]]]*8),False,"v1427 : 8 mesures, aller puis retour en miroir ; basse enregistrée",
 "Sur Mib, la #11 est La : la logique voudrait qu'il tombe sur Lab, mais la grille revient au Do, et le La remonte vers le Do.",
 "Sur Mib, la #11 est La. Puis la grille revient sur ses pas, Mib, Sib, Fa, Do, et le geste devient son miroir : c'est la fondamentale qui monte d'un demi-ton pour devenir la #11 de l'accord suivant (Mib → Mi, Sib → Si, Fa → Fa#).",extra="basseSon:\"fingerReel\", basseDb:2, basseHarmoniques:-16,")
src2=src
for gid,v in [("jz-quartal-dorien","v1427 — 8 mesures, motif à l'envers"),("jz-ii-v-altere","v1427 — 8 mesures, pont"),("jz-constant-lydien","v1427 — 8 mesures, aller-retour")]:
    m=re.search(r'\["%s","remix v14\d\d"\],[^\n]*\n'%gid,src); rep(m.group(0),'["%s","remix v1427"],   // %s\n'%(gid,v))
open('/home/claude/work7/gmm-v1427.html','w').write(src); json.dump(E,open('/home/claude/work7/e1427.json','w'),ensure_ascii=False)

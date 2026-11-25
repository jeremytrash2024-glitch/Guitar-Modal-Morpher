import sys,json,re; sys.path.insert(0,'/tmp/t'); from lib import *
src=open('/home/claude/work7/gmm-v1431.html').read(); E=[]
def rep(o,n):
    global src
    assert src.count(o)==1,(src.count(o),o[:80]); src=src.replace(o,n); E.append({"old_text":o,"new_text":n})
def reg(m):
    while m>45: m-=12
    return m
def blv(v,notes): ref=reg(low(v)-12); return [[b,midi(x)-ref,d] for b,x,d in notes]
exec(open('/tmp/t/a1431.txt').read().split('S1=')[0])
Dm=("Dm7",4,"x-5-3-5-3-x","D:1"); G7=("G7",4,"3-x-3-4-3-x","G:4"); Cj=("Cmaj7",4,"x-3-5-4-5-3","C:0"); Am=("Am7",4,"5-x-5-5-5-x","A:5")
Fj=("Fmaj7",4,"x-x-3-5-5-5","F:3"); Fm=("Fm7",2,"1-x-1-1-1-x","F:1"); Bb7=("Bb7",2,"x-1-3-1-3-1","A#:melodicMinor:3"); Em=("Em7",4,"x-7-5-7-5-x","E:2"); A7=("A7",4,"5-x-5-6-5-x","A:4")
C=[Dm,G7,Cj,Am,Dm,G7,Cj,Cj,Fj,Fm,Bb7,Em,A7,Dm,G7,Cj,Cj]
BB={"Dm7":[[0,"D3",2],[2,"A2",2]],"G7":[[0,"G2",2],[2,"D3",2]],"Cmaj7":[[0,"C3",2],[2,"G2",2]],"Am7":[[0,"A2",2],[2,"E3",2]],
    "Fmaj7":[[0,"F2",2],[2,"C3",2]],"Fm7":[[0,"F2",2]],"Bb7":[[0,"A#2",2]],"Em7":[[0,"E2",2],[2,"B2",2]],"A7":[[0,"A2",2],[2,"E3",2]]}
BL=[BB[c[0]] for c in C]
MELB=[[[0,"C5",1],[1,"A4",1],[2,"E5",2,"vib"]],
      [[0,"D#5",2,"vib"]],
      [[0,"D5",1],[1,"F5",1]],
      [[0,"E5",2.5,"vib"],[3,"D5",.5],[3.5,"B4",.5]],
      [[0,"C#5",1.5,"vib"],[1.5,"E5",.5],[2,"G5",1.5],[3.5,"E5",.5]],
      [[0,"F5",1.5,"vib"],[1.5,"E5",.5],[2,"D5",.5],[2.5,"A4",.5],[3,"C5",1]],
      [[0,"B4",2.5,"vib"],[3,"D5",.5],[3.5,"F5",.5]],
      [[0,"E5",2.5,"vib"],[3,"D5",.5],[3.5,"C5",.5]],
      [[0,"G4",1],[1,"C5",3,"vib"]]]
REPB=[[[2.5,"G4",.5],[3,"A4",1]],
      [[.5,"G4",.5],[1,"G#4",1]],
      [],
      [[.5,"G4",.5],[1,"B4",1]],
      [[.5,"G4",1]],
      [[.5,"A4",.5],[1,"C5",.5]],
      [[.5,"G4",.5],[1,"F4",.5],[1.5,"D4",1]],
      [[.5,"G4",.5],[1,"B4",.5],[1.5,"C5",1]],
      [[1.5,"G4",.5],[2,"E4",.5],[3,"G4",1,"vib"]]]
M=MEL+MELB; R=REP+REPB
st=[];t=0
for c in C: st.append(t); t+=c[1]
assert t==64 and len(M)==17 and len(R)==17
P1=[[n,st[i]+b,d] for i in range(17) for b,n,d,*_ in M[i]]
P2=[[n,st[i]+b,d] for i in range(17) for b,n,d,*_ in R[i]]
gid="jz-ii-v-i-maj"
i0=src.index('{id:"%s",'%gid); i1=src.index('\n]},',i0)+4; old=src[i0:i1]; head=old[:old.index('chords:[')]
head=re.sub(r'phrase:\[.*?\]\], phrase2:\[.*?\]\],',lambda m:'phrase:%s, phrase2:%s,'%(J(P1),J(P2)),head,count=1)
head=head.replace("réponses dans ses notes tenues */","réponses dans ses notes tenues ; v1432 : partie B (Fa maj7, Fa m7 Sib 7, Mi m7, La 7, puis le ii-V-I), le Mi qui devient Mib */",1)
head=head.replace("puis La m7 (un seul barré) qui relance, et le même chemin une seconde fois.","puis La m7 (un seul barré) qui relance, et le même chemin une seconde fois. Puis une partie B qui part ailleurs et revient : Fa maj7 (x-x-3-5-5-5), Fa m7 (1-x-1-1-1-x) et Sib 7, Mi m7 et La 7 (les formes du Ré m7 et du Sol 7, deux cases plus haut), et le ii-V-I qui ramène au Do.",1)
head=head.replace("Pendant chaque note tenue,","Dans la partie B, une seule note change de couleur : le Mi, tenu sur Fa maj7, descend à Mib sur Fa m7 (l'accord du IV devient mineur, le moment qui serre le cœur), puis redevient Mi sur Mi m7. Pendant chaque note tenue,",1)
head=head.replace("septième du La m.","septième du La m, et dans la partie B neuvième du Fa, treizième du Sib 7, tierce du Mi m, septième du La 7.",1)
for k in ['v1432','partie B qui part','Mib sur Fa m7','treizième du Sib 7']: assert k in head,k
lines=['{name:"%s",beats:%d,voicing:"%s",scale:"%s",basseLigne:%s,soloEcrit:%s,soloEcrit2:%s}'%(n,b,v,sc,J(blv(v,BL[i])),J(R[i]),J(M[i])) for i,(n,b,v,sc) in enumerate(C)]
rep(old, head+"chords:[\n"+",\n".join(lines)+"\n]},")
rep('["jz-ii-v-i-maj","remix v1431"],   // v1431 — contrebasse, mélodie et réponses réécrites\n','["jz-ii-v-i-maj","remix v1432"],   // v1432 — partie B ajoutée, 16 mesures\n')
open('/home/claude/work7/gmm-v1432.html','w').write(src); json.dump(E,open('/home/claude/work7/e1432.json','w'),ensure_ascii=False)

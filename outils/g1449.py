import json,re
src=open('/tmp/t/v1448.html',encoding='utf-8').read(); E=[]
def rep(o,n):
    global src
    assert src.count(o)==1,(src.count(o),o[:90]); src=src.replace(o,n); E.append({"old_text":o,"new_text":n})
i=src.index('SCALES = {'); j=src.index('japanese: { name: "Japonaises", modes: [',i); k=src.index('\n]}',j)
last=src[src.rindex('\n',0,k):k+3]   # dernière ligne de la famille japonaise + fermeture
assert src.count(last)==1, last
rep(last, last.replace('\n]}','\n]},\nbebop: { name: "Bebop", modes: [   // v1449 — gammes à huit notes : une note de passage en plus, et les notes de l\'accord tombent sur les temps\n{ name: "Bebop dominante", formula: [0,2,4,5,7,9,10,11], intervals: ["R","2","3","4","5","6","b7","7"] }   // mixolydien + 7e majeure de passage\n]}',1))
rep('"japanese","enigmatic"];   // v1124 : enigmatic en dernier, les identifiants existants ne bougent pas','"japanese","enigmatic","bebop"];   // v1124 : enigmatic en dernier, les identifiants existants ne bougent pas ; v1449 : bebop à la suite')
g='{id:"jz-carlton-quartes-sans-fonda",'; a=src.index(g); b=src.index('\n]},',a)
blk=src[a:b]
nb=blk.replace('{name:"Bb9",beats:8,voicing:"x-5-6-5-6-x",scale:"A#:4"','{name:"Bb9",beats:8,voicing:"x-5-6-5-6-x",scale:"A#:bebop:0"')\
      .replace('{name:"Eb9",beats:8,voicing:"x-6-5-6-6-x",scale:"D#:4"','{name:"Eb9",beats:8,voicing:"x-6-5-6-6-x",scale:"D#:bebop:0"')\
      .replace('{name:"A7",beats:8,voicing:"x-x-5-6-5-x",scale:"A:melodicMinor:4"','{name:"A7",beats:8,voicing:"x-x-5-6-5-x",scale:"A:bebop:0"')\
      .replace('["G4",57,.5],["F4",57.5,.5],["E4",58,.5]','["G4",57,.5],["F#4",57.5,.5],["E4",58,.5]')\
      .replace('[1,"G4",.5],[1.5,"F4",.5],[2,"E4",.5],[2.5,"D4",.5],[3,"C#4",.5],[3.5,"B3",.5]','[1,"G4",.5],[1.5,"F#4",.5],[2,"E4",.5],[2.5,"D4",.5],[3,"C#4",.5],[3.5,"B3",.5]')\
      .replace("En B, la gamme bebop dominante (mixolydien + 7e majeure de passage) sur Sib 9, Mib 9 et La 7","En B, la gamme bebop dominante (mixolydien + 7e majeure de passage, affichée sur le manche) sur Sib 9, Mib 9 et La 7")
assert nb.count('bebop:0')==3 and nb.count('"F#4",57.5')==1 and 'affichée sur le manche' in nb, (nb.count('bebop:0'),)
# éditions ciblées dans le bloc
for o,n in [('scale:"A#:4",basseLigne:[[0,12,2],[2,7,2],[4,12,2],[6,7,2]],soloEcrit:[[0,"D4",3.5]','scale:"A#:bebop:0",basseLigne:[[0,12,2],[2,7,2],[4,12,2],[6,7,2]],soloEcrit:[[0,"D4",3.5]'),
            ('scale:"D#:4",basseLigne:[[0,12,2],[2,7,2],[4,12,2],[6,7,2]],soloEcrit:[[0,"G4",3.5]','scale:"D#:bebop:0",basseLigne:[[0,12,2],[2,7,2],[4,12,2],[6,7,2]],soloEcrit:[[0,"G4",3.5]'),
            ('{name:"A7",beats:8,voicing:"x-x-5-6-5-x",scale:"A:melodicMinor:4"','{name:"A7",beats:8,voicing:"x-x-5-6-5-x",scale:"A:bebop:0"'),
            ('["G4",57,.5],["F4",57.5,.5],["E4",58,.5]','["G4",57,.5],["F#4",57.5,.5],["E4",58,.5]'),
            ('[0,"A4",.5],[.5,"G#4",.5],[1,"G4",.5],[1.5,"F4",.5],[2,"E4",.5]','[0,"A4",.5],[.5,"G#4",.5],[1,"G4",.5],[1.5,"F#4",.5],[2,"E4",.5]'),
            ("En B, la gamme bebop dominante (mixolydien + 7e majeure de passage) sur Sib 9, Mib 9 et La 7","En B, la gamme bebop dominante (mixolydien + 7e majeure de passage, affichée sur le manche) sur Sib 9, Mib 9 et La 7")]:
    rep(o,n)
assert src[a:src.index('\n]},',a)]==nb
open('/tmp/t/v1449.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1449.json','w'),ensure_ascii=False)
print('ok',len(E))

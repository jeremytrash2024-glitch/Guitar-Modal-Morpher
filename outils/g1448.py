import json
src=open('/tmp/t/v1447.html',encoding='utf-8').read(); E=[]
def rep(o,n):
    global src
    assert src.count(o)==1,(src.count(o),o[:80]); src=src.replace(o,n); E.append({"old_text":o,"new_text":n})
rep('''  ternaire:{coups:[[0,"don",1.0],[0.667,"ten",0.26],[1,"ten",0.3],[1.667,"ten",0.24],[2,"don",0.75],[2.667,"ten",0.26],[3,"ten",0.3],[3.667,"ten",0.28]]}
};''','''  ternaire:{coups:[[0,"don",1.0],[0.667,"ten",0.26],[1,"ten",0.3],[1.667,"ten",0.24],[2,"don",0.75],[2.667,"ten",0.26],[3,"ten",0.3],[3.667,"ten",0.28]]}
};
// v1448 — étape 2 : une mesure appelle, la suivante répond (les mesures impaires jouent la réponse)
const TAIKO_REPONSES={
  lent:    [[0,"don",0.9],[2.5,"don",0.42],[3.5,"ten",0.3]],
  fete:    [[0,"don",1.0],[1,"ten",0.3],[1.5,"ten",0.26],[2,"don",0.7],[3,"don",0.75],[3.5,"ten",0.3]],
  moteur:  [[0,"don",1.0],[0.5,"ten",0.24],[1,"don",0.7],[1.5,"ten",0.24],[2,"ten",0.24],[2.5,"don",0.75],[3,"ten",0.24],[3.5,"ten",0.28]],
  ternaire:[[0,"don",1.0],[0.667,"ten",0.24],[1,"ten",0.3],[1.667,"don",0.6],[2,"don",0.75],[3,"ten",0.3],[3.667,"ten",0.3]]
};''')
rep('''function _scheduleTaikoBar(barStart, barBeats, beatSec, derniere, chord){
  if(!_gridTaikoOn) return;
  try{
    const T=b=>barStart+b*beatSec+(Math.random()-0.5)*0.006, bb=barBeats;
    const id=_taikoMotifPour(chord, bb), M=TAIKO_MOTIFS[id];
    let coups=(id==="ternaire" && bb===3) ? [[0,"don",1.0],[1,"ten",0.3],[2,"ten",0.3]]
             : ((derniere && M.fin) ? M.fin : M.coups).filter(c=>c[0]<bb);
    if(!coups.length || coups[0][0]!==0) coups=[[0,"don",1.0]].concat(coups);
    const roule=derniere && id!=="lent";   // la ballade respire : pas de roulement, deux petits coups qui relancent''','''function _scheduleTaikoBar(barStart, barBeats, beatSec, derniere, chord, pos){
  if(!_gridTaikoOn) return;
  try{
    const T=b=>barStart+b*beatSec+(Math.random()-0.5)*0.006, bb=barBeats;
    const id=_taikoMotifPour(chord, bb), M=TAIKO_MOTIFS[id];
    // v1448 : la fin de phrase (toutes les 4 mesures, et la fin de la grille) remplace la fin de chaque accord
    const n=(pos && typeof pos.barIdx==="number") ? pos.barIdx : null;
    const finPhrase=(n===null) ? derniere : ((n%4===3) || !!(pos && pos.finGrille));
    const reponse=(n!==null) && (n%2===1);
    let coups=(id==="ternaire" && bb===3) ? (reponse ? [[0,"don",1.0],[1.5,"ten",0.26],[2,"ten",0.32]] : [[0,"don",1.0],[1,"ten",0.3],[2,"ten",0.3]])
             : ((finPhrase && M.fin) ? M.fin : (reponse ? TAIKO_REPONSES[id] : M.coups)).filter(c=>c[0]<bb);
    if(!coups.length || coups[0][0]!==0) coups=[[0,"don",1.0]].concat(coups);
    const roule=finPhrase && id!=="lent";   // la ballade respire : pas de roulement, deux petits coups qui relancent''')
rep('''_scheduleTaikoBar(barStart, barBeats, beatSec, bar===nBars-1, chord);   // v1343 : taiko (grooves décalés aussi) ; v1447 : l'accord choisit le motif''',
    '''_scheduleTaikoBar(barStart, barBeats, beatSec, bar===nBars-1, chord, {barIdx:barIdx, finGrille:(chordIdx % gr.chords.length)===gr.chords.length-1 && bar===nBars-1});   // v1343 : taiko (grooves décalés aussi) ; v1447 : l'accord choisit le motif ; v1448 : appel, réponse, fin de phrase''')
rep('''_scheduleTaikoBar(barStart, barBeats, beatSec, bar===nBars-1, chord);   // v1343 : taiko ; v1447 : l'accord choisit le motif\n''',
    '''_scheduleTaikoBar(barStart, barBeats, beatSec, bar===nBars-1, chord, {barIdx:barIdx, finGrille:(chordIdx % gr.chords.length)===gr.chords.length-1 && bar===nBars-1});   // v1343 : taiko ; v1447 : l'accord choisit le motif ; v1448 : appel, réponse, fin de phrase\n''')
rep("""    if(roule){   // la fin de l'accord : le shime roule en doubles croches, l'ōdaiko relance
      [0,0.25,0.5,0.75].forEach((d,k)=>_taikoTen(T(bb-1+d), 0.3+0.14*k));
      _taikoDon(T(bb-0.5), 0.7);
    }""","""    if(roule && id==="ternaire"){   // v1448 : en ternaire, le roulement balance aussi (triolets)
      [0,1/3,2/3].forEach((d,k)=>_taikoTen(T(bb-1+d), 0.32+0.16*k));
      _taikoDon(T(bb-1/3), 0.7);
    } else if(roule){   // la fin de phrase : le shime roule en doubles croches, l'ōdaiko relance
      [0,0.25,0.5,0.75].forEach((d,k)=>_taikoTen(T(bb-1+d), 0.3+0.14*k));
      _taikoDon(T(bb-0.5), 0.7);
    }""")
open('/tmp/t/v1448.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1448.json','w'),ensure_ascii=False)
print('ok',len(E))

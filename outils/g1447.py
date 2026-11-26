import json
src=open('/tmp/t/v1446.html',encoding='utf-8').read(); E=[]
def rep(o,n):
    global src
    assert src.count(o)==1,(src.count(o),o[:80]); src=src.replace(o,n); E.append({"old_text":o,"new_text":n})
a=src.index('function _scheduleTaikoBar(barStart, barBeats, beatSec, derniere){'); b=src.index('// ═══ v1342 — 🪕 SHAMISEN',a)
old=src[a:b]
new='''// v1447 — le taiko choisit son motif selon la grille (étape 1 : quatre motifs ; le roulement de fin d'accord ne change pas)
// lent : un coup grave et du silence (ballades, tempo < 90) ; fête (matsuri) : « don, don, do-ko-don » ;
// moteur : croches serrées, appuis en 3+3+2 (rapide, metal) ; ternaire : mesures à 3 temps et shuffle.
const TAIKO_MOTIFS={   // [temps, "don" (ōdaiko) ou "ten" (shime), force], pour une mesure de 4 temps
  lent:    {coups:[[0,"don",1.0],[3.5,"ten",0.3]], fin:[[0,"don",1.0],[3,"ten",0.28],[3.5,"ten",0.38]]},
  fete:    {coups:[[0,"don",1.0],[1,"ten",0.32],[2,"don",0.75],[2.5,"ten",0.28],[3,"don",0.6]]},
  moteur:  {coups:[[0,"don",1.0],[0.5,"ten",0.24],[1,"ten",0.24],[1.5,"don",0.75],[2,"ten",0.24],[2.5,"ten",0.24],[3,"don",0.75],[3.5,"ten",0.26]]},
  ternaire:{coups:[[0,"don",1.0],[0.667,"ten",0.26],[1,"ten",0.3],[1.667,"ten",0.24],[2,"don",0.75],[2.667,"ten",0.26],[3,"ten",0.3],[3.667,"ten",0.28]]}
};
function _taikoMotifPour(chord, barBeats){
  const gr=(typeof _activeGrid!=="undefined") ? _activeGrid : null;
  const tempo=(gr && gr.tempo) || ((typeof backingBpm!=="undefined") ? backingBpm : 100);
  const METAL=["gallop","metal","doom","djent16","breakdown","blast","punk"];
  const g=(chord && chord.groove) || (gr && gr.groove) || "";
  let feel="droit"; try{ feel=_feelEffectif(chord); }catch(e){}
  if(barBeats===3 || barBeats===6 || feel==="shuffle") return "ternaire";
  if(METAL.includes(g) || tempo>=140) return "moteur";
  if((gr && gr.preset==="ballade") || tempo<90) return "lent";
  return "fete";
}
function _scheduleTaikoBar(barStart, barBeats, beatSec, derniere, chord){
  if(!_gridTaikoOn) return;
  try{
    const T=b=>barStart+b*beatSec+(Math.random()-0.5)*0.006, bb=barBeats;
    const id=_taikoMotifPour(chord, bb), M=TAIKO_MOTIFS[id];
    let coups=(id==="ternaire" && bb===3) ? [[0,"don",1.0],[1,"ten",0.3],[2,"ten",0.3]]
             : ((derniere && M.fin) ? M.fin : M.coups).filter(c=>c[0]<bb);
    if(!coups.length || coups[0][0]!==0) coups=[[0,"don",1.0]].concat(coups);
    const roule=derniere && id!=="lent";   // la ballade respire : pas de roulement, deux petits coups qui relancent
    coups.forEach(c=>{ if(roule && c[0]>=bb-1) return; (c[1]==="don" ? _taikoDon : _taikoTen)(T(c[0]), c[2]); });
    if(roule){   // la fin de l'accord : le shime roule en doubles croches, l'ōdaiko relance
      [0,0.25,0.5,0.75].forEach((d,k)=>_taikoTen(T(bb-1+d), 0.3+0.14*k));
      _taikoDon(T(bb-0.5), 0.7);
    }
  }catch(e){}
}
'''
rep(old,new)
rep('_scheduleTaikoBar(barStart, barBeats, beatSec, bar===nBars-1);   // v1343 : taiko (grooves décalés aussi)','_scheduleTaikoBar(barStart, barBeats, beatSec, bar===nBars-1, chord);   // v1343 : taiko (grooves décalés aussi) ; v1447 : l\'accord choisit le motif')
rep('_scheduleTaikoBar(barStart, barBeats, beatSec, bar===nBars-1);   // v1343 : taiko\n','_scheduleTaikoBar(barStart, barBeats, beatSec, bar===nBars-1, chord);   // v1343 : taiko ; v1447 : l\'accord choisit le motif\n')
open('/tmp/t/v1447.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1447.json','w'),ensure_ascii=False)
print('ok',len(E), len(old))

import json
src=open('/tmp/t/v1458.html',encoding='utf-8').read(); E=[]
def rep(o,n):
    global src
    assert src.count(o)==1,(src.count(o),o[:80]); src=src.replace(o,n); E.append({"old_text":o,"new_text":n})
rep('''_gridCursor = (_gridReprise!==null) ? _gridReprise : 0;''',
    '''const _depuisDebut=(_gridReprise===null);   // v1459 : l'oroshi ne joue qu'au lancement depuis le début
_gridCursor = (_gridReprise!==null) ? _gridReprise : 0;''')
rep('''  _gridNextTime=audioCtx.currentTime+0.10;
  _gridScheduler(gr);''','''  _gridNextTime=audioCtx.currentTime+0.10;
  if(_gridTaikoOn && _depuisDebut && _gridCursor===0){ try{ _gridNextTime+=_taikoOroshi(gr, _gridNextTime); }catch(e){} }   // v1459 : l'oroshi, puis la grille
  _gridScheduler(gr);''')
rep('''function _taikoMotifPour(chord, barBeats){
  const gr=(typeof _activeGrid!=="undefined") ? _activeGrid : null;''','''function _taikoMotifPour(chord, barBeats, grImpose){
  const gr=grImpose || ((typeof _activeGrid!=="undefined") ? _activeGrid : null);''')
rep('''function _scheduleTaikoBar(barStart, barBeats, beatSec, derniere, chord, pos){''','''// v1459 — OROSHI : l'ōdaiko seul ouvre la grille ; les coups se resserrent et montent jusqu'au premier temps, où tout le monde entre.
// Deux mesures (une seule, douce et sans rafale, en ballade). Les coups partent par minuterie : l'arrêt pendant l'oroshi les annule.
function _taikoOroshi(gr, t0){
  const c0=(gr.chords||[])[0]||{}, bb=(c0.beats && c0.beats%3===0 && c0.beats%4!==0) ? 3 : 4;
  const id=_taikoMotifPour(c0, bb, gr), beatSec=60/((gr.tempo)||backingBpm||100);
  const lent=(id==="lent"), total=(lent?1:2)*bb, coups=[];
  if(lent){
    [0,0.3,0.55,0.75,0.88].forEach((x,k)=>coups.push([total*x,"don",0.3+0.08*k]));
  } else {
    const N=Math.round(total*2.2); let der=-1;
    for(let k=0;k<N;k++){ const x=k/N, p=total*(1-Math.pow(1-x,2.2));
      if(p-der<0.12 || p>total-0.25) continue; der=p;
      coups.push([p, (x>0.7 && coups.length%2===1) ? "ten" : "don", (0.35+0.55*Math.pow(x,1.5))*((x>0.7 && coups.length%2===1)?0.7:1)]); }
  }
  coups.forEach(c=>{ const t=t0+c[0]*beatSec, att=Math.max(0,(t-audioCtx.currentTime-0.15)*1000);
    _gridPlayTimers.push(setTimeout(()=>{ if(_gridPlayOn) _taikoCoup(c[1], t, c[2]); }, att)); });
  return total*beatSec;
}
function _scheduleTaikoBar(barStart, barBeats, beatSec, derniere, chord, pos){''')
open('/tmp/t/v1459.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1459.json','w'),ensure_ascii=False); print(len(E))

import json
src=open('/tmp/t/v1456.html',encoding='utf-8').read(); E=[]
def rep(o,n):
    global src
    assert src.count(o)==1,(src.count(o),o[:80]); src=src.replace(o,n); E.append({"old_text":o,"new_text":n})
# 1. rendu hors temps réel : trois variantes de ka
rep('''    const C=new OfflineAudioContext(1, Math.ceil(sr*(type==="don"?0.95:0.3)), sr);''',
    '''    const C=new OfflineAudioContext(1, Math.ceil(sr*(type==="don"?0.95:type==="ka"?0.15:0.3)), sr);''')
rep('''    } else {
      ton(560,500,0.02,0.15,0.8*v,dest);''','''    } else if(type==="ka"){   // v1457 — ka : la baguette sur le cercle de bois, sans peau
      ton(1250,1180,0.01,0.035,0.35*v,dest); ton(2100,2050,0.01,0.02,0.15*v,dest);
      bruit("bandpass",2600,2.5,0.018,0.9*v,dest); bruit("highpass",5000,0.7,0.008,0.4*v,dest);
    } else {
      ton(560,500,0.02,0.15,0.8*v,dest);''')
rep('''  Promise.all(["don","don","don","ten","ten","ten"].map(un)).then(bs=>{ _taikoEch={sr, don:bs.slice(0,3), ten:bs.slice(3)}; })''',
    '''  Promise.all(["don","don","don","ten","ten","ten","ka","ka","ka"].map(un)).then(bs=>{ _taikoEch={sr, don:bs.slice(0,3), ten:bs.slice(3,6), ka:bs.slice(6)}; })''')
# 2. jeu du ka
rep('''// v1447 — le taiko choisit son motif selon la grille''','''function _taikoKa(t, vel){   // v1457 — « ka » : le cercle du tambour, clic sec et boisé
  if(_taikoEchJouer("ka", t, vel*(0.9+Math.random()*0.2))) return; _taikoRendre();
  const out=_taikoBus(), v=vel*(0.9+Math.random()*0.2);
  _taikoTon(t, 1250, 1180, 0.01, 0.035, 0.35*v, out);
  _taikoBruitCoup(t, "bandpass", 2600, 2.5, 0.018, 0.9*v, out);
}
function _taikoCoup(type, t, vel){ (type==="don" ? _taikoDon : type==="ka" ? _taikoKa : _taikoTen)(t, vel); }
// v1447 — le taiko choisit son motif selon la grille''')
# 3. motifs
rep('''  fete:    {coups:[[0,"don",1.0],[1,"ten",0.32],[2,"don",0.75],[2.5,"ten",0.28],[3,"don",0.6]]},''',
    '''  fete:    {coups:[[0,"don",1.0],[1,"ten",0.32],[1.5,"ka",0.3],[2,"don",0.75],[2.5,"ten",0.28],[3,"don",0.6],[3.5,"ka",0.3]]},   // v1457 : ka sur les contretemps''')
rep('''  lent:    [[0,"don",0.9],[2.5,"don",0.42],[3.5,"ten",0.3]],
  fete:    [[0,"don",1.0],[1,"ten",0.3],[1.5,"ten",0.26],[2,"don",0.7],[3,"don",0.75],[3.5,"ten",0.3]],
  moteur:  [[0,"don",1.0],[0.5,"ten",0.24],[1,"don",0.7],[1.5,"ten",0.24],[2,"ten",0.24],[2.5,"don",0.75],[3,"ten",0.24],[3.5,"ten",0.28]],
  ternaire:[[0,"don",1.0],[0.667,"ten",0.24],[1,"ten",0.3],[1.667,"don",0.6],[2,"don",0.75],[3,"ten",0.3],[3.667,"ten",0.3]]''',
'''  lent:    [[0,"don",0.9],[1,"ka",0.3],[2.5,"don",0.42],[3.5,"ten",0.3]],   // v1457 : les ka
  fete:    [[0,"don",1.0],[1,"ten",0.3],[1.5,"ka",0.3],[2,"don",0.7],[3,"don",0.75],[3.5,"ka",0.32]],
  moteur:  [[0,"don",1.0],[0.5,"ten",0.24],[1,"don",0.7],[1.5,"ka",0.28],[2,"ten",0.24],[2.5,"don",0.75],[3,"ka",0.28],[3.5,"ten",0.28]],
  ternaire:[[0,"don",1.0],[0.667,"ka",0.28],[1,"ten",0.3],[1.667,"don",0.6],[2,"don",0.75],[2.667,"ka",0.28],[3,"ten",0.3],[3.667,"ten",0.3]]''')
rep('''(reponse ? [[0,"don",1.0],[1.5,"ten",0.26],[2,"ten",0.32]]''','''(reponse ? [[0,"don",1.0],[1.5,"ka",0.28],[2,"ten",0.32]]''')
# 4. ka avant le roulement, et aiguillage des coups
rep('''    coups.forEach(c=>{ if(roule && c[0]>=bb-1) return; (c[1]==="don" ? _taikoDon : _taikoTen)(T(c[0]), c[2]); });''',
    '''    if(roule && bb>=2){   // v1457 : un ka annonce le roulement
      const tk=(id==="ternaire") ? bb-1-1/3 : bb-1.5;
      if(!coups.some(c=>Math.abs(c[0]-tk)<0.01 && c[1]==="don")) coups=coups.filter(c=>Math.abs(c[0]-tk)>0.01).concat([[tk,"ka",0.4]]);
    }
    coups.forEach(c=>{ if(roule && c[0]>=bb-1) return; _taikoCoup(c[1], T(c[0]), c[2]); });''')
open('/tmp/t/v1457.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1457.json','w'),ensure_ascii=False); print(len(E))

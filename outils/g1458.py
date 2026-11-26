import json
src=open('/tmp/t/v1457.html',encoding='utf-8').read(); E=[]
def rep(o,n):
    global src
    assert src.count(o)==1,(src.count(o),o[:80]); src=src.replace(o,n); E.append({"old_text":o,"new_text":n})
rep('''    const roule=finPhrase && id!=="lent";   // la ballade respire : pas de roulement, deux petits coups qui relancent
    if(roule && bb>=2){   // v1457 : un ka annonce le roulement
      const tk=(id==="ternaire") ? bb-1-1/3 : bb-1.5;
      if(!coups.some(c=>Math.abs(c[0]-tk)<0.01 && c[1]==="don")) coups=coups.filter(c=>Math.abs(c[0]-tk)>0.01).concat([[tk,"ka",0.4]]);
    }
    coups.forEach(c=>{ if(roule && c[0]>=bb-1) return; _taikoCoup(c[1], T(c[0]), c[2]); });
    if(roule && id==="ternaire"){   // v1448 : en ternaire, le roulement balance aussi (triolets)
      [0,1/3,2/3].forEach((d,k)=>_taikoTen(T(bb-1+d), 0.32+0.16*k));
      _taikoDon(T(bb-1/3), 0.7);
    } else if(roule){   // la fin de phrase : le shime roule en doubles croches, l'ōdaiko relance
      [0,0.25,0.5,0.75].forEach((d,k)=>_taikoTen(T(bb-1+d), 0.3+0.14*k));
      _taikoDon(T(bb-0.5), 0.7);
    }''','''    // v1458 : le roulement devient rare (toutes les 8 mesures et à la fin de la grille) ; les autres fins de phrase : un ka, puis un don qui relance
    const grandeFin=(n===null) ? derniere : ((n%8===7) || !!(pos && pos.finGrille));
    const fin=finPhrase && id!=="lent" && bb>=2;   // la ballade respire : pas de roulement, deux petits coups qui relancent
    const roule=fin && grandeFin;
    if(fin){   // v1457 : un ka annonce la fin de phrase
      const tk=(id==="ternaire") ? bb-1-1/3 : bb-1.5;
      if(!coups.some(c=>Math.abs(c[0]-tk)<0.01 && c[1]==="don")) coups=coups.filter(c=>Math.abs(c[0]-tk)>0.01).concat([[tk,"ka",0.4]]);
    }
    coups.forEach(c=>{ if(fin && c[0]>=bb-1) return; _taikoCoup(c[1], T(c[0]), c[2]); });
    const tDon=(id==="ternaire") ? bb-1/3 : bb-0.5;
    if(roule && id==="ternaire"){   // v1458 : roulement court, deux coups en triolet puis le don
      _taikoTen(T(bb-1), 0.32); _taikoTen(T(bb-2/3), 0.42); _taikoDon(T(tDon), 0.7);
    } else if(roule){   // v1458 : « tere-don », deux ten serrés puis l'ōdaiko
      _taikoTen(T(bb-1), 0.32); _taikoTen(T(bb-0.75), 0.42); _taikoDon(T(tDon), 0.7);
    } else if(fin){
      _taikoDon(T(tDon), 0.65);
    }''')
open('/tmp/t/v1458.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1458.json','w'),ensure_ascii=False); print(len(E))

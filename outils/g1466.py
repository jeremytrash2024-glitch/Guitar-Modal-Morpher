import json
src=open('/tmp/t/v1465.html',encoding='utf-8').read(); E=[]
def rep(o,n):
    global src
    assert src.count(o)==1,(src.count(o),o[:80]); src=src.replace(o,n); E.append({"old_text":o,"new_text":n})
rep('function _autoPenta(formula){\n','''// v1466 — GAMMES BEBOP : la note de passage n'est pas une note de l'accord. Pour simplifier, pour l'arpège du repère et pour la note
// caractéristique, on travaille sur la gamme mère (dominante → mixolydien, majeure → ionien, dorienne → dorien, mineure mélodique).
const BEBOP_PASSAGE={"0,2,4,5,7,9,10,11":11,"0,2,4,5,7,8,9,11":8,"0,2,3,4,5,7,9,10":4,"0,2,3,5,7,8,9,11":8};
function _gammeMere(formula){ if(!Array.isArray(formula)) return formula; const p=BEBOP_PASSAGE[formula.join(",")]; return p===undefined ? formula : formula.filter(x=>x!==p); }
function _autoPenta(formula){
''')
rep('''if(!pentaSimplifyOn) return modeObj.formula;
const key=modeObj.formula.join(",");
return PENTA_TABLE[key] || _autoPenta(modeObj.formula);''','''if(!pentaSimplifyOn) return modeObj.formula;
const f=_gammeMere(modeObj.formula), key=f.join(",");   // v1466 : bebop → la penta de la gamme mère
return PENTA_TABLE[key] || _autoPenta(f);''')
rep('function _repPenta(f){ if(','function _repPenta(f){ f=_gammeMere(f); if(')
rep('''function _repArp(formula){
  if(!Array.isArray(formula) || !formula.length) return null;''','''function _repArp(formula){
  if(!Array.isArray(formula) || !formula.length) return null;
  formula=_gammeMere(formula);   // v1466 : bebop dorienne → La m (Do), pas La 7 (Do# de passage)''')
rep('''function _caracSemis(formula){
  if(!formula || formula.length!==7) return [];''','''function _caracSemis(formula){
  formula=_gammeMere(formula);   // v1466
  if(!formula || formula.length!==7) return [];''')
open('/tmp/t/v1466.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1466.json','w'),ensure_ascii=False); print(len(E))

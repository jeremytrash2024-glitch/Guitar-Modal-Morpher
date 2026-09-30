// gmm-tests-870-groove-accord.js — le groove écrit sur un accord doit être joué en lecture normale
// Usage : node gmm-tests-870-groove-accord.js fichier.html [sabotage N]
// Rouge sur la v869 (le groove d'accord n'était honoré que sélecteur sur « Perso »), vert sur la v870.
const fs=require('fs'),vm=require('vm');
const file=process.argv[2], sabo=process.argv[3]==='sabotage'?+process.argv[4]:0;
let src=fs.readFileSync(file,'utf8');
function bloc(i,open){let j=src.indexOf(open,i),d=0,k=j,q=null;
 for(;k<src.length;k++){const c=src[k];if(q){if(c==='\\'){k++;continue}if(c===q)q=null;continue}
  if(c==='"'||c==="'"||c==='`'){q=c;continue}if(c==='/'&&src[k+1]==='/'){k=src.indexOf('\n',k);continue}
  if(c==='['||c==='{')d++;else if(c===']'||c==='}'){d--;if(!d)break}}return src.slice(j,k+1)}
function fn(name){const i=src.indexOf('function '+name+'(');if(i<0)throw new Error('absente : '+name);
 const b=src.indexOf('{',src.indexOf(')',i));return src.slice(i,b)+bloc(b,'{')}
let code=[fn('_grooveEmpan'),fn('_grooveTient'),fn('_gridGrooveName')].join('\n');
// Sabotages : chacun doit rougir au moins une assertion précise
if(sabo===1) code=code.replace(/_gridGrooveLock===null && chord && chord\.groove/,'false && chord && chord.groove');           // retour au comportement v869
if(sabo===2) code=code.replace(/if\(_gridGrooveLock===null && chord/,'if(chord');                                            // le choix manuel ne gagne plus
if(sabo===3) code=code.replace(/DRUM_GROOVES\[chord\.groove\] && _grooveTient\(chord\.groove, sig\)\) return chord\.groove;   \/\/ v870/,'DRUM_GROOVES[chord.groove]) return chord.groove;   // v870'); // plus de filet de débord
if(sabo===4) code=code.replace(/chord && chord\.groove && DRUM_GROOVES\[chord\.groove\] && _grooveTient/,'chord && chord.groove && _grooveTient'); // groove inconnu accepté
if(sabo===5) code=code.replace(/if\(typeof _gridBandOn!=="undefined" && _gridBandOn && _activeGrid\) return "perso";/,'');   // le Groupe perd la main
if(sabo && code===[fn('_grooveEmpan'),fn('_grooveTient'),fn('_gridGrooveName')].join('\n')){console.log('SABOTAGE '+sabo+' SANS EFFET — ancre introuvable');process.exit(2)}
const DG=vm.runInNewContext('('+bloc(src.indexOf('const DRUM_GROOVES'),'{')+')',{});
const ctx={DRUM_GROOVES:DG,_gridBandOn:false,_gridGrooveLock:null,_activeGrid:null,currentGroove:'rock'};
vm.createContext(ctx);vm.runInContext(code,ctx);
const F=vm.runInNewContext('('+bloc(src.indexOf('const STYLE_FAMILIES=['),'[')+')',{});
let ok=0,ko=0;const t=(nom,cond)=>{if(cond){ok++}else{ko++;console.log('  ✗',nom)}};
const G=(chord,sig)=>ctx._gridGrooveName(chord,sig);
function charge(gr,fam){ctx._activeGrid=gr;ctx.currentGroove=gr.groove||fam.groove;ctx._gridGrooveLock=null;ctx._gridBandOn=false}
// A — lecture normale : l'accord impose son groove
const fam={groove:'rock'},gr={groove:'prog5'};charge(gr,fam);
t('A1 accord cinemaOst dans une grille prog5 → cinemaOst',G({groove:'cinemaOst'},4)==='cinemaOst');
t('A2 accord sans groove → groove de grille',G({name:'X'},4)==='prog5');
t('A3 accord sans rien → groove de grille',G(null,4)==='prog5');
// B — le choix manuel du menu gagne sur tout
ctx._gridGrooveLock='jazz';ctx.currentGroove='jazz';
t('B1 menu Groove verrouillé sur jazz → jazz, même sur un accord à groove',G({groove:'cinemaOst'},4)==='jazz');
// C — Groupe ON → perso
charge(gr,fam);ctx._gridBandOn=true;
t('C1 Groupe ON → perso même sur un accord à groove',G({groove:'cinemaOst'},4)==='perso');
ctx._gridBandOn=false;
// D — filets
t('D1 groove inconnu → groove de grille',G({groove:'nexistepas'},4)==='prog5');
t('D1b groove inconnu sans sig (4/4 par défaut) → groove de grille',G({groove:'nexistepas'},undefined)==='prog5');
const long=Object.keys(DG).find(k=>ctx._grooveEmpan(k)>=3.5 && ctx._grooveEmpan(k)<Infinity);
t('D2 groove qui déborde la mesure ('+long+' sur 3.5) → groove de grille',!long||G({groove:long},3.5)==='prog5');
// E — comportement Perso hérité conservé
charge({groove:'perso'},fam);
t('E1 grille Magic en perso, accord sans groove → perso',G({name:'X'},4)==='perso');
// F — audit générique du corpus : tout accord qui déclare un groove qui tient l'obtient au chargement
let vus=0;
for(const f of F)for(const g of f.grids||[]){charge(g,f);
 for(const c of g.chords){if(!c.groove)continue;vus++;
  const sig=c.sig||g.sig;const attendu=(DG[c.groove]&&ctx._grooveTient(c.groove,sig))?c.groove:ctx.currentGroove;
  t('F '+g.id+' '+c.name+' → '+attendu,G(c,sig)===attendu);
  t('F+ '+g.id+' '+c.name+' joue bien le groove écrit',G(c,sig)===c.groove);}}
t('F0 au moins trois grilles portent un groove d\'accord',vus>=3);
console.log((ko?'ROUGE':'VERT')+' — '+ok+' ok, '+ko+' ko'+(sabo?' (sabotage '+sabo+')':''));
process.exit(ko?1:0);

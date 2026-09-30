// gmm-tests-871-remix-timmons.js — remix de « Lumière en La » : arc ballade → rock → ballade, accords intacts
// Usage : node gmm-tests-871-remix-timmons.js fichier.html [avant.html] [sabotage N]
const fs=require('fs'),vm=require('vm');
const file=process.argv[2];const si=process.argv.indexOf('sabotage');const sabo=si>0?+process.argv[si+1]:0;
const avant=process.argv[3]&&process.argv[3]!=='sabotage'?process.argv[3]:null;
let src=fs.readFileSync(file,'utf8');
const scope=()=>{const i=src.indexOf('{id:"rock-timmons-lumiere-la"');return [i,src.indexOf(']},',i)+3]};
function patch(a,b){const [i,j]=scope();const bloc=src.slice(i,j);if(!bloc.includes(a)){console.log('SABOTAGE '+sabo+' SANS EFFET');process.exit(2)}src=src.slice(0,i)+bloc.replace(a,b)+src.slice(j)}
if(sabo===1) patch('groove:"rock",feel:"laid"','feel:"laid"');                       // le Mi 7sus4 ne passe plus en rock
if(sabo===2) patch('voicing:"x-2-4-2-3-x"','voicing:"x-2-4-2-2-x"');                  // un doigté touché
if(sabo===3) patch('{name:"Amaj9",beats:16,','{name:"Amaj9",beats:16,groove:"rock",'); // l'atterrissage reste en rock
if(sabo===4){const a='["rock-timmons-lumiere-la","remix v871"],';if(!src.includes(a)){console.log('SABOTAGE 4 SANS EFFET');process.exit(2)}src=src.replace(a,'')}
if(sabo===5) patch('{name:"D/F#",beats:2,','{name:"D/F#",beats:4,');               // la durée totale bouge
if(sabo===6) patch('{name:"Bm7",beats:8,decale:-0.5,','{name:"Bm7",beats:8,');     // plus d'anticipation
function bloc(i,open){let j=src.indexOf(open,i),d=0,k=j,q=null;for(;k<src.length;k++){const c=src[k];if(q){if(c==='\\'){k++;continue}if(c===q)q=null;continue}
 if(c==='"'||c==="'"||c==='`'){q=c;continue}if(c==='/'&&src[k+1]==='/'){k=src.indexOf('\n',k);continue}if(c==='['||c==='{')d++;else if(c===']'||c==='}'){d--;if(!d)break}}return src.slice(j,k+1)}
function fn(n){const i=src.indexOf('function '+n+'(');const b=src.indexOf('{',src.indexOf(')',i));return src.slice(i,b)+bloc(b,'{')}
const lire=s=>{const o=src;src=s;const F=vm.runInNewContext('('+bloc(src.indexOf('const STYLE_FAMILIES=['),'[')+')',{});src=o;return F};
const F=lire(src);const G=F.flatMap(f=>(f.grids||[]).map(g=>Object.assign(g,{_fam:f}))).find(g=>g.id==='rock-timmons-lumiere-la');
let ok=0,ko=0;const t=(n,c)=>{if(c)ok++;else{ko++;console.log('  ✗',n)}};
const C=G.chords;
// A — les accords ne bougent pas (un remix touche le rythme, jamais l'harmonie)
const REF=[["Amaj9","x-0-6-4-2-x"],["Dadd9","x-x-0-2-5-2"],["Gmaj7","3-x-0-0-0-2"],["D/F#","2-x-0-2-3-2"],["Bm7","x-2-4-2-3-x"],["Amaj9","x-0-6-4-2-x"],["E7sus4","x-7-9-7-10-7"],["Amaj9","x-x-6-6-5-7"]];
t('A1 huit accords, mêmes noms, mêmes doigtés',C.length===8&&REF.every(([n,v],i)=>C[i].name===n&&C[i].voicing===v));
if(avant){const Ga=lire(fs.readFileSync(avant,'utf8')).flatMap(f=>f.grids||[]).find(g=>g.id==='rock-timmons-lumiere-la');
 t('A2 identique à la version d\'avant hors rythme (nom, doigté, gamme)',JSON.stringify(Ga.chords.map(c=>[c.name,c.voicing,c.scale]))===JSON.stringify(C.map(c=>[c.name,c.voicing,c.scale])));}
t('A3 durée totale inchangée : 16 mesures',C.reduce((a,c)=>a+c.beats,0)===64);
// B — le rythme raconte la grille
t('B1 D/F# est la plus courte : une basse de passage',C[3].beats===Math.min(...C.map(c=>c.beats))&&C[3].beats<=2);
t('B2 le Si mineur 7 arrive en avance',C[4].decale<0);
t('B3 le Mi 7sus4 est suspendu : plus long que 2 mesures, posé',C[6].beats>8&&C[6].feel==='laid');
t('B4 l\'atterrissage final est la plus longue',C[7].beats===Math.max(...C.map(c=>c.beats)));
// C — l'arc ballade → rock → ballade, joué par le vrai moteur
const DG=vm.runInNewContext('('+bloc(src.indexOf('const DRUM_GROOVES'),'{')+')',{});
const ctx={DRUM_GROOVES:DG,_gridBandOn:false,_gridGrooveLock:null,_activeGrid:G,currentGroove:G.groove||G._fam.groove};
vm.createContext(ctx);vm.runInContext([fn('_grooveEmpan'),fn('_grooveTient'),fn('_gridGrooveName')].join('\n'),ctx);
const joue=C.map(c=>ctx._gridGrooveName(c,c.sig||G.sig));
t('C1 groove de grille = ballade',G.groove==='ballad');
t('C2 début en ballade (accords 1 à 5) : '+joue.slice(0,5),joue.slice(0,5).every(x=>x==='ballad'));
t('C3 retour du La maj9 et Mi 7sus4 en rock : '+joue.slice(5,7),joue[5]==='rock'&&joue[6]==='rock');
t('C4 l\'atterrissage retombe en ballade : '+joue[7],joue[7]==='ballad');
t('C5 un seul passage en rock, d\'un bloc',joue.join(',').split('rock').length-1===2&&/ballad,rock,rock,ballad$/.test(joue.join(',')));
// D — registre et texte
t('D1 libellé « remix v871 » dans NOUVEAUTES',/\["rock-timmons-lumiere-la","remix v871"\]/.test(src));
t('D2 la description parle de l\'arc',/ballade/.test(G.desc)&&/rock entre/.test(G.desc)&&/retombe en ballade/.test(G.desc));
t("D3 badge v871 ou plus",/>v8(7[1-9]|[89]\d) · /.test(src));
console.log((ko?'ROUGE':'VERT')+' — '+ok+' ok, '+ko+' ko'+(sabo?' (sabotage '+sabo+')':''));process.exit(ko?1:0);

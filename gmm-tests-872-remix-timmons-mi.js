// gmm-tests-872-remix-timmons-mi.js — remix du « Mi qui ne bouge pas » : on s'attarde où le Mi est riche, on passe où il est simple
// Usage : node gmm-tests-872-remix-timmons-mi.js fichier.html [avant.html] [sabotage N]
const fs=require('fs'),vm=require('vm');
const file=process.argv[2];const si=process.argv.indexOf('sabotage');const sabo=si>0?+process.argv[si+1]:0;
const avant=process.argv[3]&&process.argv[3]!=='sabotage'?process.argv[3]:null;
let src=fs.readFileSync(file,'utf8');const ID='rock-timmons-mi-pedale';
const scope=()=>{const i=src.indexOf('{id:"'+ID+'"');return [i,src.indexOf(']},',i)+3]};
function patch(a,b){const [i,j]=scope();const bl=src.slice(i,j);if(!bl.includes(a)){console.log('SABOTAGE '+sabo+' SANS EFFET');process.exit(2)}src=src.slice(0,i)+bl.replace(a,b)+src.slice(j)}
if(sabo===1) patch('{name:"Aadd9/C#",beats:4,','{name:"Aadd9/C#",beats:8,');        // le passage ne passe plus
if(sabo===2) patch('voicing:"3-x-0-4-0-0"','voicing:"3-x-0-4-3-3"');                // le Mi à vide disparaît du Sol 6
if(sabo===3) patch('{name:"Asus4",beats:12,feel:"laid",','{name:"Asus4",beats:12,'); // la suspension n'est plus posée
if(sabo===4) patch('{name:"Em7",beats:8,','{name:"Em7",beats:8,groove:"rock",');     // un passage rock s'invite
if(sabo===5){const a='["'+ID+'","remix v872"],';if(!src.includes(a)){console.log('SABOTAGE 5 SANS EFFET');process.exit(2)}src=src.replace(a,'')}
if(sabo===6) patch('{name:"Bm7(11)",beats:8,','{name:"Bm7(11)",beats:4,');         // une couleur riche écourtée (et total faux)
function bloc(i,open){let j=src.indexOf(open,i),d=0,k=j,q=null;for(;k<src.length;k++){const c=src[k];if(q){if(c==='\\'){k++;continue}if(c===q)q=null;continue}
 if(c==='"'||c==="'"||c==='`'){q=c;continue}if(c==='/'&&src[k+1]==='/'){k=src.indexOf('\n',k);continue}if(c==='['||c==='{')d++;else if(c===']'||c==='}'){d--;if(!d)break}}return src.slice(j,k+1)}
function fn(n){const i=src.indexOf('function '+n+'(');const b=src.indexOf('{',src.indexOf(')',i));return src.slice(i,b)+bloc(b,'{')}
const lire=s=>{const o=src;src=s;const F=vm.runInNewContext('('+bloc(src.indexOf('const STYLE_FAMILIES=['),'[')+')',{});src=o;return F};
const F=lire(src);const G=F.flatMap(f=>(f.grids||[]).map(g=>Object.assign(g,{_fam:f}))).find(g=>g.id===ID);
let ok=0,ko=0;const t=(n,c)=>{if(c)ok++;else{ko++;console.log('  ✗',n)}};const C=G.chords;
// A — l'harmonie ne bouge pas, et le Mi aigu reste à vide partout
const REF=[["Dadd9","x-5-4-2-3-0"],["Aadd9/C#","x-4-2-2-0-0"],["Bm7(11)","x-2-0-2-0-0"],["G6","3-x-0-4-0-0"],["F#m7","2-x-2-2-2-0"],["Em7","0-2-2-0-3-0"],["Asus4","x-0-2-2-3-0"],["Dadd9","x-5-4-2-3-0"]];
t('A1 huit accords, mêmes noms, mêmes doigtés',C.length===8&&REF.every(([n,v],i)=>C[i].name===n&&C[i].voicing===v));
t('A2 la corde de Mi aiguë est à vide sur chaque accord',C.every(c=>c.voicing.split('-')[5]==='0'));
if(avant){const Ga=lire(fs.readFileSync(avant,'utf8')).flatMap(f=>f.grids||[]).find(g=>g.id===ID);
 t('A3 identique à la version d\'avant hors rythme',JSON.stringify(Ga.chords.map(c=>[c.name,c.voicing,c.scale]))===JSON.stringify(C.map(c=>[c.name,c.voicing,c.scale])));}
t('A4 durée totale inchangée : 16 mesures',C.reduce((a,c)=>a+c.beats,0)===64);
// B — le rythme suit le rôle du Mi
const riches=[0,2,3],simples=[1,4];   // 9, 11, 6  contre  quinte, septième
t('B1 là où le Mi est simple, on passe (1 mesure)',simples.every(i=>C[i].beats===4));
t('B2 là où le Mi est une couleur riche, on s\'attarde (2 mesures au moins)',riches.every(i=>C[i].beats>=8));
t('B3 l\'Asus4 est suspendu : 3 mesures, posé',C[6].beats===12&&C[6].feel==='laid');
t('B4 le Ré add9 final atterrit plus long que celui du début',C[7].beats>C[0].beats);
// C — tout en ballade, par le vrai moteur
const DG=vm.runInNewContext('('+bloc(src.indexOf('const DRUM_GROOVES'),'{')+')',{});
const ctx={DRUM_GROOVES:DG,_gridBandOn:false,_gridGrooveLock:null,_activeGrid:G,currentGroove:G.groove||G._fam.groove};
vm.createContext(ctx);vm.runInContext([fn('_grooveEmpan'),fn('_grooveTient'),fn('_gridGrooveName')].join('\n'),ctx);
const joue=C.map(c=>ctx._gridGrooveName(c,c.sig||G.sig));
t('C1 les huit accords jouent la ballade : '+joue,joue.every(x=>x==='ballad'));
// D — registre et texte
t('D1 libellé « remix v872 »',new RegExp('\\["'+ID+'","remix v872"\\]').test(src));
t('D2 la description dit où l\'on s\'attarde',/s'attarde/.test(G.desc)&&/ballade/.test(G.desc));
t('D3 badge v872',/>v872 · /.test(src));
console.log((ko?'ROUGE':'VERT')+' — '+ok+' ok, '+ko+' ko'+(sabo?' (sabotage '+sabo+')':''));process.exit(ko?1:0);

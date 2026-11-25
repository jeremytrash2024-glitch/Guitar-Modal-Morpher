import asyncio, sys, json
from playwright.async_api import async_playwright
JS=r'''(id)=>{
 const N=["Do","Do#","Ré","Ré#","Mi","Fa","Fa#","Sol","Sol#","La","La#","Si"], nm=m=>N[((m%12)+12)%12]+(Math.floor(m/12)-1);
 let gr=null; STYLE_FAMILIES.forEach(f=>(f.grids||[]).forEach(x=>{ if(x.id===id) gr=x; })); _loadGridOntoBoard(gr); initAudio();
 const tuning=[...INSTRUMENTS[appState.instrument].tunings].reverse();
 const B=_ligneBasseEcrite(gr); const out=[]; let t0=0; _shoPrec=null; const prob=[];
 gr.chords.forEach((c,ci)=>{
   const S=_shoGamme(c,gr).pcs; const vm=voicingToMidi(_parseVoicing(c.voicing), tuning);
   const sig=_chordSig(gr,c), beats=c.beats;
   // arpège : notes et temps
   const am=_arpMotifDe(c)||{motif:gr.arpMotif,pas:gr.arpPas}; const arp=[];
   if(gr.arpMotif) _gridBarPlan(beats,sig).forEach(p=>{ _motifEvents({motif:gr.arpMotif,pas:gr.arpPas}, vm.length, p.beats).forEach(e=>arp.push([p.start+e.k*gr.arpPas, vm[e.i], e.dur])); });
   const bass=B.notes.filter(n=>n.ci===ci).map(n=>[n.temps-t0, n.midi, n.dur]);
   const sho=_shoAitake(c, vm, gr);
   const solo=(c.soloEcrit||[]).map(e=>[e[0], _soloNoteMidi(e[1]), e[2], e[3]||""]);
   const ph=(gr.phrase||[]).filter(x=>x[1]>=t0 && x[1]<t0+beats).map(x=>[x[1]-t0,_phraseMidi(x[0]),x[2]]);
   const hors=(L,nomI)=>L.forEach(x=>{ if(!S.has(((x[1]%12)+12)%12)) prob.push(`${c.name} : ${nomI} ${nm(x[1])} hors gamme`); });
   hors(arp,"arpège"); hors(bass,"basse"); hors(solo,"Solo"); hors(ph,"Phrase"); sho.notes.forEach(m=>{ if(!S.has(m%12)) prob.push(`${c.name} : shō ${nm(m)} hors gamme`); });
   // frottements Solo / basse et Solo / arpège sur notes longues (≥1 temps qui se chevauchent ≥0,5)
   const frot=(A,a,Bv,b)=>A.forEach(x=>Bv.forEach(y=>{ const o=Math.min(x[0]+x[2],y[0]+y[2])-Math.max(x[0],y[0]); const iv=Math.abs(x[1]-y[1])%12; if(o>=0.5 && (iv===1||iv===11)) prob.push(`${c.name} t${x[0]} : ${a} ${nm(x[1])} / ${b} ${nm(y[1])} — demi-ton`); }));
   frot(solo,"Solo",bass,"basse");
   out.push({accord:c.name, doigte:c.voicing, cordes:vm.map(nm).join(" "), basse:bass.map(x=>`${nm(x[1])}@${x[0]}(${x[2]})`).join(" "),
     arpege:arp.slice(0,8).map(x=>nm(x[1])).join(" ")+(arp.length>8?" …":""), sho:sho.nom+" ["+sho.notes.map(nm).join(" ")+"]",
     solo:solo.map(x=>nm(x[1])+(x[3]?"("+x[3]+")":"")).join(" "), registreBasse:[Math.min(...bass.map(x=>x[1])),Math.max(...bass.map(x=>x[1]))].map(nm).join("–")});
   t0+=beats;
 });
 return {grille:gr.name, voix:gr.voix, basseSon:gr.basseSon, nappe:gr.nappe, groove:gr.groove, tempo:gr.tempo, total:t0, phrase:(gr.phrase||[]).length, accords:out, problemes:prob};
}'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=["--autoplay-policy=no-user-gesture-required"]); pg=await b.new_page(); errs=[]; pg.on("pageerror",lambda e: errs.append(str(e)))
        await pg.goto("file://"+sys.argv[1]); await pg.wait_for_timeout(4000)
        r=await pg.evaluate(JS, sys.argv[2])
        print(json.dumps({k:v for k,v in r.items() if k!="accords"},ensure_ascii=False,indent=0))
        for a in r["accords"]: print(json.dumps(a,ensure_ascii=False))
        print(errs[:3]); await b.close()
asyncio.run(main())

# enveloppe du mix réel : RMS par fenêtre de 170 ms + index d'accord ; usage: env.py html id secondes [couche|mix]
import asyncio, sys, json
from playwright.async_api import async_playwright
JS=r'''async ([id,sec,L])=>{
 let gr=null; STYLE_FAMILIES.forEach(f=>(f.grids||[]).forEach(x=>{ if(x.id===id){gr=x; _currentFamily=f;} }));
 _loadGridOntoBoard(gr); initAudio();
 const btn=document.createElement("button"); document.body.appendChild(btn); toggleGridPlay(gr,btn);
 let iv=null; if(L!=="mix"){ const set=()=>{ _gridGuitarOn=(L==="guitare"); _gridBassOn=(L==="basse"); _gridDrumsOn=(L==="batterie"); _gridNappeOn=false; _gridSoloOn=(L==="solo"); _gridPhraseOn=(L==="phrase"); }; set(); iv=setInterval(set,50); }
 const an=audioCtx.createAnalyser(); an.fftSize=8192; _sfMix.connect(an); const b=new Float32Array(8192); const out=[]; const t0=performance.now();
 const etat=[_gridGuitarOn,_gridBassOn,_gridDrumsOn,_gridSoloOn,_gridPhraseOn,_gridNappeOn].join(",");
 while(performance.now()-t0<sec*1000){ await new Promise(r=>setTimeout(r,100)); an.getFloatTimeDomainData(b); let s=0; for(const x of b) s+=x*x;
   out.push([((performance.now()-t0)/1000).toFixed(2), _gridCursor, (10*Math.log10(s/b.length+1e-12)).toFixed(1)]); }
 if(iv) clearInterval(iv); return {etat, out};
}'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=["--autoplay-policy=no-user-gesture-required"]); pg=await b.new_page()
        await pg.goto("file://"+sys.argv[1]); await pg.wait_for_timeout(5000)
        r=await pg.evaluate(JS,[sys.argv[2],float(sys.argv[3]),sys.argv[4] if len(sys.argv)>4 else "mix"]); print(json.dumps(r)); await b.close()
asyncio.run(main())

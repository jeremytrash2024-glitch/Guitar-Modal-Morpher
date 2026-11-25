import asyncio, sys, json
from playwright.async_api import async_playwright
JS=r'''async ([id,L,extra])=>{
 let gr=null; STYLE_FAMILIES.forEach(f=>(f.grids||[]).forEach(x=>{ if(x.id===id){gr=x; _currentFamily=f;} }));
 eval(extra||"");
 _loadGridOntoBoard(gr); initAudio();
 const set=()=>{ _gridGuitarOn=(L==="guitare"); _gridBassOn=(L==="basse"); _gridDrumsOn=(L==="batterie"); _gridNappeOn=(L==="nappe"); _gridSoloOn=(L==="solo"); _gridPhraseOn=(L==="phrase"); _gridTaikoOn=false; };
 set(); const btn=document.createElement("button"); document.body.appendChild(btn);
 toggleGridPlay(gr,btn); const iv=setInterval(set,50);
 await new Promise(r=>setTimeout(r,800));
 const bp=audioCtx.createBiquadFilter(); bp.type="highpass"; bp.frequency.value=300; const lp=audioCtx.createBiquadFilter(); lp.type="lowpass"; lp.frequency.value=3000; bp.connect(lp);
 const an=audioCtx.createAnalyser(); an.fftSize=8192; lp.connect(an); const an2=audioCtx.createAnalyser(); an2.fftSize=8192; _sfMix.connect(bp); _sfMix.connect(an2);
 const b=new Float32Array(8192); let s=0,s2=0,n=0;
 for(let i=0;i<80;i++){ await new Promise(r=>setTimeout(r,150)); an.getFloatTimeDomainData(b); for(const x of b){s+=x*x;} an2.getFloatTimeDomainData(b); for(const x of b){s2+=x*x;} n+=b.length; }
 clearInterval(iv);
 return {couche:L, bandeTel:(10*Math.log10(s/n+1e-12)).toFixed(1), total:(10*Math.log10(s2/n+1e-12)).toFixed(1), soloVoix:(typeof _soloVoixId==="function"?_soloVoixId():null), phraseSon:_phraseSonGrille};
}'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=["--autoplay-policy=no-user-gesture-required"])
        for L in sys.argv[3].split(","):
            pg=await b.new_page(); await pg.goto("file://"+sys.argv[1]); await pg.wait_for_timeout(5000)
            r=await pg.evaluate(JS,[sys.argv[2],L,sys.argv[4] if len(sys.argv)>4 else ""]); print(json.dumps(r,ensure_ascii=False)); await pg.close()
        await b.close()
asyncio.run(main())

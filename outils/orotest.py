import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=["--autoplay-policy=no-user-gesture-required"]); pg=await b.new_page(); errs=[]
        pg.on("pageerror", lambda e: errs.append(str(e)))
        await pg.goto("file://"+sys.argv[1]); await pg.wait_for_timeout(4000)
        r=await pg.evaluate('''async()=>{ initAudio(); const out={};
          for(const [nom,g] of [["fete",{tempo:110,groove:"rock",chords:[{beats:4}]}],["moteur",{tempo:160,groove:"metal",chords:[{beats:4}]}],["lent",{tempo:70,preset:"ballade",chords:[{beats:4}]}],["ternaire",{tempo:100,groove:"rock",chords:[{beats:3}]}]]){
            const log=[]; const C=_taikoCoup; window._taikoCoup=(ty,t,v)=>log.push(ty[0]+((t-1)/(60/g.tempo)).toFixed(2)+"/"+v.toFixed(2));
            _gridPlayOn=true; const d=_taikoOroshi(g, audioCtx.currentTime+1-0+0);
            await new Promise(r=>setTimeout(r, d*1000+1300)); window._taikoCoup=C; out[nom]=[d.toFixed(2), log.length, log.join(" ")]; }
          _gridPlayOn=false; return out; }''')
        for k,v in r.items(): print(k,v)
        print(errs); await b.close()
asyncio.run(main())

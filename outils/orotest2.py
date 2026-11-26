import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=["--autoplay-policy=no-user-gesture-required"]); pg=await b.new_page(); errs=[]
        pg.on("pageerror", lambda e: errs.append(str(e)))
        await pg.goto("file://"+sys.argv[1]); await pg.wait_for_timeout(4000)
        r=await pg.evaluate('''async()=>{ let gr=null,fam=null; STYLE_FAMILIES.forEach(f=>(f.grids||[]).forEach(x=>{ if(!gr && !f.nouveautes && _taikoAuto(x)){gr=x;fam=f;} }));
          _currentFamily=fam; _loadGridOntoBoard(gr); initAudio(); const btn=document.createElement("button"); document.body.appendChild(btn);
          let n=0; const C=_taikoCoup; window._taikoCoup=(a,b,c)=>{n++; C(a,b,c);};
          const t0=audioCtx.currentTime; toggleGridPlay(gr,btn); const st=[];
          for(let i=0;i<8;i++){ await new Promise(r=>setTimeout(r,800)); st.push((audioCtx.currentTime-t0).toFixed(1)+"s c"+_gridCursor+" oroshi"+n); }
          stopGridPlay(true); const n1=n; await new Promise(r=>setTimeout(r,500));
          // relance après pause : pas d'oroshi
          n=0; toggleGridPlay(gr,btn); await new Promise(r=>setTimeout(r,2500)); stopGridPlay(false);
          return [gr.id, gr.tempo, _gridTaikoOn, st, "reprise:"+n]; }''')
        print(r, errs); await b.close()
asyncio.run(main())

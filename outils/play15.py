import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=["--autoplay-policy=no-user-gesture-required"]); pg=await b.new_page(); errs=[]; pg.on("pageerror",lambda e: errs.append(str(e))); pg.on("console",lambda m: errs.append("C:"+m.text) if m.type in("error","warning") else None)
        await pg.goto("file://"+sys.argv[1]); await pg.wait_for_timeout(4000)
        r=await pg.evaluate('''async(id)=>{ let gr=null; STYLE_FAMILIES.forEach(f=>f.grids.forEach(x=>{ if(x.id===id){gr=x;_currentFamily=f;} }));
          _loadGridOntoBoard(gr); initAudio(); const btn=document.createElement("button"); document.body.appendChild(btn);
          const st=[]; toggleGridPlay(gr,btn); for(let i=0;i<10;i++){ await new Promise(r=>setTimeout(r,1500)); st.push([_gridPlayOn,_gridCursor, typeof _diagRetard!=="undefined"?_diagRetard:""].join("/")); }
          return st; }''', sys.argv[2])
        print(r, errs[:8]); await b.close()
asyncio.run(main())

import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=["--autoplay-policy=no-user-gesture-required"]); pg=await b.new_page(); errs=[]
        pg.on("pageerror", lambda e: errs.append(str(e)))
        await pg.goto("file://"+sys.argv[1]); await pg.wait_for_timeout(4000)
        r=await pg.evaluate('''async()=>{ initAudio(); _taikoRendre(); for(let i=0;i<40 && !_taikoEch;i++) await new Promise(r=>setTimeout(r,200));
          const pk=b=>{let m=0;const d=b.getChannelData(0);for(const x of d)m=Math.max(m,Math.abs(x));return m.toFixed(3);};
          _taikoKa(audioCtx.currentTime+0.1,0.5);
          return {don:_taikoEch.don.map(pk), ten:_taikoEch.ten.map(pk), ka:_taikoEch.ka.map(pk), dur:_taikoEch.ka[0].duration}; }''')
        print(r, errs); await b.close()
asyncio.run(main())

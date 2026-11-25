import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(); await pg.goto("file://"+sys.argv[1]); await pg.wait_for_timeout(3500)
        r=await pg.evaluate('''(id)=>{ let gr=null; STYLE_FAMILIES.forEach(f=>f.grids.forEach(x=>{ if(x.id===id) gr=x; })); _loadGridOntoBoard(gr);
          const B=_ligneBasseEcrite(gr).notes, out=[];
          [0,1].forEach(v=>{ const P=(v&&gr.phrase2?gr.phrase2:gr.phrase).map(([n,t,d])=>[_phraseMidi(n),t,d,n]);
            P.forEach(([m,t,d,n])=>B.forEach(x=>{ const o=Math.min(t+d,x.temps+x.dur)-Math.max(t,x.temps); const iv=Math.abs(m-x.midi)%12; if(o>=0.5&&(iv==1||iv==11)) out.push("tour"+(v+1)+" "+n+"@"+t+" / basse "+x.midi+"@"+x.temps); })); });
          return out; }''', sys.argv[2])
        print(r); await b.close()
asyncio.run(main())

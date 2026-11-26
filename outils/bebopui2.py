import asyncio, sys
from playwright.async_api import async_playwright
JS=r'''()=>{
 const r={}; const N=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"];
 r.modes=SCALES.bebop.modes.map(m=>m.name+" : "+m.formula.map(x=>N[x]).join(" "));
 r.optgroups=[...document.querySelectorAll("optgroup")].filter(o=>o.label==="Bebop").map(o=>o.children.length);
 r.mem=[0,1,2,3].map(i=>{ try{ return _memNom(10*MEM_FAMS.indexOf("bebop")+i); }catch(e){ return String(e); } });
 return r;
}'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(); errs=[]
        pg.on("pageerror", lambda e: errs.append(str(e)))
        await pg.goto("file://"+sys.argv[1]); await pg.wait_for_timeout(4000)
        r=await pg.evaluate(JS)
        for k,v in r.items(): print(k,v)
        print('erreurs JS:',errs); await b.close()
asyncio.run(main())

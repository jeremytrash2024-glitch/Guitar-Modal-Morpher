import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(); await pg.goto("file://"+sys.argv[1]); await pg.wait_for_timeout(3000)
        r=await pg.evaluate('''()=>{ const out=[]; STYLE_FAMILIES.forEach(f=>{ if(f.id!=="jazz") return; f.grids.forEach(g=>{
          let mx=0, bad=[]; g.chords.forEach(c=>{ const fr=c.voicing.split("-").filter(x=>x!=="x").map(Number).filter(x=>x>0); if(!fr.length) return; const s=Math.max(...fr)-Math.min(...fr); if(s>mx) mx=s; if(s>=4) bad.push(c.name+" "+c.voicing); });
          out.push([g.id, g.tempo, g.chords.length, mx, g.phrase?"ECRIT":"", bad.join(" ; ")].join(" | ")); }); }); return out; }''')
        print("\n".join(r)); await b.close()
asyncio.run(main())

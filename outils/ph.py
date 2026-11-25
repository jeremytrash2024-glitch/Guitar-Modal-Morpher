import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(); await pg.goto("file://"+sys.argv[1]); await pg.wait_for_timeout(4000)
        for gid in sys.argv[2:]:
            r=await pg.evaluate('''(gid)=>{ let gr=null; STYLE_FAMILIES.forEach(f=>(f.grids||[]).forEach(x=>{ if(x.id===gid) gr=x; }));
              const m=n=>_phraseMidi(n); let t=0; const out=[];
              gr.chords.forEach(c=>{ const s0=t; const T=[40,45,50,55,59,64]; const vm=String(c.voicing).split("-").map((x,i)=>x==="x"?null:T[i]+(+x)).filter(x=>x!==null); ["soloEcrit","soloEcrit2"].forEach(k=>(c[k]||[]).forEach(n=>{ const a=s0+n[0], z=a+n[2], sm=m(n[1]);
                 gr.phrase.forEach(p=>{ const pa=p[1], pz=p[1]+p[2]; if(pa<z && a<pz){ const d=Math.abs(sm-m(p[0]))%12; if(d===1||d===11) out.push(k+" "+c.name+" "+n[1]+"/"+p[0]); } }); }));
                 gr.phrase.forEach(p=>{ if(p[1]>=s0 && p[1]<s0+c.beats){ const pc=m(p[0])%12; vm.forEach(v=>{ const d=Math.abs(v-m(p[0]))%12; if(d===1||d===11) out.push("accord "+c.name+" "+p[0]); }); } });
                 t+=c.beats; });
              return out; }''',gid)
            print(gid, r)
        await b.close()
asyncio.run(main())

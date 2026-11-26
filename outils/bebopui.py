import asyncio, sys
from playwright.async_api import async_playwright
JS=r'''()=>{
 const r={};
 r.famille=SCALES.bebop && SCALES.bebop.modes[0].name;
 r.memFams=MEM_FAMS.slice(-2);
 // menu de gammes : l'optgroup Bebop existe-t-il quelque part ?
 r.optgroups=[...document.querySelectorAll("optgroup")].filter(o=>o.label==="Bebop").length;
 // affichage de la gamme sur le manche pour l'accord Sib 9
 let gr=null; STYLE_FAMILIES.forEach(f=>(f.grids||[]).forEach(x=>{ if(x.id==="jz-carlton-quartes-sans-fonda") gr=x; }));
 const c=gr.chords.find(c=>c.name==="Bb9"); r.gammeSib9=JSON.stringify(c.scale);
 try{ _loadGridOntoBoard(gr); r.charge=true; }catch(e){ r.charge=String(e); }
 // la mémoire : chaque identifiant valide
 try{ r.memNom=_memNom(10*MEM_FAMS.indexOf("bebop")); }catch(e){ r.memNom=String(e); }
 return r;
}'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(); errs=[]
        pg.on("pageerror", lambda e: errs.append(str(e)))
        await pg.goto("file://"+sys.argv[1]); await pg.wait_for_timeout(4000)
        print(await pg.evaluate(JS)); print('erreurs JS:',errs); await b.close()
asyncio.run(main())

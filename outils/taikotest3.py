import asyncio, sys
from playwright.async_api import async_playwright
JS=r'''()=>{
 const log=[]; const D=_taikoDon, Tn=_taikoTen, K=_taikoKa; window._taikoKa=(t,v)=>log.push("K"+(Math.round(t*100)/100));
 window._taikoDon=(t,v)=>log.push("D"+(Math.round(t*100)/100)); window._taikoTen=(t,v)=>log.push("t"+(Math.round(t*100)/100));
 _gridTaikoOn=true; const out={};
 for(const [nom,gr,ch] of [["lent",{tempo:70,preset:"ballade",groove:"jazz"},{}],["fete",{tempo:110,groove:"rock"},{}],["moteur",{tempo:160,groove:"rock"},{}],["ternaire",{tempo:100,groove:"shuffleBlues"},{groove:"shuffleBlues"}]]){
   _activeGrid=gr; out[nom]=[];
   for(let n=0;n<16;n++){ log.length=0; _scheduleTaikoBar(0,4,1,(n%2===1),ch,{barIdx:n,finGrille:n===15}); out[nom].push("m"+(n+1)+": "+log.join(" ")); }
 }
 window._taikoDon=D; window._taikoTen=Tn; window._taikoKa=K; return out;
}'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(); errs=[]
        pg.on("pageerror", lambda e: errs.append(str(e)))
        await pg.goto("file://"+sys.argv[1]); await pg.wait_for_timeout(4000)
        r=await pg.evaluate(JS)
        for k,v in r.items():
            print(k); [print('   ',x) for x in v]
        print('erreurs JS:',errs); await b.close()
asyncio.run(main())

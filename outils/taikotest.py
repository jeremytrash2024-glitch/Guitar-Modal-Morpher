import asyncio, sys, json
from playwright.async_api import async_playwright
JS=r'''()=>{
 const log=[]; const D=_taikoDon, Tn=_taikoTen;
 window._taikoDon=(t,v)=>log.push(["don",+t.toFixed(3),+v.toFixed(2)]); window._taikoTen=(t,v)=>log.push(["ten",+t.toFixed(3),+v.toFixed(2)]);
 _gridTaikoOn=true; const out={};
 const cas=[["ballade 70",{tempo:70,preset:"ballade",groove:"jazz"},{},4,false],["ballade fin",{tempo:70,preset:"ballade",groove:"jazz"},{},4,true],
   ["fête 110",{tempo:110,groove:"rock"},{},4,false],["fête fin",{tempo:110,groove:"rock"},{},4,true],
   ["metal 120",{tempo:120,groove:"gallop"},{},4,false],["rapide 160",{tempo:160,groove:"rock"},{},4,false],
   ["3/4",{tempo:100,groove:"valse"},{},3,false],["shuffle",{tempo:100,groove:"shuffleBlues"},{groove:"shuffleBlues"},4,false]];
 for(const [nom,gr,ch,bb,fin] of cas){ _activeGrid=gr; log.length=0; _scheduleTaikoBar(0,bb,1,fin,ch); out[nom]={motif:_taikoMotifPour(ch,bb), coups:log.map(x=>x[0]+"@"+(Math.round(x[1]*100)/100))}; }
 window._taikoDon=D; window._taikoTen=Tn; return out;
}'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(); errs=[]
        pg.on("pageerror", lambda e: errs.append(str(e)))
        await pg.goto("file://"+sys.argv[1]); await pg.wait_for_timeout(4000)
        r=await pg.evaluate(JS)
        for k,v in r.items(): print(k, v['motif'], ' '.join(v['coups']))
        print('erreurs JS:',errs)
        await b.close()
asyncio.run(main())

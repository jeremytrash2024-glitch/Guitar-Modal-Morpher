import re,sys,json
sys.path.insert(0,'/tmp/t'); from lib import midi
src=open(sys.argv[1]).read(); gid=sys.argv[2]
i0=src.index('{id:"%s",'%gid); blk=src[i0:src.index('\n{id:',i0+10)]
O=[40,45,50,55,59,64]
ch=re.findall(r'\{name:"([^"]+)",beats:([\d.]+)[^}]*?voicing:"([^"]+)"[^}]*?basseLigne:(\[\[.*?\]\]),soloEcrit:(\[\[.*?\]\]),soloEcrit2:(\[\[.*?\]\])\}',blk)
def J2(s): return json.loads(re.sub(r"(?<![\d])\.(\d)",r"0.\1",s))
N=["Do","Do#","Ré","Ré#","Mi","Fa","Fa#","Sol","Sol#","La","La#","Si"]
def nm(m): return N[m%12]+str(m//12-1)
for k,(name,beats,v,bl,se,se2) in enumerate(ch):
    vm=[O[i]+int(f) for i,f in enumerate(v.split('-')) if f!='x']
    ref=min(vm)-12
    while ref>45: ref-=12
    bass=[(b,ref+o,d) for b,o,d in J2(bl)]
    mel=[(b,midi(n),d) for b,n,d,*_ in J2(se2)]
    rep=[(b,midi(n),d) for b,n,d,*_ in J2(se)]
    out=[]
    for lab,L in (("sax",mel),("rép",rep)):
        for b,m,d in L:
            for c in vm:
                if d>=1 and (m-c)%12==1 and m>c: out.append(f"{lab} {nm(m)}@{b} ({d}t) / accord {nm(c)}")
            for bb,bm,bd in bass:
                if bb<b+d and b<bb+bd and (m-bm)%12==1 and min(b+d,bb+bd)-max(b,bb)>=1: out.append(f"{lab} {nm(m)}@{b} / basse {nm(bm)}@{bb}")
    print(k+1,name,v,"| "+" ; ".join(out) if out else "")

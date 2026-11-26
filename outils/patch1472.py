import sys,json,re; sys.path.insert(0,'/tmp/t'); from lib import J
src=open('/tmp/t/v1471.html',encoding='utf-8').read(); E=[]
def P(s): return json.loads(re.sub(r'(?<![\d"])\.(\d)',r'0.\1',s))
CH=re.compile(r'\{name:"([^"]+)",beats:([\d.]+),(sig:[\d.]+,)?voicing:"([^"]+)",scale:"([^"]+)",basseLigne:(\[\[.*?\]\]),soloEcrit:(\[\[.*?\]\]),soloEcrit2:(\[\[.*?\]\])\}')
def patch(gid, mods, phrase2_from_R=True, note=""):
    global src
    i0=src.index('{id:"%s",'%gid); i1=src.index('\n{id:',i0+10); old=src[i0:i1]; blk=old
    ms=list(CH.finditer(blk)); assert len(ms)==16,(gid,len(ms))
    rows=[]; t=0
    for k,m in enumerate(ms):
        name,beats,sig,v,sc,bl,se,se2=m.groups(); beats=float(beats)
        bl,se,se2=P(bl),P(se),P(se2)
        md=mods.get(k+1,{})
        name=md.get("name",name); v=md.get("voicing",v)
        if "M" in md: se2=md["M"]
        if "R" in md: se=md["R"]
        if "bl" in md:
            for idx,val in md["bl"]: bl[idx][1]=val
        rows.append((name,beats,sig,v,sc,bl,se,se2,t)); t+=beats
    newchords=[]
    for (name,beats,sig,v,sc,bl,se,se2,t0) in rows:
        b='%g'%beats
        newchords.append('{name:"%s",beats:%s,%svoicing:"%s",scale:"%s",basseLigne:%s,soloEcrit:%s,soloEcrit2:%s}'%(name,b,sig or "",v,sc,J(bl),J(se),J(se2)))
    a=ms[0].start(); z=ms[-1].end()
    blk=blk[:a]+",\n".join(newchords)+blk[z:]
    P1=[[n,t0+b,d] for (_,_,_,_,_,_,_,se2,t0) in rows for b,n,d,*_ in se2]
    def fixnum(x):
        return [[n,(int(tt) if float(tt).is_integer() else tt),d] for n,tt,d in x]
    blk=re.sub(r'phrase:\[\[.*?\]\], phrase2:', 'phrase:%s, phrase2:'%J(fixnum(P1)), blk, count=1)
    if phrase2_from_R:
        P2=[[n,t0+b,d] for (_,_,_,_,_,_,se,_,t0) in rows for b,n,d,*_ in se]
        blk=re.sub(r'phrase2:\[\[.*?\]\],', 'phrase2:%s,'%J(fixnum(P2)), blk, count=1)
    blk=blk.replace(" ; contrebasse */"," ; v1472 : frottements tenus retirés%s ; contrebasse */"%note,1)
    # édition minimale : du premier au dernier caractère différent
    p=0
    while old[p]==blk[p]: p+=1
    q=0
    while old[-1-q]==blk[-1-q]: q+=1
    o=old[p:len(old)-q]; n=blk[p:len(blk)-q]
    while src.count(o)!=1: p-=1; o=old[p:len(old)-q]; n=blk[p:len(blk)-q]
    src=src.replace(o,n); E.append({"old_text":o,"new_text":n})
patch("jz-wes-quintes-fam",{14:{"M":[[0,"A#4",1],[1,"G#4",.5],[1.5,"F#4",.5],[2,"A#4",1.5]]}},phrase2_from_R=False)
patch("jz-drop2-voiceleading",{3:{"name":"C6","voicing":"x-x-7-9-8-8"},12:{"M":[[0,"F5",1],[1,"D5",.5],[1.5,"C5",.5],[2,"A#4",1.5]]}})
patch("jz-cm-tour-riche",{6:{"M":[[0,"D5",1],[1,"C5",.5],[1.5,"A#4",.5],[2,"F4",1.5]]},8:{"bl":[(1,10)]},14:{"M":[[0,"F4",1],[1,"G4",.5],[1.5,"B4",.5],[2,"F4",1],[3,"G#4",.5]]}})
patch("jz-descente-eclats",{12:{"M":[[0,"G#4",1],[1,"F4",.5],[1.5,"C5",.5],[2,"G4",1.5]]},14:{"M":[[0,"B4",1],[1,"C5",.5],[1.5,"D5",.5],[2,"E5",1.5]]}})
patch("jz-mesure-impaire",{6:{"R":[[3,"D5",.5],[3.5,"C5",.5],[4,"F4",1]]},7:{"M":[[0,"A#4",2.5,"vib"],[3,"A4",.5],[3.5,"G4",.5],[4,"A4",1]]},10:{"M":[[0,"E5",.5],[.5,"D5",.5],[1,"G4",1]]}})
patch("jz-trois-paliers",{2:{"name":"F#9","voicing":"2-x-2-3-2-4"},7:{"name":"Bbm7","voicing":"6-x-6-6-6-x"},15:{"name":"G#m7","voicing":"4-x-4-4-4-x"}})
patch("jz-paliers-quarte",{2:{"name":"F#9","voicing":"2-x-2-3-2-4"},6:{"M":[[0,"D#5",1],[1,"C5",.5],[1.5,"A4",.5],[2,"B4",1.5]]},14:{"M":[[0,"C#5",1],[1,"A#4",.5],[1.5,"G4",.5],[2,"G4",1.5]]}})
open('/tmp/t/v1472.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1472.json','w'),ensure_ascii=False)
print(len(E),[len(e["old_text"]) for e in E])

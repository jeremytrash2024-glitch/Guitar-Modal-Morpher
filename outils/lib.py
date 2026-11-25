import json,re
PC={'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11}
def midi(n): m=re.match(r'([A-G]#?)(\d)',n); return 12*(int(m.group(2))+1)+PC[m.group(1)]
TUN=[40,45,50,55,59,64]
def low(v): return min(TUN[i]+int(x) for i,x in enumerate(v.split('-')) if x!='x')
def J(x): return re.sub(r'(?<![0-9])0\.5',r'.5',json.dumps(x,separators=(',',':')).replace('.0,',',').replace('.0]',']'))
def bassline(v, notes):  # notes: [[beat,"F2",dur],...]
    ref=low(v)-12; return [[b, midi(n)-ref, d] for b,n,d in notes]
def chordline(name,b,v,sc,bl,s1,s2,extra=""):
    return '{name:"%s",beats:%d,voicing:"%s",scale:"%s"%s,basseLigne:%s,soloEcrit:%s,soloEcrit2:%s}'%(name,b,v,sc,extra,J(bassline(v,bl)),J(s1),J(s2))

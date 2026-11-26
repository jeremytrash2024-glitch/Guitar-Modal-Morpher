import re
s=open('/tmp/t/g1468.py').read()
a=s.index('S={'); b=s.index('for i in range(16):\n    for b,n,d,*_ in M[i]+Rp[i]: assert')
new=open('/tmp/t/data1474.txt').read()
s=s[:a]+new+s[b:]
s=s.replace("v1467.html","v1473.html").replace("'/tmp/t/v1468.html','w'","'/tmp/t/v1474.html','w'").replace("e1468.json","e1474.json")
s=s.replace('gid="jz-trois-paliers"','gid="jz-modulations-tierces"')
a=s.index('desc=('); b=s.index('new=(')
s=s[:a]+open('/tmp/t/desc1474.txt').read()+s[b:]
s,k=re.subn(r"/\* v1468 : [^*]*\*/","/* v1474 : ballade à 72 bpm, rythme droit, 16 mesures ; A descend par tierces majeures (Do, Lab, Mi, Do) par les V, B remonte par ii-V ; la quinte tenue devient la septième majeure ; contrebasse */",s); assert k==1
s=s.replace('lecons:{cadences:4, modal:4, couleurs:4}, root:"B", scale:"B:0"','lecons:{cadences:4, modal:4}, root:"C", scale:"C:0"')
s=s.replace('name:"Quatre paliers qui glissent — Si, Sib, La, Sol#"','name:"Par tierces majeures — Do, Lab, Mi"')
a=s.index("rep('const NOUVEAUTES"); b=s.index("open('/tmp/t/v1474.html'")
s=s[:a]+open('/tmp/t/nv1474.txt').read()+s[b:]
open('/tmp/t/g1474.py','w').write(s)

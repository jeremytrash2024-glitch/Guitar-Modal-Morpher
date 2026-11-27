import re
s=open('/tmp/t/g1468.py').read()
a=s.index('S={'); b=s.index('for i in range(16):\n    for b,n,d,*_ in M[i]+Rp[i]: assert')
new=open('/tmp/t/data1475.txt').read()
s=s[:a]+new+s[b:]
s=s.replace("v1467.html","v1474.html").replace("'/tmp/t/v1468.html','w'","'/tmp/t/v1475.html','w'").replace("e1468.json","e1475.json")
s=s.replace('gid="jz-trois-paliers"','gid="jz-substitution-triton"')
a=s.index('desc=('); b=s.index('new=(')
s=s[:a]+open('/tmp/t/desc1475.txt').read()+s[b:]
s,k=re.subn(r"/\* v1468 : [^*]*\*/","/* v1475 : ballade à 72 bpm, rythme droit, 16 mesures en Do ; la cadence avec Sol 13 puis avec Réb 9 (mêmes doigts au milieu, basse chromatique), B Mib 9 pour La 7 ; contrebasse */",s); assert k==1
s=s.replace('lecons:{cadences:4, modal:4, couleurs:4}, root:"B", scale:"B:0"','lecons:{dominantes:4, cadences:4, voicings:3}, root:"C", scale:"C:0"')
s=s.replace('name:"Quatre paliers qui glissent — Si, Sib, La, Sol#"','name:"La substitution tritonique — même cadence, autre basse"')
a=s.index("rep('const NOUVEAUTES"); b=s.index("open('/tmp/t/v1475.html'")
s=s[:a]+open('/tmp/t/nv1475.txt').read()+s[b:]
open('/tmp/t/g1475.py','w').write(s)

import re
s=open('/tmp/t/g1468.py').read()
a=s.index('S={'); b=s.index('for i in range(16):\n    for b,n,d,*_ in M[i]+Rp[i]: assert')
new=open('/tmp/t/data1476.txt').read()
s=s[:a]+new+s[b:]
s=s.replace("v1467.html","v1475.html").replace("'/tmp/t/v1468.html','w'","'/tmp/t/v1476.html','w'").replace("e1468.json","e1476.json")
s=s.replace('gid="jz-trois-paliers"','gid="jz-rhythm-changes-pont"')
a=s.index('desc=('); b=s.index('new=(')
s=s[:a]+open('/tmp/t/desc1476.txt').read()+s[b:]
s,k=re.subn(r"/\* v1468 : [^*]*\*/","/* v1476 : ballade à 72 bpm, rythme droit, 16 mesures ; A en Sib (I vi ii V deux fois), pont de quatre dominantes par quartes, la septième glisse vers la tierce suivante ; contrebasse */",s); assert k==1
s=s.replace('lecons:{cadences:4, modal:4, couleurs:4}, root:"B", scale:"B:0"','lecons:{cadences:2, voicings:2, dominantes:2}, root:"A#", scale:"A#:0"')
s=s.replace('name:"Quatre paliers qui glissent — Si, Sib, La, Sol#"','name:"Le pont en ballade — rhythm changes en Sib"')
a=s.index("rep('const NOUVEAUTES"); b=s.index("open('/tmp/t/v1476.html'")
s=s[:a]+open('/tmp/t/nv1476.txt').read()+s[b:]
open('/tmp/t/g1476.py','w').write(s)

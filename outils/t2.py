import re,sys
s=open(sys.argv[1]).read(); gid=sys.argv[2]
i=s.index('{id:"%s"'%gid); j=s.index(']}]},',s.index('chords:[',i))+5
g=s[i:j]
p1=re.search(r'phrase:(\[\[.*?\]\]), phrase2:(\[\[.*?\]\])',g)
g2=g.replace('phrase:'+p1.group(1)+', phrase2:'+p1.group(2),'phrase:'+p1.group(2)) if p1 else g
g2=re.sub(r'soloEcrit:(\[\]|\[\[.*?\]\]),soloEcrit2:(\[\]|\[\[.*?\]\])',lambda m:'soloEcrit:'+m.group(2),g2)
open('/tmp/t/tour2.html','w').write(s[:i]+g2+s[j:])

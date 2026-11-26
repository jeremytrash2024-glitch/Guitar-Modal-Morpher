import json
src=open('/tmp/t/v1449.html',encoding='utf-8').read(); E=[]
def rep(o,n):
    global src
    assert src.count(o)==1,(src.count(o),o[:90]); src=src.replace(o,n); E.append({"old_text":o,"new_text":n})
rep('''{ name: "Bebop dominante", formula: [0,2,4,5,7,9,10,11], intervals: ["R","2","3","4","5","6","b7","7"] }   // mixolydien + 7e majeure de passage
]}''','''{ name: "Bebop dominante", formula: [0,2,4,5,7,9,10,11], intervals: ["R","2","3","4","5","6","b7","7"] },   // mixolydien + 7e majeure de passage
{ name: "Bebop majeure", formula: [0,2,4,5,7,8,9,11], intervals: ["R","2","3","4","5","b6","6","7"] },   // v1450 — ionien + b6 de passage : pour les maj7 et les 6
{ name: "Bebop dorienne", formula: [0,2,3,4,5,7,9,10], intervals: ["R","2","b3","3","4","5","6","b7"] },   // v1450 — dorien + tierce majeure de passage : pour les m7
{ name: "Bebop mineure mélodique", formula: [0,2,3,5,7,8,9,11], intervals: ["R","2","b3","4","5","b6","6","7"] }   // v1450 — mineur mélodique + b6 de passage : pour les m6 et m(maj7)
]}''')
open('/tmp/t/v1450.html','w',encoding='utf-8').write(src); json.dump(E,open('/tmp/t/e1450.json','w'),ensure_ascii=False)
print('ok',len(E))

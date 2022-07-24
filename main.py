import json

f = open('data.json','rb')
f2 = {'player:' '',
      'game:' '',
      'win:' ''
      }
B = json.load(f)

i = 1
n = 0

for a in B:
    for c in f2:
      print(c, B[n][i])
      i += 1
      if i == 3:
       i = 0
    n += 1







    

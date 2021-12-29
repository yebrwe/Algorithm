a=input()
b=input()
d=dict()
for x in a:
    d[x]=d.get(x,0) + 1
for x in b:
    d[x]=d.get(x,0) - 1
if all(d[k]==0 for k in d):
    print('YES')
else:
    print('NO')

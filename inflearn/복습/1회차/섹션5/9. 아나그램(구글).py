a=input()
b=input()
ch1=dict()
ch2=dict()

for x in a:
  ch1[x]=ch1.get(x, 0) + 1
for x in b:
  ch2[x]=ch2.get(x, 0) + 1

for key, val in  ch1.items():
  if ch2[key] != val:
    print('NO')
    break
else:
  print('YES')
e=[True]*1001
e[0]=e[1]=False
for i in range(2, 1001):
  if e[i]:
    for j in range(2*i, 1001, i):
      e[j] = False
print(e)
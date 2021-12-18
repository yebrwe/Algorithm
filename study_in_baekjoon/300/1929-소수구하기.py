m, n=map(int, input().split())
e=[True]*1000001

e[0]=False
e[1]=False
primes = []
for i in range(2, 1000001):
  if e[i]:
    for j in range(2*i, 1000001, i):
      e[j] = False

for i in range(m, n+1):
  if e[i]:
    print(i)
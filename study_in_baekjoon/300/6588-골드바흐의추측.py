e=[True]*1000001
e[0]=False
e[1]=False
primes = []
for i in range(2, 1000001):
  if e[i]:
    for j in range(2*i, 1000001, i):
      e[j] = False

result = ''
n=int(input())
while n!=0:
  for i in range(n):
    if e[i] and e[n-i]:
      result += f'{n} = {i} + {n-i}\n'
      break
  n=int(input())
print(result[:-1])
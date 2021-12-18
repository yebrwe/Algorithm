n=int(input())
e=[True]*1001
numbers=list(map(int, input().split()))

e[0]=False
e[1]=False
primes = []
for i in range(2, 1001):
  if e[i]:
    for j in range(2*i, 1001, i):
      e[j] = False

print(len([number for number in numbers if e[number]]))
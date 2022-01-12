n, m=map(int, input().split())
a=dict()
for i in range(1, n+1):
    for j in range(1, m+1):
        a[i+j] = a.get(i+j, 0) + 1
max=-2147000000
for x in a:
    if a[x] > max:
        max=a[x]
for x in a:
    if max==a[x]:
        print(x, end=' ')
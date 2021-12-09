n=int(input())
a=[]
d=[[0]*2 for _ in range(n)]

for _ in range(n):
    a.append(int(input()))

if n==1: print(a[0])
else:
    d[0][0]=a[0]
    d[0][1]=0
    d[1][0]=d[0][0]+a[1]
    d[1][1]=a[1]
    for i in range(2, n):
        d[i][0] = a[i] + d[i-1][1]
        d[i][1] = a[i] + max(d[i-2][0], d[i-2][1])
    print(max(d[-1]))


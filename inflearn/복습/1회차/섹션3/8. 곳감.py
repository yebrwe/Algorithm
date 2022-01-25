n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
m=int(input())
for _ in range(m):
    i, d, c=map(int, input().split())
    if d==0:
        for _ in range(c):            
            a[i-1].append(a[i-1].pop(0))
    elif d==1:
        for _ in range(c):
            a[i-1].insert(0, a[i-1].pop())
lt=0
rt=n-1
res=0
for i in range(n):
    for j in range(lt, rt+1):
        res+=a[i][j]
    if i < n//2:
        lt+=1
        rt-=1
    else:
        lt-=1
        rt+=1
print(res)



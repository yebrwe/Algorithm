n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
m=int(input())
b=[list(map(int, input().split())) for _ in range(m)]

for i, dir, cnt in b:
    for _ in range(cnt):
        if dir == 0:
            a[i-1].append(a[i-1].pop(0))
        else:
            a[i-1].insert(0, a[i-1].pop())
s=0
e=n-1
res=0
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i < n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)
    

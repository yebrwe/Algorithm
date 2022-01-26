n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
dx=[0, 1, -1, 0]
dy=[1, 0, 0 ,-1]
cnt=0
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)

for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i+dx[k]][j+dy[k]] < a[i][j] for k in range(4)):
            cnt+=1
print(cnt)



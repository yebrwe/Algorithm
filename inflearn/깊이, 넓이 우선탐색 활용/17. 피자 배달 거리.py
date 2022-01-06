def DFS(L, s):
    global res
    if L==m:
        sum=0
        for x1, y1 in house:
            dis=2147000000
            for x2, y2 in cb:
                dis=min(dis, abs(x1-x2)+abs(y1-y2))
            sum+=dis
        if sum<res:
            res=sum
    else:
        for i in range(s, len(pizza)):
            cb[L]=pizza[i]
            DFS(L+1, i+1)

n, m=map(int, input().split())
board=[list(map(int, input().split())) for _ in range(n)]
house=[]
pizza=[]
cb=[0]*m
res=2147000000
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house.append((i, j))
        if board[i][j] == 2:
            pizza.append((i, j))
DFS(0, 0)
print(res)



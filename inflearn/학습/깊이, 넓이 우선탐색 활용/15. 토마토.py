import sys
from collections import deque
def check():
    for i in range(n):
        for j in range(m):
            if board[i][j]==0:
                return False
    return True
    
dx=[1, 0,-1, 0]
dy=[0, 1, 0,-1]
m, n=map(int, input().split())
board=[list(map(int, input().split())) for _ in range(n)]
dis=[[0]*m for _ in range(n)]
res=0
Q=deque()
for i in range(n):
    for j in range(m):
        if board[i][j]==1:
            Q.append((i, j))
while Q:
    x, y=Q.popleft()
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<m and board[xx][yy]==0:
            board[xx][yy]=1
            dis[xx][yy]=dis[x][y]+1
            Q.append((xx, yy))
            res=max(res, dis[xx][yy])

if check():
    print(res)
else:
    print(-1)




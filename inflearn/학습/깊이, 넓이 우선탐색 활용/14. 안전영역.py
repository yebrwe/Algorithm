import sys
from collections import deque
sys.stdin=open(r'./inflearn/input.txt', 'rt')
# sys.setrecursionlimit(10**6)

dx=[0, 1, 0,-1]
dy=[1, 0,-1, 0]
Q=deque()
def BFS(x, y, k):    
    ch[x][y]=1
    Q.append((x, y))
    while Q:
        x, y=Q.popleft()
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<n and 0<=yy<n and board[xx][yy]>k and ch[xx][yy]==0:
                ch[xx][yy]=1
                Q.append((xx, yy))

if __name__ == '__main__':
    n=int(input())
    board=[list(map(int, input().split())) for _ in range(n)]
    res=-2147000000
    for k in range(100):
        cnt=0
        ch=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if board[i][j] > k and ch[i][j]==0:
                    BFS(i, j, k)
                    cnt+=1
        if cnt>res:
            res=cnt
    print(res)
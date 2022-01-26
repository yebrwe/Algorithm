from collections import deque
dx=[-1, 0, 1, 0,-1, 1,-1, 1]
dy=[ 0, 1, 0,-1, 1,-1,-1, 1]
def BFS(x, y):
    Q=deque()
    Q.append((x, y))
    board[x][y]=0
    while Q:
        x, y=Q.popleft()
        for i in range(8):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<n and 0<=yy<n and board[xx][yy]==1:
                board[xx][yy]=0
                Q.append((xx, yy))
    
if __name__ == '__main__':
    n=int(input())
    board=[list(map(int, input().split())) for _ in range(n)]
    cnt=0
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                cnt+=1
                BFS(i, j)
    print(cnt)




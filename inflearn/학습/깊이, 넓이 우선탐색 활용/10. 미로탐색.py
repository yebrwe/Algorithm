import sys
def DFS(x, y):
    global cnt
    if x==6 and y==6:
        cnt+=1
    else:
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<7 and 0<=ny<7 and board[nx][ny]==0:
                board[nx][ny]=1
                DFS(nx, ny)
                board[nx][ny]=0
dx=[1,0,-1,0]
dy=[0,1,0,-1]
board=[list(map(int, input().split())) for _ in range(7)]
cnt=0
board[0][0]=1
DFS(0, 0)
print(cnt)


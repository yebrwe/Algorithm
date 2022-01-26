dx=[0, 0,-1]
dy=[1,-1,0]
def DFS(x, y):
    ch[x][y]=1
    if x==0:
        print(y)
    else:
        for i in range(3):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<10 and 0<=yy<10 and ch[xx][yy]==0 and board[xx][yy]==1:
                DFS(xx, yy)
                break

board=[list(map(int, input().split())) for _ in range(10)]
ch=[[0]*10 for _ in range(10)]
for i in range(10):
    if board[9][i]==2:
        DFS(9, i)
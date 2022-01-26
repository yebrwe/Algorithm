dx=[1,0,-1,0]
dy=[0,1,0,-1]
def DFS(x, y):
    global cnt
    if x==maxx and y==maxy:
        cnt+=1
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<=n-1 and 0<=yy<=n-1 and ch[xx][yy]==0 and board[x][y] < board[xx][yy]:
                ch[xx][yy]=1
                DFS(xx, yy)
                ch[xx][yy]=0

if __name__=='__main__':
    n=int(input())
    board=[list(map(int, input().split())) for _ in range(n)]
    min=2147000000
    minx=0
    miny=0
    max=-2147000000
    maxx=0
    maxy=0
    for i in range(n):
        for j in range(n):
            if board[i][j] < min:
                min=board[i][j]
                minx=i
                miny=j
            if board[i][j] > max:
                max=board[i][j]
                maxx=i
                maxy=j
    ch=[[0]*n for _ in range(n)]
    cnt=0
    ch[minx][miny]=1
    DFS(minx, miny)
    print(cnt)
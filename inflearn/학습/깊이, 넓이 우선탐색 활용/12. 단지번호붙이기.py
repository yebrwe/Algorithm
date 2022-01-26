from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def DFS(x, y):
    global cnt
    board[x][y]=0
    cnt+=1
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<=n-1 and 0<=yy<=n-1 and board[xx][yy]==1:
            DFS(xx, yy)

def BFS(x, y):
    global cnt
    Q=deque()
    Q.append((x, y))
    board[x][y]=0
    cnt+=1
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<=n-1 and 0<=yy<=n-1 and board[xx][yy]==1:
                board[xx][yy]=0
                cnt+=1
                Q.append((xx, yy))

if __name__ == '__main__':
    n=int(input())
    board=[list(map(int, input())) for _ in range(n)]
    res=[]
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                cnt=0
                # DFS(i, j)
                BFS(i, j)
                res.append(cnt)
    res.sort()
    print(len(res))
    for x in res:
        print(x)



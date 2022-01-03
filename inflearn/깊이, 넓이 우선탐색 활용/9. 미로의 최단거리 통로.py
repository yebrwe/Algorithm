from collections import deque
a=[list(map(int, input().split())) for _ in range(7)]
dx=[0, 1, -1 ,0]
dy=[1, 0, 0, -1]
dis=[[0]*7 for _ in range(7)]
Q=deque()
Q.append((0, 0))
a[1][1]=1
while Q:
    tmp = Q.popleft()
    for j in range(4):
        x=tmp[0]+dx[j]
        y=tmp[1]+dy[j]
        if 0<=x<7 and 0<=y<7 and a[x][y]==0:
            a[x][y]=1
            dis[x][y]=dis[tmp[0]][tmp[1]]+1
            Q.append((x, y))
if dis[6][6]==0:
    print(-1)
else:
    print(dis[6][6])
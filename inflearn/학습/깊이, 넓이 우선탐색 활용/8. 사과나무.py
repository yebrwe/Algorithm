import sys
from collections import deque
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
ch=[[0]*n for _ in range(n)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
Q=deque()
Q.append((n//2, n//2))
sum=a[n//2][n//2]
ch[n//2][n//2]=1
L=0
while True:
    if L==n//2:
        break
    size=len(Q)
    for i in range(size):
        tmp=Q.popleft()
        for j in range(4):
            x=tmp[0]+dx[j]
            y=tmp[1]+dy[j]
            if ch[x][y]==0:
                sum+=a[x][y]
                ch[x][y]=1
                Q.append((x, y))
    L+=1
print(sum)

from collections import deque
from sys import stdin
INF=10**8
dy=[-1,0,1,0]
dx=[0,-1,0,1]

def solution():
    w, h = map(int, stdin.readline().split(' '))    
    
    fire_visited = [[INF]*w for _ in range(h)]
    person_visited = [[0]*w for _ in range(h)]

    _map = []
    for i in range(h):
        _map.append(stdin.readline())
    
    q=deque([])
    sy=sx=0
    for i in range(h):
        for j in range(w):
            if _map[i][j] == '*':
                q.appendleft([i,j])
                fire_visited[i][j]=1
            if _map[i][j] == '@':
                sy,sx = i,j
    while q:
        y,x=q.pop()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if not (0<=nx<=w-1 and 0<=ny<=h-1): continue
            if fire_visited[ny][nx] != INF: continue
            if _map[ny][nx] == '#': continue
            fire_visited[ny][nx]=fire_visited[y][x]+1
            q.appendleft([ny,nx])
    
    person_visited[sy][sx]=1
    q=deque([[sy,sx]])
    while q:
        y,x=q.pop()
        if x==0 or y==0 or x==w-1 or y==h-1:
            return person_visited[y][x]            
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if not (0<=nx<=w-1 and 0<=ny<=h-1): continue
            if person_visited[ny][nx] != 0: continue
            if _map[ny][nx] == '#': continue
            if person_visited[y][x]+1 < fire_visited[ny][nx]:
                person_visited[ny][nx]=person_visited[y][x]+1
                q.appendleft([ny,nx])
    return 'IMPOSSIBLE'
    
T=int(stdin.readline())
for _ in range(T):
    print(solution())


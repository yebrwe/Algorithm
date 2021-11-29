from collections import deque

def solution():
    INF = 10**8
    r,c = map(int, input().split())
    maze = ['' for _ in range(r)]
    for i in range(r):
        maze[i]= input()

    q=deque([])
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0 ,1]

    fire_visited = [[INF]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if maze[i][j] == 'F':
                q.appendleft([i,j])
                fire_visited[i][j] = 1

    while q:
        y, x = q.pop()
        for i in range(4):
            ny, nx  = y+dy[i], x+dx[i]
            if nx<0 or nx>c-1 or ny<0 or ny>r-1 or fire_visited[ny][nx] != INF:continue
            if maze[ny][nx] != '#':
                fire_visited[ny][nx] = fire_visited[y][x] + 1
                q.appendleft([ny,nx])
    
    q= deque([])
    human_visited = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if maze[i][j] == 'J':
                q.appendleft([i,j])
                human_visited[i][j] = 1

    while q:
        y, x = q.pop()
        if x == c-1 or x == 0 or y == r-1 or y == 0:
            print(human_visited[y][x])
            return
        for i in range(4):
            ny, nx  = y+dy[i], x+dx[i]
            if nx<0 or nx>c-1 or ny<0 or ny>r-1 or human_visited[ny][nx] != 0:continue
            if maze[ny][nx] != '#' and human_visited[y][x] + 1 < fire_visited[ny][nx]:
                human_visited[ny][nx] = human_visited[y][x] + 1
                q.appendleft([ny,nx])
    print('IMPOSSIBLE')
solution()
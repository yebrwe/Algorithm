from collections import deque
# python 기본 배열로 큐를 사용하면 매우 느리다..
m, n = map(int, input().split())
farm = []

q = deque([])
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def bfs():
    result = 0 

    for i in range(n):
        farm.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(m):
            if farm[i][j] == 1:
                q.appendleft([j, i, 0])
    
    while q:
        x, y, day = q.pop()
        for i in range(4):
            px = x + dx[i]
            py = y + dy[i]
            if px < 0 or py < 0 or px > m - 1 or py > n - 1: continue
            if farm[py][px] == 0: 
                farm[py][px] = day + 1
                q.appendleft([px, py, farm[py][px]])
                result = max(result, farm[py][px])
    
    for i in range(n):
        for j in range(m):
            if farm[i][j] == 0:
                return -1
    return result

print(bfs())
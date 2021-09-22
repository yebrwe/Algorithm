n, m = list(map(int, input().split()))
d = []
visited = []
for _ in range(n):
    d.append(list(map(int, input())))
    visited.append([False] * m)

def bfs() -> int:
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = []

    q.append([0,0,1])
    visited[0][0] = True
    while len(q) > 0:
        x, y, level = q.pop()

        for i in range(4):
            px = x + dx[i]
            py = y + dy[i]

            if px < 0 or py < 0 or px >= n or py >= m: continue
            if visited[px][py]: continue
            if px == n-1 and py == m-1:
                return level + 1
            if d[px][py] == 1:
                visited[px][py] = True
                q.insert(0, [px, py, level + 1])
print(bfs())
from collections import deque
def dfs(graph, v, visited):
    if v not in graph:
        if v not in visited:
            visited.append(v)
    else:
        for vv in sorted(graph[v]):
            if vv not in visited:
                visited.append(vv)
                dfs(graph, vv, visited)
def bfs(graph, v, visited):
    q = deque([v])
    while q:
        vv = q.pop()
        if vv in graph:
            for vvv in sorted(graph[vv]):
                if vvv not in visited:
                    visited.append(vvv)
                    q.insert(0, vvv)

n, m, v = map(int, input().split())
graph = {}
for _ in range(m):
    x, y = map(int, input().split())
    if x not in graph:
        graph[x] = []
    if y not in graph:
        graph[y] = []
    graph[x].append(y)
    graph[y].append(x)

dfs_visited = [v]
dfs(graph, v, dfs_visited)
bfs_visited = [v]
bfs(graph, v, bfs_visited)
print(' '.join([str(v) for v in dfs_visited]))
print(' '.join([str(v) for v in bfs_visited]))



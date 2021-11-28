def solution(n, computers):
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
    count = 0
    visited = []
    while len(visited) < n:
        dfs(graph, visited)
        count += 1
    return count 

def dfs(graph, visited):
    not_visited = [i for i in range(len(graph)) if i not in visited]
    stack = [not_visited[0]]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
        waited = [j for j in graph[node] if j not in visited]
        stack += waited


# print(solution(3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]) ==	2)
# print(solution(3,	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]) ==	1)
print(solution(3,	[[1, 0, 0], [0, 1, 0], [0, 0, 1]]) ==	3)
print(solution(5,	[[1, 1, 0, 0, 0], [1, 1, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 1]]) ==	2)
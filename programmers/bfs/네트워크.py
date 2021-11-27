def solution(n, computers):
    return dfs(n, computers)

def dfs(n, computers):    
    count = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        visited[i][i] = True
    for i in range(n):
        stack=[i]
        while stack:
            i = stack.pop()
            for j in range(i+1, n):
                if visited[i][j]: continue
                visited[i][j] = True
                if computers[i][j] == 1 and i<j:
                    stack.append(j)
                else:
                    count += 1
    return count

    


print(solution(3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]) ==	2)
print(solution(3,	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]) ==	1)
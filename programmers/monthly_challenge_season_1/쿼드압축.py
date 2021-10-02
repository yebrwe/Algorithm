def solution(arr):
    answer = []
    n = len(arr)
    
    print(arr[0][0:2])
    print(arr[0:n//2][0:n//2])
    print(arr[n//2:n][0:n//2])
    print(arr[0:n//2][n//2:n])
    print(arr[n//2:n][n//2:n])

    # while n:
      # print(bfs(arr[0:n//2][0:n//2]))
      # print(bfs(arr[n//2:n][0:n//2]))
      # print(bfs(arr[0:n//2][n//2:n]))
      # print(bfs(arr[n//2:n][n//2:n]))
      # n //= 2
    return answer


def bfs(arr):
    n = len(arr)
    q = [(0,0)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    only = True
    count = [0, 0]
    count[arr[0][0]] += 1
    visited = [[False] * n for _ in range(n)]
    while q:
        x, y = q.pop()
        if x == n-1 and y == n-1: break
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>n-1 or ny<0 or ny>n-1: continue
            if visited[nx][ny]: continue
            if arr[x][y] != arr[nx][ny]: only = False
            count[arr[nx][ny]] += 1
            visited[nx][ny] = True
            q.insert(0, (nx, ny))
    if only:
        return arr[0][0]
    return count


solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])
        
                
                
            
               
    
    
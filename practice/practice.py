def solution(n):
    answer = []
    end = sum([i for i in range(1, n+1)])
    angle = [[0] * i for i in range(1, n+1)]
    visited = [[False] * i for i in range(1, n+1)]
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    
    q = [[0,0]]
    visited[0][0] = True
    angle[0][0] = 1
    cnt = 1
    dir = 0
    while q:
        x, y = q.pop()
        nx, ny = x+dx[dir], y+dy[dir]
        if cnt == end: break
        if 0<=nx<n and 0<=ny<len(angle[nx]) and not visited[nx][ny]:
            cnt += 1
            angle[nx][ny] = cnt
            visited[nx][ny] = True
            q.insert(0, [nx, ny])
        else:
            dir = (dir + 1) % 3
            q.insert(0, [x, y])
    
    for a in angle:
        print(a)
    return answer

print(solution(4))
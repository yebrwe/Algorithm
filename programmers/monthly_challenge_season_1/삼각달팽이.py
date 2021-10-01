def solution(n):
    if n == 1:
        return [1]
    answer = []
    arr = []
    visited = []
    for i in range(1, n+1):
        arr.append([0] * i)
        visited.append([False] * i)

    arr[0][0] = 1
    dir = 0
    q = [(0, 0, 2)]
    #0 - 아래, 1 - 오른쪽, 2 - 위, 3 - 왼쪽
    dx = [1, 0, -1, 0]
    dy = [0, 1, -1, -1]
    while q:        
        x, y, num = q.pop()
        px = x + dx[dir]
        py = y + dy[dir]

        print('(', x, ',',y,') ->', '(', px, ',',py,')', 'dir: ', dir, 'num: ', num)
        
        if px < 0 or py < 0 or px > n-1 or len(arr[px]) <= py:
            dir = (dir + 1) % 4 
            q.insert(0, (x, y, num))
        elif arr[px][py] == 0:
            arr[px][py] = num
            q.insert(0, (px, py, num + 1))
        elif num <= (n * (n+1) /2):
                dir = (dir + 1) % 4 
                q.insert(0, (x, y, num))

    for v in arr:
        answer += v
    
    answer = sum(arr, [])

    return answer
solution(40)
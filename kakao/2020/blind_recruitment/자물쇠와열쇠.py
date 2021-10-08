def solution(key, lock):
    answer = True
    
    return answer



arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

def move(arr, dir):
    n = len(arr)
    tmp = [ [0] * n for _ in range(n)]    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for x in range(n):
        for y in range(n):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or ny < 0 or nx > n-1 or ny > n-1: continue
            tmp[nx][ny] = arr[x][y]
    return tmp

def rotate90(arr):
    n = len(arr)
    tmp = [ [0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[i][j] = arr[n-1-j][i]
    return tmp

def printArray(arr):
    print("============")
    n = len(arr)
    for i in range(n):
        print(arr[i])

printArray(arr)
arr = rotate90(arr)
printArray(arr)
arr = move(arr, 0)
arr = move(arr, 0)
arr = move(arr, 0)
printArray(arr)


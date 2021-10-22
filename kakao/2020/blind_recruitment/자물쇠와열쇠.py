from collections import deque

def reverse_lock(arr):
    n = len(arr)
    tmp = [ [0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[i][j] = 0 if arr[i][j] == 1 else 1
    return tmp

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

def open_lock(key, lock, n):
    q = deque([[key, 0]])
    while q:
        [key, level] = q.pop()
        if level > n // 2: break
        for i in range(4):
            new_key = move(key, i)
            new_key_90 = rotate90(new_key)
            new_key_180 = rotate90(new_key_90)
            new_key_270 = rotate90(new_key_180)
            if lock in [new_key, new_key_90, new_key_180, new_key_270]:
                return True
            q.insert(0, [new_key, level+1])
    return False

def solution(key, lock):
    lock = reverse_lock(lock)
    key_90 = rotate90(key)
    key_180 = rotate90(key_90)
    key_270 = rotate90(key_180)
    if lock in [key, key_90, key_180, key_270]: return True
    n = len(key)
    return open_lock(key, lock, n)


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))



# print('---key---')
# for k in key:
#     print(''.join([str(i) for i in k]))
# print('---lock---')
# for l in lock:
#     print(''.join([str(i) for i in l]))
# print('---new_key-', level, '---')
# for k in new_key:
#     print(''.join([str(i) for i in k]))
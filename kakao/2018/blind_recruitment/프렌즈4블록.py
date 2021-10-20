from collections import Counter
def solution(m, n, board):
    answer = 0
    map = [[board[i][j] for j in range(n)] for i in range(m) ]
    deleted = [[False] * n for i in range(m)]

    while(find(m, n, map, deleted)):
        delete(m, n, map, deleted)
        is_move = True
        while is_move:
            is_move = move(m, n, map)
        deleted = [[False] * n for i in range(m)]

    for i in range(m):
        for j in range(n):
            if map[i][j] == '#':
                answer += 1
    return answer

def find(m, n, map, deleted):
    flag = False
    dirs = [ [-1, 0], [0, -1], [-1, -1] ]
    for i in range(m):
        for j in range(n):
            x, y= i, j
            count = 0
            for [dx, dy] in dirs:
                nx, ny = x+dx, y+dy
                if nx < 0 or ny < 0 or nx > m-1 or ny > n-1: continue
                if map[x][y] != '#' and map[x][y] == map[nx][ny]:
                    count += 1
            if count == 3:
                flag = True
                deleted[x][y] = True
                for [dx, dy] in dirs:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx > m-1 or ny > n-1: continue
                    if map[x][y] == map[nx][ny]:
                        deleted[nx][ny] = True
    return flag

def delete(m, n, map, deleted):
    for i in range(m):
        for j in range(n):
            if deleted[i][j]:
                map[i][j] = '#'  

def move(m, n, map):
    flag = False
    for i in range(m):
        for j in range(n):
            if i+1 == m: continue
            if map[i][j] != '#' and map[i+1][j] == '#':
                flag = True
                map[i][j], map[i+1][j] = map[i+1][j], map[i][j]
    return flag


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]) == 14)
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]) == 15)
print(solution(4, 4, ["CCCC", "CCCC", "CBBC", "CBBC"]) == 12)

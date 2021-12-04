from collections import deque
def solution(drum):
    answer = 0
    for i in range(len(drum)):
        if dfs(drum, 0, i): answer += 1
    return answer

def dfs(drum, y, x):
    n = len(drum)
    dy = [1, 0, 0]
    dx = [0, -1, 1]
    dir = {
        '#': 0,
        '<': 1,
        '>': 2,
        '*': 0
    }
    stack = [[y, x, 0, x]]
    while stack:
        y, x, exit_count, trace = stack.pop()
        #if y == n-1 and dir[drum[y][x]] == 0: #테스트 당시에 문제가 된 부분일듯
        if y == n-1: #구슬이 마지막줄 까지 왔을때는 방향 상관없나봄..
            return True
        next_dir = dir[drum[y][x]]
        ny, nx = y+dy[next_dir], x+dx[next_dir]
        if not (0<=ny<=n-1 and 0<=nx<=n-1): continue
        if drum[ny][nx] == '*':
            if exit_count == 1: return False
            stack.append([ny, nx, exit_count+1, trace])
        else:            
            stack.append([ny, nx, exit_count, trace])
    return False

print(solution(["######",">#*###","####*#","#<#>>#",">#*#*<","######"])==4)
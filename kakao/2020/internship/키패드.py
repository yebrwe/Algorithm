from collections import deque
def solution(numbers, hand):
    answer = ''
    numpad = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        ['*',0,'#'],
    ]

    def get_distance(number, target):
        n, m = len(numpad), len(numpad[0])
        q = deque([])
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        visited = [[False]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if numpad[i][j] == number:
                    visited[i][j] = True
                    q.insert(0, [j, i, 0])
        while q:
            [x, y, w] = q.pop()
            if numpad[y][x] == target: return w
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx > 2 or ny < 0 or ny > 3: continue
                if visited[ny][nx]: continue
                q.insert(0, [nx, ny, w+1])
                visited[ny][nx] = True
        return -1

    left = '*'
    right = '#'
    for number in numbers:
        if number in [1,4,7]:
            left = number
            answer += 'L'
        elif number in [3,6,9]:
            right = number
            answer += 'R'
        else:
            lw, rw = get_distance(left, number), get_distance(right, number)
            if lw < rw:
                answer += 'L'
                left = number
            elif lw > rw:
                answer += 'R'
                right = number
            else:
                if hand == 'right':
                    answer += 'R'
                    right = number
                else:
                    answer += 'L'
                    left = number
    return answer
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == "LRLLLRLLRRL")
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") == "LRLLRRLLLRR")#
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") == "LLRLLRLLRL")
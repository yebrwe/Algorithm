def solution(numbers, target):
    return dfs(numbers, target, 0)

def dfs(numbers, target, result):
    cnt = 0
    if not numbers:
        return 1 if target == result else 0
    cnt += dfs(numbers[1:], target, result + numbers[0])
    cnt += dfs(numbers[1:], target, result - numbers[0])
    return cnt
    



print(solution([1, 1, 1, 1, 1],	3)==	5)
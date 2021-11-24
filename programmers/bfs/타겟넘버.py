def solution(numbers, target):
    # return dfs(numbers, target, 0)
    return dfs_by_stack(numbers, target)

def dfs(numbers, target, result):
    cnt = 0
    if not numbers:
        return 1 if target == result else 0
    cnt += dfs(numbers[1:], target, result + numbers[0])
    cnt += dfs(numbers[1:], target, result - numbers[0])
    return cnt

def dfs_by_stack(numbers, target):
    cnt = 0 
    stack = []
    last_idx = len(numbers) - 1
    stack.append([0, numbers[0]])
    stack.append([0, -numbers[0]])
    while stack:
        idx, rst = stack.pop()
        
        if idx == last_idx:
            if rst == target:
                cnt += 1
        else:
            stack.append([idx+1, rst+numbers[idx+1]])
            stack.append([idx+1, rst-numbers[idx+1]])
    return cnt


print(solution([1, 1, 1, 1, 1],	3)==	5)
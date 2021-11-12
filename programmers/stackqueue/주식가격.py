from collections import deque
def solution(prices):
    answer = []
    n = len(prices)
    for i, p in enumerate(prices):
        time = 0
        for i in range(i+1, n):
            time+=1
            if p > prices[i]: break
        answer.append(time)
    return answer

print(solution([1, 2, 3, 2, 3]) == [4, 3, 1, 1, 0])
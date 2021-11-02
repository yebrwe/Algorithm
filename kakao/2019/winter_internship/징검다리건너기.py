def solution(stones, k):
    left, right = 1, max(stones) + 1
    while left < right:
        print(left, right)
        
        mid = (left + right) // 2
        if test(stones, k, mid):
            left = mid + 1
        else:
            right = mid
    return left
def test(stones, k, mid):
    cnt = 0
    for stone in stones:
        if stone - mid <= 0:
            cnt += 1
        else:
            cnt = 0
        if cnt == k:
            return False
    return True

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
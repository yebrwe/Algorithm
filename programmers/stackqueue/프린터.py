def solution(priorities, location):
    answer = 0

    q = []
    for i, p in enumerate(priorities):
        q.insert(0, [i, p])

    cnt = 0
    while q:
        max = get_max_priority(q)
        i, p = q[-1]
        print(i, q)
        if q[-1][1] < max:
            q.insert(0, q.pop())
        else:
            q.pop()
            cnt += 1
            if location == i: break
    print(cnt)
    return answer
def get_max_priority(arr):
    max = -1
    for i, p in arr:
        if max < p:
            max = p
    return max
solution([2, 1, 3, 2], 1)
solution([1, 1, 9, 1, 1, 1], 0)
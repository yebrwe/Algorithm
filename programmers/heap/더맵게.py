import heapq
def solution(scoville, K):
    answer = 0
    heap = []

    for s in scoville:
        heapq.heappush(heap, s)

    while heap:
        min_scv = abs(heapq.heappop(heap))
        if min_scv < K:
            if heap:
                mix_scv = min_scv + 2 * abs(heapq.heappop(heap))
                heapq.heappush(heap, mix_scv)
                answer +=  1
            else:
                return -1

    return answer

print(solution([1, 2, 3, 9, 10, 12],	7) == 2)
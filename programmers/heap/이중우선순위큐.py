import heapq
def solution(operations):
    h = []
    prev = 1
    for o in operations:
        cmd, n = o.split(" ")
        n = int(n)
        if cmd == 'I':
            if prev == 1:
                heapq.heappush(h, (-n,n))
            else:
                heapq.heappush(h, (n,n))
        else:
            if not h: continue
            k = int(n)
            if prev != k:
                h = [(-a[0], a[1]) for a in h]
                heapq.heapify(h)
            heapq.heappop(h)
            prev = k
    if not h: return [0, 0]
    a1 = heapq.heappop(h)[1]
    h = [(-a[0], a[1]) for a in h]
    heapq.heapify(h)
    a2 = heapq.heappop(h)[1]
    return sorted([a1, a2], reverse=True)



print(solution(["I 16","D 1"])==	[0,0])
print(solution(["I 7","I 5","I -5","D -1"])==	[7,5])
print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"])==	[6,5])
print(solution(	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])==	[333,-45])
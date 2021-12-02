def solution(citations):
    answer = 0
    n = len(citations)
    if sum(citations) == 0: return 0
    for c in sorted(citations, reverse=True):
        h = len([cc for cc in citations if c <= cc])
        if n-h == len([cc for cc in citations if c > cc and h >= cc]):
            answer = h
            break
    return answer
print(solution([3, 0, 6, 1, 5])==	3)
print(solution([0,0,0,0,0]))
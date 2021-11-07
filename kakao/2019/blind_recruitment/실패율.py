def solution(N, stages):
    users = len(stages)
    hash = {}
    for i in range(1, N+1):
        fail = stages.count(i)
        hash[i] = 0 if users == 0 else fail / users
        users -= fail
    return sorted(hash, key=lambda x: -hash[x])

print(solution(5,	[2, 1, 2, 6, 2, 4, 3, 3]) ==	[3,4,2,1,5])
print(solution(4,	[4,4,4,4,4])   ==	[4,1,2,3])

 

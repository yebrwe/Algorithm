def solution(answers):
    a, b, c = [1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]
    len_a, len_b, len_c = len(a), len(b), len(c)
    counts = [0,0,0]
    for i, ans in enumerate(answers):
        counts[0] += 1 if a[i%len_a] == ans else 0
        counts[1] += 1 if b[i%len_b] == ans else 0
        counts[2] += 1 if c[i%len_c] == ans else 0
    max_count = max(counts)
    return [i + 1 for i, count in enumerate(counts) if max_count == count]

print(solution([1,2,3,4,5])==	[1])
print(solution([1,3,2,4,2])==	[1,2,3])
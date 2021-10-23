def convert(n, k):
    if n == 0: return '0'
    notation = ''
    while n > 0:
        div = n // k
        mod = n % k
        notation = str(mod if mod < 10 else hex(mod)[2:]).upper() + notation
        n = div
    return notation

def solution(n, t, m, p):
    arr = []
    for i in range(t*m):
        k = convert(i, n)
        arr.append(k)
    return ''.join([n for i, n in enumerate(''.join(arr)) if i%m+1==p][:t])

print(solution(2	,4	,2	,1	) == "0111")
print(solution(16	,16	,2	,1	) == "02468ACE11111111")
print(solution(16	,16	,2	,2	) == "13579BDF01234567")
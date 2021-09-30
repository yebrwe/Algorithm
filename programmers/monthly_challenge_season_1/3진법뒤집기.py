def solution(n):
    answer = 0
    ntt = notation(n, 3)
    stack = []
    for c in ntt:
        stack.append(c)
    for i in range(len(stack)):
        num = stack.pop()
        answer += 3**i*int(num)
    return answer

def notation(n, base):
    ntt = ''
    while n > 0:
        div = n // base
        mod = n % base
        ntt += str(mod)
        n = div
    return ntt
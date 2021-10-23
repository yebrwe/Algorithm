# 10진수 -> 2진수 변환
def to_bin(n):
    bin = ''
    while n > 0:
        div = n // 2
        mod = n % 2
        bin += str(mod)
        n = div
    return bin[::-1]

# 10진수 -> n진수 변환
def convert(n, k):
    if n == 0: return '0'
    notation = ''
    while n > 0:
        div = n // k
        mod = n % k
        notation = str(mod if mod < 10 else hex(mod)[2:]).upper() + notation
        n = div
    return notation
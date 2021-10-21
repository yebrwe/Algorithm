# 10진수 -> 2진수 변환
def to_bin(n):
    bin = ''
    while n > 0:
        div = n // 2
        mod = n % 2
        bin += str(mod)
        n = div
    return bin[::-1]
def solution(x):
    zero_count = 0
    convert_count = 0
    while x != '1':
        for n in x:
            if n == '0':
                zero_count += 1
        x = to_bin(len(''.join(x.split('0'))))
        convert_count += 1
    return [convert_count, zero_count]
def to_bin(n):
    bin = ''
    while n > 0:
        div = n // 2
        mod = n % 2
        bin += str(mod)
        n = div
    return bin[::-1]
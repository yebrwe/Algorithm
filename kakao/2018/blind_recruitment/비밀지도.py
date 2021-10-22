def solution(n, arr1, arr2):
    answer = ['' for _ in range(n)]
    arr1_bin = [to_bin(x, n).replace('0', ' ').replace('1', '#') for x in arr1]
    arr2_bin = [to_bin(x, n).replace('0', ' ').replace('1', '#') for x in arr2]
    for i in range(n):
        for j in range(n):
            if arr1_bin[i][j] == '#' or arr2_bin[i][j] == '#':
                answer[i] += '#'
            else:
                answer[i] += ' '
    return answer
    
def another_solution(n, arr1, arr2):
    return [to_bin(a|b, n).replace('0', ' ').replace('1', '#') for a,b in zip(arr1, arr2)]

def to_bin(n, w):
    bin = ''
    while n > 0:
        div = n // 2
        mod = n % 2
        bin += str(mod)
        n = div
    return ('0' * (w - len(bin))) + bin[::-1]


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(another_solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
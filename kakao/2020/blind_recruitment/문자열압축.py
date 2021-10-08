def solution(s):
    answer = 0
    n = len(s)
    answer = n
    for i in range(1, n + 1):
        j=0
        k = s
        prev = ''
        cnt = 1
        result = ''
        while k:
            if prev == k[0:i]:
                cnt += 1
            else:
                result += prev if cnt == 1 else str(cnt) + prev
                cnt = 1
                prev = k[0:i]
            k = k[i:]
        result += prev if cnt == 1 else str(cnt) + prev

        l = len(result)
        if answer > l:
            answer = l

    return answer


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
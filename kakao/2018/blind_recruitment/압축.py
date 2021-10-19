def solution(msg):
    answer = []
    dic = {}
    for i in range(26):
        dic[chr(ord('A')+i)] = i + 1
    find(msg, dic, answer)
    # print(dic)
    return answer

def find(w, dic, output):
    if w in dic:
        output.append(dic[w])
        return
    cur = 0
    str = ''
    last_idx = 0
    for i, c in enumerate(w):        
        str += c
        if str not in dic: break
        last_idx = dic[str]
        cur = i
    output.append(last_idx)    
    dic[str] = len(dic) + 1
    find(w[cur+1:], dic, output)

print(solution('KAKAO') == [11, 1, 27, 15])
print(solution('TOBEORNOTTOBEORTOBEORNOT') == [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34])
print(solution('ABABABABABABABAB') == [1, 2, 27, 29, 28, 31, 30])
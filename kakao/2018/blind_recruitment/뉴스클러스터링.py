def solution(str1, str2):
    if str1.lower() == str2.lower(): return 65536
    str1_multi_set = to_multi_set(str1.lower())
    str2_multi_set = to_multi_set(str2.lower())
    
    union = str2_multi_set.copy()
    for v in str1_multi_set:
        if v not in str2_multi_set:
            union.append(v)

    inter = []
    for v in str1_multi_set:
        if v in str2_multi_set:
            inter.append(v)

    union_len = len(union)
    inter_len = len(inter)
    if union_len == 0: return 1
    return int(inter_len / union_len * 65536)

def to_multi_set(str):
    s = []
    l = len(str)
    for i, _ in enumerate(str):
        if i == l - 1: break
        if 'a' <= str[i] <='z' and 'a' <= str[i+1] <= 'z':
            s.append(str[i:i+2])
    return s

print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))
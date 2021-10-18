from collections import Counter
def solution(str1, str2):
    if str1.lower() == str2.lower(): return 65536
    str1_counter = Counter(to_multiset(str1.lower()))
    str2_counter = Counter(to_multiset(str2.lower()))

    union_len = len(list((str1_counter | str2_counter).elements()))
    inter_len = len(list((str1_counter & str2_counter).elements()))
    if union_len == 0: return 1
    return int(inter_len / union_len * 65536)

def to_multiset(str):
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
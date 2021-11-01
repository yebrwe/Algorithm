def solution(s):
    s_arr = [ss.split(',') for ss in s[2:-2].split('},{')]
    tuple = []
    for t in sorted(s_arr, key=lambda x: len(x)):
        for v in t:
            if v not in tuple:
                tuple.append(v)
    return [int(i) for i in tuple]

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}") == [2, 1, 3, 4])
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}") == [2, 1, 3, 4])
print(solution("{{20,111},{111}}") == [111,20])
print(solution("{{123}}") == [123])
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}") == [3, 2, 4, 1])
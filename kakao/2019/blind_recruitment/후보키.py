from itertools import combinations

def solution(relation):
    answer = 0
    keys = []
    row_size = len(relation)
    col_size = len(relation[0])
    for i in range(1, col_size + 1):
        keys.extend(combinations(range(col_size), i))
    keys = [key for key in keys if row_size == len(set([tuple(r[k] for k in key) for r in relation]))]
    
    for i, key in enumerate(keys):
        flag = True
        for subkey in keys[:i] + keys[i+1:]:
            if set(subkey).intersection(set(key)) == set(subkey):
                flag = False
        if flag: answer += 1

    return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]) == 2)
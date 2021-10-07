def solution(clothes):
    answer = 1
    hash = {}
    for c in clothes:
        if c[1] not in hash:            
            hash[c[1]] = [c[0]]
        else:
            hash[c[1]].append(c[0])


    for k in hash:
        answer *= len(hash[k]) + 1
        
    
    return answer - 1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"], ["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))


def solution(k, room_number):
    answer = []
    hash = {}
    for n in room_number:
        if n not in hash:
            hash[n] = n + 1
            answer.append(n)
        else:
            l = n
            fp = [l]
            while True:
                r = hash[l]
                if r not in hash:
                    hash[r] = r + 1
                    answer.append(r)
                    for kk in fp:
                        hash[kk] = r + 1
                    break
                l = r
                fp += [l]
    return answer

print(solution(10**12,	[1,3,4,1,3,1]) == 	[1,3,4,2,5,6])
print(solution(10**12,	[1,5,9,8,7,6,5]) == 	[1,5,9,8,7,6,10])


#Union-Find로도 풀어볼 것
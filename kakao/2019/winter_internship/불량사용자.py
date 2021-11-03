def solution(user_id, banned_id):
    ban_list=[[] for _ in range(len(banned_id))]
    for i, b in enumerate(banned_id):
        for u in user_id:
            if check(b, u) and u not in ban_list[i]:
                ban_list[i] += [u]
    n = len(banned_id)
    print(ban_list)
    arr = [sorted(b) for b in perm(ban_list, []) if len(set(b)) == n]
    new_arr = []

    for a in arr:
        if a not in new_arr:
            new_arr += [a]
    return len(new_arr)

def perm(ban_list, contain):
    output = []
    
    for i, b in enumerate(ban_list):
        for bb in b:
            if bb in contain: continue
            if len(ban_list) == 1:
                output += [[bb]]
            else:
                for a in perm(ban_list[i+1:], contain + [bb]):
                    output += [[bb] + a]
    return output
    

def check(b, u):
    if len(u) != len(b): return False
    for i in range(len(u)):
        if u[i] != b[i] and b[i] != '*': 
            return False
    return True

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],	["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],	["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],	["fr*d*", "*rodo", "******", "******"]))
print(solution(["a", "b", "c", "d", "e", "f", "g", "h"],	["*","*","*","*","*","*","*","*"]))
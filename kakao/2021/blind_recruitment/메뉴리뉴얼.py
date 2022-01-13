comb=['']*10
def solution(orders, course):
    answer = []
    for c in course:
        res=dict()
        for o in orders:
            DFS(0, 0, o, c, res)
        max=2
        for x in res:
            if res[x]>=max:
                max=res[x]
        for x in res:
            if max==res[x]:
                answer.append(x)
    answer.sort()
    return answer

def DFS(L, s, o, c, res):
    if L==c:        
        key=''.join(sorted(list(''.join(comb))))
        res[key]=res.get(key, 0) + 1
    else:
        for i in range(s, len(o)):
            comb[L]=o[i]
            DFS(L+1, i+1, o, c, res)            
        
    
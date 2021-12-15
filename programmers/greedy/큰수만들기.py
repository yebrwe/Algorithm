def solution(number, k):
    stack = []
    cnt=0
    for n in number:
        if not stack:
            stack.append(n)
        else:
            while stack and stack[-1] < n:
                if cnt == k: break
                stack.pop()
                cnt+=1
            stack.append(n)
    return ''.join(stack[:len(number)-k])
        
        
        
        

print(solution("1924",	2)==	"94")
print(solution("1231234",	3)==	"3234")
print(solution("4177252841",	4)==	"775841")

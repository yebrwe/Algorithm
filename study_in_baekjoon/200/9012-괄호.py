n=int(input())
for _ in range(n):
    stack = []
    flag = False
    for c in input():
        if c =='(':
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:                
                flag = True
                break
    
    if flag or stack:
        print('NO')
    else:
        print('YES')
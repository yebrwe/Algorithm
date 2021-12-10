n=int(input())
numbers = [int(input()) for _ in range(n)]
stack = []
pos = 0
result = []
for i in range(1, n+1):
    if not stack or stack[-1] <= numbers[pos]:
        stack.append(i)
        result.append('+')
        if stack[-1] == numbers[pos]:
            while stack and stack[-1] == numbers[pos]:
                pos+=1
                stack.pop()
                result.append('-')
if stack: 
    print('NO')
else:
    for r in result:
        print(r)
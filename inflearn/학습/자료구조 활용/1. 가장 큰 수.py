n, m=map(int, input().split())
a=list(map(int, str(n)))
cnt=0
stack = []
for x in a:
    while stack and stack[-1] < x and cnt < m:
        stack.pop()
        cnt+=1
    stack.append(x)
while cnt < m:
    stack.pop()
    cnt+=1
res=''.join(map(str, stack))
print(res)

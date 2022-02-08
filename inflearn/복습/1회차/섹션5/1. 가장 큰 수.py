n, m=map(int, input().split())
stack=[]
cnt=0
for x in str(n):
    x=int(x)
    while stack and stack[-1] < x and cnt < m:
        stack.pop()
        cnt+=1
    stack.append(x)
for x in stack[:len(str(n))-m]:
    print(x, end='')
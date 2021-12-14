n=int(input())
a=list(map(int, input().split()))
f={}
for i in a:
    if i not in f:
        f[i]=0
    f[i]+=1
result = [-1] * n
stack = [0]
for i in range(1, n):
    while stack and f[a[i]] > f[a[stack[-1]]]:
        result[stack.pop()] = a[i]
    stack.append(i)
print(*result)
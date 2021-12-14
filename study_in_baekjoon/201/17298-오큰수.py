n=int(input())
a = list(map(int, input().split()))
stack=[0]
result = [-1] * n
for i in range(1, n):
    while stack and a[i] > a[stack[-1]]:
        result[stack.pop()] = a[i]
    stack.append(i)
print(*result)
def DFS(L, sum):
    global result
    if result <= L:
        return
    if sum > m:
        return
    if sum == m:
        result=L
    else:
        for i in range(n):
            DFS(L+1, sum + a[i])


n=int(input())
a=list(map(int, input().split()))
m=int(input())
a.sort(reverse=True)
result=2147000000
DFS(0, 0)
print(result)



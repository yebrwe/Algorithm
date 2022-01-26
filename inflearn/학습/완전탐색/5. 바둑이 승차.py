def DFS(L, sum, tsum):
    global max
    if sum+(total-tsum) < max:
        return
    if sum > c:
        return
    if L==n:
        if sum > max:
            max = sum
    else:
        DFS(L+1, sum+a[L], tsum+a[L])
        DFS(L+1, sum, tsum+a[L])
    
c, n=map(int, input().split())
a=[]
max=-2147000000
for _ in range(n):
    a.append(int(input()))
total=sum(a)
DFS(0, 0, 0)
print(max)
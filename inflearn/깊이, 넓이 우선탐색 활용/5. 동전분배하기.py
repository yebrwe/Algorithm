def DFS(L, A, B, C):
    global res
    if L==n:
        if A!=B and B!=C and A!=C:
            mx = max(A,B,C)-min(A,B,C)
            if res > mx:
                res = mx
    else:        
        DFS(L+1, A+a[L], B, C)
        DFS(L+1, A, B+a[L], C)
        DFS(L+1, A, B, C+a[L])
n=int(input())
a=[]
res=2147000000
for _ in range(n):
    a.append(int(input()))
DFS(0, 0, 0, 0)
print(res)
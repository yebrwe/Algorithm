def DFS(L, sum, time):
    global res
    if time>m:
        return
    if L==n:
        if sum>res:
            res=sum  
    else:
        DFS(L+1, sum+pv[L], time+pt[L])
        DFS(L+1, sum, time)
n, m=map(int, input().split())
pv=[]
pt=[]
res=-2147000000
for _ in range(n):
    v, t=map(int, input().split())
    pv.append(v)
    pt.append(t)
DFS(0, 0, 0)
print(res)
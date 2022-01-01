import sys
def DFS(L, sum):
    global res
    if L==n+1:
        if sum>res:
            res=sum
    else:
        if L+T[L] <= n+1:
            DFS(L+T[L], sum+P[L])
        DFS(L+1, sum)
n=int(input())
T=[]
P=[]
res=-2147000000
for _ in range(n):
    t, p=map(int, input().split())
    T.append(t)
    P.append(p)
T.insert(0, 0)
P.insert(0, 0)
DFS(1,0)
print(res)

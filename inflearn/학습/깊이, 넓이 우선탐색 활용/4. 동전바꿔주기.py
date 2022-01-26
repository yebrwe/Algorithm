def DFS(L, sum):
    global cnt
    if sum>t:
        return
    if L==k:
        if sum==t:
            cnt+=1
    else:
        for i in range(N[L]+1):
            DFS(L+1, sum+(P[L]*i))
t=int(input())
k=int(input())
cnt=0
P=[]
N=[]
for _ in range(k):
    p, n=map(int, input().split())
    P.append(p)
    N.append(n)
DFS(0, 0)
print(cnt)

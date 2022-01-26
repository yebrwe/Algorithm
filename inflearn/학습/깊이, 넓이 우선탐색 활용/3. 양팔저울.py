def DFS(L, sum):
    if L==k:
        if sum>0:
            res.add(sum)
    else:
        DFS(L+1, sum+G[L])
        DFS(L+1, sum-G[L])
        DFS(L+1, sum)

        
k=int(input())
G=list(map(int, input().split()))
s=sum(G)
res=set()
DFS(0, 0)
print(s-len(res))
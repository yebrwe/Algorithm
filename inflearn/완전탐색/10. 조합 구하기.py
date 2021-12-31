import sys
def DFS(L, S):
    global cnt
    if L==m:
        for x in res:
            print(x, end=' ')
        print()
        cnt+=1
    else:
        for i in range(S, n+1):
            res[L]=i
            DFS(L+1, i+1)
        
n, m=map(int, input().split())
res=[0]*m
cnt=0
DFS(0, 1)
print(cnt)
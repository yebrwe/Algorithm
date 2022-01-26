import sys
input=sys.stdin.readline

def DFS(L):
    global cnt
    if L==m:
        for x in res:
            print(x, end=' ')
        cnt+=1
        print()
    else:
        for i in range(1, n+1):
            res[L]=i
            DFS(L+1)
n, m=map(int, input().split())
res=[0]*m
cnt=0
DFS(0)
print(cnt)

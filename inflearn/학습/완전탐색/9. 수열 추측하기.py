import sys
def DFS(L, sum):
    if L==n and sum==f:
        for x in p:
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                p[L]=i
                DFS(L+1, sum+(p[L]*b[L]))
                ch[i]=0
            
n, f=map(int, input().split())
a=list(range(1,n+1))
p=[0]*n
b=[1]*n
ch=[0]*(n+1)
for i in range(1, n-1):
    b[i]=b[i-1]*(n-i)//i
DFS(0, 0)

import sys
def DFS(L, sum, tsum):
  global res
  if sum + tot-tsum < res:
    return
  if L==n:
    if c>=sum and res<sum:      
      res=sum
  else:
    DFS(L+1, sum+a[L], tsum+a[L])
    DFS(L+1, sum, tsum+a[L])
c, n=map(int, input().split())
a=[]
res=-2147000000
for _ in range(n):
  a.append(int(input()))
tot=sum(a)
DFS(0, 0, 0)
print(res)


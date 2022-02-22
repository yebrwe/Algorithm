import sys
sys.stdin=open(r"./inflearn/input.txt", "rt")

def DFS(L):
  global cnt
  if L==n:
    sub=0
    for i in range(n):
      if ch[i]==1:
        sub+=a[i]
    if sum-sub==sub:
      cnt+=1
    return
  else:
    ch[L]=1
    DFS(L+1)
    ch[L]=0
    DFS(L+1)
n=int(input())
a=list(map(int, input().split()))
ch=[0]*n
sum=sum(a)
cnt=0
DFS(0)
if cnt==0:
  print('NO')
else:
  print('YES')
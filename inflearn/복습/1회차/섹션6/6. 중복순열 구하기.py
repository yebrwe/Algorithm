import sys
# sys.stdin=open(r"./inflearn/input.txt", "rt")
def DFS(L):
  global cnt
  if L==m:
    cnt+=1
    for x in ch:
      print(x, end=' ')
    print()
  else:
    for i in range(1, n+1):
      ch[L]=i
      DFS(L+1)
n, m=map(int, input().split())
ch=[0]*m
cnt=0
DFS(0)
print(cnt)

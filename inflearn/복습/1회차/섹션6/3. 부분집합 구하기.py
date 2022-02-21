import sys
# sys.stdin=open(r"./inflearn/input.txt", "rt")

def DFS(L):
  if L==n+1:    
    return
  else:
    for i in range(L+1, n+1):
      if i not in res and res[L]==0:
        res[L]=i
        DFS(i)
        for x in res: 
          if x!=0:
            print(x, end=' ')
        print()
        res[L]=0
      
n=int(input())
res=[0]*n
DFS(0)
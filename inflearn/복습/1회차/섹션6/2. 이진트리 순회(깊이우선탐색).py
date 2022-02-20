import sys
sys.stdin=open(r"./inflearn/input.txt", "rt")
def DFS(L):
  if L>7:
    return
  else:
    # print(L, end=' ')
    DFS(2*L)
    # print(L, end=' ')
    DFS(2*L+1)
    # print(L, end=' ')
DFS(1)
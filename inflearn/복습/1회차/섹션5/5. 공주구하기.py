import sys
from collections import deque
# sys.stdin=open(r"./inflearn/input.txt", "rt")
n, k=map(int, input().split())
a=list(range(1, n+1))
a=deque(a)
cnt=0
res=0
while a:
  cnt+=1
  tmp=a.popleft()  
  if cnt==k:
    res=tmp
    cnt=0
  else:
    a.append(tmp)
print(res)

  


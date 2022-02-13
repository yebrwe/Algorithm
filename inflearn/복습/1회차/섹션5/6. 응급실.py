import sys
from collections import deque
# sys.stdin=open(r"./inflearn/input.txt", "rt")
n, m=map(int, input().split())
a=[(x[0], x[1]) for x in enumerate(list(map(int, input().split())))]
a=deque(a)
cnt=0
while a:
  tmp=a.popleft()
  if any(tmp[1] < x[1] for x in a):
    a.append(tmp)
  else:
    cnt+=1
    if tmp[0]==m:
      print(cnt)
      break
    


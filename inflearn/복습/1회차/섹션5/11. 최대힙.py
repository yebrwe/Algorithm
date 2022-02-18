import sys
import heapq as hq
h=[]
while True:
  n=int(input())
  if n==-1:
    break
  elif n==0:
    if hq:
      print(hq.heappop(h)[1])
    else:
      print(-1)
  elif n>0:
    hq.heappush(h, (-n, n))
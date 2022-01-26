import sys
from collections import deque
s=input()
n=int(input())
for i in range(n):    
    plan=input()
    Q = deque(s)
    for x in plan:
        if x in Q and x != Q.popleft():
            break
    if not Q:
        print('#%d YES'%(i+1))
    else:
        print('#%d NO'%(i+1))
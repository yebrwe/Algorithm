from collections import deque
n, m=map(int, input().split())
a=list(map(int, input().split()))
a.sort()
cnt=0
a=deque(a)
while a:
    if len(a) == 1:
        cnt+=1
        break
    if a[0] + a[-1] > m:
        a.pop()
        cnt+=1
    else:
        a.popleft()
        a.pop()
        cnt+=1
print(cnt)
from collections import deque
n, k = map(int, input().split())
result = []
d = deque([i+1 for i in range(n)])
cnt = 0
while d:
    cnt += 1
    if cnt < k:
        d.append(d.popleft())        
    elif cnt == k:
        result.append(str(d.popleft()))
        cnt = 0
print('<'+', '.join(result)+'>')
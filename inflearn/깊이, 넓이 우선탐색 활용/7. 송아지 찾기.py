from collections import deque
MAX=10000
s, e=map(int, input().split())
dis=[0]*MAX
ch=[0]*MAX
dQ=deque()
dQ.append(s)
while dQ:
    now=dQ.popleft()
    if now==e:
        break
    for next in(now+1, now-1, now+5):
        if 0<=next<MAX:
            if ch[next]==0:
                dQ.append(next)
                ch[next]=1
                dis[next]=dis[now]+1
print(dis[e])



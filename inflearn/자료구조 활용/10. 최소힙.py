import heapq as hq

h=[]
while True:
    n=int(input())
    if n==-1:
        break
    elif n==0:
        if h:
            print(hq.heappop(h))
        else:
            print(-1)

    else:
        hq.heappush(h, n)
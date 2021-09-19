import heapq

N = 3
INF = 10**8 + 10
dist = [INF] * (N+1)   #minium distance
roads = [[1, 2, 2], [2, 3, 3]]  #start, end, distance
adj = [[] for _ in range(1004)]
def dijkstra(start)->int:
    heap = []
    dist[start]=0
    heapq.heappush(heap, (start, 0)) # heap -> start, distance

    for s,e,w in roads:
        adj[s].append((e, w))

    while len(heap) > 0:
        u, w = heapq.heappop(heap)

        if dist[u] < w: continue

        for v, ww in adj[u]:
            www = w+ww
            if dist[v] > www:
                dist[v] = www
                heapq.heappush(heap, (v, www))
    return dist


print(dijkstra(1))

            

        
    
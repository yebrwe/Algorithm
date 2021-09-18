import heapq

N = 3
INF = 10**8 + 10
dist = [INF] * (N+1)   #minium distance
roads = [[1, 2, 2], [2, 3, 3]]  #start, end, distance
def dijkstra(start)->int:
    heap = []
    dist[start]=0
    heapq.heappush(heap, (start, 0)) # heap -> start, distance

    edges = {}
    for s,e,w in roads:
        edges[s] = (e, w)

    while len(heap) > 0:
        u, w = heapq.heappop(heap)

        if dist[u] < w:
            continue

        for k in edges:
            v, ww = edges[k]
            www = w+ww
            if dist[v] > www:
                dist[v] = www
                heapq.heappush(heap, (v, www))
    return dist


print(dijkstra(1))

            

        
    
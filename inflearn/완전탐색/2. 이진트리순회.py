def DFS(v):
    if v>7:
        return
    else:
        print(v, end=' ')
        DFS(2*v)
        DFS(2*v+1)
DFS(1)
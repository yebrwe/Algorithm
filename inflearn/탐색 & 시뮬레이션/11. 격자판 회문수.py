a=[list(map(int, input().split())) for _ in range(7)]
res=0
for i in range(7):
    for j in range(3):
        sx=j
        ex=7-3+j
        for k in range(3):
            if a[i][sx+k] != a[i][ex-k]:break
        else:
            res+=1

for i in range(3):
    for j in range(7):
        sy=i
        ey=7-3+i
        for s in range(3):
            if a[sy+s][j] != a[ey-s][j]:break
        else:
            res+=1
print(res)

                

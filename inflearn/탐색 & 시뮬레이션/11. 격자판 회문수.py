import sys
sys.stdin=open(r"./inflearn/input.txt", "rt")
a=[list(map(int, input().split())) for _ in range(7)]
res=0
for i in range(3):
    for j in range(3):
        sx=i
        ex=7-3+i
        sy=j
        ey=7-3+j
        for k in range(3):
            if a[sx][sy+k] != a[sx][ey-k]:break
        else:
            res+=1
        for s in range(3):
            if a[sx+s][sy] != a[ex-s][sy]:break
        else:
            res+=1
print(res)

                

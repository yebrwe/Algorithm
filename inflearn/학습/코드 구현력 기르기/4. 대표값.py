n=int(input())
a=list(map(int, input().split()))
avg=int(sum(a) / n + 0.5)
min=2147000000
score=0
for i,x in enumerate(a):
    k = abs(x-avg)
    if k < min:
        min = k
        score = x
        res = i
    elif k == min:
        if x > score:
            score = x
            res = i
print(avg, res+1)

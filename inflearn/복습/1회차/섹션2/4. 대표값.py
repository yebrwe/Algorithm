n=int(input())
a=list(map(int, input().split()))
avg = int(sum(a) / n + 0.5)
res=2147000000
idx=2147000000
for i, x in enumerate(a):
    if abs(x-avg) < abs(res-avg):        
        res=x
        idx=i
    elif abs(x-avg) == abs(res-avg):
        if  x > res:
            res=x
            idx=i
print(avg, idx+1)
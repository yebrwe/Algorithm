k, n=map(int, input().split())
a=[int(input()) for _ in range(k)]
lt=0
rt=max(a)
res=-2147000000
while lt<=rt:
    mid=(lt+rt)//2
    cnt=0
    for x in a:
        cnt += x//mid
    if cnt < n :
        rt = mid - 1
    elif cnt >= n:
        res = mid
        lt = mid + 1
print(res)
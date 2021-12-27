n, m=map(int, input().split())
a=list(map(int, input().split()))
def Count(mid):
    cnt=0
    sum=0
    for x in a:
        if sum + x > mid:
            sum=0
            cnt+=1
        sum +=x
    return cnt
        
lt=1
rt=sum(a)
res=0
while lt<=rt:
    mid=(lt+rt)//2
    if mid >= max(a) and Count(mid) < m:
        rt = mid-1
        res = mid
    else:
        lt = mid+1
print(res)
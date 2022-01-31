n, m=map(int, input().split())
a=list(map(int, input().split()))
lt=0
rt=sum(a)
res=0
while lt<=rt:
    mid=(lt+rt)//2
    cnt=0
    sum=0
    for x in a:
        if sum+x>=mid:
            sum=0
            cnt+=1
        sum+=x
    if cnt>m:
        lt=mid+1
    elif cnt==m:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)




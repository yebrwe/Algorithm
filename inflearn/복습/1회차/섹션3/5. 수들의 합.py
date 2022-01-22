n, m=map(int, input().split())
a=list(map(int, input().split()))
lt=0
rt=0
cnt=0
sum=0
while lt<n and rt<n:
    if sum<m:
        sum+=a[rt]
        rt+=1
    elif sum>m:
        sum-=a[lt]
        lt+=1
    else:
        cnt+=1
        sum-=a[lt]
        lt+=1
while lt<rt:
    if sum==m:
        cnt+=1
    sum-=a[lt]
    lt+=1
print(cnt)
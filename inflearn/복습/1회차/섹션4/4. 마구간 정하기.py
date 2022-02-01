n, c=map(int, input().split())
a=[]
for _ in range(n):
    a.append(int(input()))
a.sort()
lt=a[0]
rt=a[n-1]
res=0
while lt<=rt:
    mid=(lt+rt)//2
    cnt=1
    cur=a[0]
    for i in range(1, n):
        if a[i]-cur>=mid:
            cnt+=1
            cur=a[i]
    if cnt>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)
    




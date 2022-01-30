k, n=map(int, input().split())
a=[]
for _ in range(k):
    a.append(int(input()))

lt=0
rt=max(a)
res=-2147000000
while lt<=rt:
    mid=(lt+rt)//2    
    cnt=0
    for x in a:
        cnt+=x//mid
    if cnt>=n:
        lt=mid+1
        res=mid
    else:
        rt=mid-1
print(res)
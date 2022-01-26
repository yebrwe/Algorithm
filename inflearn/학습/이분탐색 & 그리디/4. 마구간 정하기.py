def Count(dist):
    cur=0
    cnt=1
    for i in range(1, n):
        if abs(a[cur] - a[i]) >= dist:
            cnt+=1
            cur=i
    return cnt
n, c=map(int, input().split())
a=[]
for _ in range(n):
    tmp = int(input())
    a.append(tmp)
a.sort()
lt=1
rt=a[-1]
res=0
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid) < c:
        rt=mid-1
    else:
        lt=mid+1
        res=mid
print(res)
        


n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int, input().split()))
res=[]
p1=p2=0
while p1<n and p2<m:
    if a[p1] < b[p2]:
        res.append(a[p1])
        p1+=1
    else:
        res.append(b[p2])
        p2+=1
if p1<n:
    res+=a[p1:]
if p2<m:
    res+=b[p2:]
for x in res:
    print(x, end=' ')

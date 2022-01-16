n=int(input())
res=-2147000000
for _ in range(n):
    a, b, c=map(int, input().split())
    if a==b and b==c:
        sum=10000+a*1000
    elif a==b or a==c:
        sum=1000+a*100
    elif b==c:
        sum=1000+b*100
    else:
        sum=100*max(a,b,c)
    if sum>res:
        res=sum
print(res)
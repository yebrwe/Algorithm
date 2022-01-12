def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10
        x=x//10
    return sum

n=int(input())
a=list(map(int, input().split()))
max=-2147000000
res=0
for x in a:
    tmp=digit_sum(x)
    if tmp>max:
        max=tmp
        res=x
print(res)


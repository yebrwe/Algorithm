n=int(input())
a=list(map(int, input().split()))
res=0
cnt=0
for x in a:
    if x==1:
        cnt+=1
    else:
        cnt=0
    res+=cnt
print(res)

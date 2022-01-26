n=int(input())
a=list(map(int, input().split()))
last=0
res=""
lt=0
rt=n-1
tmp=[]
while lt<=rt:
    if last < a[lt]:
        tmp.append((a[lt], 'L'))
    if last < a[rt]:
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp) == 0:
        break
    last = tmp[0][0]
    res += tmp[0][1]
    if tmp[0][1]=='L':
        lt+=1
    else:
        rt-=1
    tmp.clear()
print(len(res))
print(res)
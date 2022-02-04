n, m=map(int, input().split())
a=list(map(int, input().split()))
a.sort()
cnt=0
while a:
    if a[0]+a[-1]<=m and len(a)>=2:
        a.pop()
        a.pop(0)
    else:
        a.pop()
    cnt+=1
print(cnt)
        
    
    
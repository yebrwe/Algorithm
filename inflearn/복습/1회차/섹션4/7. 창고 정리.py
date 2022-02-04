L=int(input())
a=list(map(int, input().split()))
m=int(input())
for _ in range(m):
    a.sort()
    a[0]+=1
    a[-1]-=1
a.sort()
print(a[-1]-a[0])
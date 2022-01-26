n=int(input())
a=[]
for _ in range(n):
    h, w=map(int, input().split())
    a.append((h, w))
a.sort(reverse=True)
cnt=0
largest=0
for x, y in a:
    if y > largest:
        largest=y
        cnt+=1
print(cnt)
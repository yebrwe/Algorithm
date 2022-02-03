n=int(input())
a=[]
for _ in range(n):
    h, w=map(int, input().split())
    a.append((h, w))
a.sort(reverse=True)
max=0
cnt=0
for h, w in a:
    if w>max:
        max=w
        cnt+=1
print(cnt)


    




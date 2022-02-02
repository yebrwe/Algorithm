n=int(input())
a=[]
for _ in range(n):
    s, e=map(int, input().split())
    a.append((s, e))
a.sort(key=lambda x: x[1])
end=0
cnt=0
for s, e in a:
    if s>=end:
        end=e
        cnt+=1
print(cnt)

    




s=input()
res=0
for c in s:
    if c.isnumeric():
        res=res*10+int(c)
print(res)
cnt=0
for i in range(1, res+1):
    if res%i==0:
        cnt+=1
print(cnt)

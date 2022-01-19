s=input()
res=''
for x in s:
    if x.isdecimal():
        res+=x        
res=int(res)
cnt=0

for i in range(1, res+1):
    if res % i == 0:
        cnt+=1
print(res)
print(cnt)

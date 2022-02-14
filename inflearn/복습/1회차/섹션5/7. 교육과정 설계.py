s=input()
n=int(input())
for i in range(1, n+1):
  a=input()
  ch=[]
  pos=0
  for x in a:
    if x in s and x not in ch:
      if s[pos]==x:
        pos+=1
        ch.append(x)
      else:
        print('#%d NO' %(i))
        break
  else:
    if len(s)==pos:
      print('#%d YES' %(i))
    else:
      print('#%d NO' %(i))

      




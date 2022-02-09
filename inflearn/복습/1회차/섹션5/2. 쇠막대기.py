s=input()
stack=[]
prev=''
res=0
for x in s:
    if x=='(':
        stack.append(x)
    elif x==')' and prev=='(':
        stack.pop()
        res+=len(stack)
    else:
        stack.pop()
        res+=1
    prev=x
print(res)

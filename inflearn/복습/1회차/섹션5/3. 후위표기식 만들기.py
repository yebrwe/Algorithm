s=input()
stack=[]
res=''
for x in s:
    if x.isdecimal():
        res+=x
    else:
        if x==')':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.pop()
        elif x=='*' or x=='/':
            while stack and stack[-1] and (stack[-1]=='*' or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(x)
        elif x=='+' or x=='-':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.append(x)
        else:
            stack.append(x)
while stack:
    res+=stack.pop()
print(res)

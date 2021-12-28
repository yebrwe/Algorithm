a=input()
stack=[]
for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        b, a=stack.pop(), stack.pop()
        if x == '*':
            stack.append(a*b)
        elif x == '/':
            stack.append(a//b)
        elif x == '+':
            stack.append(a+b)
        elif x == '-':
            stack.append(a-b)
print(stack[-1])
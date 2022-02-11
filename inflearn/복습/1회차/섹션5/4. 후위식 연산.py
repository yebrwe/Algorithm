s=input()
stack=[]
for x in s:
  if x.isdecimal():
    stack.append(int(x))
  else:
    b = stack.pop()
    a = stack.pop()
    if x == '+':
      stack.append(a+b)
    elif x == '-':
      stack.append(a-b)
    elif x == '*':
      stack.append(a*b)
    elif x == '/':
      stack.append(a/b)
print(stack[0])

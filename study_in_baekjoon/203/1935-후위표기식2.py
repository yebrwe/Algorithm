n=int(input())
opt=input()
params = {}
for i in range(n):
    params[chr(ord('A') + i)] = int(input())
stack=[]
for o in opt:
    if o in params:
        stack.append(params[o])
    else:
        y, x = stack.pop(), stack.pop()
        if o == '*':
            stack.append(x*y)
        elif o == '+':
            stack.append(x+y)
        elif o == '/':
            stack.append(x/y)
        elif o == '-':
            stack.append(x-y)
print(f'{stack.pop():.2f}')
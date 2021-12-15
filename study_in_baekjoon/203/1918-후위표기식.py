s=input()
opt = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1,
    '(': 2,
    ')': 2,
}
result = ''
stack=[]
for o in s:
    if o in opt:
        if not stack:
            stack.append(o)
        else:            
            if o == ')':
                while stack:
                    if stack[-1] == '(':
                        stack.pop()
                        break
                    result += stack.pop()
            elif opt[stack[-1]] < opt[o] or opt[stack[-1]] > opt[o]:
                stack.append(o)
            else:
                while stack:
                    result += stack.pop()
                stack.append(o)
    else:
        result += o
while stack:
    result += stack.pop()
print(result)

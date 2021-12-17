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
        if o == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        else:
            while stack and opt[stack[-1]] >= opt[o] and stack[-1] != '(':
                result += stack.pop()
            stack.append(o)
    else:
        result += o
while stack:
    result += stack.pop()
print(result)
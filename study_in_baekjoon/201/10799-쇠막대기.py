l = input()
sum = 0
stack = []
prev = ''
for c in l:
    if c == '(':
        stack.append(c)
    elif prev == '(' and c == ')':
        stack.pop()
        sum += len(stack)
    else:
        stack.pop()
        sum += 1
    prev = c
print(sum)
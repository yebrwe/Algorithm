s = input()
stack = []
prev = ''
sum = 0
for letter in s:
    if letter == '(':
        stack.append(letter)
    elif prev == '(' and letter == ')':
        stack.pop()
        sum += len(stack)
    elif letter == ')':
        stack.pop()
        sum += 1
    prev = letter
print(sum)


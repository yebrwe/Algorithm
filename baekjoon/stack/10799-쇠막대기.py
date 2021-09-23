# s = input()
s = '()(((()())(())()))(())'
stack = []
total_count = 0
count = 0
for letter in s:
    if letter == '(':
        stack.append(letter)
    elif len(stack) == 1 and stack[-1] == '(' and letter == ')' and count > 0: #Bar
        stack.pop()
    else: #Laser
        stack.pop()
        count += 1


print(count)
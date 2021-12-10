import sys
from collections import deque

str = input()
n = int(input())
left = deque(str)
right = deque([])

for _ in range(n):
    commands = sys.stdin.readline().split()
    if len(commands) == 2:
        left.append(commands[1])
    else:
        if commands[0] == 'L' and left:
            right.appendleft(left.pop())
        elif commands[0] == 'D' and right:
            left.append(right.popleft())
        elif commands[0] == 'B' and left:
            left.pop()
result = ''
for c in left:
    result += c
for c in right:
    result += c
print(result)
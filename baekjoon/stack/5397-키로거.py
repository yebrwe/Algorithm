from collections import deque

n = int(input())
for _ in range(n):
  left = deque([])
  right = deque([])
  log = input()
  for c in log:
    if c == '<':
      if len(left) > 0:
        v = left.pop()
        right.appendleft(v)
    elif c == '>':
      if len(right) > 0:
        v = right.popleft()
        left.append(v)
    elif c == '-':
      if len(left) > 0:
        left.pop()
    else:
      left.append(c)
  
  result = ''
  for v in [v for v in left] + [v for v in right]:
    result += v
  print(result)
  
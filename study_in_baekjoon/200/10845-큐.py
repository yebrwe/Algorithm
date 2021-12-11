from sys import stdin
n=int(stdin.readline())
q = []
result = ''
for _ in range(n):  
  cmd = stdin.readline().split()
  if len(cmd) == 2:
    q.insert(0, cmd[1])
  else:
    if cmd[0] == 'front':
      if q: result += f'{q[-1]}\n'
      else: result += f'-1\n'
    elif cmd[0] == 'back':
      if q: result += f'{q[0]}\n'
      else: result += f'-1\n'
    elif cmd[0] == 'size':
      result += f'{len(q)}\n'      
    elif cmd[0] == 'pop':
      if q: result += f'{q.pop()}\n'
      else: result += f'-1\n'
    elif cmd[0] == 'empty':
      result += f'{0 if q else 1}\n'  
print(result[:-1])
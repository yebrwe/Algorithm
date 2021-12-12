from sys import stdin
from collections import deque

n=int(stdin.readline())
d=deque([])
result = ''
for _ in range(n):  
    cmd = stdin.readline().split()
    if len(cmd) == 2:
        if cmd[0] == 'push_front':
            d.appendleft(cmd[1])
        elif cmd[0] == 'push_back':
            d.append(cmd[1])
    else:
        if cmd[0] == 'pop_front':
            if d: result += f'{d.popleft()}\n'
            else: result += '-1\n'
        elif cmd[0] == 'pop_back':
            if d:result += f'{d.pop()}\n'
            else: result += '-1\n'                
        elif cmd[0] == 'size':
            result += f'{len(d)}\n'            
        elif cmd[0] == 'empty':
            if d: result += '0\n'                
            else: result += '1\n'                
        elif cmd[0] == 'front':
            if d: result += f'{d[0]}\n'                
            else: result += '-1\n'
        elif cmd[0] == 'back':
            if d: result += f'{d[-1]}\n'                
            else: result += '-1\n'
print(result[:-1])

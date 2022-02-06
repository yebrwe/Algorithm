import sys
from collections import deque
n=int(input())
a=list(map(int, input().split()))
a=deque(a)
numbers=[]
res=''
if a[0] < a[-1]:
    numbers.append(a.popleft())
    res+='L'
else:
    numbers.append(a.pop())
    res+='R'

while True:
    cur=numbers[-1]
    if len(a)==1:
        if cur < a[0]:
            numbers.append(a.popleft())
            res+='L'
        break
    if cur < a[0] and cur < a[-1]:
        if a[0] < a[-1]:
            numbers.append(a.popleft())
            res+='L'
        else:
            numbers.append(a.pop())
            res+='R'
    elif cur < a[0]:
        numbers.append(a.popleft())
        res+='L'
    elif cur < a[-1]:
        numbers.append(a.pop())
        res+='R'
    else:
        break
print(len(res))
print(res)


    

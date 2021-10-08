from collections import deque

def valid(p):
    left = deque([])
    for c in p:
        if c == '(':
            left.appendleft(c)
        elif c == ')':
            if left:
                left.pop()
            else:
                return False
    return True

def convert(p):
    if not p: return ''

    left = deque([])
    right = deque([])
    u = v = ''

    for i, c in enumerate(p):
        if c == '(':
            left.appendleft(c)
        else:
            right.appendleft(c)            

        if len(left) == len(right):
            u = p[0:i+1]
            v = p[i+1:]
            break
    if valid(u):
        return u + convert(v)
    else:
        str = '(' + convert(v) + ')'
        for c in u[1:len(u)-1]:
            str += ')' if c=='(' else '('
        return str



def solution(p):
    if valid(p): return p
    return convert(p)



print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
#balanced parenthesis check
# ({[]})
# ((())

def balance_check(s:str)->bool:
  opening = set('({[')
  matches = set([('(', ')'),('{', '}'),('[', ']')])
  stack = []
  if len(s) % 2 != 0:
    return False

  for paren in s:
    if paren in opening:
      stack.append(paren)
    else:
      if len(stack) == 0:
        return False
      else:
        last_open = stack.pop()
        if (last_open, paren) not in matches:
          return False
  return len(stack) == 0

    

print(balance_check('(())[]'))  #True
print(balance_check('({[]})'))  #True
print(balance_check('({[]'))   #False
print(balance_check('({[]}'))   #False






    


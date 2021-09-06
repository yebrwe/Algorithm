#balanced parenthesis check
# ({[]})
# ((())
class Stack():
  def __init__(self):
    self.top = -1
    self.items = [0 for _ in range(50)]
  def isEmpty(self):
    return self.top == -1
  def push(self, item):
    self.top+=1
    self.items[self.top] = item
  def pop(self):
    item = self.items[self.top]
    self.top-=1
    return item
  def size(self):
    return self.top + 1

def check(str:str)->bool:
  pair = {
    '(' : ')',
    '{' : '}',
    '[' : ']'
  }
  stack = Stack()
  for p in str:
    if p in pair:
      stack.push(p)
    else:
      open = stack.pop()      
      if p != pair[open]:
        return False
  if stack.size() > 0:
    return False
  return True

print(check('(())[]'))  #True
print(check('({[]})'))  #True
print(check('({[]'))   #False
print(check('({[]}'))   #False






    


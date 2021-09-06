#implementationOfStack

class Stack():
  def __init__(self):
    self.items=[]  
  def isEmpty(self):
    return self.items == []
  def push(self, object):
    self.items.append(object)
  def pop(self):
    return self.items.pop()
  def peek(self):
    return self.items[len(self.items) - 1]
  def size(self):
    return len(self.items)

stack = Stack()

print(stack.isEmpty())
stack.push(1)
stack.push('two')
print(stack.peek())
print(stack.size())
stack.push(True)
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.isEmpty())
#implementationOfStackAnother

class Stack():
  def __init__(self):
    self.maximum_size = 3
    self.top=-1
    self.items=[0 for _ in range(self.maximum_size)]  
  def isEmpty(self):
    return self.top == -1
  def push(self, object):
    if self.top == self.maximum_size - 1:
      raise "스택이 꽉 찼습니다!"
    self.top += 1
    self.items[self.top] = object
  def pop(self):
    if self.top == -1:
      raise "스택이 비어있습니다!"
    item = self.items[self.top]
    self.top -= 1
    return item
  def peek(self):
    return self.items[self.top]
  def size(self):
    return self.top + 1

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
print(stack.pop())
print(stack.isEmpty())
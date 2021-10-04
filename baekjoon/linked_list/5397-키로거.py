import sys
class Node:
  def __init__(self, value):
    self.prev = None
    self.next = None
    self.value = value

n = int(input())
logs = [sys.stdin.readline().rstrip() for _ in range(n)]
for log in logs:
  head = Node(-1)
  tail = Node(-1)
  head.next = tail
  tail.prev = head
  current = head

  for c in log:
    if c == '<':
      if current.prev: 
        current = current.prev
    elif c == '>':
      if current.next: 
        current = current.next
    elif c == '-':
      if current == head or current == tail: continue
      prevNode = current.prev
      nextNode = current.next
      prevNode.next = nextNode
      nextNode.prev = prevNode

      if nextNode == tail: current = prevNode
      elif prevNode == head: current = nextNode
      else: current = nextNode
    else:
      newNode = Node(c)
      if current == head:
        nextNode = head.next
        head.next = newNode
        nextNode.prev = newNode
        newNode.next = nextNode
        newNode.prev = head
      elif current == tail:
        prevNode = tail.prev
        tail.prev = newNode
        prevNode.next = newNode
        newNode.prev = prevNode
        newNode.next = tail
      else:
        nextNode = current.next
        current.next = newNode
        newNode.prev = current
        newNode.next = nextNode
        nextNode.prev = newNode
      current = newNode
  
  password = ''
  node = head.next
  while node.next:
      password += node.value
      node = node.next
  print(password)
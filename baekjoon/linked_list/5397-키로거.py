class Node:
  def __init__(self, value) -> None:
      self.next = None
      self.prev = None
      self.value = value
      

n = int(input())
for _ in range(n):
  head = Node(-1)
  tail = Node(-1)
  head.next = tail
  tail.prev = head
  current = head

  for c in input():
    if c == '<':
      if current.prev: current = current.prev
    elif c == '>':
      if current.next: current = current.next
    elif c == '-':
      prevNode = current.prev
      nextNode = current.next
      if prevNode: prevNode.next = nextNode
      if nextNode: nextNode.prev = prevNode
    else:
      newNode = Node(c)      
      nextNode = current.next
      
      current.next = newNode
      newNode.prev= current

      newNode.next = nextNode
      if nextNode: nextNode.prev = newNode
      else: current.prev.next = newNode
      current = newNode
  
  
  result = ''
  while node != tail:
    result += node.value
    node = node.next
  result += node.value
  print(result)
      

class Node:
  def __init__(self, value) -> None:
      self.next = None
      self.prev = None
      self.value = value
class LinkedList:
    def __init__(self, arr):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.deleted = [0] * 1000000
        self.deleted_top = -1
        self.current = self.head

        if not arr: return
        for o in arr:
            self.add(o)
        self.current = self.head
    def add(self, value) :
        newNode = Node(value)
        currentPrevNode = self.current
        currentNextNode = self.current.next
        newNode.prev = currentPrevNode
        newNode.next = currentPrevNode.next
        currentPrevNode.next = newNode
        currentNextNode.prev = newNode
        self.current = newNode
    def remove(self) :
        if self.current == self.head or self.current == self.tail: return
        prevNode = self.current.prev
        nextNode = self.current.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        self.deleted_top += 1
        self.deleted[self.deleted_top] = self.current
        if nextNode == self.tail:
            self.current = prevNode
        else:
            self.current = nextNode

    def restore(self) :
        if self.deleted_top == -1: return
        node = self.deleted[self.deleted_top]
        self.deleted_top -= 1
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode.prev = node

    def next(self) :
        if self.current == self.tail: return
        self.current = self.current.next
        return self

    def prev(self) :
        if self.current == self.head: return
        self.current = self.current.prev
        return self

n = int(input())
for _ in range(n):
  password = input()
  list = LinkedList([])
  for c in password:
    if c == '<':
      list.prev()
    elif c == '>':
      list.next()
    elif c == '-':
      list.remove()
    else:
      list.add(c)
  
  node = list.head
  while list.next:
    print(list.value)
  
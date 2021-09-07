#implementation of singly linked list
class Node():
    def __init__(self, value):
        self.value = value
        self.nextNode:Node = None

a = Node(1)
b = Node(2)
c = Node(3)
a.nextNode = b
b.nextNode = c
print(a.value)
print(a.nextNode.value)
print(a.nextNode.nextNode.value)
        
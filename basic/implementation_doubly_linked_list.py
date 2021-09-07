#implementation doubly linked list
class DoublyLinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next:DoublyLinkedListNode = None
        self.prev:DoublyLinkedListNode = None

def searchAllNode(node:DoublyLinkedListNode):
    currentNode = node
    while True:
        print(currentNode.value)
        currentNode = currentNode.next

        if not currentNode:
            break

a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)
a.next = b
b.prev = a
b.next = c
c.prev = b
searchAllNode(a)
print('delete b Node')
a.next = c
c.prev = a
searchAllNode(a)
    


class Node():
    def __init__(self):
        self.next = None
    
def cycle_check(node:Node):
    check = {}
    currentNode = node
    while currentNode.next:
        currentNode = currentNode.next
        if currentNode in check:
            return True
        else:
            check[currentNode] = True
    return False
a = Node()
b = Node()
c = Node()
d = Node()

a.next = b
b.next = c
c.next = d

print(cycle_check(a))

d.next = a
print(cycle_check(a))
#linked list nth to last node

class Node():
    def __init__(self, value) -> None:
        self.next:Node = None
        self.value = value



def nth_to_last_node(head:Node, n:int):
    left_pointer = head
    right_pointer = head
    for _ in range(n-1):
        if not right_pointer:
            raise LookupError('Error: n is larger than linked list')
        right_pointer = right_pointer.next
    
    while right_pointer.next:
        left_pointer = left_pointer.next
        right_pointer = right_pointer.next
    return left_pointer
a=Node(0)
b=Node(1)
c=Node(2)
d=Node(3)
e=Node(4)
f=Node(5)
g=Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

print(nth_to_last_node(a, 2).value)


    
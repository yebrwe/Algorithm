#linked list reversal
class Node():
    def __init__(self, value) -> None:
        self.next:Node = None
        self.value = value

def see_all_nodes(head:Node):
    
    current_node = head
    while current_node:
        print(current_node.value)
        current_node = current_node.next
    
def reversal_linked_list(head:Node):
    
    prev_node = None
    next_node = None
    current_node = head
    while current_node:
        next_node = current_node.next       
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    
    return prev_node

a = Node(1)
b = Node(2)
c = Node(3)

a.next =b
b.next =c

see_all_nodes(a)

new_head = reversal_linked_list(a)

see_all_nodes(new_head)


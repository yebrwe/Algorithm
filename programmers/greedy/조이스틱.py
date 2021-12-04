class Node():
    def __init__(self, value):
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.value = value
def ud_find(node, target):
    up_count = up_find(node, target, 0)
    down_count = down_find(node, target, 0)
    min_count = 0 
    if up_count < down_count:
        min_count = up_count
    else:
        min_count = down_count
    return min_count
def up_find(node, target, count):
    if node.value == target:
        return [count, node]
    return  up_find(node.up, target, count + 1)

def down_find(node, target, count):    
    if node.value == target:
        return [count, node]
    return down_find(node.down, target, count + 1)

def lr_find(node, target):
    left_count, left_node = left_find(node, target, 0)
    right_count, right_node = right_find(node, target, 0)
    min_count = 0 
    if left_count < right_count:
        node = left_node
        min_count = left_count
    else:
        node = right_node
        min_count = right_count
    return [min_count, node]
def left_find(node, target, count):
    if node.value == target:
        return [count, node]
    return  left_find(node.left, target, count + 1)

def right_find(node, target, count):    
    if node.value == target:
        return [count, node]
    return right_find(node.right, target, count + 1)

def solution(name):
    answer = 0    
    n = len(name)
    
    ud_root = Node('A')
    start_node = ud_root
    for i in range(1, 26):
        new_node = Node(chr(ord('A') + i))
        start_node.down = new_node
        new_node.up = start_node
        start_node = new_node
    start_node.down = ud_root
    ud_root.up = start_node

    lr_root = Node(0)
    start_node = lr_root
    for i in range(1,n):
        new_node = Node(i)
        start_node.right = new_node
        new_node.left = start_node
        start_node = new_node
    start_node.right = lr_root
    lr_root.left = start_node


    def find_index(name, node, visited):
        left_node = node
        right_node = node
        left = 0
        right = 0
        while True:
            if name[left_node.value] != 'A' and left_node.value not in visited:
                break
            left += 1
            left_node = left_node.left
        while True:
            if name[right_node.value] != 'A' and right_node.value not in visited:
                break
            right += 1
            right_node = right_node.right
        return left_node.value if left < right else right_node.value
        
    cur = 0
    visited = []
    while len(visited) != n - name.count('A'):
        #min distance find index
        cur = find_index(name, lr_root, visited)
        if cur not in visited and name[cur] != 'A':
            visited.append(cur)
        #min distance target index
        lr_count, lr_node = lr_find(lr_root, cur)
        answer += lr_count
        lr_root = lr_node
        #min distacne alphabet
        ud_count = ud_find(ud_root, name[cur])
        answer += ud_count
    return answer
print(solution("JEROEN")==   56)
print(solution("JAN")==   23)
print(solution("JAZ")==11)
print(solution("ZAAAZZZZZZZ")==15)


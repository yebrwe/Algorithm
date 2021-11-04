# 값이 0인 노드가 최상위노드 일때 
# 최상위까지 올라가면서 올라가는 구간을 모두 최상위 노드로 바꾼다
def find(tree, x):
    if tree[x] == 0: return x
    tree[x] = find(tree, tree[x])
    return tree[x]
tree = {
    1:2,
    2:3,
    3:4,
    4:5,
    5:6,
    6:0
}

print(find(tree, 1), tree)
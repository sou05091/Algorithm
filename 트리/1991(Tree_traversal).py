class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# 전위 순회
def preorder(node):
    if node:
        print(node.data, end="")
        preorder(node.left)
        preorder(node.right)
# 중위 순회
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end="")
        inorder(node.right)
# 후위 순회
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end="")
# 이진 트리 생성 함수
def create_binary_tree(nodes):
    tree = {}
    for node_data, left_child, right_chind in nodes:
        if node_data not in tree:
            tree[node_data] = Node(node_data)
        if left_child != '.':
            tree[left_child] = Node(left_child)
            tree[node_data].left = tree[left_child]
        if right_chind != '.':
            tree[right_chind] = Node(right_chind)
            tree[node_data].right = tree[right_chind]
    return tree['A']

n = int(input())
nodes = []
for _ in range(n):
    node_data, left_child, right_child = input().split()
    nodes.append((node_data, left_child, right_child))
# 이진 트리 생성
root = create_binary_tree(nodes)

#전위 순회
preorder(root)
print()

#중위 순회
inorder(root)
print()

#후위 순회
postorder(root)
print()


        
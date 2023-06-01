import sys

def find_parent(nodes, start):
    parent = [0] * (len(nodes) + 1)
    stack = [start]
    
    while stack:
        node = stack.pop()
        
        for child in nodes[node]:
            if parent[child] == 0:
                parent[child] = node
                stack.append(child)
    
    return parent

# 입력 받기
n = int(sys.stdin.readline())
nodes = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)

# 부모 찾기
parents = find_parent(nodes, 1)

# 출력
for i in range(2, n + 1):
    print(parents[i])

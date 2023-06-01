import sys

# 각 노드의 부모를 찾는 함수
def find_parent(nodes, start):
    # 각 노드의 부모를 저장하는 리스트
    parent = [0] * (len(nodes) + 1)
    # DFS를 위한 스택
    stack = [start]
    
    while stack:
        # 스택에서 노드 하나를 꺼냄
        node = stack.pop()
        
        # 해당 노드의 자식들을 탐색
        for child in nodes[node]:
            # 아직 부모가 설정되지 않은 자식이라면
            if parent[child] == 0:
                # 부모를 현재 노드로 설정하고
                parent[child] = node
                # 스택에 추가하여 자식의 자식을 탐색하도록 함
                stack.append(child)
    
    # 부모 리스트 반환
    return parent

# 입력 받기
n = int(sys.stdin.readline())  # 노드의 개수
nodes = [[] for _ in range(n + 1)]  # 노드 연결 관계를 저장하는 리스트

# 트리의 간선 정보 입력받기
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    # 두 노드를 연결
    nodes[a].append(b)
    nodes[b].append(a)

# 부모 찾기
parents = find_parent(nodes, 1)  # 루트 노드는 1로 설정

# 출력
for i in range(2, n + 1):
    print(parents[i])

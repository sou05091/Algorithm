from collections import defaultdict
def count(graphy, start):
    # 중복을 허용하지 않는 집합
    visited = set()
    stack = [start]
    count = 0
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            count += 1
            # 현재 노드와 연결된 이웃 노드들의 리스트 값을 모두 추가
            # graph[node] = 현재 노드의 연결된 이웃 노드들의 리스트
            stack.extend(graph[node])
    return count


#간선정보 입력하기
graph = defaultdict(list)
m = int(input())
n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
result = count(graph, 1) - 1
print(result)
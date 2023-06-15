from collections import deque

def bfs(campus, start):
    n, m = len(campus), len(campus[0])
    visited = [[False] * m for _ in range(n)]
    dx = [-1, 1, 0, 0]  # 상하좌우 이동을 위한 dx, dy
    dy = [0, 0, -1, 1]
    queue = deque([start])
    count = 0  # 만난 사람 수를 저장하는 변수

    while queue:
        x, y = queue.popleft()

        # 도연이가 사람을 만난 경우
        if campus[x][y] == 'P':
            count += 1

        # 상하좌우로 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 이동 가능한 위치인지 확인
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and campus[nx][ny] != 'X':
                visited[nx][ny] = True
                queue.append((nx, ny))

    return count

# 입력 받기
n, m = map(int, input().split())
campus = [list(input()) for _ in range(n)]

# 도연이의 위치 찾기
for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            start = (i, j)
            break

result = bfs(campus, start)

if result == 0:
    print("TT")
else:
    print(result)

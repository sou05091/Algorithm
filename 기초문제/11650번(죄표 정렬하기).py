n = int(input())  # 좌표 개수 입력 받기

rs = []
for i in range(n):
    x, y = map(int, input().split())
    rs.append((x, y))

result = sorted(rs)

for r in range(n):
    print(result[r][0], result[r][1])

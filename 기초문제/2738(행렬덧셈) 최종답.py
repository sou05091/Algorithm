N, M = map(int, input().split())

# 행렬 A 입력 받기
matrix_A = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix_A.append(row)

# 행렬 B 입력 받기
matrix_B = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix_B.append(row)

# 두 행렬을 더하여 결과 행렬 생성
result = []
for i in range(N):
    row = []
    for j in range(M):
        sum_value = matrix_A[i][j] + matrix_B[i][j]
        row.append(sum_value)
    result.append(row)

# 결과 행렬 출력
for row in result:
    print(' '.join(map(str, row)))

n = int(input())
scores = []
for _ in range(n):
    scores.append(int(input()))

# 길이가 n인 리스트 dp를 생성하고, 모든 요소를 0으로 초기화하는 구문
dp = [0] * n
dp[0] = scores[0]
if n > 1:
    dp[1] = scores[0] + scores[1]
if n > 2:
    dp[2] = max(scores[0] + scores[2], scores[1] + scores[2])

for i in range(3, n):
    dp[i] = max(dp[i-2] + scores[i], dp[i-3] + scores[i-1] + scores[i])

print(dp[n-1])

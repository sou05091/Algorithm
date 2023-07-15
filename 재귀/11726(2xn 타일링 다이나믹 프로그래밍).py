def cal(m):
    if m == 1:
        return 1
    if m == 2:
        return 2
    #인덱스 1부터 m까지의 값을 저장하기 위해 리스트 생성
    dp = [0] * (m + 1)
    # dp[1], dp[2]초기조건
    dp[1] = 1
    dp[2] = 2
    # 3부터 m+1까지 반복
    for i in range(3, m + 1):
        #재귀와 같음
        dp[i] = dp[i-1] + dp[i-2]
    return dp[m] % 10007

m = int(input())
result = cal(m)
print(result)

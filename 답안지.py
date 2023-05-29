def factorial(n):
    if n == 0:  # 종료 조건: n이 0이면 1을 반환
        return 1
    else:       # 재귀 호출: n과 factorial(n-1)의 곱을 반환
        return n * factorial(n-1)

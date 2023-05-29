def factorial(n):
    res = 1
    for i in range(n, 1, -1):
        res *= i
    return res
def findzero(res):
    count = 0
    while res % 10 == 0:
        res = res // 10
        count += 1
    return count

n = int(input())
if 0 <= n <= 500:
    result = factorial(n)
    result2 = findzero(result)
    print(result)
    print(result2)
else:
    print("0 ~ 500 사이의 숫자를 입력해주세요")

#백준 제출 코드
# import sys

# def factorial(n):
#     res = 1
#     for i in range(1, n+1):
#         res *= i
#     return res

# def findzero(res):
#     count = 0
#     while res % 10 == 0:
#         res //= 10
#         count += 1
#     return count

# n = int(sys.stdin.readline().rstrip())

# if 0 <= n <= 500:
#     result = factorial(n)
#     result2 = findzero(result)
#     print(result2)
# else:
#     print("0 ~ 500 사이의 숫자를 입력해주세요")

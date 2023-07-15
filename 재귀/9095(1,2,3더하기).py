def cal(m):
    if m == 1:
        return 1
    if m == 2:
        return 2
    if m == 3:
        return 4
    return cal(m-1) + cal(m-2) + cal(m-3)

n = int(input())

for _ in range(n):
    m = int(input())
    result = cal(m)
    print(result)

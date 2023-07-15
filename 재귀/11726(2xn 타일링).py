def cal(m):
    if m == 1:
        return 1
    if m == 2:
        return 2
    return cal(m-1) + cal(m-2)

m = int(input())
result = cal(m)%10007
print(result)

def find(n):
    rs = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            if (i+j)%2 == 1:
                rs.append((i, j))
            else:
                rs.append((j, i))
    sorted_rs = sorted(rs, key=lambda x: x[0]+x[1])
    result = sorted_rs[n-1]
    return f"{result[0]}/{result[1]}"

n = int(input())
res = find(n)
print(res)
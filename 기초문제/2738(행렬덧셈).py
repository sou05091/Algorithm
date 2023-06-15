n,m = map(int, input().split())
arr = []
arr1 = []
for i in range(n):
    row = list(map(int, input().split()))
    row1 = list(map(int, input().split()))
    if len(row) != m:
        print("wrong num")
        break
    else:
        arr.append(row)
        arr1.append(row1)
rs = []
for x in range(n):
    row_rs = []
    for y in range(m):
        res = arr[x][y] + arr1[x][y]
        row_rs.append(res)
    rs.append(row_rs)
for row in rs:
    print(' '.join(map(str, row)))
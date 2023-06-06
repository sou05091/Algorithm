# 중복된 값 제거
def remove(arr, arr1):
    rem = set()
    for value in arr:
        rem.add(value)
    for value in arr1:
        rem.discard(value)
    return list(rem)
arr = []
arr1 = []
n = 1
x = 1
while n <= 10000:
    n_str = str(n)
    res = list(n_str)
    total = n + sum(int(digit) for digit in res)
    n += 1 
    arr.append(total)
while x <= 10000:
    arr1.append(x)
    x += 1
result = sorted(remove(arr1, arr))
for c in result:
    print(c)
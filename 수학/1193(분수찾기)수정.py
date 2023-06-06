def find(n):
    dia = 1 # 대각선의 번호 
    count = 0 # 분수의 갯수
    while count < n:
        count += dia
        dia += 1
    dia -= 1
    res = n - (count - dia) # 대각선의 거리
    if dia % 2 == 0:
        chi = res
        par = dia - res + 1
    else:
        chi = dia - res + 1
        par = res
    return f"{chi}/{par}"
    #return dia
n = int(input())
res = find(n)
print(res)

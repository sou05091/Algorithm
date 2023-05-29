def cal(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # cal(2)를 불러오기 위해서 cal(1) + cal(0)을 함 여기서 조건식으로 인해
        # cla(2) = 1+0으로 계산을함 return을 해주어서 cal(2) = 1로 저장후 반복
        # 하지만 여기서 n은 입력받은 값으로 실질적으로 호출해오는 방식은
        # cal(5)부터 시작하여 아래로 내려오는 방식이다.
        return cal(n-1) + cal(n-2) 
def sum_num(n):
    # 종료 조건: n이 1 이하일 때
    if n <= 0:
        return 0
    else:
        return cal(n)
n = int(input())
if 1 <= n <= 20:
    result = sum_num(n)
    print(result)
else:
    print("1~20사이의 숫자만 입력하세요")
    
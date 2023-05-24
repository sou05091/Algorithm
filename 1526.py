def set_numbers(num, max):
    if num > max:
        return []
    numbers =[]
    #재귀함수 리스트 생성

    numbers.append(num)
    #각 숫자들 배열에 저장

    #불러온 숫자에 * 10을 하고 4와 7을 더하여 4,44,47,444,447 순서로 배열 저장
    numbers += set_numbers(num*10+4, max)
    numbers += set_numbers(num*10+7, max)

    return numbers
def find_numbers(N) :
    #0~N까지의 배열 생성
    rs = set_numbers(0,N)
    #생성된 배열을 내림차순으로 정렬 (가장큰값이 리스트의 맨앞으로 옴)
    rs.sort(reverse=True)
    #리스트의 가장 큰 값을 반환
    return rs[0]

N = int(input("N을 입력하세요: "))
if N>=4 and N<=1000000:
    result = find_numbers(N)
    print(f"결과는: {result}")
else :
    print("4~1000000사이의 숫자를 입력해주세요.")



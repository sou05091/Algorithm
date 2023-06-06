def remove_duplicates(array1, array2):
    # 중복된 값을 저장할 set을 생성합니다.
    duplicates = set()

    # 첫 번째 배열의 값들을 set에 추가합니다.
    for value in array1:
        duplicates.add(value)

    # 두 번째 배열에서 중복된 값을 제거합니다.
    for value in array2:
        duplicates.discard(value)

    # 중복된 값이 제거된 배열을 반환합니다.
    return list(duplicates)


# 두 배열을 정의합니다.
array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]

# 중복된 값이 제거된 배열을 얻습니다.
result = remove_duplicates(array1, array2)

# 결과 출력
print(result)

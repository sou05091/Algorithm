def rs(grade):
    if grade == 'A+':
        grade = 4.5
    elif grade == 'A0':
        grade = 4.0
    elif grade == 'B+':
        grade = 3.5
    elif grade == 'B0':
        grade = 3.0
    elif grade == 'C+':
        grade = 2.5
    elif grade == 'C0':
        grade = 2.0
    elif grade == 'D+':
        grade = 1.5
    elif grade == 'D0':
        grade = 1.0
    elif grade == 'F':
        grade = 0
    elif grade == 'P':
        return None
    else:
        print("올바르지 않은 점수입니다.")
        return None
		#수정 필요
    return grade
mul = []  # 결과를 저장할 리스트
plu = []
for n in range(3): 
    inputs = input("입력값: ")
    inputs = inputs.strip('()')  # 입력값 앞뒤의 괄호 제거
    subject, score, grade = inputs.split()
    score = float(score)
    if not (1 <= len(subject) <= 50):
        print("과목명은 1자 이상 50자 이하여야 합니다. ")
        break
    gr = rs(grade)
    if gr is None:
        print("P 학점은 계산에서 제외됩니다.")
        continue
    res = gr * score
    mul.append(res)
    plu.append(score)

sumplu = sum(plu)
summul = sum(mul)
result = summul/sumplu
if(score != 1.0 and score != 2.0 and score != 3.0 and score != 4.0):
    errormessane = print("1.0 ~ 4.0사이의 숫자만 입력하세요")
else:
    print(result)

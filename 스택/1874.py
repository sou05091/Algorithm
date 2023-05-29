def check_sequence(n, sequence):
    stack = []
    result = []
    #num = 차례대로 증가하는 숫자
    num = 1
    #for x in 배열에 저장된 1번째 값을 순서대로 불러온다.
		#Sequence안에 있는 x값 가져옴
    for x in sequence:
        while num <= x:
            #num 과 x의 값이 같거나 커질때까지 push/num증가
            stack.append(num)
            result.append('+')
            num += 1
        #stack[-1]은 스택의 가장 위에 있는 값?
        if stack[-1] == x:
            stack.pop()
            result.append('-')
        else:
            return 'NO'

    return '\n'.join(result)


n = int(input())
sequence = []
for _ in range(n):
    x = int(input())
    sequence.append(x)

answer = check_sequence(n, sequence)
print(answer)
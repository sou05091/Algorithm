class Stack:
    def __init__(K):
        K.items = []
    def pop(K):
        if not K.is_empty():
            return K.items.pop()
        else:
            print("스택이 비어 있습니다.")
    def push(K, item):
        K.items.append(item)
    def is_empty(K):
        return len(K.items) == 0
    #배열 더하기 함수
    def sum(K):
        return sum(K.items)
#배열길이 입력받음
rs = int(input())
stack = Stack()
#입력받은 배열의 값만큼 for문 작동
for _ in range(rs):
    #배열값 입력
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.push(num)
print(stack.sum())

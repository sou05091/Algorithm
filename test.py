class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print("푸시하였습니다.")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("스택이 비어 있습니다.")

    def sum_of_numbers(self):
        return sum(self.items)

print("배열길이를 설정해주세요")
K = int(input())
stack = Stack()

for _ in range(K):
    print("숫자를 입력해주세요")
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.push(num)

print(f"테스트 정답은{stack.sum_of_numbers()}")

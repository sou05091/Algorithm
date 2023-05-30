from collections import deque
def res(n):
    stack = deque()
    rs = n
    while rs >= 1: 
        stack.append(rs)
        rs -= 1
    return stack
def que(stack):
    while len(stack) > 1:
        stack.pop()
        item = stack.pop()
        stack.appendleft(item)
    return stack[0]
n = int(input())
answer = res(n)
test = que(answer)
print(test)
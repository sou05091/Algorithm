import sys

M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    operation = sys.stdin.readline().split()
    if operation[0] == "add":
        S.add(int(operation[1]))
    elif operation[0] == "remove":
        S.discard(int(operation[1]))
    elif operation[0] == "check":
        if int(operation[1]) in S:
            print(1)
        else:
            print(0)
    elif operation[0] == "toggle":
        x = int(operation[1])
        if x in S:
            S.discard(x)
        else:
            S.add(x)
    elif operation[0] == "all":
        S = set(range(1, 21))
    elif operation[0] == "empty":
        S = set()

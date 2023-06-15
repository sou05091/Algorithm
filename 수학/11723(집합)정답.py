import sys
#많은 수를 처리하기 위해 readline함수 사용
M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    oper = sys.stdin.readline().split()
    
    if oper[0] == "add":
        S.add(int(oper[1]))
    elif oper[0] == "remove":
        S.discard(int(oper[1]))
    elif oper[0] == "check":
        if int(oper[1] in S):
            print(1)
        else:
            print(0)
    elif oper[0] == "toggle":
        x = int(oper[1])
        if x in S:
            S.discard(x)
        else:
            S.add(x)
    elif oper[0] == "all":
        S = set(range(1, 21))
    elif oper[0] == "empty":
        S = set()
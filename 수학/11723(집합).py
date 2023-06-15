rs = []
def add(n):
    if n not in rs:
        rs.append(n)
def remove(n):
    rs.remove(n)
def check(n):
    if n in rs:
        print(1)
    else:
        print(0)
def toggle(n):
    if n in rs:
        rs.remove(n)
    else:
        rs.append(n)
def all():
    return [i for i in range(1,21)]

def empty():
    rs.clear()

m = int(input())

for _ in range(m):
    command = input().split()

    if command[0] == "add":
        add(int(command[1]))
    elif command[0] == "remove":
        remove(int(command[1]))
    elif command[0] == "check":
        check(int(command[1]))
    elif command[0] == "toggle":
        toggle(int(command[1]))
    elif command[0] == "all":
        rs = all()
    elif command[0] == "empty":
        empty()
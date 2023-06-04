while True:
    s = input()
    if int(s) == 0:
        break
    reversed_s = s[::-1]
    if s == reversed_s:
        print("yes")
    else:
        print("no")
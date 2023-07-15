def move(n, x, y, path):
    if n > 0:
        move(n - 1, x, 6 - x - y, path)
        path.append((x, y))
        move(n - 1, 6 - x - y, y, path)

n = int(input())
path = []
move(n, 1, 3, path)

print(len(path))
for move in path:
    print(move[0], move[1])

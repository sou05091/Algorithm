def move(n ,x, y, path):
    if n>0:
        # 기둥번호의 합이 6이므로 시작기둥 목표기둥이 어느 기둥이라도
        # 중간기둥은 6-x-y로 구할 수 있다.
        move(n-1, x, 6-x-y,path)
        path.append((n,x,y))
        move(n-1, 6-x-y, y, path)

n = int(input())
path=[]
move(n,1,3,path)
print(len(path))
for move in path:
    print("원반" + move[0] + "기둥(기존)" + move[1] + "기둥(이동)" + move[2])

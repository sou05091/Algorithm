import sys
from collections import Counter
#Counter 중복되는 값이 있으면
#Key값 = 중복된 숫자가 있을경우 그 숫자의 number
# Value값 = 중복한 숫자의 갯수 만큼 저장 
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))
#딕셔너리 형태로 저장
a_count = Counter(a)
m = int(sys.stdin.readline().rstrip())
#찾아야 하는 숫자
targets = list(map(int, sys.stdin.readline().split()))
result = [a_count[i] for i in targets]
print(' '.join(map(str, result)))
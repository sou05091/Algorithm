from itertools import combinations
n, m = map(int, input().split())
r = list(map(int, input().split()))
target_sum = m
# r 배열에 3개의 숫자를 선택하는 모든 조합을 생성함
c_list = list(combinations(r,3))
rs = []
for com in c_list:
    if sum(com) <= target_sum:
        rs.append(sum(com))
sorted_result = sorted(rs)
res = sorted_result[-1]
print(res)
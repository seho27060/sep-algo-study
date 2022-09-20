# 그리드 문제
# 양수 음수를 나눈 후 m개씩 묶어 이동거리를 구하자
# 절대값이 제일 큰 수는 돌아올 필요 없음!

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
minus = []
plus = []
ans = 0
maxV = 0
for i in arr:
    if i < 0:
        minus.append(i)
    else:
        plus.append(i)
    if abs(i) > abs(maxV):
        maxV = i
    
minus.sort()
plus.sort(reverse=True)
ans += maxV

for i in range(0, len(minus), m):
    if abs(minus[i]) != maxV:
        ans += abs(minus[i] * 2)
for i in range(0, len(plus), m):
    if plus[i] != maxV:
        ans += abs(plus[i] * 2)
print(ans)
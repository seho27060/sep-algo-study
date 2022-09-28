# 누적합 문제
# 꿀통이 가장 왼쪽, 가장 오른쪽, 벌 사이에 위치한 경우를 나누고 가장 최대값을 구한다

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
ans = 0
sumV = []
sumV.append(arr[0])

for i in range(1, N):
    sumV.append(sumV[i-1] + arr[i])

for i in range(1, N-1):
    ans = max(ans, sumV[N-2] + sumV[i-1] - arr[i])

for i in range(1, N-1):
    ans = max(ans, sumV[N-1] - sumV[0] - arr[i] + sumV[N-1] - sumV[i])

for i in range(1, N-1):
    ans = max(ans, sumV[N-2] - sumV[0] + arr[i])
print(ans)
# DP문제
# 메모리 제한이 강해 배열을 2개만 선언한 뒤 갱신하는 방향으로 풀이

import sys
input = sys.stdin.readline

N = int(input())
maxDp = [[0] * 3 for _ in range(2)]
minDp = [[0] * 3 for _ in range(2)]

for i in range(N):
    lst = list(map(int, input().split()))

    maxDp[1][0] = max(maxDp[0][0], maxDp[0][1]) + lst[0]
    minDp[1][0] = min(minDp[0][0], minDp[0][1]) + lst[0]
 
    maxDp[1][1] = max(maxDp[0][0], maxDp[0][1], maxDp[0][2]) + lst[1]
    minDp[1][1] = min(minDp[0][0], minDp[0][1], minDp[0][2]) + lst[1]
 
    maxDp[1][2] = max(maxDp[0][1], maxDp[0][2]) + lst[2]
    minDp[1][2] = min(minDp[0][1], minDp[0][2]) + lst[2]
 
    maxDp[0][0], maxDp[0][1], maxDp[0][2] = maxDp[1][0], maxDp[1][1], maxDp[1][2]
    minDp[0][0], minDp[0][1], minDp[0][2] = minDp[1][0], minDp[1][1], minDp[1][2]

print(max(maxDp[1]), min(minDp[1]))
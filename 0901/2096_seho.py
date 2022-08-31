# 220901 2096 내려가기
# n < 십만 dp  ㄱㄱ
# 얻을수있는 최대 점수 최소 점수

import sys

input = sys.stdin.readline

n = int(input())

maxDp = [0,0,0]
minDp = [0,0,0]

for idx in range(n):
    board = list(map(int, input().split()))
    max1 = max(maxDp[0],maxDp[1]) + board[0]
    max2 = max(maxDp) + board[1]
    max3 = max(maxDp[1], maxDp[2]) + board[2]
    min1 = min(minDp[0], minDp[1]) + board[0]
    min2 = min(minDp) + board[1]
    min3 = min(minDp[1], minDp[2]) + board[2]
    maxDp = [max1,max2,max3]
    minDp = [min1,min2,min3]

print(max(maxDp),min(minDp))
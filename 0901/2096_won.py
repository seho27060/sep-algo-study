import sys
# sys.stdin = open("sample_input.txt", "r")
input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations


N = int(input())

maxV = 0
minV = float('inf')
dp1 = [0] * 3
dp2 = [0] * 3
dp3 = [0] * 3
dp4 = [0] * 3

for i in range(N):
    a, b, c = map(int, input().split())
    for k in range(3):
        if k == 0:
            dp3[k] = a + max(dp1[k], dp1[k + 1])
            dp4[k] = a + min(dp2[k], dp2[k + 1])
        if k == 1:
            dp3[k] = b + max(dp1[k - 1], dp1[k], dp1[k + 1])
            dp4[k] = b + min(dp2[k - 1], dp2[k], dp2[k + 1])
        if k == 2:
            dp3[k] = c + max(dp1[k], dp1[k - 1])
            dp4[k] = c + min(dp2[k], dp2[k - 1])
    dp1 = dp3[:]
    dp2 = dp4[:]

print(max(dp1), min(dp2))

import sys
# sys.stdin = open("sample_input.txt", "r")
# input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations
# import itertools

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
pos = []
neg = []
flag = "pos"
maxV = 0
for i in arr:
    if i > 0:
        pos.append(i)
        tmp = abs(i)
        if maxV < tmp:
            maxV = tmp
            flag = "pos"
    else:
        neg.append(i)
        tmp = abs(i)
        if maxV < tmp:
            maxV = tmp
            flag = "neg"
pos.sort(reverse=True)


arr += [0] * 100

if flag == "neg":
    for i in range(0, len(neg), M):
        if i == 0:
            ans += abs(neg[i])
        else:
            ans += abs(neg[i]) * 2
    for i in range(0, len(pos), M):
        ans += pos[i] * 2
else:
    for i in range(0, len(pos), M):
        if i == 0:
            ans += pos[i]
        else:
            ans += pos[i] * 2
    for i in range(0, len(neg), M):
        ans += abs(neg[i]) * 2

print(ans)
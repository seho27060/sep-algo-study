import sys
# sys.stdin = open("sample_input.txt", "r")
# input = sys.stdin.readline
# from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations
# import itertools
from itertools import combinations

N = int(input())
arr = set()
ans = 0
for _ in range(N):
    arr.add(int(input()))

sumArr = set()

for i in arr:
    for k in arr:
        sumArr.add(i + k)

tmp = dict()
for i in arr:
    for k in arr:
        if i - k in sumArr:
            tmp[i] = (i, k, i - k)

ans = list(tmp.keys())
ans.sort(reverse=True)
print(ans[0])
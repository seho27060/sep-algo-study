# 220921 2212 센서
#

import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
lst = sorted(map(int,input().split()))
lst2 = []
if n > k:
    for idx in range(1, n):
        lst2.append(lst[idx] - lst[idx - 1])

    lst2.sort(reverse=True)
    for _ in range(k - 1):
        lst2.pop(0)

    print(sum(lst2))
else:
    print(0)

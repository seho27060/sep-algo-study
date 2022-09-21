import sys
input = sys.stdin.readline
# from collections import deque
# from heapq import heappush, heappop

N = int(input())
K = int(input())
arr = list(map(int, input().split()))
arr.sort()
diff = []

if K >= N:
    print(0)
    exit()

for i in range(N - 1):
    tmp = arr[i + 1] - arr[i]
    diff.append(tmp)

diff.sort()

for i in range(K - 1):
    diff.pop()

print(sum(diff))
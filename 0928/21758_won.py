import sys
input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop

N = int(input())
arr = list(map(int, input().split()))
ans = 0
# 꿀벌벌
for i in range(1, N - 1):
    front = sum(arr[:-1]) - arr[i]
    back = sum(arr[:i])
    res = front + back
    ans = max(ans, res)

# 벌꿀벌
for i in range(1, N - 1):
    front = sum(arr[1:i + 1])
    back = sum(arr[i:-1])
    res = front + back
    ans = max(ans, res)

for i in range(1, N):
    front = sum(arr[1:]) - arr[i]
    back = sum(arr[i + 1:])
    res = front + back
    ans = max(ans, res)

print(ans)
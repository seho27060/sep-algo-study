import sys
input = sys.stdin.readline
# from collections import deque
# from heapq import heappush, heappop

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0

for i in range(N):
    exec = arr[:i] + arr[i + 1:]
    l = 0
    r = len(exec) - 1
    while l < r:
        sumV = exec[l] + exec[r]
        if sumV == arr[i]:
            ans += 1
            break
        if sumV < arr[i]:
            l += 1
        else:
            r -= 1
print(ans)
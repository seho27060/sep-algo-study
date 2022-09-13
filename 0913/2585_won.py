import sys
# sys.stdin = open("sample_input.txt", "r")
# input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations

n, k = map(int, input().split())

air = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]

def f(c, fuel):
    cnt = 0
    qu = deque()
    visited = [0] * (n + 1)
    qu.append(c)
    # visited[c] = 1
    while qu:
        if cnt > k:
            return False

        for _ in range(len(qu)):
            c = qu.popleft()

            if visited[c] == 0:
                visited[c] = 1

                for i in range(1, n + 1):
                    dist = ((air[c][0] - air[i][0]) ** 2 + (air[c][1] - air[i][1]) ** 2) ** (1 / 2)

                    if dist <= fuel:
                        dist2 = ((10000 - air[i][0]) ** 2 + (10000 - air[i][1]) ** 2) ** (1 / 2)

                        if dist2 <= fuel:
                            return True
                        qu.append(i)
        cnt += 1
    return False

l = 0
r = 10000
ans = 0

while l <= r:
    mid = (l + r) // 2

    if f(0, mid * 10):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)
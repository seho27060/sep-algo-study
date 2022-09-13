import math
from collections import deque

n, k = map(int, input().split())
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]

def dist1(x1, y1, x2, y2):
    return math.ceil((((x1-x2)**2 + (y1-y2)**2) ** 0.5) / 10)

def dist2(x1, y1):
    return math.ceil((((10000-x1)**2 + (10000-y1)**2) ** 0.5) / 10)

def bfs(mid):
    visited = [0]*(n+1)
    q = deque()
    q.append((0, 0))
    while q:
        t, cnt = q.popleft()
        if cnt > k:
            continue
        for i in range(1, n+1):
            if visited[i] == 0:
                if dist1(arr[t][0], arr[t][1], arr[i][0], arr[i][1]) <= mid:
                    if dist2(arr[i][0], arr[i][1]) <= mid:
                        return True
                    q.append((i, cnt+1))
                    visited[i] = 1
    return False

l, r = 0, 100000001
ans = 0
while l <= r:
    mid = (l+r)//2
    if bfs(mid):
        ans = mid
        r = mid-1
    else:
        l = mid+1

print(ans)
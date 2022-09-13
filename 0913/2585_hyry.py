import sys
from math import ceil

input = sys.stdin.readline


def calculateDistance(curX, curY, neiX, neiY):
    return ceil(((curX - neiX) ** 2 + (curY - neiY) ** 2) ** 0.5 / 10)


def bfs(oil):
    Q = [(0, 0, 0)]
    visit = [False] * (N + 1)

    while Q:
        cnt, curX, curY = Q.pop(0)
        if curX == curY == 10_000: return True

        for idx in range(N + 1):
            if visit[idx]: continue
            neiX, neiY = stops[idx]
            if cnt + 1 <= K + 1 and calculateDistance(curX, curY, neiX, neiY) <= oil:
                Q.append((cnt + 1, neiX, neiY))
                visit[idx] = True

    return False


def fuel():
    left, right = 0, 1e10
    ans = 1e10
    while left <= right:
        mid = (left + right) // 2
        if bfs(mid):
            ans = min(ans, mid)
            right = mid - 1
        else:
            left = mid + 1
    return int(ans)


N, K = map(int, input().rstrip().split())
stops = [(10_000, 10_000)]
for _ in range(N):
    x, y = map(int, input().rstrip().split())
    stops.append((x, y))

print(fuel())

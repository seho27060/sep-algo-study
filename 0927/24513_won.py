import sys
input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]

qu = deque()
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for k in range(M):
        if G[i][k] == 1:
            qu.append([i, k, 1, 0])
        if G[i][k] == 2:
            qu.append([i, k, 2, 0])
while qu:
    cr, cc, num, tmp = qu.popleft()
    if G[cr][cc] != 3:
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                if G[nr][nc] == 0:
                    visited[nr][nc] = tmp + 1
                    qu.append([nr, nc, num, tmp + 1])
                    G[nr][nc] = num
                elif G[nr][nc] != -1 and G[nr][nc] != num and visited[nr][nc] == tmp + 1:
                    G[nr][nc] = 3
ans = [0] * 3
for i in range(N):
    for k in range(M):
        for p in range(3):
            if G[i][k] == p + 1:
                ans[p] += 1
print(*ans)
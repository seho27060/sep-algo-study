import sys
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
v = [[0] * m for _ in range(n)]
arr = [list(map(int, input())) for _ in range(n)]
ans = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            ans[i][j] = 1



def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    cnt = 1
    lst = []

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and v[nx][ny] == 0:
                v[nx][ny] = 1
                if arr[nx][ny] == 0:
                    q.append((nx, ny))
                    cnt += 1

                else:
                    lst.append((nx, ny))

    for x, y in lst:
        v[x][y] = 0
        ans[x][y] += cnt
        if ans[x][y] >= 10:
            ans[x][y] %= 10


for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            if not v[i][j]:
                v[i][j] = 1
                bfs(i, j)

for i in range(n):
    for j in range(m):
            print(ans[i][j], end ='')
    print()
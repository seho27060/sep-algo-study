from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j, 1, 0))
        elif arr[i][j] == 2:
            q.append((i, j, 2, 0))

while q:
    x, y, a, b = q.popleft()
    if arr[x][y] != 3:
        for dx, dy in (-1, 0), (1, 0), (0, 1), (0, -1):
            nx = x+dx
            ny = y+dy
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = a
                    visited[nx][ny] = b+1
                    q.append((nx, ny, a, b+1))
                elif arr[nx][ny] != -1 and arr[nx][ny] != a and visited[nx][ny] == b+1:
                    arr[nx][ny] = 3

ans1, ans2, ans3 = 0, 0, 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            ans1 += 1
        elif arr[i][j] == 2:
            ans2 += 1
        elif arr[i][j] == 3:
            ans3 += 1
print(ans1, ans2, ans3)
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]


v = [[[0]* 3 for _ in range(m)] for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] > 0:
            q.append((i, j))
            v[i][j][arr[i][j]] = 1

while q:
    cx, cy = q.popleft()
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[cx][cy] == 3 or arr[nx][ny] == -1:
                continue
            elif arr[cx][cy] == 1:
                if v[nx][ny][2] == 0 and v[nx][ny][1] == 0:
                    v[nx][ny][1] = v[cx][cy][1]+1
                    q.append((nx, ny))
                    arr[nx][ny] = 1
                elif v[nx][ny][2] == v[cx][cy][1] + 1:
                    v[nx][ny][1] = v[cx][cy][1] +1
                    q.append((nx, ny))
                    arr[nx][ny] = 3
            elif arr[cx][cy] == 2:
                if v[nx][ny][2] == 0 and v[nx][ny][1] == 0:
                    v[nx][ny][2] = v[cx][cy][2]+1
                    q.append((nx, ny))
                    arr[nx][ny] = 2
                elif v[nx][ny][1] == v[cx][cy][2] + 1:
                    v[nx][ny][2] = v[cx][cy][2] +1
                    q.append((nx, ny))
                    arr[nx][ny] = 3
one = 0
two = 0
three = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            one += 1
        elif arr[i][j] == 2:
            two += 1
        elif arr[i][j] == 3:
            three += 1
print(one, two, three)
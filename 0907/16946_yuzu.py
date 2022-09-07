from collections import deque

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
ans = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == '1':
            ans[i][j] = 1

for i in range(N):
    for j in range(M):
        if arr[i][j] == '0':
            if visited[i][j] == 0:
                visited[i][j] = 1
                q = deque()
                q.append((i, j))
                cnt = 1
                visit = deque()
                while q:
                    x, y = q.popleft()
                    for dx, dy in (-1, 0), (1, 0), (0, 1), (0, -1):
                        nx = x+dx
                        ny = y+dy
                        if 0<=nx<N and 0<=ny<M:
                            if arr[nx][ny] == '0' and visited[nx][ny] == 0:
                                q.append((nx, ny))
                                visited[nx][ny] = 1
                                cnt += 1
                            elif visited[nx][ny] == 1:
                                continue
                            else:
                                visited[nx][ny] = 1
                                visit.append((nx, ny))
                for u, v in visit:
                    visited[u][v] = 0
                    ans[u][v] += cnt
                    ans[u][v] %= 10
for an in ans:
    for a in an:
        print(a, end='')
    print()
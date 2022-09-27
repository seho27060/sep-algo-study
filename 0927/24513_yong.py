# bfs문제
# 바이러스의 좌표 종류, 전파시간을 큐에 담아서 진행
# 조건에 맞게 1, 2, 3을 배열에 표시하고 마지막으로 출력

from collections import deque
import sys
input = sys.stdin.readline

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs():
    visited = [[0] * m for _ in range(n)]
    while v:
        y, x, num, t = v.popleft()
        if arr[y][x] != 3:
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < n and 0 <= nx < m:
                    if not arr[ny][nx]:
                        arr[ny][nx] = num
                        visited[ny][nx] = t+1
                        v.append((ny, nx, num, t+1))
                    elif arr[ny][nx] != -1 and arr[ny][nx] != num:
                        if visited[ny][nx] == t+1:
                            arr[ny][nx] = 3

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
v = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            v.append((i, j, 1, 0))
        if arr[i][j] == 2:
            v.append((i, j, 2, 0))
bfs()

vi = [0] * 3
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            vi[0] += 1
        elif arr[i][j] == 2:
            vi[1] += 1
        elif arr[i][j] == 3:
            vi[2] += 1
print(*vi)
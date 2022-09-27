# 백준 24513 좀비 바이러스 - bfs
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = []
visited = [[0 for _  in range(M)] for _ in range(N)]    # 방문 체크 배열
Q = deque()

for i in range(N):
    m = list(map(int, input().split()))
    for j in range(M):
        if m[j] == 1:   # 1번 바이러스
            Q.append((i, j, 1, 0))  # Q에 1번 바이러스 저장, 0은 시간 저장을 위해 저장
        elif m[j] == 2: # 2번 바이러스
            Q.append((i, j, 2, 0))

    arr.append(m)


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while Q:
    x, y, v, t = Q.popleft()
    if arr[x][y] != 3:  # 3번 바이러스가 아니면
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:     # 범위 체크
                if arr[nx][ny] == 0:    # 바이러스가 없다면
                    arr[nx][ny] = v     # 바이러스 감염
                    visited[nx][ny] = t + 1 # visited에 시간 저장
                    Q.append((nx, ny, v, t+1))  # Q에 새롭게 감염된 위치, 바이러스 종류, 시간 저장

                elif arr[nx][ny] != -1 and arr[nx][ny] != v:    # 치료제 없고 이미 다른 바이러스가 있는 곳이면
                    if visited[nx][ny] == t + 1:    # 도달 시간이 같다면
                        arr[nx][ny] = 3 # 3번 바이러스 두두등장


ans = [0, 0, 0]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            ans[0] = ans[0] + 1

        elif arr[i][j] == 2:
            ans[1] += 1

        elif arr[i][j] == 3:
            ans[2] += 1

print(*ans)

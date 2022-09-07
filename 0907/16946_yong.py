# bfs를 활용한 탐색문제
# 벽이 아닌곳의 영역을 구분하여 딕셔너리에 저장
# 벽인 곳에서 탐색을 진행하여 갈 수 있는 거리의 수를 저장한다.

import sys
input = sys.stdin.readline
from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs(y, x, val):
    q = deque()
    q.append((y, x))
    visited[y][x] = val
    cnt = 1
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == '0' and not visited[ny][nx]:
                cnt += 1
                visited[ny][nx] = val
                q.append((ny, nx))
    dic[val] = cnt

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

dic = dict()
val = 1
for i in range(N):
    for j in range(M): 
        if arr[i][j] == '0' and not visited[i][j]:
            bfs(i, j, val)
            val += 1

for i in range(N):
    for j in range(M):
        if arr[i][j] != '0':
            val = 1
            check = set()
            for d in range(4):
                ni = i + dy[d]
                nj = j + dx[d]
                if 0 <= ni < N and 0 <= nj < M and visited[ni][nj]:
                    check.add(visited[ni][nj])
            for idx in check:
                val += dic[idx]
            arr[i][j] = str(val%10)
for i in range(N):
    for j in range(M):
        print(arr[i][j], end='')
    print()
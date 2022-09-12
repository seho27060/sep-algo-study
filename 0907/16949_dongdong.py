# 백준 16946 벽 부수고 이동하기4

from collections import deque

# 현재 위치에서 방문가능한 갯수 세기
def bfs(sx, sy):
    Q = deque()
    Q.append((sx, sy))
    visited[sx][sy] = 1   # 시작 위치 방문 표시
    cnt = 1

    while Q:
        x, y = Q.popleft()
        zero[x][y] = num    # 현재 세고 있는 그룹에 포함

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:  # 맵을 벗어남
                continue    # 건너뛰기

            if visited[nx][ny]: # 이미 방문했으면 건너뛰기
                continue

            if not arr[nx][ny]: # 이동할 위치가 비어있다면
                Q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1

    return cnt

# 이동 가능한 그룹 총개수 세기
def move(x, y):
    tmp = set()     # 그룹번호를 담기 위한 set

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:  # 맵을 벗어남
            continue  # 건너뛰기

        if not zero[nx][ny]:  # 그룹에 속해있지 않으면 건너뛰기
            continue
        tmp.add(zero[nx][ny])   # 현재 그룹에 포합된 0갯수를 set 데이터에 추가

    cnt = 1
    for a in tmp:
        cnt += info[a]
        cnt %= 10   # 이동 가능한 칸 갯수를 10으로 나눈 나머지 계산

    return cnt

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]   # 방문 저장 배열
# 0으로 인접해 있는 모든 개수를 세준다 - 플러드 필 알고리즘,,
# 0으로 인접한 칸들을 모두 그룹으로 묶고 번호를 매겨준 뒤 0의 갯수를 세어서 딕셔너리에 저장
zero = [[0] * M for _ in range(N)]
ans = [[0] * M for _ in range(N)]

num = 1
info = {}   # 그룹명 : 그룹 안에 포함된 0 총 갯수

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(N):
    for j in range(M):
        if not arr[i][j] and not visited[i][j]:
            cnt = bfs(i, j)
            info[num] = cnt
            num += 1

for i in range(N):
    for j in range(M):
        if arr[i][j]:   # 벽일 경우
            ans[i][j] = move(i, j)  # 벽을 부수고 인접해있는 그룹의 총 갯수

for i in range(N):
    print("".join(map(str, ans[i])))
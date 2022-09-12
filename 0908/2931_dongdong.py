# 백준 2931 가스관

from collections import deque

def direction(a):   # 각 가스관에서 다음 칸으로 이동할 수 있는 방향을 저장하는 함수
    if a == '1':
        return [0, 1]
    elif a == '2':
        return [0, 3]
    elif a == '3':
        return [2, 3]
    elif a == '4':
        return [1, 2]
    elif a == '+' or a == 'M' or a == 'Z':
        return [0, 1, 2, 3]
    elif a == '|':
        return [1, 3]
    elif a == '-':
        return [0, 2]


def bfs(x, y, dir):
    global fx, fy
    q = deque()
    q.append([x, y, dir])
    visited[x][y] = 1
    while q:
        x, y, dir = q.popleft()
        for d in dir:
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                if tmp[nx][ny] != '.':
                    visited[nx][ny] = 1
                    next_dir = direction(tmp[nx][ny])
                    q.append([nx, ny, next_dir])
                else:
                    if tmp[x][y] == 'M' or tmp[x][y] == 'Z':
                        continue
                    if not fx and not fy:
                        fx, fy = nx + 1, ny + 1
                    nd = (d + 2) % 4
                    if nd not in check_list:
                        check_list.append(nd)


R, C = map(int, input().split())
visited = [[0] * C for _ in range(R)]   # 방문 저장 배열

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

tmp = []
for i in range(R):
    row = list(input())
    tmp.append(row)
    for j in range(C):
        if row[j] == 'M':
            sx, sy = i, j
        elif row[j] == 'Z':
            zx, zy = i, j

check_list, fx, fy = [], 0, 0
bfs(sx, sy, [0, 1, 2, 3])
bfs(zx, zy, [0, 1, 2, 3])

for i in range(R):
    for j in range(C):
        if tmp[i][j] != '.' and not visited[i][j]:
            bfs(i, j, direction(tmp[i][j]))
check_list.sort()

if len(check_list) == 4:
    print(fx, fy, '+')
else:
    block_list = ['|', '-', '1', '2', '3', '4']
    for s in block_list:
        if check_list == direction(s):
            print(fx, fy, s)

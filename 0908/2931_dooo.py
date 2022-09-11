
from collections import deque
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
mapping = {'1': {2: 1, 3: 0}, '2': {1: 0, 2: 3}, '3': {0: 3, 1: 2}, '4': {0: 1, 3: 2}}
dot = {0: 2, 1: 3, 2: 0, 3: 1}
sy, sx = 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'M':
            sy, sx = i, j
def chk(ny, nx, cur_d):
    if cur_d == 0 and arr[ny][nx] in ('3', '4'):
        return True
    if cur_d == 1 and arr[ny][nx] in ('2', '3'):
        return True
    if cur_d == 2 and arr[ny][nx] in ('1', '2'):
        return True
    if cur_d == 3 and arr[ny][nx] in ('1', '4'):
        return True
    return False
def bfs():
    q = deque()
    q.append((sy, sx, -1))
    v = [[False for _ in range(m)] for _ in range(n)]
    v[sy][sx] = True
    while q:
        y, x, d = q.popleft()
        if arr[y][x] == 'M':
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] != '.':
                    v[ny][nx] = True
                    q.append((ny, nx, i))
        elif arr[y][x] == '|' or arr[y][x] == '-':
            ny, nx = y+dy[d], x+dx[d]
            if 0 <= ny < n and 0 <= nx < m and not v[ny][nx]:
                v[ny][nx] = True
                q.append((ny, nx, d))
        elif arr[y][x] == '+':
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < n and 0 <= nx < m and not v[ny][nx]:
                    v[ny][nx] = True
                    q.append((ny, nx, i))
        elif arr[y][x] in ('1', '2', '3', '4'):
            nxt_d = mapping[arr[y][x]][d]
            ny, nx = y+dy[nxt_d], x+dx[nxt_d]
            if 0 <= ny < n and 0 <= nx < m and not v[ny][nx]:
                v[ny][nx] = True
                q.append((ny, nx, nxt_d))
        elif arr[y][x] == '.':
            tmp = []
            for i in range(4):
                if i == dot[d]:
                    continue
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < n and 0 <= nx < m:
                    if arr[ny][nx] != '.':
                        if arr[ny][nx] == '+' or (i in (1, 3) and arr[ny][nx] == '|') or (i in (0, 2) and arr[ny][nx] == '-') or chk(ny, nx, i):
                            tmp.append(i)
            if len(tmp) == 1:
                if d == tmp[0]:
                    if tmp[0] == 1 or tmp[0] == 3:
                        result = [y+1, x+1, '|']
                        return result
                    if tmp[0] == 0 or tmp[0] == 2:
                        result = [y+1, x+1, '-']
                        return result
                else:
                    for key, value in mapping.items():
                        for before, nxt in mapping[key].items():
                            if d == before and tmp[0] == nxt:
                                result = [y+1, x+1, key]
                                return result
            elif len(tmp) == 3:
                result = [y+1, x+1, '+']
                return result
print(*bfs())
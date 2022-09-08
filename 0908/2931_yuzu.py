R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]

dict = {'|':[0, 2], '-':[1, 3], '+':[0, 1, 2, 3], '1':[1, 2], '2':[0, 1], '3':[0, 3], '4':[2, 3], 'M':[0, 1, 2, 3], 'Z':[0, 1, 2, 3]}
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'M':
            sx, sy = i, j
        elif arr[i][j] == 'Z':
            ex, ey = i, j

ans = []
bx, by = 0, 0
def bfs(x, y, z):
    global bx, by
    q = [(x, y, z)]
    visited[x][y] = 1
    while q:
        x, y, z = q.pop(0)
        for d in z:
            nx = x+dx[d]
            ny = y+dy[d]
            if 0<=nx<R and 0<=ny<C and visited[nx][ny] == 0:
                if arr[nx][ny] != '.':
                    visited[nx][ny] = 1
                    q.append((nx, ny, dict[arr[nx][ny]]))
                else:
                    for k in range(4):
                        bbx = nx+dx[k]
                        bby = ny+dy[k]
                        cnt = 0
                        if 0 <= bbx < R and 0 <= bby < C:
                            if k == 0:
                                if arr[bbx][bby] == '|' or arr[bbx][bby] == '1' or arr[bbx][bby] == '4' or arr[bbx][
                                    bby] == '+':
                                    cnt += 1
                            elif k == 1:
                                if arr[bbx][bby] == '-' or arr[bbx][bby] == '3' or arr[bbx][bby] == '4' or arr[bbx][
                                    bby] == '+':
                                    cnt += 1
                            elif k == 2:
                                if arr[bbx][bby] == '|' or arr[bbx][bby] == '2' or arr[bbx][bby] == '3' or arr[bbx][
                                    bby] == '+':
                                    cnt += 1
                            elif k == 3:
                                if arr[bbx][bby] == '-' or arr[bbx][bby] == '1' or arr[bbx][bby] == '2' or arr[bbx][
                                    bby] == '+':
                                    cnt += 1
                        if cnt > 0:
                            bx = nx+1
                            by = ny+1
                            break

bfs(sx, sy, [0, 1, 2, 3])

for z in range(4):
    nbx = bx+dx[z]-1
    nby = by+dy[z]-1
    if 0 <= nbx < R and 0 <= nby < C:
        if z == 0:
            if arr[nbx][nby] == '|' or arr[nbx][nby] == '1' or arr[nbx][nby] == '4' or arr[nbx][nby] == '+':
                ans.append(0)
        elif z == 1:
            if arr[nbx][nby] == '-' or arr[nbx][nby] == '3' or arr[nbx][nby] == '4' or arr[nbx][nby] == '+':
                ans.append(1)
        elif z == 2:
            if arr[nbx][nby] == '|' or arr[nbx][nby] == '2' or arr[nbx][nby] == '3' or arr[nbx][nby] == '+':
                ans.append(2)
        elif z == 3:
            if arr[nbx][nby] == '-' or arr[nbx][nby] == '1' or arr[nbx][nby] == '2' or arr[nbx][nby] == '+':
                ans.append(3)

if ans == [0, 2]:
    print(bx, by, '|')
elif ans == [1, 3]:
    print(bx, by, '-')
elif ans == [0, 1, 2, 3]:
    print(bx, by, '+')
elif ans == [1, 2]:
    print(bx, by, 1)
elif ans == [0, 1]:
    print(bx, by, 2)
elif ans == [0, 3]:
    print(bx, by, 3)
elif ans == [2, 3]:
    print(bx, by, 4)
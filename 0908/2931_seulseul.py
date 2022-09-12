from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
visited = [[False]*C for _ in range(R)]

# 상하좌우
dY = [-1, 1, 0, 0]
dX = [0, 0, -1, 1]

# 시작점과 끝점 찾기
maps = []
for row in range(R):
    maps.append(list(input().rstrip()))
    if 'M' in maps[row]:
        sY = row
        sX = maps[row].index('M')
    if 'Z' in maps[row]:
        eY = row
        eX = maps[row].index('Z')

# 방향성 반환 함수
def direction(c):
    if c == '|':
        return [0, 1]
    elif c == '-':
        return [2, 3]
    elif c == '+' or c == 'M' or c == 'Z':
        return [0, 1, 2, 3]
    elif c == '1':
        return [1, 3]
    elif c == '2':
        return [0, 3]
    elif c == '3':
        return [0, 2]
    elif c == '4':
        return [1, 2]

def bfs(y, x, dir):
    global bY, bX
    q = deque([[y, x, dir]])
    visited[y][x] = True
    while q:
        cY, cX, Dlst = q.popleft()
        for cD in Dlst:
            nY = cY+dY[cD]
            nX = cX+dX[cD]
            # 0->1 1->0 2->3 3->2
            nD = (cD+1)%2 if cD<2 else (cD+1)%2+2
            if 0<=nY<R and 0<=nX<C and not visited[nY][nX]:
                # 만약 방문X q라면 방문처리 & q에 추가
                if maps[nY][nX]!='.':
                    visited[nY][nX] = True
                    q.append([nY, nX, direction(maps[nY][nX])])
                else:
                    # 시작점||끝점이리면 continue
                    if maps[cY][cX]=='M' or maps[cY][cX]=='Z':
                        continue
                    if bY==0 and bX==0:
                        bY, bX = nY, nX
                    if nD not in Darr:
                        Darr.append(nD)

bY, bX, Darr = 0, 0, []
bfs(sY, sX, [0, 1, 2, 3])
bfs(eY, eX, [0, 1, 2, 3])

for row in range(R):
    for col in range(C):
        if maps[row][col]!='.' and not visited[row][col]:
            bfs(row, col, direction(maps[row][col]))

Darr.sort()

check = ['|', '-', '+', '1', '2', '3', '4']

for ans in check:
    if Darr == direction(ans):
        print(bY+1, bX+1, ans)
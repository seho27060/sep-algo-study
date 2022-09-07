from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(N)]
# 구간 나눠버리기
route = [[[] for _ in range(M)] for _ in range(N)]
ans = [[0]*M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dY = [-1, 1, 0, 0]
dX = [0, 0, -1, 1]
num = 1

def bfs(sY, sX, number):
    tmp = 1
    lst = [[sY, sX]]
    q = deque([[sY, sX]])
    visited[sY][sX] = True
    while q:
        cY, cX = q.popleft()
        for i in range(4):
            nY = cY+dY[i]
            nX = cX+dX[i]
            if 0<=nY<N and 0<=nX<M and not visited[nY][nX] and maps[nY][nX]=='0':
                q.append([nY, nX])
                tmp+=1
                lst.append([nY, nX])
                visited[nY][nX] = True
    for y, x in lst:
        route[y][x] = [number, tmp]

for row in range(N):
    for col in range(M):
        if maps[row][col]=='0' and not route[row][col]:
            bfs(row, col, num)
            num+=1

for row in range(N):
    for col in range(M):
        if maps[row][col]=='1':
            ans[row][col]=1
            lst = []
            for i in range(4):
                nY = row+dY[i]
                nX = col+dX[i]
                if 0<=nY<N and 0<=nX<M and route[nY][nX] and route[nY][nX][0] not in lst:
                    lst.append(route[nY][nX][0])
                    ans[row][col]+=route[nY][nX][1]
                    ans[row][col]%=10

for x in ans:
    print("".join(map(str, x)))
from collections import deque
import sys
input = sys.stdin.readline

dY = [0, 0, -1, 1]
dX = [-1, 1, 0, 0]

N, M = map(int, input().split())
maps = []

for i in range(N):
    x = list(map(int, input().split()))
    for j in range(M):
        if x[j] == 1:
            first = [i, j]
        elif x[j] == 2:
            second = [i, j]
    maps.append(x)

a, b, c = 1, 1, 0

fQ = deque([first])
sQ = deque([second])

def F():
    global a, fQ
    tmp = deque()
    while fQ:
        cY, cX = fQ.popleft()
        if maps[cY][cX] != 1:
            continue
        for _ in range(4):
            nY = cY+dY[_]
            nX = cX+dX[_]
            if 0<=nY<N and 0<=nX<M and not maps[nY][nX]:
                maps[nY][nX] = 1
                tmp.append([nY, nX])
                a+=1
    fQ = tmp

def S():
    global a, b, c, sQ
    tmp = deque()
    while sQ:
        cY, cX = sQ.popleft()
        if maps[cY][cX] != 2:
            continue
        for _ in range(4):
            nY = cY+dY[_]
            nX = cX+dX[_]
            if 0<=nY<N and 0<=nX<M:
                if not maps[nY][nX]:
                    maps[nY][nX] = 2
                    tmp.append([nY, nX])
                    b+=1
                elif maps[nY][nX] == 1:
                    maps[nY][nX] += 2
                    c+=1
                    a-=1
    sQ = tmp

while fQ or sQ:
    F()
    S()

print(a, b, c)
import sys
input = sys.stdin.readline
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def infeste1():
    while ST1:
        nx,ny = ST1.popleft()

        for i in range(4):
            X = nx + dx[i]
            Y = ny + dy[i]
            if 0<=X<M and 0<=Y<N and city[Y][X] == 0:
                virus1.append((X,Y))

def infeste2():
    C = len(ST2)
    while C:
        nx,ny = ST2.popleft()

        for i in range(4):
            X = nx + dx[i]
            Y = ny + dy[i]
            if 0 <= X < M and 0 <= Y < N and city[Y][X] == 0:
                if (X,Y) in virus1:
                    city[Y][X] = 3
                    result[2] += 1
                else:
                    city[Y][X] = 2
                    result[1] += 1
                    ST2.append((X,Y))

        C -=1

N,M = map(int,input().split())
city = []
for i in range(N):
    A = list(map(int,input().split()))
    for j in range(M):
        if A[j] == 1:
            one = (j,i)
        if A[j] == 2:
            two = (j,i)
    city.append(A)

ST1 = deque()
ST1.append(one)
ST2 =deque()
ST2.append(two)

virus1=deque()
result =[1,1,0]
while 1:
    infeste1()
    infeste2()

    while virus1:
        nx,ny = virus1.popleft()
        if city[ny][nx] == 0:
            city[ny][nx] = 1
            result[0] += 1
            ST1.append((nx,ny))

    if len(ST1)==0 and len(ST2) ==0:
        break

print(*result)


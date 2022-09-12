dx=[1,-1,0,0]
dy=[0,0,1,-1]
pipe = {
    '|':[2,3],
    '-':[0,1],
    '+':[0,1,2,3],
    '1':[0,2],
    '2':[0,3],
    '3':[1,3],
    '4':[1,2]
}
DSNB = { 0:1, 1:0, 2:3, 3:2}

R,C = map(int,input().split())
road = []
visit = [[0]*C for _ in range(R)]

for i in range(R):
    A = input()
    for j in range(C):
        if A[j] == 'M':
            M = (j,i)
            visit[i][j] = 1
        if A[j] == 'Z':
            Z = (j,i)
    road.append(A)


for i in range(4):
    X = M[0] + dx[i]
    Y = M[1] + dy[i]
    if 0<=X<C and 0<=Y<R and road[Y][X] != '.' and road[Y][X] != 'Z':
        if i == 0 and 1 in pipe[road[Y][X]]:
            start = (X,Y,i)
            visit[Y][X] = 1
        elif i == 1 and 0 in pipe[road[Y][X]]:
            start = (X, Y,i)
            visit[Y][X] = 1
        elif i == 2 and 3 in pipe[road[Y][X]]:
            start = (X, Y,i)
            visit[Y][X] = 1
        elif i == 3 and 2 in pipe[road[Y][X]]:
            start = (X, Y,i)
            visit[Y][X] = 1
ST = [start]
while ST:
    nx,ny,I=ST.pop(0)
    if road[ny][nx] == '.':
        break

    if road[ny][nx] == '+':
        X = nx + dx[I]
        Y = ny + dy[I]
        visit[ny][nx] = 2
        ST.append((X,Y,I))
        visit[Y][X] = 1
        continue

    for i in pipe[road[ny][nx]]:
        if I == DSNB[i]: continue
        X = nx + dx[i]
        Y = ny + dy[i]
        ST.append((X,Y,i))
        visit[Y][X] = 1


result = [DSNB[I]]
for i in range(4):
    if I == DSNB[i]: continue
    X = nx + dx[i]
    Y = ny + dy[i]
    if 0 <= X < C and 0 <= Y < R and road[Y][X] != '.' and road[Y][X] != 'M' and road[Y][X] !='Z' and visit[Y][X] != 1 and DSNB[i] in pipe[road[Y][X]]:
        result.append(i)

result.sort()
for r in pipe.keys():
    if pipe[r] == result:
        R = r
        break
print(ny+1, nx+ 1, R)
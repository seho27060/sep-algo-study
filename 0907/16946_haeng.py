import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x,y):
    global level
    ST = [(x,y)]

    visit[y][x] = 1

    cnt = 0
    while ST:
        nx,ny = ST.pop(0)
        cnt += 1
        result[ny][nx] = level
        for i in range(4):
            X = nx + dx[i]
            Y = ny + dy[i]
            if 0<=X<M and 0<=Y<N and road[Y][X]=='0' and visit[Y][X] == 0:
                ST.append((X,Y))
                visit[Y][X] = 1

    check[level]=cnt
    return

N,M = map(int,input().split())
road = []
for _ in range(N):
    road.append(list(input()))

visit = [[0]*M for _ in range(N)]
result = [[0]*M for _ in range(N)]
level = 1
check = {0:0}

for y in range(N):
    for x in range(M):
        if road[y][x] == '0' and result[y][x] == 0:
            bfs(x,y)
            level += 1

for r in range(N):
    for e in range(M):
        if road[r][e] == '1':
            s = 1
            visit = []
            for u in range(4):
                R = r + dy[u]
                E = e + dx[u]
                if 0<=R<N and 0<=E<M and result[R][E] not in visit:
                    s += check[result[R][E]]
                    visit.append(result[R][E])
            road[r][e] = str(s)[-1]

for j in range(N):
    a = ''
    for k in range(M):
        a += str(road[j][k])
    print(a)
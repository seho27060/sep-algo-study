dx=[1,-1,0,0]
dy=[0,0,1,-1]

def findIn():
    global result
    for i in range(w):
        if space[0][i] != '*':
            visit[0][i] = 1
            if space[0][i] == '$':
                result +=1
                start.append((i, 0))
            elif space[0][i] == '.' or space[0][i] in key:
                start.append((i,0))
            else:
                if space[0][i].islower():
                    key.append(space[0][i].upper())
                    start.append((i, 0))
                else:
                    block.append((i,0))

        if space[h-1][i] != '*':
            visit[h-1][i] = 1
            if space[h-1][i]  == '$':
                result +=1
                start.append((i, h - 1))
            elif space[h-1][i] == '.' or space[h-1][i] in key:
                start.append((i,h-1))
            else:
                if space[h-1][i].islower():
                    key.append(space[h-1][i].upper())
                    start.append((i, h-1))
                else:
                    block.append((i,h-1))
    for i in range(1, h - 1):
        if space[i][0] != '*':
            visit[i][0] = 1
            if space[i][0] == '$':
                result +=1
                start.append((0, i))
            elif space[i][0] == '.' or space[i][0] in key:
                start.append((0, i))
            else:
                if space[i][0].islower():
                    key.append(space[i][0].upper())
                    start.append((0,i))
                else:
                    block.append((0,i))
        if space[i][w-1] != '*':
            visit[i][w-1] = 1
            if space[i][w-1] == '$':
                result +=1
                start.append((w - 1, i))
            elif space[i][w - 1] == '.' or space[i][w - 1] in key:
                start.append((w-1,i))
            else:
                if space[i][w-1].islower():
                    key.append(space[i][w-1].upper())
                    start.append((w-1, i))
                else:
                    block.append((w-1, i))

def goStart():
    global result
    while start:
        nx,ny = start.pop(0)

        for i in range(4):
            X = nx + dx[i]
            Y = ny + dy[i]
            if 0<=X<w and 0<=Y<h and space[Y][X] != '*' and visit[Y][X] == 0:
                visit[Y][X] = 1
                if space[Y][X] == '$':
                    result += 1
                    start.append((X, Y))
                elif space[Y][X] == '.' or space[Y][X] in key:
                    start.append((X,Y))
                else:
                    if space[Y][X].islower():
                        key.append(space[Y][X].upper())
                        start.append((X,Y))
                    else:
                        block.append((X,Y))

def CheckBlock():
    for nx,ny in block:
        if space[ny][nx] in key and visit[ny][nx] == 1:
            start.append((nx,ny))
            visit[ny][nx] = 2


T = int(input())
for t in range(T):
    h,w = map(int,input().split())

    space = []
    for i in range(h):
        space.append(input())

    K = input()
    key = []
    if K != '0':
        for k in K:
            key.append(k.upper())

    start = []
    block = []
    visit = [[0]*w for _ in range(h)]
    result = 0


    findIn()
    while 1:
        goStart()
        CheckBlock()
        if len(start) == 0:
            break
    print(result)

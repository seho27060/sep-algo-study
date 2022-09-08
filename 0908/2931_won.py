import sys
# sys.stdin = open("sample_input.txt", "r")
input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations

# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def getDir(d):
    if d == '|':
        return [0, 2]
    if d == '1':
        return [1, 2]
    if d == '2':
        return [0, 1]
    if d == '3':
        return [0, 3]
    if d == '4':
        return [2, 3]
    if d == '-':
        return [1, 3]
    if d == '+' or d == 'M' or d == 'Z':
        return [0, 1, 2, 3]

def f(sr, sc, dir):
    global tr, tc
    qu = deque()
    visited[sr][sc] = 1
    qu.append([sr, sc, dir])
    while qu:
        cr, cc, dir = qu.popleft()

        for d in dir:
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == 0:
                if G[nr][nc] != '.':
                    visited[nr][nc] = 1
                    new_dir = getDir(G[nr][nc])
                    qu.append([nr, nc, new_dir])
                else:
                    if G[cr][cc] == 'M' or G[cr][cc] == 'Z':
                        continue
                    if tr == -1 and tc == -1:
                        tr = nr + 1
                        tc = nc + 1
                    nd = (d + 2) % 4
                    if nd not in tmp:
                        tmp.append(nd)

R, C = map(int, input().split())
G = [input().rstrip() for _ in range(R)]
visited = [[0] * C for _ in range(R)]
mr = mc = zr = zc = -1
for i in range(R):
    for k in range(C):
        if G[i][k] == 'M':
            mr, mc = i, k
        if G[i][k] == 'Z':
            zr, zc = i, k

tmp = []
tr, tc = -1, -1
f(mr, mc, [0, 1, 2, 3])
f(zr, zc, [0, 1, 2, 3])

for i in range(R):
    for k in range(C):
        if G[i][k] != '.' and visited[i][k] == 0:
            f(i, k, getDir(G[i][k]))

tmp.sort()

if len(tmp) == 4:
    print(tr, tc, '+')
else:
    remain = ['|', '1', '2', '3', '4', '-']
    for r in remain:
        if tmp == getDir(r):
            print(tr, tc, r)
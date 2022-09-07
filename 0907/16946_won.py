import sys
# sys.stdin = open("sample_input.txt", "r")
input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def f(sr, sc, num):
    cnt = 1
    qu = deque()
    visited[sr][sc] = 1
    qu.append([sr, sc])
    G2[sr][sc] = num
    while qu:
        cr, cc = qu.popleft()
        for d in range(4):
            nr, nc = cr + dr [d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and G[nr][nc] == 0:
                visited[nr][nc] = 1
                qu.append([nr, nc])
                G2[nr][nc] = num
                cnt += 1
    return cnt

N, M = map(int, input().split())
G = [list(map(int, input().rstrip())) for _ in range(N)]
G2 = [[0] * M for _ in range(N)]
ans = [[0] * M for _ in range(N)]
num = 1
dic = dict()
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for k in range(M):
        if G[i][k] == 0 and visited[i][k] == 0:
            res = f(i, k, num)
            dic[num] = res
            num += 1

for cr in range(N):
    for cc in range(M):
        if G[cr][cc] == 1:
            res = set()
            for d in range(4):
                nr, nc = cr + dr[d], cc + dc[d]
                if 0 <= nr < N and 0 <= nc < M and G2[nr][nc] != 0:
                    res.add(G2[nr][nc])
            ans[cr][cc] = 1
            for r in res:
                ans[cr][cc] += dic[r]
            ans[cr][cc] = ans[cr][cc] % 10

for i in ans:
    for k in i:
        print(k, end='')
    print()
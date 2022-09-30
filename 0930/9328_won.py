import sys
input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop
# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())

def bfs(sr, sc):
    cnt = 0
    qu = deque()
    visited = [[0] * (w + 2) for _ in range(h + 2)]
    visited[sr][sc] = 1
    qu.append([sr, sc])
    while qu:
        cr, cc = qu.popleft()

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < h + 2 and 0 <= nc < w + 2 and visited[nr][nc] == 0:
                if G[nr][nc] == '*':
                    continue
                if G[nr][nc] == '.':
                    visited[nr][nc] = 1
                    qu.append([nr, nc])
                if G[nr][nc].isupper():
                    if door[ord(G[nr][nc]) - ord('A')] == 1:
                        visited[nr][nc] = 1
                        G[nr][nc] = '.'
                        qu.append([nr, nc])
                if G[nr][nc].islower():
                    door[ord(G[nr][nc]) - ord('a')] = 1
                    qu = deque()
                    visited = [[0] * (w + 2) for _ in range(h + 2)]
                    G[nr][nc] = '.'
                    qu.append([nr, nc])
                if G[nr][nc] == '$':
                    visited[nr][nc] = 1
                    cnt += 1
                    G[nr][nc] = '.'
                    qu.append([nr, nc])
    return cnt

for _ in range(T):
    h, w = map(int, input().split())
    G = [['.'] * (w + 2) for _ in range(h + 2)]
    for i in range(1, h + 1):
        tmp = input().rstrip()
        for k in range(1, w + 1):
            G[i][k] = tmp[k - 1]
    key = input().rstrip()
    door = [0] * 26
    for k in key:
        if k != '0':
            door[ord(k) - ord('a')] = 1
    ans = bfs(0, 0)
    print(ans)

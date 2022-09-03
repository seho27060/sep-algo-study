# bfs문제
# 모든 경우의 수를 탐색하다가 첫번째 물통이 비어있을 때 3번째 물통의 양을 확인

import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    while q:
        y, x = q.popleft()
        z = c - y - x

        if not y:
            ans.append(z)

        val = min(y, b-x)
        if not visited[y-val][x+val]:
            visited[y-val][x+val] = 1
            q.append((y-val, x+val))
        
        val = min(y, c-z)
        if not visited[y-val][x]:
            visited[y-val][x] = 1
            q.append((y-val, x))

        val = min(x, c-z)
        if not visited[y][x-val]:
            visited[y][x-val] = 1
            q.append((y, x-val))
        
        val = min(x, a-y)
        if not visited[y+val][x-val]:
            visited[y+val][x-val] = 1
            q.append((y+val, x-val))
        
        val = min(z, a-y)
        if not visited[y+val][x]:
            visited[y+val][x] = 1
            q.append((y+val, x))
        
        val = min(z, b-x)
        if not visited[y][x+val]:
            visited[y][x+val] = 1
            q.append((y, x+val))

a, b, c = map(int, input().split())

q = deque()
q.append((0, 0))

visited = [[0] * (b+1) for _ in range(a+1)]
visited[0][0] = 1

ans = []

bfs()

ans.sort()
print(*ans)
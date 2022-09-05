# 너비우선탐색문제
# 거리값을 누적해 visited에 저장해 목표 지점까지의 거리를 구한다

import sys
input = sys.stdin.readline
from collections import deque

def bfs(start, end):
    q = deque()
    q.append(start)
    visited = [-1] * (N+1)
    visited[start] = 0
    while q:
        s = q.popleft()
        if s == end:
            break
        for e, d in arr[s]:
            if visited[e] == -1:
                visited[e] = visited[s] + d
                q.append(e)
    return visited[end]

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

for _ in range(M):
    s, e = map(int, input().split())
    print(bfs(s, e))
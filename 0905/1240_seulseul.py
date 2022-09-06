from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
TREE = [[] for _ in range(N+1)]

def func(s, e):
    q = deque([[s, 0]])
    visited = [False] * (N+1)
    visited[s] = True
    while q:
        now, dist = q.popleft()
        if now==e:
            return dist
        for next, cost in TREE[now]:
            if not visited[next]:
                visited[next]=True
                q.append([next, cost+dist])


for i in range(N-1):
    a, b, c = map(int, input().split())
    TREE[a].append([b, c])
    TREE[b].append([a, c])

for i in range(M):
    start, end = map(int, input().split())
    print(func(start, end))
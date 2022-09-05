# 220905 1240 노드사이의 거리
#
import sys
from collections import deque

input = sys.stdin.readline

def bfs(start,end):
    global graph
    queue = deque([[start,0]])
    visited = [0]*(n)

    while queue:
        now, cost = queue.popleft()
        visited[now] = 1
        if now == end:
            print(cost)
            return
        else:
            for nxt, nxtCost in graph[now]:
                if visited[nxt] == 0:
                    queue.append([nxt, cost+nxtCost])

n, m = map(int,input().split())

graph = [[] for _ in range(n)]

for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a-1].append([b-1,c])
    graph[b-1].append([a-1,c])

for _ in range(m):
    s, e = map(int,input().split())
    bfs(s-1,e-1)
import heapq
import collections
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = collections.defaultdict(list)
for _ in range(n-1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def dijkstra(x):
    dist = [1e9] * (n + 1)
    q = [(0, x)]
    dist[x] = 0
    while q:
        d, node = heapq.heappop(q)
        if dist[node] < d:
            continue
        for v, w in graph[node]:
            if d+w < dist[v]:
                dist[v] = d+w
                heapq.heappush(q, (d+w, v))
    return dist[b]

for _ in range(m):
    a, b = map(int, input().split())
    print(dijkstra(a))
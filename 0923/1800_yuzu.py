import heapq
import collections
import sys
input = sys.stdin.readline

N, P, K = map(int, input().split())

graph = collections.defaultdict(list)
for _ in range(P):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def dijkstra(mid):
    net = [1e9] * (N+1)
    net[1] = 0
    q = [(0, 1)]
    while q:
        d, node = heapq.heappop(q)
        if net[node] < d:
            continue
        for v, w in graph[node]:
            if mid < w:
                if d+1 < net[v]:
                    net[v] = d+1
                    heapq.heappush(q, (d+1, v))
            else:
                if d < net[v]:
                    net[v] = d
                    heapq.heappush(q, (d, v))

    if net[-1] > K:
        return False
    return True

l, r = 0, 1000001
ans = 1000001
while l <= r:
    mid = (l+r)//2
    if dijkstra(mid):
        r = mid-1
        ans = mid
    else:
        l = mid+1

print(-1) if ans == 1000001 else print(ans)
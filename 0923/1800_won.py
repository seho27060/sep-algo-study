import sys
input = sys.stdin.readline
# from collections import deque
from heapq import heappush, heappop

INF = float('inf')
N, P, K = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(P):
    u, v, w = map(int, input().split())
    G[u].append([w, v])
    G[v].append([w, u])

def f(s, e):
    qu = []
    dist = [INF] * (N + 1)
    heappush(qu, [0, s])
    dist[s] = 0
    while qu:
        cur_cost, cur_node = heappop(qu)
        if dist[cur_node] < cur_cost:
            continue
        for new_cost, new_node in G[cur_node]:
            if new_cost > e:
                if dist[new_node] > cur_cost + 1:
                    dist[new_node] = cur_cost + 1
                    heappush(qu, [cur_cost + 1, new_node])
            else:
                if dist[new_node] > cur_cost:
                    dist[new_node] = cur_cost
                    heappush(qu, [cur_cost, new_node])
    if dist[N] > K:
        return False
    else:
        return True

l = 0
r = 1000001
ans = INF
while l <= r:
    mid = (l + r) // 2
    res = f(1, mid)
    if res:
        r = mid - 1
        ans = mid
    else:
        l = mid + 1

if ans == INF:
    print(-1)
else:
    print(ans)
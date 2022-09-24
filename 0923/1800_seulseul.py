import sys
import heapq
input = sys.stdin.readline

N, P, K = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(P):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

INF = 1e10

def dijkstra(start, limit):
    q = []
    total = [INF] * (N+1)
    heapq.heappush(q, [0, start])
    total[start] = 0

    while q:
        cost, now = heapq.heappop(q)
        # 만약 전체 총합보다 값이 높다면 구할필요X
        if total[now] < cost:
            continue
        for goCost, next in graph[now]:
            if goCost > limit:
                if cost+1 < total[next]:
                    total[next] = cost+1
                    heapq.heappush(q, [cost+1, next])
            else:
                if cost < total[next]:
                    total[next] = cost
                    heapq.heappush(q, [cost, next])
    if total[N] > K:
        return False
    return True

left, right = 0, 1000001
ans = INF
while left <= right:
    mid = (left+right)//2
    flag = dijkstra(1, mid)
    if flag:
        right = mid-1
        ans = mid
    else:
        left = mid+1

if ans==INF:
    print(-1)
else:
    print(ans)
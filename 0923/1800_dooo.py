import heapq

def dijk(start, t):
    q = []
    d = [inf] * (n+1)
    d[start] = 0
    heapq.heappush(q, (0, start))
    while q:

        dist, now = heapq.heappop(q)
        if d[now] < dist:
            continue
        for j in G[now]:
            if j[1] > t:

                if dist + 1 <d[j[0]]:
                    d[j[0]] = dist + 1
                    heapq.heappush(q, (dist +1 , j[0]))
            else:
                if dist < d[j[0]]:
                    d[j[0]] = dist
                    heapq.heappush(q, (dist, j[0]))
    if d[n] > k:
        return False
    else:
        return True
n, m, k = map(int, input().split())

G = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))
inf =1e9

s = 0
e = 1000001
ans = inf
while s <= e:

    mid = (s+e)//2
    flag = dijk(1, mid)
    if flag:
        e = mid -1
        ans = mid
    else:
        s = mid + 1
if ans == inf:
    print(-1)
else:
    print(ans)


# 이분탐색, 다익스트라 문제
# 이분탐색으로 케이블의 기준 가격을 정하기
# 다익을 통해 N번케이블까지 이을 수 있는지 판단하여 출력

import heapq
import sys
input = sys.stdin.readline

def dijk(s, e):
    q = []
    D = [1000000000] * (N+1)
    heapq.heappush(q, (0, s))
    D[s] = 0
    
    while q:
        val, idx = heapq.heappop(q)
        if D[idx] < val:
            continue
        for v, i in G[idx]:
            if v > e:
                if val +1 < D[i]:
                    D[i] = val+1
                    heapq.heappush(q, (val+1, i))
            else:
                if val < D[i]:
                    D[i] = val
                    heapq.heappush(q, (val, i))

    if D[N] > K:
        return False
    else:
        return True

N, P, K = map(int, input().split())
G = [[] for _ in range(N+1)]
for i in range(P):
    a, b, c = map(int, input().split())
    G[a].append((c, b))
    G[b].append((c, a))

l = 0
r = 1000000
ans =1000000000
while l <= r:
    m = (l + r) // 2
    result = dijk(1, m)
    if result:
        r  = m - 1
        ans = m
    else:
        l = m + 1
if ans == 1000000000:
    print(-1)
else:
    print(ans)
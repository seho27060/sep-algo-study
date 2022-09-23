import sys
from heapq import heappop, heappush
input = sys.stdin.readline


def dijkstra(maxCost):
    Q = [(0, 1)]

    while Q:
        overCnt, curV = heappop(Q)
        if curV == V: return True
        if visit[curV] or overCnt > K: continue
        visit[curV] = True

        for neiV, cost in adj[curV]:
            if cost > maxCost and overCnt < K:
                heappush(Q, (overCnt + 1, neiV))
            elif cost <= maxCost:
                heappush(Q, (overCnt, neiV))

    return False


def binarySearch():
    left, right = 0, maxW

    ans = 1e10
    while left <= right:
        mid = (left + right) // 2
        for i in range(V + 1):
            visit[i] = False
        if dijkstra(mid):
            right = mid - 1
            ans = min(ans, mid)
        else:
            left = mid + 1

    if ans == 1e10: return -1
    return ans


V, E, K = map(int, input().rstrip().split())
adj = [[] for _ in range(V + 1)]
maxW = -1
for _ in range(E):
    v1, v2, w = map(int, input().rstrip().split())
    maxW = max(maxW, w)
    adj[v1].append((v2, w))
    adj[v2].append((v1, w))

visit = [False] * (V + 1)
print(binarySearch())


# dfs 시간 초과 
# import sys
# input = sys.stdin.readline
#
#
# def dfs(curV, freeCnt, maxCost):
#     if freeCnt < 0: return False
#     if curV == V: return True
#
#     for neiV, cost in adj[curV]:
#         if not visit[neiV]:
#             if cost <= maxCost:
#                 visit[neiV] = True
#                 if dfs(neiV, freeCnt, maxCost): return True
#                 visit[neiV] = False
#             elif freeCnt > 0:
#                 visit[neiV] = True
#                 if dfs(neiV, freeCnt - 1, maxCost): return True
#                 visit[neiV] = False
#
#     return False
#
#
# def binarySearch():
#     left, right = 0, 1_000_000
#
#     ans = 1e10
#     while left <= right:
#         mid = (left + right) // 2
#         for i in range(V + 1):
#             visit[i] = False
#         if dfs(1, K, mid):
#             right = mid - 1
#             ans = min(ans, mid)
#         else:
#             left = mid + 1
#
#     if ans == 1e10: return -1
#     return ans
#
#
# V, E, K = map(int, input().rstrip().split())
# adj = [[] for _ in range(V + 1)]
# for _ in range(E):
#     v1, v2, w = map(int, input().rstrip().split())
#     adj[v1].append((v2, w))
#     adj[v2].append((v1, w))
#
# visit = [False] * (V + 1)
# print(binarySearch())
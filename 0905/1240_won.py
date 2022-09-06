import sys
# sys.stdin = open("sample_input.txt", "r")
input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    G[u].append([v, w])
    G[v].append([u, w])

def f(start, target):
    qu = deque()
    visited = [0] * (N + 1)
    qu.append([start, 0])
    visited[start] = 1
    while qu:
        start, total = qu.popleft()

        if start == target:
            return total

        for new_start, new_dist in G[start]:
            if visited[new_start] == 0:
                visited[new_start] = 1
                qu.append([new_start, total + new_dist])

    return

for _ in range(M):
    s, e = map(int, input().split())
    res = f(s, e)
    print(res)

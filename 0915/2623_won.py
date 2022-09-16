import sys
# sys.stdin = open("sample_input.txt", "r")
# input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for i in range(M):
    arr = list(map(int, input().split()))
    for i in range(1, arr[0]):
        G[arr[i]].append(arr[i + 1])
        indegree[arr[i + 1]] += 1

qu = deque()
ans = []
for i in range(1, N + 1):
    if indegree[i] == 0:
        qu.append(i)

while qu:
    cur = qu.popleft()
    ans.append(cur)
    for i in G[cur]:
        indegree[i] -= 1

        if indegree[i] == 0:
            qu.append(i)

if len(ans) == N:
    for i in ans:
        print(i)
else:
    print(0)
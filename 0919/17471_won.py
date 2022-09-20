import sys
# sys.stdin = open("sample_input.txt", "r")
# input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations

N = int(input())
popul = [0] + list(map(int, input().split()))
G = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    tmp = list(map(int, input().split()))
    M = tmp[0]
    for k in range(1, M + 1):
        G[i].append(tmp[k])

def f(arr):
    cnt = 1
    qu = deque()
    visited = [1] * (N + 1)
    for i in range(len(arr)):
        visited[arr[i]] = 0
    qu.append(arr[0])
    visited[arr[0]] = 1
    while qu:
        cur = qu.popleft()

        for new in G[cur]:
            if visited[new] == 0:
                visited[new] = 1
                qu.append(new)
                cnt += 1
    if cnt == len(arr):
        tmp = 0
        for i in range(len(arr)):
            tmp += popul[arr[i]]
        return tmp
    return False

def comb(x, a, b):
    global ans
    if x == N + 1:
        if len(a) == N or not a or len(b) == N or not b:
            return
        res1 = f(a)
        res2 = f(b)
        if not res1 or not res2:
            return
        res = abs(res1 - res2)
        ans = min(ans, res)
        return
    comb(x + 1, a + [x], b)
    comb(x + 1, a, b + [x])
    return

INF = float('inf')
ans = INF
comb(1, [], [])
if ans == INF:
    print(-1)
else:
    print(ans)
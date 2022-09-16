import sys
input = sys.stdin.readline
# from collections import deque
# from heapq import heappush, heappop

sys.setrecursionlimit(10 ** 6)

def f(c):
    global res
    visited[c] = 1
    tmp.append(c)
    new = G[c]

    if visited[new] == 0:
        f(new)
    else:
        if new in tmp:
            idx = tmp.index(new)
            res += tmp[idx:]
        return
    return

T = int(input())
for _ in range(T):
    N = int(input())
    G = [0] + list(map(int, input().split()))
    visited = [0] * (N + 1)
    visited[0] = 1
    res = []
    for i in range(1, N + 1):
        if visited[i] == 0:
            tmp = []
            f(i)
    print(N - len(res))


import sys
input = sys.stdin.readline
# from collections import deque
from heapq import heappush, heappop

N = int(input())
M = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
arr = list(map(int, input().split()))

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

parents = [i for i in range(N)]
for i in range(N):
    for k in range(N):
        if G[i][k] == 1:
            union(i, k)

parents = [0] + parents
S = parents[arr[0]]
for i in range(1, M):
    if parents[arr[i]] != S:
        print("NO")
        break
else:
    print("YES")
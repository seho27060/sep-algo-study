
# 220915 2623 음악프로그램
# bb

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())
singers = [[] for _ in range(n+1)]
start = [0]*(n+1)

for _ in range(m):
    getLst = list(map(int,input().split()))
    for idx in range(1, getLst[0]):
        singers[getLst[idx]].append(getLst[idx+1])
        start[getLst[idx+1]] += 1
queue = deque([])
answer = []
for idx in range(1, n + 1):
    if start[idx] == 0:
        queue.append(idx)

while queue:
    now = queue.popleft()
    answer.append(now)
    for nxt in singers[now]:
        start[nxt] -= 1
        if start[nxt] == 0:
            queue.append(nxt)

if len(answer) == n:
    for ans in answer:
        print(ans)
else:
    print(0)


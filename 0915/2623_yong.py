# 위상정렬 문제
# 각 노드별 진입차수를 저장
# 0인 노드를 q에 저장하고 계속 진입 차수를 줄여가며 0인 노드를 큐에 추가

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
node = [0] * (N+1)

lst = [list(map(int, input().split())) for _ in range(M)]
for i in lst:
    for j in range(1, i[0]):
        G[i[j]].append(i[j+1])
        node[i[j+1]] += 1

q = deque()
ans = []
for i in range(1, N+1):
    if not node[i]:
        q.append(i)

while q:
    val = q.popleft()
    ans.append(val)
    for i in G[val]:
        node[i] -= 1

        if not node[i]:
            q.append(i)

if len(ans) != N:
    print(0)
else:
    for i in ans:
        print(i)
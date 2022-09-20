# 220920 17471 게리맨더링
# 그래프
# n개의 노드에 대해 1,2,..n-1개씩 조합뽑ㅂ기
# 조합에 해당하는 탐색/ 미해당에 탐색 -> 전체 돌면서 차이계산 -> 다돌았다? answer과 비교

import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

def bfs(lst):
    global n, secNums, graphs, answer
    visited = [0] * (n)

    queue = deque([lst[0]])

    while queue:
        now = queue.popleft()
        visited[now] = 1
        for nxt in graphs[now]:
            if visited[nxt] == 0 and  nxt in lst:
                queue.append(nxt)

    queue = deque([])

    for start in range(n):
        if visited[start] == 0:
            queue.append(start)
            break
    while queue:
        now = queue.popleft()
        visited[now] = 2
        for nxt in graphs[now]:
            if visited[nxt] == 0 and nxt not in lst:
                queue.append(nxt)

    secCheck = True
    result = 0
    for idx in range(n):
        if visited[idx] == 0:
            secCheck = False
            break
        elif visited[idx] == 1:
            result += secNums[idx]
        elif visited[idx] == 2:
            result -= secNums[idx]
    if secCheck:
        answer = min(answer,abs(result))
    return

n = int(input())

secNums = list(map(int,input().split()))
sections = [0]*(n)
graphs = [[] for _ in range(n)]

for i in range(n):
    getLst = list(map(int,input().split()))
    for j in range(getLst[0]):
        graphs[i].append(getLst[j+1]-1)

answer = float("inf")
for com in range(1,n):
    findLst = list(combinations(range(n),com))
    for check in findLst:
        bfs(check)
if answer >= float("inf"):
    print(-1)
else:
    print(answer)
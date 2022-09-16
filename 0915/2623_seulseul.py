from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for i in range(M):
    lst = list(map(int, input().split()))
    for j in range(1, lst[0]):
        # graph[숫자]에 숫자 다음에 오는 녀석들 추가
        graph[lst[j]].append(lst[j+1])
        # 해당 숫자에 간선이 몇개나 있는지
        indegree[lst[j+1]]+=1

print(graph)
print(indegree)

q = deque()

# 1. 부모 노드들 전부 q에 넣기
for i in range(1, N+1):
    if indegree[i]==0:
        q.append(i)

# 2. 돌면서 q에서 하나씩 빼기
ans = []
while q:
    now = q.popleft()
    ans.append(now)
    for next in graph[now]:
        indegree[next]-=1
        if indegree[next]==0:
            q.append(next)

if len(ans)==N:
    for num in ans:
        print(num)
else:
    print(0)
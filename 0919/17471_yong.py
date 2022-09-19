# dfs, bfs를 활용한 문제
# dfs를 통해 조합을 만든 뒤 bfs로 인접했는지 확인하기

import sys
from collections import deque

def bfs(que):
    q = deque()
    check = [0] * n
    q.append(que[0])
    check[que[0]] = 1
    cnt = 1
    ans = 0
    while q:
        val = q.popleft()
        ans += arr[val]
        for i in G[val]:
            if i in que and not check[i]:
                check[i] = 1
                cnt += 1
                q.append(i)
    if cnt == len(que):
        return ans
    else:
        return False

def dfs(cnt, s, e):
    global ans
    if cnt != e:
        for i in range(s, n):
            if visited[i]:
                continue
            visited[i] = 1
            dfs(cnt+1, i, e)
            visited[i] = 0

    else:
        q1 = deque()
        q2 = deque()

        for i in range(n):
            if visited[i]:
                q1.append(i)
            else:
                q2.append(i)
        
        val1 = bfs(q1)
        val2 = bfs(q2)

        if not val1 or not val2:
            return
        
        ans = min(ans, abs(val1 - val2))
        return

n = int(input())
arr = list(map(int, input().split()))
G = [[] for _ in range(n)]
for i in range(n):
    lst = list(map(int, input().split()))
    for j in lst[1:]:
        G[i].append(j-1)

ans = 1000000000

for i in range(1, n//2 + 1):
    visited = [0] * n
    dfs(0, 0, i)

if ans == 1000000000:
    print(-1)
else:
    print(ans)
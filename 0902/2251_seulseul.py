from collections import deque
import sys
input = sys.stdin.readline

visited = [[False] * 201 for _ in range(201)]
A, B, C = map(int, input().split())

q = deque([[0, 0]])
visited[0][0] = True
lst = []

while q:
    a, b = q.popleft()
    c = C-a-b
    if a==0:
        lst.append(c)
    
    # [붓는 물]과 [남은 용량] 중 작은 값을 더해야 한다.
    tmp = min(a, B-b)
    if not visited[a-tmp][b+tmp]:
        visited[a-tmp][b+tmp] = True
        q.append([a-tmp, b+tmp])
    tmp = min(a, C-c)
    if not visited[a-tmp][b]:
        visited[a-tmp][b] = True
        q.append([a-tmp, b])
    tmp = min(b, A-a)
    if not visited[a+tmp][b-tmp]:
        visited[a+tmp][b-tmp] = True
        q.append([a+tmp, b-tmp])
    tmp = min(b, C-c)
    if not visited[a][b-tmp]:
        visited[a][b-tmp] = True
        q.append([a, b-tmp])
    tmp = min(c, A-a)
    if not visited[a+tmp][b]:
        visited[a+tmp][b] = True
        q.append([a+tmp, b])
    tmp = min(c, B-b)
    if not visited[a][b+tmp]:
        visited[a][b+tmp] = True
        q.append([a, b+tmp])

lst.sort()
print(*lst)
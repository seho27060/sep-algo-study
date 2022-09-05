from collections import deque
def bfs(s, e):
    q = deque()
    q.append(s)
    v = [0] * (n+1)
    v[s] = 1
    while q:
        c = q.popleft()
        if c == e:
            return v[e]-1
        for k, d in G[c]:
            if v[k] == 0:
                v[k] = v[c] + d
                q.append(k)

n, m = map(int, input().split())

G = [[] for _ in range(n+1)]


for _ in range(n-1):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))

for _ in range(m):
    s, e = map(int, input().split())
    print(bfs(s, e))
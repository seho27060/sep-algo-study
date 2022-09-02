A, B, C = map(int, input().split())
visit = [[0]*(B+1) for _ in range(A+1)]
visit_c = [0]*(C+1)

q = [(0, 0, C)]

while q:
    x, y, z = q.pop(0)
    if x == 0:
        visit_c[z] = 1
    k = min(x, B-y)
    if visit[x-k][y+k] == 0:
        visit[x-k][y+k] = 1
        q.append((x-k, y+k, z))
    k = min(x, C-z)
    if visit[x-k][y] == 0:
        visit[x-k][y] = 1
        q.append((x-k, y, z+k))
    k = min(y, A-x)
    if visit[x+k][y-k] == 0:
        visit[x+k][y-k] = 1
        q.append((x+k, y-k, z))
    k = min(y, C-z)
    if visit[x][y-k] == 0:
        visit[x][y-k] = 1
        q.append((x, y-k, z+k))
    k = min(z, A-x)
    if visit[x+k][y] == 0:
        visit[x+k][y] = 1
        q.append((x+k, y, z-k))
    k = min(z, B-y)
    if visit[x][y+k] == 0:
        visit[x][y+k] = 1
        q.append((x, y+k, z-k))

for c in range(C+1):
    if visit_c[c] == 1:
        print(c, end=' ')
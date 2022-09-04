from collections import deque

def bfs():
    while q:
        x, y, z = q.popleft()

        if v[x][y] == 1:
            continue
        v[x][y] = 1
        if x == 0:
            ans.append(z)
        if x + y > b:
            q.append([x + y - b, b, z])
        else:
            q.append([0, x + y, z])
        if x + z > c:
            q.append([x + z - c, y, c])
        else:
            q.append([0, y, x + z])
        if y + x > a:
            q.append([a, y + x - a, z])
        else:
            q.append([y + x, 0, z])
        if y + z > c:
            q.append([x, y + z - c, c])
        else:
            q.append([x, 0, y + z])
        if z + x > a:
            q.append([a, y, z + x - a])
        else:
            q.append([z + x, y, 0])
        if z + y > b:
            q.append([x, b, z + y - b])
        else:
            q.append([x, z + y, 0])
a, b, c = map(int, input().split())
v = [[0] * (b+1) for i in range(a+1)]
ans = []
q = deque()
q.append([0, 0, c])
bfs()
ans.sort()
print(*ans)
n = int(input())
m = int(input())

G = [list(map(int, input().split())) for _ in range(n)]
lst = list(map(int, input().split()))
p = list(range(n+1))

def find(a):
    if p[a] != a:
        p[a] = find(p[a])
    return p[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        p[a] = b
    else:
        p[b] = a


for i in range(n):
    for j in range(n):
        if G[i][j] == 1:
            union(i+1, j+1)

for i in range(m):
    if p[lst[i]] != p[lst[0]]:
        print('NO')
        break
else:
    print('YES')

import sys
input = sys.stdin.readline


class DSU:
    def __init__(self, V):
        self.parent = [i for i in range(V + 1)]
        self.rank = [0 for _ in range(V + 1)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)

        if xRoot == yRoot:
            return False

        if self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = xRoot
        elif self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot] = yRoot
        else:
            self.parent[xRoot] = yRoot
            self.rank[yRoot] += 1

        return True


N = int(input().rstrip())
M = int(input().rstrip())

dsu = DSU(N)
for city in range(1, N + 1):
    cities = list(map(int, input().rstrip().split()))
    for neiCity in range(1, N + 1):
        if cities[neiCity - 1]:
            dsu.union(city, neiCity)

route = list(map(int, input().rstrip().split()))
startCityRoot = dsu.find(route[0])

ans = 'YES'
for idx in range(1, len(route)):
    if dsu.find(route[idx]) != startCityRoot:
        ans = 'NO'
        break

print(ans)

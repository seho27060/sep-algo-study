import sys
input = sys.stdin.readline

def union(x, y):
    # x의 부모 노드와 y의 부모 노드를 찾는다.
    x = find(x)
    y = find(y)
    # x의 부모 노드가 더 작다면 y의 부모노드는 x
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

# 재귀로 부모 노드를 찾아나감
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

N = int(input())
M = int(input())
parents = [i for i in range(N)]

for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(N):
        if lst[j] == 1:
            union(i, j)

parents = [-1] + parents
route = list(map(int, input().split()))
start = parents[route[0]]
for destination in route[1:]:
    if parents[destination] != start:
        print("NO")
        break
else:
    print("YES")
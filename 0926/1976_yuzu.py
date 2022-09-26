import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))
parent = [i for i in range(N+1)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            union(i, j)

ans = 'YES'
for i in range(1, M):
    if parent[plan[i]-1] != parent[plan[0]-1]:
        ans = 'NO'
        break

print(ans)
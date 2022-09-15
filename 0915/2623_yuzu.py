N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
r = [0]*(N+1)

for i in range(M):
    l = list(map(int, input().split()))
    for i in range(1, l[0]):
        arr[l[i]].append(l[i+1])
        r[l[i+1]] += 1

q = []
for i in range(1, N+1):
    if r[i] == 0:
        q.append(i)

ans = []
while q:
    x = q.pop(0)
    ans.append(x)
    for i in arr[x]:
        r[i] -= 1
        if r[i] == 0:
            q.append(i)

if len(ans) != N:
    print(0)
else:
    for a in ans:
        print(a)
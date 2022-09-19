from collections import deque, defaultdict
from itertools import combinations

def bfs(comb):
    q = deque([comb[0]])
    visited = deque([comb[0]])
    res = 0
    while q:
        x = q.popleft()
        res += arr[x]
        for l in link[x]:
            if l not in visited and l in comb:
                q.append(l)
                visited.append(l)
    return res, len(visited)

N = int(input())
arr = [0] + list(map(int, input().split()))
link = defaultdict(list)

ans = 1e9
for i in range(1, N+1):
    lst = list(map(int, input().split()))
    link[i] = lst[1:]

for i in range(1, N//2+1):
    com = list(combinations(range(1, N+1), i))
    for c in com:
        res1, cnt1 = bfs(c)
        res2, cnt2 = bfs(list(set([i+1 for i in range(N)]) - set(c)))
        if cnt1 + cnt2 == N:
            ans = min(ans, abs(res1-res2))

print(ans) if ans != 1e9 else print(-1)
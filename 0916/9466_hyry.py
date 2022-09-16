import sys
input = sys.stdin.readline


def dfs(startV):
    ST = [startV]
    route = [startV]

    while ST:
        curV = ST.pop()
        visit[curV] = True
        route.append(curV)

        for neiV in adj[curV]:
            if visit[neiV]:
                isCycle = False
                for r in route:
                    if r == neiV: isCycle = True
                    if isCycle: cycle[r] = True
            else:
                ST.append(neiV)


T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    arr = [0] + list(map(int, input().split()))

    visit = [False] * (N + 1)
    cycle = [False] * (N + 1)
    cycle[0] = True

    adj = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        if i == adj[i]:
            visit[i] = cycle[i] = True
        else:
            adj[i].append(arr[i])

    for i in range(1, N + 1):
        if not visit[i]:
            dfs(i)

    ans = 0
    for c in cycle:
        if not c: ans += 1

    print(ans)
    
# 220916 9466 팀 프로젝트
# 그래프로 표현했을때.. 다시 자기 자신으로 돌아오는가?
# 처음부터 순회하면서.. 체크체크체크 같은 팀 확인되면 visited
# 단방향 그래프..

import sys
sys.setrecursionlimit(10**6)
def dfs(now):
    global getLst, result, visited, check
    visited[now] = 1
    check.append(now)
    nxt = getLst[now]

    if visited[nxt]:
        if nxt in check:
            result.extend(check[check.index(nxt):])
        return
    else:
        dfs(nxt)

tcNum = int(input())

for tc in range(tcNum):
    getLst = [-1]
    n = int(input())
    getLst.extend(list(map(int,input().split())))
    result = []
    visited = [0]*(n+1)
    for idx in range(1,n+1):
        if visited[idx] == 0:
            check = []
            dfs(idx)

    print(n - len(result))
import sys
sys.setrecursionlimit(10**6)

T = int(input())

def dfs(x):
    global res
    visited[x] = 1
    graph.append(x)

    if visited[lst[x]-1] == 0:
        dfs(lst[x]-1)
    else:
        if lst[x]-1 in graph:
            for g in range(len(graph)):
                if graph[g] == lst[x]-1:
                    res += len(graph)-g
                    break
        return

for _ in range(T):
    n = int(input())
    lst = list(map(int, input().split()))
    visited = [0]*n
    res = 0

    for i in range(n):
        if visited[i] == 0:
            graph = []
            dfs(i)

    print(n-res)
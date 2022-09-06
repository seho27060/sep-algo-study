# 백준 1240 노드 사이의 거리

from collections import deque


def bfs(start, find):
    Q = deque()
    Q.append([start, 0])  # 노드번호와 거리 정보 append, 시작이니까 0 집어넣기
    visited = [0] * (N + 1)
    visited[start] = 1

    while Q:
        v, dist = Q.popleft()
        if v == find:  # 찾는 노드와 번호가 일치할 때
            return dist

        for node, l in graph[v]:    # 노드와 길이
            if visited[node] == 0:
                visited[node] = 1
                Q.append([node, dist + l])  # 길이를 누적하면서 기록하기


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    n1, n2, leng = map(int, input().split())
    graph[n1].append((n2, leng))  # 거리정보를 튜플로 묶어서 그래프에 추가
    graph[n2].append((n1, leng))

for _ in range(M):
    s, f = map(int, input().split())
    print(bfs(s, f))

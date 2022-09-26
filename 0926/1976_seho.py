# 220926 1976 여행 가자
# 그래프/ 여행계획대로 이동이 가능한가 n = 200*200

import sys
from collections import deque

input = sys.stdin.readline

def bfs(s):
    global n, graphs, board

    queue = deque([s])

    while queue:
        now = queue.popleft()

        for nxt in range(n):
            if graphs[now][nxt] and board[s][nxt] == 0:
                queue.append(nxt)
                board[s][nxt] = 1

n = int(input())
m = int(input())
graphs = [list(map(int,input().split())) for _ in range(n)]
plan = list(map(int,input().split()))

# i-j 로 아무튼 이동이 가능한가에 대한 board 생성?

board = [[0]*(n) for _ in range(n)]

for start in range(n):
    bfs(start)

answer = "YES"
for i in range(n):
    board[i][i] = 1
for idx in range(1,m):
    if board[plan[idx-1]-1][plan[idx]-1] == 0:
        answer = "NO"
        break
print(answer)
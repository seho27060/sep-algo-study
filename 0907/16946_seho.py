# 220907 16946 벽 부수고 이동하기 4
# 1000*1000. 전체 칸 순회하면서 bfs로 이동가능 범위 탐색
# 벽이 있는곳에 벽을 없애고 인접 4방향의 이동가능 범위
# 맞왜틀~ 맞왜틀~
from collections import deque
import sys

input = sys.stdin.readline

def bfs(r,c,idx):
    global moves, n, m, visited
    queue = deque([[r,c]])
    cnt = 1

    while queue:
        now = queue.popleft()

        for move in moves:
            nxtR, nxtC = now[0] + move[0], now[1] + move[1]
            if 0 <= nxtR < n and 0 <= nxtC < m:
                if visited[nxtR][nxtC] == 0 and board[nxtR][nxtC] == 0:
                    visited[nxtR][nxtC] = idx
                    queue.append([nxtR,nxtC])
                    cnt += 1
    return cnt


n, m = map(int,input().split())
board = [list(map(int,list(input().rstrip()))) for _ in range(n)]
visited = [[0]*(m) for _ in range(n)]
visitedList = []
startIdx = 1
moves = [[0,1],[1,0],[-1,0],[0,-1]]
wallList = []

for row in range(n):
    for col in range(m):
        if board[row][col] == 0 and visited[row][col] == 0:
            # print(row,col)
            visited[row][col] = startIdx
            visitedList.append(bfs(row,col,startIdx))
            startIdx += 1
        elif board[row][col] == 1:
            wallList.append([row,col])
# for kk in visited:
#     print(kk)
# print(visitedList)
# print(wallList)

answer = [[0]*(m) for _ in range(n)]
for wall in wallList:
    addSet = set()
    for move in moves:
        findR, findC = wall[0] + move[0], wall[1] + move[1]
        if 0 <= findR < n and 0 <= findC < m:
            if board[findR][findC] == 0:
                addSet.add(visited[findR][findC])
    for add in addSet:
        answer[wall[0]][wall[1]] += visitedList[add-1]
    answer[wall[0]][wall[1]] += 1

for ans in answer:
    for an in ans:
        print(an%10, end="")
    print()

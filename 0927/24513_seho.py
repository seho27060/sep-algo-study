# 220927 24513 좀비 바이러스
# 1,2 는 "동시에" 펴져나감
# 동시에 퍼져나가는 동시에 다른 바이러스가 침투하면 3번생성
# 치료제있는 마을은 건들수없음
# 다퍼지고 1,2,3 개수 구하기
# n*m = 1000*1000

import sys
from collections import deque

input = sys.stdin.readline

def bfs(queueA, queueB):
    global board, n, m, moves
    nowA, nowB = deque(queueA),deque(queueB)


    while nowA or nowB:
        nxtA, nxtB, nxtF = set(),set(),set()

        for a in nowA:
            for move in moves:
                nxtR, nxtC = a[0] + move[0], a[1] + move[1]
                if 0 <= nxtR < n and 0<= nxtC<m:
                    if board[nxtR][nxtC] == 0:
                        nxtA.add((nxtR,nxtC))
        for b in nowB:
            for move in moves:
                nxtR, nxtC = b[0] + move[0], b[1] + move[1]
                if 0 <= nxtR < n and 0<= nxtC<m:
                    if board[nxtR][nxtC] == 0:
                        nxtB.add((nxtR,nxtC))

        for r,c in nxtA:
            board[r][c] += 1

        for r, c in nxtB:
            board[r][c] += 2
            if board[r][c] == 3:
                nxtF.add((r,c))

        for r, c in nxtF:
            nxtA.remove((r,c))
            nxtB.remove((r,c))
        nowA, nowB = nxtA,nxtB


n, m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*(n) for _ in range(m)]
moves = [[0,1],[0,-1],[1,0],[-1,0]]

queueA = []
queueB = []


for row in range(n):
    for col in range(m):
        if board[row][col] == 1:
            queueA.append([row,col,1])
        elif board[row][col] == 2:
            queueB.append([row,col,2])
answer =[0,0,0]
bfs(queueA,queueB)
for row in range(n):
    for col in range(m):
        if board[row][col] == 1:
            answer[0] += 1
        elif board[row][col] == 2:
            answer[1] += 1
        elif board[row][col] == 3:
            answer[2] += 1
# for ll in board:
#     print(ll)
print(*answer)


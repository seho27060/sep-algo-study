# 220930 9328 열쇠
# . 빈공간/ * 벽/ $ 문서/ A 문 -> 여러개일수도/ a 열쇠
# n*n = 100*100 = 10000
import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    global w, h, board, keys, doorsAndKeys, unlockDoors, moves, visited, answer

    queue = deque([start])

    while queue:
        now = queue.popleft()
        check = True
        if 65 <= ord(board[now[0]][now[1]]) <= 90:
            if doorsAndKeys[board[now[0]][now[1]]] == 1:
                visited[now[0]][now[1]] = 1
                board[now[0]][now[1]] = "."
            else:
                if now not in unlockDoors[board[now[0]][now[1]]]:
                    unlockDoors[board[now[0]][now[1]]].append([now[0], now[1]])
                check = False
        elif 97 <= ord(board[now[0]][now[1]]) <= 122:
            doorsAndKeys[board[now[0]][now[1]].upper()] = 1
            visited[now[0]][now[1]] = 1
            if board[now[0]][now[1]].upper() in unlockDoors.keys():
                if unlockDoors[board[now[0]][now[1]].upper()]:
                    while unlockDoors[board[now[0]][now[1]].upper()]:
                        getN = unlockDoors[board[now[0]][now[1]].upper()].pop()
                        if getN not in queue and visited[getN[0]][getN[1]] == 0:
                            queue.append(getN)
            board[now[0]][now[1]] = "."
        elif board[now[0]][now[1]]== "$":
            answer += 1
            visited[now[0]][now[1]] = 1
            board[now[0]][now[1]] = "."
        elif board[now[0]][now[1]] == ".":
            visited[now[0]][now[1]] = 1
        if check:
            for move in moves:
                nxtR, nxtC = now[0] + move[0], now[1] + move[1]
                if 0 <= nxtR < h and 0 <= nxtC < w:
                    if visited[nxtR][nxtC] == 0 and board[nxtR][nxtC] != "*":
                        if [nxtR,nxtC] not in queue:
                            queue.append([nxtR,nxtC])

tc_num = int(input())

for tc in range(tc_num):
    h, w = map(int,input().split())
    board = [list(input().rstrip()) for _ in range(h)]
    keys = list(input().rstrip())
    if keys[0] == "0":
        keys = []
    doorsAndKeys = dict()
    unlockDoors = dict()
    for row in range(h):
        for col in range(w):
            if 65 <= ord(board[row][col]) <= 90:
                if board[row][col] not in doorsAndKeys.keys():
                    doorsAndKeys[board[row][col]] = 0
                if board[row][col] not in unlockDoors.keys():
                    unlockDoors[board[row][col]] = []

    for key in keys:
        if key.upper() in doorsAndKeys.keys():
            doorsAndKeys[key.upper()] = 1


    moves = [[0,1],[0,-1],[1,0],[-1,0]]
    visited = [[0]*(w) for _ in range(h)]

    answer = 0
    startLst = []
    for row in range(h):
        for col in [0,w-1]:
            if board[row][col] != "*":
                startLst.append([row,col])
    for row in [0,h-1]:
        for col in range(w):
            if board[row][col] != "*":
                startLst.append([row,col])
    for [row, col] in startLst:
        if board[row][col] != "*" and visited[row][col] == 0:
            bfs([row,col])

    print(answer)

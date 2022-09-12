# 220908 2931 가스관
# 한칸씩 이동. 진행방향과 이동방향이 일치해야함
# 한칸이동하고 해당 칸에 파이프방향에 따라 탐색
# 탐색하다 이동할수있는데 막혀있다? -> 블록 추가.
# 가스는 모스크바에서 자레스크로 흐름

# | 상하/ -좌우/ +상하좌우/ 1하우/ 2상우/ 3상좌/ 4좌하
import sys
from collections import deque

input = sys.stdin.readline

def bfs(s):
    global r, c, board, blockMoves, moveBlocks, moves, visited,answer

    queue = deque([s])

    while queue:
        now = queue.popleft()
        visited[now[0]][now[1]] = 1
        # print(now, answer)
        nxtMoveIdxs = blockMoves[board[now[0]][now[1]]]

        for idx in nxtMoveIdxs:
            nxtR, nxtC = now[0] + moves[idx][0], now[1] + moves[idx][1]
            # print(nxtR,nxtC,idx)
            if board[nxtR][nxtC] in moveBlocks[idx]:
                if visited[nxtR][nxtC] == 0:
                    visited[nxtR][nxtC] = 1
                    queue.append([nxtR,nxtC])
            else:
                for block in moveBlocks[idx]:
                    check = True
                    # print(block)
                    for checkIdx in range(4):
                        nxtCheckR, nxtCheckC = nxtR + moves[checkIdx][0], nxtC + moves[checkIdx][1]
                        if checkIdx in blockMoves[block]:
                            if 0 <= nxtCheckR < r and 0 <= nxtCheckC < c:
                                if board[nxtCheckR][nxtCheckC] in moveBlocks[checkIdx]:
                                    continue
                                else:
                                    check = False
                            else:
                                check = False
                        else:
                            if 0 <= nxtCheckR < r and 0 <= nxtCheckC < c:
                                if board[nxtCheckR][nxtCheckC] in moveBlocks[checkIdx]:
                                    check = False
                    if check:
                        board[nxtR][nxtC] = block
                        answer = [nxtR+1,nxtC+1,block]
                        # print("!!",answer)
                        break
moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
r, c = map(int,input().split())
board = [list(input().rstrip()) for _ in range(r)]

# block에 따른 이동가능 방향
blockMoves = {"|":[0,1], "-":[2,3],"+":[0,1,2,3],"1":[1,3],"2":[0,3],"3":[0,2],"4":[1,2]}
# 이동방향에 따른 가능 block
moveBlocks =[["|","+","1","4"],["|","+","2","3"],["-","+","1","2"],["-","+","3","4"]]
visited = [[0]*(c) for _ in range(r)]

for row in range(r):
    for col in range(c):
        if board[row][col] == "M":
            visited[row][col] = 1
            M = [row,col]
        elif board[row][col] == "Z":
            visited[row][col] = 1
            Z = [row,col]
        elif board[row][col] == ".":
            visited[row][col] = 1

for moveIdx in range(4):
    nxtR, nxtC = M[0] + moves[moveIdx][0], M[1] + moves[moveIdx][1]
    if 0  <= nxtR < r and 0<= nxtC <c:
        if board[nxtR][nxtC] in moveBlocks[moveIdx]:
            start = [nxtR,nxtC]
for moveIdx in range(4):
    nxtR, nxtC = Z[0] + moves[moveIdx][0], Z[1] + moves[moveIdx][1]
    if 0  <= nxtR < r and 0<= nxtC <c:
        if board[nxtR][nxtC] in moveBlocks[moveIdx]:
            end = [nxtR,nxtC]

answer = 0 # null or [ansR,ansC,ansBlock]
bfs(start)
print(*answer)

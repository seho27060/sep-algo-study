# 구현 문제
# 가스관의 입구방향과 출구방향을 딕셔너리에 저장
# bfs로 탐색을 진행하며 만들 수 있는 가스관의 모양을 대조해보며 답을 찾기
import sys
from collections import deque
input = sys.stdin.readline

# 우, 좌, 하, 상
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
opp = {0 : 1, 1 : 0, 2 : 3, 3: 2}

def bfs():
    q = deque()
    q.append((sy, sx, -1))
    visited[sy][sx] = 1
    while q:
        y, x, dir = q.popleft()
        if arr[y][x] == 'M':
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < R and 0 <= nx < C and arr[ny][nx] != '.':
                    visited[ny][nx] = 1
                    q.append((ny, nx, d))
        elif arr[y][x] == '|':
            ny = y + dy[dir]
            nx = x + dx[dir]
            if 0 <= ny < R and 0 <= nx < C and not visited[ny][nx]:
                visited[ny][nx] = 1
                q.append((ny, nx, dir))
        elif arr[y][x] == '-':
            ny = y + dy[dir]
            nx = x + dx[dir]
            if 0 <= ny < R and 0 <= nx < C and not visited[ny][nx]:
                visited[ny][nx] = 1
                q.append((ny, nx, dir))
        elif arr[y][x] == '+':
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < R and 0 <= nx < C and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    q.append((ny, nx, d))
        elif arr[y][x] in dic.keys():
            ny = y + dy[dic[arr[y][x]][dir]]
            nx = x + dx[dic[arr[y][x]][dir]]
            if 0 <= ny < R and 0 <= nx < C and not visited[ny][nx]:
                visited[ny][nx] = 1
                q.append((ny, nx, dic[arr[y][x]][dir]))
        elif arr[y][x] == '.':
            ans = []
            for d in range(4):
                if d != opp[dir]:
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0 <= ny < R and 0 <= nx < C:
                        if arr[ny][nx] != '.':
                            if arr[ny][nx] == '|' and (d == 2 or d == 3):
                                ans.append(d)
                            elif arr[ny][nx] == '-' and (d == 0 or d == 1):
                                ans.append(d)
                            elif arr[ny][nx] == '+':
                                ans.append(d)
                            elif (arr[ny][nx] == '1' or arr[ny][nx] == '2') and d == 1:
                                ans.append(d)
                            elif (arr[ny][nx] == '1' or arr[ny][nx] == '4') and d == 3:
                                ans.append(d)
                            elif (arr[ny][nx] == '2' or arr[ny][nx] == '3') and d == 2:
                                ans.append(d)
                            elif (arr[ny][nx] == '3' or arr[ny][nx] == '4') and d == 0:
                                ans.append(d)
            if len(ans) == 3:
                ans = [y+1, x+1, "+"]
                return ans
            elif len(ans) == 1:
                if dir == ans[0]:
                    if ans[0] == 2 or ans[0] == 3:
                        ans = [y+1, x+1, "|"]
                        return ans
                    if ans[0] == 0 or ans[0] == 1:
                        ans = [y+1, x+1, "-"]
                        return ans
                else:
                    for k in dic.keys():
                        for enter, out in dic[k].items():
                            if dir == enter and ans[0] == out:
                                ans = [y+1, x+1, k]
                                return ans

R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
dic = {'1' : {1:2, 3:0}, '2':{2:0, 1:3}, '3': {0:3, 2:1}, '4':{0:2, 3:1}}
sy, sx = 0, 0
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'M':
            sy = i
            sx = j
print(*bfs())
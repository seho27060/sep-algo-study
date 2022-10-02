# bfs를 활용한 구현 문제
# 벽이 아닌곳 중 문은 따로 저장하고 나머지는 q에 저장
# bfs진행 후 door리스트에서 열쇠를 보유중인 경우 q에 추가하여 다시 bfs 진행

import sys
from collections import deque
input = sys.stdin.readline

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def check(y, x):
    global ans
    q = deque()
    if arr[y][x] == '.':
        visited[y][x] = 1
        q.append((y, x))
    elif arr[y][x] == '$':
        visited[y][x] = 1
        q.append((y, x))
        ans += 1
        q.append((y, x))
    elif arr[y][x].islower():
        visited[y][x] = 1
        key.append(arr[y][x])
        q.append((y, x))
    elif arr[y][x].isupper():
        door.append((y, x))
    if door:
        for _ in range(len(door)):
            c, r = door.popleft()
            if arr[c][r].lower() in key:
                q.append((c, r))
                visited[c][r] = 1
            else:
                door.append((c, r))
    return q
def bfs(y, x):
    global ans
    q = check(y, x)
    while  True:
        while q:
            c, r = q.popleft()
            for d in range(4):
                nc = c + dy[d]
                nr = r + dx[d]
                if 0 <= nc < h and 0 <= nr < w and arr[nc][nr] != '*' and not visited[nc][nr]:
                    if arr[nc][nr] == '.':
                        visited[nc][nr] = 1
                        q.append((nc, nr))
                    elif arr[nc][nr] == '$':
                        visited[nc][nr] = 1
                        q.append((nc, nr))
                        ans += 1
                    elif arr[nc][nr].islower():
                        visited[nc][nr] = 1
                        key.append(arr[nc][nr])
                        q.append((nc, nr))
                    elif arr[nc][nr].isupper():
                        door.append((nc, nr))
        if door:
            flag = False
            for _ in range(len(door)):
                c, r = door.popleft()
                if arr[c][r].lower() in key:
                    q.append((c, r))
                    visited[c][r] = 1
                    flag = True
                else:
                    door.append((c, r))
            if not flag:
                return
        else:
            return

T = int(input())

for tc in range(T):
    h, w = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(h)]
    key = list(input().rstrip())
    if key[0] == '0':
        key = []
    visited = [[0] * w for _ in range(h)]
    door = deque()
    ans = 0
    for i in range(w):
        if arr[0][i] != '*' and not visited[0][i]:
            bfs(0, i)
        if arr[h-1][i] != '*' and not visited[h-1][i]:
            bfs(h-1, i)
    
    for i in range(1, h-1):
        if arr[i][0] != '*' and not visited[i][0]:
            bfs(i, 0)
        if arr[i][w-1] != '*' and not visited[i][w-1]:
            bfs(i, w-1) 
    print(ans)
from collections import deque

T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    arr = []
    arr.append(['.'] * (w + 2))
    for _ in range(h):
        arr.append(['.']+list(input())+['.'])
    arr.append(['.']*(w+2))
    key = list(input())
    ans = 0
    doors = [0] * 26

    for k in key:
        if k == '0':
            break
        doors[ord(k) - 97] = True

    for i in range(1, h+1):
        for j in range(1, w+1):
            if arr[i][j].isupper() and doors[ord(arr[i][j].lower()) - 97]:
                arr[i][j] = '.'

    visited = [[0]*(w+2) for _ in range(h+2)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, 1), (0, -1):
            nx = x+dx
            ny = y+dy
            if 0<=nx<h+2 and 0<=ny<w+2 and arr[nx][ny] != '*' and visited[nx][ny] == 0:
                if arr[nx][ny] == '.':
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                else:
                    if arr[nx][ny] == '$':
                        ans += 1
                        arr[nx][ny] = '.'
                        q.append((nx, ny))
                        visited[nx][ny] = 1
                    elif arr[nx][ny].isupper():
                        if doors[ord(arr[nx][ny].lower()) - 97]:
                            arr[nx][ny] = '.'
                            q.append((nx, ny))
                            visited[nx][ny] = 1
                    elif arr[nx][ny].islower():
                        doors[ord(arr[nx][ny].lower()) - 97] = 1
                        arr[nx][ny] = '.'
                        visited = [[0] * (w+2) for _ in range(h+2)]
                        q = deque()
                        q.append((nx, ny))

    print(ans)
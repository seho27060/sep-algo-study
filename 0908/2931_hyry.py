def checkPipe(r, c):
    global resR, resC
    Q = [(r, c)]
    visited[r][c] = True

    while Q:
        curR, curC = Q.pop(0)
        pipe = MAP[curR][curC]

        for dr, dc in shape[pipe]:
            newR, newC = curR + dr, curC + dc
            if 0 <= newR < R and 0 <= newC < C and not visited[newR][newC]:
                if MAP[newR][newC] == '.':
                    resR, resC = newR, newC
                    return
                else:
                    Q.append((newR, newC))
                visited[newR][newC] = True


R, C = map(int, input().split())
MAP = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
D = ((-1, 0), (0, -1), (0, 1), (1, 0))
shape = {
    '|': ((-1, 0), (1, 0)),
    '-': ((0, -1), (0, 1)),
    '+': D,
    '1': ((0, 1), (1, 0)),
    '2': ((-1, 0), (0, 1)),
    '3': ((-1, 0), (0, -1)),
    '4': ((0, -1), (1, 0)),
    'M': (),
    'Z': (),
}
rShape = {v: k for k, v in shape.items()}
resR = resC = -1

for row in range(R):
    for col in range(C):
        if MAP[row][col] == 'M':
            visited[row][col] = True
            for dr, dc in D:
                newR, newC = row + dr, col + dc
                if 0 <= newR < R and 0 <= newC < C and \
                        not visited[newR][newC] and MAP[newR][newC] != '.':
                    checkPipe(newR, newC)
                    # 가스관 따라가며 체크하기
                    # 그러면서 visit 체크
                    # '.'인 경우는 생각 안 해도 된다
                    # if MAP[newR][newC] != '.':
                    #     pass
                    # else:
                    #     pass

# resR, resC 체크
resPos = []
flip = {
    (1, 0): (-1, 0),
    (-1, 0): (1, 0),
    (0, -1): (0, 1),
    (0, 1): (0, -1)
}

for dr, dc in D:
    newR, newC = resR + dr, resC + dc
    if 0 <= newR < R and 0 <= newC < C:
        if MAP[newR][newC] != '.':
            # 연결된 부위가 뚫려 있는 지도 확인 해야 한다.
            if flip[(dr, dc)] in shape[MAP[newR][newC]]:
                resPos.append((dr, dc))

print(resR + 1, resC + 1, rShape[tuple(sorted(resPos))])

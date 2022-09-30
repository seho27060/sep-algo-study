import sys
input = sys.stdin.readline


def doorToQueue():
    global doors
    toBeRemoved = set()
    for r, c, d in doors:
        if (d + 32) in keys:
            Q.append((r, c))
            visit[r][c] = True
            toBeRemoved.add((r, c, d))
    doors = doors - toBeRemoved


def rob():
    global papers
    while Q:
        curR, curC = Q.pop(0)
        if MAP[curR][curC] == '$':
            papers += 1

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            newR, newC = curR + dr, curC + dc
            if 0 <= newR < R and 0 <= newC < C and not visit[newR][newC] and \
                MAP[newR][newC] != '*':
                val = MAP[newR][newC]
                if val == '$':
                    visit[newR][newC] = True
                    Q.append((newR, newC))
                if val == '.':
                    visit[newR][newC] = True
                    Q.append((newR, newC))
                # 소문자
                if 97 <= ord(val) < 123:
                    keys.add(ord(val))
                    visit[newR][newC] = True
                    Q.append((newR, newC))
                # 대문자
                if 65 <= ord(val) < 91:
                    doors.add((newR, newC, ord(val)))

        doorToQueue()


T = int(input().rstrip())
for _ in range(T):
    R, C = map(int, input().rstrip().split())
    MAP = [list(input().rstrip()) for _ in range(R)]
    keys = set(map(lambda x: ord(x), input().rstrip()))

    # 전체를 한바퀴 순회하면서
    # 시작 지점이 될 수 있는 곳은 넣기
    Q = []
    doors = set()
    visit = [[False] * C for _ in range(R)]
    papers = 0
    for row in range(R):
        for col in range(C):
            if row in (0, R - 1) or col in (0, C - 1):
                val = MAP[row][col]
                if val == '*': continue
                if val == '.':
                    Q.append((row, col))
                    visit[row][col] = True
                # 소문자인 경우 - 다시 방문할 필요 X, keys에 체크
                if 97 <= ord(val) < 123:
                    Q.append((row, col))
                    keys.add(ord(val))
                    visit[row][col] = True
                # 대문자인 경우 - 열쇠가 있는 지 여부에 따라 방문 확신 가능
                if 65 <= ord(val) < 91:
                    doors.add((row, col, ord(val)))
                if val == '$':
                    Q.append((row, col))
                    visit[row][col] = True
                    # papers += 1  # 함수에서 체크할 것이기 때문

    # 무조건 Queue에 다 넣으면 문제가 된다.
    # while Q로 체크할 때 계속 남아있는 게 있을 수 있기 때문
    # 그렇기 때문에 doors는 바로 Q에 넣지 않고
    # key가 있는 경우에만 넣고
    # key가 있다면 doors에서 remove
    doorToQueue()
    rob()

    print(papers)
    # print(ord('a'))  # 97  열쇠 = 문 + 32/ 문 = 열쇠 - 32
    # print(ord('z'))  # 122
    # print(ord('A'))  # 65
    # print(ord('Z'))  # 90

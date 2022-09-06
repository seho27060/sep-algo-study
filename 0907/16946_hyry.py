
import sys
input = sys.stdin.readline

# 가다가 0인 곳을 만나면 인접한 0의 개수를 모두 세기 cnt
# 센 cnt를 4면 인접한 곳에 1인 지점에 +=

def bfs(row, col):
    Q = [(row, col)]
    visit[row][col] = True
    adj = []
    cnt = 0

    while Q:
        curR, curC = Q.pop(0)
        adj.append((curR, curC))
        cnt += 1

        for dr, dc in D:
            newR, newC = curR + dr, curC + dc
            if 0 <= newR < R and 0 <= newC < C and \
                    not visit[newR][newC] and not MAP[newR][newC]:
                Q.append((newR, newC))
                visit[newR][newC] = True

    return cnt, adj


def addCount(cnt, lst):
    _visit = set()
    for curR, curC in lst:
        for dr, dc in D:
            newR, newC = curR + dr, curC + dc
            if 0 <= newR < R and 0 <= newC < C and\
                    (newR, newC) not in _visit and MAP[newR][newC]:
                MAP[newR][newC] += cnt
                _visit.add((newR, newC))


R, C = map(int, input().rstrip().split())
MAP = [list(map(int, input().rstrip())) for _ in range(R)]
visit = [[False] * C for _ in range(R)]
D = ((1, 0), (-1, 0), (0, 1), (0, -1))

for row in range(R):
    for col in range(C):
        # 방문하지 않은 0인 지점인 경우
        if not visit[row][col] and not MAP[row][col]:
            cnt, adj = bfs(row, col)
            addCount(cnt, adj)

nameoji = lambda x: str(x % 10)
for subMap in MAP:
    print(''.join(map(nameoji, subMap)))

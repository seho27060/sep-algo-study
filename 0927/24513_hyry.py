import sys
input = sys.stdin.readline


R, C = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
infected = set()  # 완전히 감염 완료된 곳이나 치료제가 있는 곳만

one = set()
two = set()
for row in range(R):
    for col in range(C):
        if MAP[row][col] != 0:
            infected.add((row, col))
        if MAP[row][col] == 1:
            one.add((row, col))
        if MAP[row][col] == 2:
            two.add((row, col))

D = ((1, 0), (0, 1), (-1, 0), (0, -1))
while one or two:
    # 1. 1번과 2번이 새로 감염할 장소
    tmpOne = set()
    tmpTwo = set()
    for oneR, oneC in one:
        for dr, dc in D:
            newOneR, newOneC = oneR + dr, oneC + dc
            if 0 <= newOneR < R and 0 <= newOneC < C and \
                (newOneR, newOneC) not in infected and not MAP[newOneR][newOneC]:
                tmpOne.add((newOneR, newOneC))

    for twoR, twoC in two:
        for dr, dc in D:
            newTwoR, newTwoC = twoR + dr, twoC + dc
            if 0 <= newTwoR < R and 0 <= newTwoC < C and \
                (newTwoR, newTwoC) not in infected and not MAP[newTwoR][newTwoC]:
                tmpTwo.add((newTwoR, newTwoC))

    for oneR, oneC in tmpOne:
        MAP[oneR][oneC] += 1
        infected.add((oneR, oneC))

    toRemove = []
    for twoR, twoC in tmpTwo:
        MAP[twoR][twoC] += 2
        if MAP[twoR][twoC] == 3:
            toRemove.append((twoR, twoC))
        infected.add((twoR, twoC))

    for r, c in toRemove:
        tmpOne.remove((r, c))
        tmpTwo.remove((r, c))

    one = tmpOne
    two = tmpTwo

cnt1 = cnt2 = cnt3 = 0
for row in range(R):
    for col in range(C):
        if MAP[row][col] == 1:
            cnt1 += 1
        if MAP[row][col] == 2:
            cnt2 += 1
        if MAP[row][col] == 3:
            cnt3 += 1

print(cnt1, cnt2, cnt3)

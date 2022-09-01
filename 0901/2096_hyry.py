import sys
input = sys.stdin.readline

N = int(input())
ANS = [(1e10, 0) for _ in range(3)]

for r in range(N):
    arr = list(map(int, input().split()))

    if r == 0:
        for col in range(3):
            ANS[col] = (arr[col], arr[col])
    else:
        tmp = [(1e10, 0) for _ in range(3)]
        tmp[0] = (
            min(ANS[0][0], ANS[1][0]) + arr[0],
            max(ANS[0][1], ANS[1][1]) + arr[0]
        )
        tmp[2] = (
            min(ANS[2][0], ANS[1][0]) + arr[2],
            max(ANS[2][1], ANS[1][1]) + arr[2]
        )
        tmp[1] = (
            min(ANS[1][0], ANS[2][0], ANS[0][0]) + arr[1],
            max(ANS[1][1], ANS[2][1], ANS[0][1]) + arr[1]
        )
        ANS = tmp

minV, maxV = 1e10, 0
for col in range(3):
    minV = min(minV, ANS[col][0])
    maxV = max(maxV, ANS[col][1])

print(maxV, minV)
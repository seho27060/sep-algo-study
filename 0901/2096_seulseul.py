import sys
input = sys.stdin.readline

N = int(input())
minA = [[0]*3 for _ in range(2)]
maxA = [[0]*3 for _ in range(2)]

for i in range(N):
    x = list(map(int, input().split()))
    
    minA[1][0] = min(minA[0][0], minA[0][1]) + x[0]
    maxA[1][0] = max(maxA[0][0], maxA[0][1]) + x[0]

    minA[1][1] = min(minA[0][0], minA[0][1], minA[0][2]) + x[1]
    maxA[1][1] = max(maxA[0][0], maxA[0][1], maxA[0][2]) + x[1]

    minA[1][2] = min(minA[0][2], minA[0][1]) + x[2]
    maxA[1][2] = max(maxA[0][2], maxA[0][1]) + x[2]
    
    for j in range(3):
        minA[0][j] = minA[1][j]
        maxA[0][j] = maxA[1][j]

print(max(maxA[0]), min(minA[0]))
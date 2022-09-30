import sys
input = sys.stdin.readline

N = int(input())

S = set()
for i in range(N):
    S.add(int(input()))

sumValues = set()
for i in S:
    for j in S:
        sumValues.add(i+j)

maxV = 0
for i in S:
    for j in S:
        if (i-j) in sumValues:
            maxV = max(maxV, i)

print(maxV)
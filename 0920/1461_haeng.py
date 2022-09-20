N,M = map(int,input().split())
BOOK = list(map(int,input().split()))

L = []
R = []
H = 0
for i in BOOK:
    if i < 0:
        L.append(-i)
    else:
        R.append(i)
    H = max(abs(i),H)

result = 0
result += H
if L:
    L.sort()
    L.reverse()
    for i in range(0, len(L), M):
        if L[i] != H:
            result += L[i]*2


if R:
    R.sort()
    R.reverse()
    for i in range(0, len(R), M):
        if R[i] != H:
            result += R[i]*2

print(result)
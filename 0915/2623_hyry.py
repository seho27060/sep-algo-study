import sys
input = sys.stdin.readline


N, M = map(int, input().rstrip().split())

preCnt = [0] * (N + 1)
adjL = [[] for _ in range(N + 1)]
for _ in range(M):
    num, *arr = map(int, input().rstrip().split())

    adjL[arr[0]].append(arr[1])
    preCnt[arr[1]] += 1
    for idx in range(1, num - 1):
        adjL[arr[idx]].append(arr[idx + 1])
        preCnt[arr[idx + 1]] += 1

Q = []
for idx in range(1, N + 1):
    if not preCnt[idx]:
        Q.append(idx)

ans = []
while Q:
    curV = Q.pop(0)
    ans.append(str(curV))

    for neiV in adjL[curV]:
        preCnt[neiV] -= 1
        if not preCnt[neiV]:
            Q.append(neiV)

if len(ans) != N: print(0)
else: print('\n'.join(ans).rstrip())

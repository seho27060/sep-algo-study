import sys
from collections import deque

input = sys.stdin.readline

fillZero = lambda x: x[:2] + '0' * (5 - len(x)) + x[2:]

def entrance():
    sortedIdx = 0
    ST = deque()
    total = 5 * N

    while tickets and sortedIdx < total:
        curT = tickets[0]
        minT = sortedTickets[sortedIdx]

        if minT == curT:
            sortedIdx += 1
            tickets.popleft()
        elif ST and ST[0] == minT:
            ST.popleft()
            sortedIdx += 1
        else:
            ST.appendleft(curT)
            tickets.popleft()

    # ST에 남은 수 처리
    lenST = len(ST)
    if lenST <= 1: return True

    for idx in range(lenST - 1):
        if ST[idx] > ST[idx + 1]:
            return False

    return True


N = int(input().rstrip())
tickets = deque()
for _ in range(N):
    tickets.extend(map(fillZero, input().rstrip().split()))

sortedTickets = sorted(tickets)

if entrance(): print('GOOD')
else: print('BAD')

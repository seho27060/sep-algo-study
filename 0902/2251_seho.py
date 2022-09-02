# 220902 2251 물통
#
import sys
from collections import deque

input = sys.stdin.readline

a, b, c = map(int,input().split())
waterA, waterB, waterC = 0,0, c
answer = set()
lst = []
limit = [a,b,c]

queue = deque([[0,0,c]])

while queue:
    now = queue.popleft()
    lst.append(now)
    if now[0] == 0:
        answer.add(now[2])
        # print("!!!",now)
    for start in range(3):
        for end in range(3):
            if start != end:
                nxtEnd = now[end] + now[start]
                nxtStart = 0
                if nxtEnd > limit[end]:
                    nxtStart = nxtEnd - limit[end]
                    nxtEnd = limit[end]
                nxtWaters = now.copy()
                nxtWaters[start] = nxtStart
                nxtWaters[end] = nxtEnd
                if nxtWaters not in lst:
                    lst.append(nxtWaters)
                    queue.append(nxtWaters)

print(*sorted(answer))
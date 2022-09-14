# 220914 17178 줄서기
# 대기공간 후입선출
# 번호표 순서대로만 통과할수있음

import sys
from collections import deque

n = int(input())
wait = deque([])

for _ in range(n):
    getLst = list(input().split(" "))

    for idx in range(5):
        text, num = getLst[idx].split("-")
        wait.append([text,int(num)])

concert = []
waitSpace = []
orderWait = deque(sorted(wait))

while wait or waitSpace:
    # print(wait)
    # print(waitSpace)
    # print(orderWait)
    # print(concert)
    #
    # print()
    if wait:
        check = 0
        if wait[0][0] == orderWait[0][0]:
            if wait[0][1] == orderWait[0][1]:
                check = 1
        if waitSpace:
            if waitSpace[-1][0] == orderWait[0][0]:
                if waitSpace[-1][1] == orderWait[0][1]:
                    check = 2
    else:
        check = 0
        if waitSpace[-1][0] == orderWait[0][0]:
            if waitSpace[-1][1] == orderWait[0][1]:
                check = 2
        else:
            break

    if check == 0:
        waitSpace.append(wait.popleft())
    elif check == 1:
        concert.append(wait.popleft())
        orderWait.popleft()
    elif check == 2:
        concert.append(waitSpace.pop())
        orderWait.popleft()

# print(wait)
# print(waitSpace)
# print(orderWait)
# print()
# print(concert)
if len(concert) == n*5:
    print("GOOD")
else:
    print("BAD")
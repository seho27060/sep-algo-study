# q는 정렬이 필요하며 좌측부터 빼오기 위해 heapq
# lst는 기존 배열을 나열하고 좌측부터 빼오기 위해 deque
# wait은 대기열이며 마지막부터 빼오기 때문에 그냥 리스트
# 꼼꼼하지 못해서 시간을 너무 버렸다....

import sys
import heapq
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [input().split() for _ in range(n)]
lst = deque()
q = []
wait = []
for i in arr:
    for j in i:
        a, b = j.split("-")
        heapq.heappush(q, [a, int(b)])
        lst.append([a, int(b)])
while q:
    qVal = heapq.heappop(q)
    while lst:
        lstVal = lst.popleft()
        if lstVal != qVal:
            if wait:
                waitVal = wait.pop()
                if waitVal != qVal:
                    wait.append(waitVal)
                    wait.append(lstVal)
                else:
                    if q:
                        qVal = heapq.heappop(q)
                        lst.appendleft(lstVal)
            else:
                wait.append(lstVal)
        else:
            if q:
                qVal = heapq.heappop(q)
        
    while wait:
        lstVal = wait.pop()
        if lstVal == qVal:
            if q:
                qVal = heapq.heappop(q)
            else:
                print("GOOD")
                exit()
        else:
            print("BAD")
            exit()
print("GOOD")
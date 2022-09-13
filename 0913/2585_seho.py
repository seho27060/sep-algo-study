# 220913 2585 경비행기
# k번 이하로 이동할때 최소의 연료통구하기.. 이진탐색을 활용?
# n < 1000
# 0,0 -> 10000,10000 으로 이동

import sys
from collections import deque

def dstCal(s,e):
    return (((s[0]-e[0])**2+(s[1]-e[1])**2)**0.5)//10+1

def bfs(dst):
    global n, k, stops, end
    visited = [0 for _ in range(n+1)]
    cnt = 0
    queue = deque([0])

    while queue:
        if cnt > k:
            return False

        for idx in range(len(queue)):
            now = queue.popleft()
            if visited[now] == False:
                visited[now] = True

                for nxt in range(1,n+1):
                    nxtDst = dstCal(stops[now],stops[nxt])
                    if nxtDst <= dst:
                        endDst = dstCal([10000,10000],stops[nxt])
                        if endDst <= dst:
                            return True
                        queue.append(nxt)
        cnt += 1
    return False

n, k = map(int,input().split())

start = [0,0]
end = [10000,10000]
stops = [start]
for _ in range(n):
    stops.append(list(map(int,input().split())))
stops.sort()
# print(stops)

answer = 0
# print(visited)
minDst = 0
maxDst = 10000

while minDst <= maxDst:
    midDst = (minDst+maxDst)//2
    # print(midDst)
    result = bfs(midDst)
    if result:
        answer = midDst
        maxDst = midDst-1
    else:
        minDst = midDst+1

print(answer)
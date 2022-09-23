# 220923 1800 인터넷 설치
# 1 ~ n의 노드/ p개 쌍만 연결가능/ 1번은 연결, 모두 연결안됐을때 n번컴퓨터를 연결해야함
# 근데, p개 연결선중 k개의 연결선을 제외하고 가장 비싼 하나만 가격을 받겠다. 이때 최소비용

import sys
from heapq import *

input = sys.stdin.readline

def djk(start, limit):
    global graphs,k

    queue = []
    distance = [float('inf')]*(n+1)
    heappush(queue,(0,start))
    distance[start] = 0

    while queue:
        cost, now = heappop(queue)

        if distance[now] < cost:
            continue
        for nxt in graphs[now]:
            if nxt[1] > limit:
                if cost + 1 < distance[nxt[0]]:
                    distance[nxt[0]] = cost + 1
                    heappush(queue,(cost+1,nxt[0]))
            else:
                if cost < distance[nxt[0]]:
                    distance[nxt[0]] = cost
                    heappush(queue,(cost, nxt[0]))
    if distance[n] > k:
        return False
    else:
        return True
n, p, k = map(int,input().split())
connects = [-1]*(n+1)
connects[1] = 0
graphs = [[] for _ in range(n+1)]

for _ in range(p):
    start, end, cost = map(int,input().split())
    graphs[start].append((end,cost))
    graphs[end].append((start,cost))

answer = float("inf")
left = 0
right = 10000000

while left <= right:
    mid = (left+right)//2
    result = djk(1, mid)
    if result:
        right = mid -  1
        answer = mid
    else:
        left = mid + 1
if answer >= float('inf'):
    print(-1)
else:
    print(answer)
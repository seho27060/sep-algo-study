import heapq

def djk(cost):
    ST = []
    heapq.heappush(ST,(0,1))
    visit = [1000001]*(N+1)
    visit[1] = 0

    while ST:
        cnt,now = heapq.heappop(ST)
        if visit[now] < cnt:
            continue
        for c,next in road[now]:
            if c > cost:
                if visit[next] > cnt + 1:
                    visit[next] = cnt +1
                    heapq.heappush(ST,(cnt+1,next))
            else:
                if visit[next] > cnt:
                    visit[next] = cnt
                    heapq.heappush(ST, (cnt,next))

    if visit[N] > K:
        return 0
    else:
        return 1

N, P, K = map(int,input().split())
road = {i:[] for i in range(1,N+1)}
for i in range(P):
    a,b,c = map(int,input().split())
    road[a].append((c,b))
    road[b].append((c,a))

L = 0
R = 1000001
result = 1000001
while L <= R:
    mid = (L+R) //2
    if djk(mid):
        R = mid-1
        result = mid
    else:
        L = mid+1

if result == 1000001:
    print(-1)
else:
    print(result)


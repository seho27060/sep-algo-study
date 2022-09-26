N = int(input())
M = int(input())
road = [0]
for i in range(N):
    road.append([0]+list(map(int,input().split())))

route = list(map(int,input().split()))

visit = [1] + [0]*(N)

ST = [route[0]]
visit[route[0]] = 1

while ST:
    now = ST.pop(0)

    for i,j in enumerate(road[now]):
        if i == 0: continue
        if j and visit[i] == 0:
            ST.append(i)
            visit[i] = 1

result = 'YES'
for i in route:
    if visit[i] == 0:
        result = 'NO'
print(result)
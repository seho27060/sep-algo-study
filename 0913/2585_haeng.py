def gogo(X):
    ST = [(0,0,0)]
    visit = [0]*(N)
    while ST:
        x,y,c = ST.pop(0)
        goal = math.ceil((((x-10000) ** 2 + (y-10000) ** 2) ** 0.5) / 10)
        if goal <= X and c<=K:
            return 1

        for i in range(N):
            goal = math.ceil((((x-OIL[i][0])**2+(y-OIL[i][1])**2)**0.5)/10)
            if goal <= X and visit[i] == 0:
                ST.append((OIL[i][0],OIL[i][1],c+1))
                visit[i] = 1
    return 0


import math
N,K = map(int,input().split())

OIL = []
for _ in range(N):
    A,B = list(map(int,input().split()))
    OIL.append((A,B))

D = math.ceil((((10000)**2+(10000)**2)**0.5)/10)
result = D
l = 0
r = D
while l <= r:
    mid = (l+r)//2
    if gogo(mid):
        result = mid
        r=mid-1
    else:
        l=mid+1

print(result)
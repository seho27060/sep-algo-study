def gogo(x,y):
    ST = [(x,0)]
    visit = [0]*(N+1)
    visit[x] = 1
    while ST:
        now,cnt = ST.pop(0)

        if now == y:
            return cnt

        for next,c in TREE[now]:
            if visit[next] == 0:
                ST.append((next,cnt+c))
                visit[next] = 1


N,M = map(int,input().split())
TREE = { i:[] for i in range(1,N+1)}
for i in range(N-1):
    a,b,c = map(int,input().split())
    TREE[a].append((b,c))
    TREE[b].append((a,c))


for i in range(M):
    s,e = map(int,input().split())
    print(gogo(s,e))




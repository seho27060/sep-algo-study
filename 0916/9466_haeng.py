import sys
input = sys.stdin.readline

def circle(x):
    global cnt

    ST=[x]
    while ST:
        now = ST[-1]
        next = want[now]
        if visit[next]:
            if next in ST:
                cnt += len(ST[ST.index(next)::])
            return
        else:
            ST.append(next)
            visit[next] =1


T = int(input())
for t in range(T):
    N = int(input())
    want = [0] + list(map(int,input().split()))
    visit = [0] * (N+1)

    cnt = 0
    for i in range(1,N+1):
        if visit[i]==0:
            visit[i]=1
            circle(i)

    print(N-cnt)
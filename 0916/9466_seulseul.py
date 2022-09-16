import sys
input = sys.stdin.readline

def dfs(now):
    global ans
    visited[now] = True
    # 순환 확인용 배열에 추가
    arr.append(now)
    next = lst[now]

    if visited[next]:
        if next in arr:
            ans+=arr[arr.index(next):]
        return
    else:
        dfs(next)


T = int(input())
for TC in range(T):
    ans = []
    n = int(input())
    visited = [False] * (n+1)
    lst = [0] + list(map(int, input().split()))
    
    for i in range(1, n+1):
        if not visited[i]:
            # 순환 확인용 배열
            arr = []
            dfs(i)
    print(n-len(ans))
# 이분탐색과 bfs를 활용한 문제
# 이분 탐색을 활용해 최소 연료통 용량을 구하면서 BFS할 때마다 이동할 수 있는 거리에 제한을 두는 방식으로 푼다고 합니다 ^^...
# 3번 틀리고 답 참조했음....

from collections import deque
import sys
input = sys.stdin.readline

def distance(y, x):
    dis = ((arr[y][0] - arr[x][0]) ** 2 + (arr[y][1] - arr[x][1]) ** 2) **(1/2)
    return int((dis//10) + 1 if dis % 10 else (dis // 10))

def bfs(val):
    visited = set([0])
    q = deque()
    q.append([0, 0])

    while q:
        s, cnt = q.popleft()
        if cal[s][n+1] <= val:
            return True
        if cnt >= k:
            continue
        for i in range(n+2):
            if i not in visited and cal[s][i] <= val:
                visited.add(i)
                q.append((i, cnt+1))
    return False



n, k = map(int, input().split())
arr = [[0,0]]+[list(map(int, input().split())) for _ in range(n)] + [[10000, 10000]]
cal = [[0] * (n+2) for _ in range(n+2)]
for i in range(n+2):
    for j in range(n+2):
        cal[i][j] = distance(i, j)

l = 0
r = distance(0, n+1)
ans = 0

while l <= r:
    mid = (l+r)//2
    if bfs(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1
print(ans)
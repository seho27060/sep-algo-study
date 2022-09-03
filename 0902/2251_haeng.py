import sys
from collections import deque
input = sys.stdin.readline


A,B,C = map(int,input().split())
ST = deque()
ST.append((0,0,C))

result = []
visit = [[0]*(B+1) for _ in range(A+1)]
while ST:
    a,b,c = ST.popleft()
    if visit[a][b]: continue
    else: visit[a][b] = 1

    if a == 0 and c not in result:
        result.append(c)


    if c+b <= B:
        ST.append((a,c+b,0))
    if c+a <= A:
        ST.append((a+c,b,0))
    if a+b <= A:
        ST.append((a+b,0,c))
    if a+b <= B:
        ST.append((0,a+b,c))
    if c+b <= C:
        ST.append((a,0,c+b))
    if c+a <= C:
        ST.append((0,b,c+a))

    if c + b > B:
        ST.append((a,B,c+b-B))
    if c + a > A:
        ST.append((A,b,c+a-A))
    if a + b > A:
        ST.append((A,a+b-A, c))
    if a + b > B:
        ST.append((a+b-B,B,c))
    if c + b > C:
        ST.append((a,c+b-C,C))
    if c + a > C:
        ST.append((c+a-C,b,C))

result.sort()

print(*result)
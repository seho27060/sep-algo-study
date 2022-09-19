import sys
from itertools import combinations
from collections import deque

n = int(input())
arr = [[0]*(n+1) for _ in range(n+1)]
pop = [int(i) for i in sys.stdin.readline().split()]

def bfs(v, team):
    global arr, n, pop
    q = deque()
    q.append(team[0])
    v[team[0]] = 1
    sum = 0
    while q:
        c = q.popleft()
        sum += pop[c-1]
        for i in range(1, n+1):
            if v[i] == 0 and arr[c][i] == 1 and i in team:
                q.append(i)
                v[i] = 1
    return sum

for j in range(1, n+1):
    input = [int(x) for x in sys.stdin.readline().split()]
    for i in range(1, len(input)):
        arr[j][input[i]] = 1

com = [i for i in range(1, n+1)]
res = 1e9
for i in range(1, n//2+1):
    for comb in combinations(com, i):
        v = [0]*(n+1)
        team1 = list(comb)
        team2 = list(set(com) - set(comb))
        sum1 = bfs(v, team1)
        sum2 = bfs(v, team2)
        check = True
        for i in range(1, n+1):
            if v[i] == 0:
                check = False
                break
        if check == False:
            continue
        res = min(res, abs(sum1-sum2))
if res == 1e9:
    print(-1)
else:
    print(res)
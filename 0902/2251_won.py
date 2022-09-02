import sys
# sys.stdin = open("sample_input.txt", "r")
input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations

def f(aaa, bbb):
    if visited[aaa][bbb] == 0:
        visited[aaa][bbb] = 1
        qu.append([aaa, bbb])

a, b, c = map(int, input().split())
visited = [[0] * (b + 1) for _ in range(a + 1)]
ans = set()
qu = deque()
visited[0][0] = 1
qu.append([0, 0])
while qu:
    aa, bb = qu.popleft()
    cc = c - aa - bb
    if aa == 0:
        ans.add(cc)
    tmp = min(aa, b - bb)
    f(aa - tmp, bb + tmp)

    tmp = min(aa, c - cc)
    f(aa - tmp, bb)

    tmp = min(bb, a - aa)
    f(aa + tmp, bb - tmp)

    tmp = min(bb, c - cc)
    f(aa, bb - tmp)

    tmp = min(cc, a - aa)
    f(aa + tmp, bb)

    tmp = min(cc, b - bb)
    f(aa, bb + tmp)

ans = list(ans)
ans.sort()
print(*ans)

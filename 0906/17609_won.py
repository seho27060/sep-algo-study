import sys
# sys.stdin = open("sample_input.txt", "r")
input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations


def isPal(strV, l, r):
    while l < r:
        if strV[l] == strV[r]:
            l += 1
            r -= 1
        else:
            return False
    return True

def pal(strV):
    l = 0
    r = len(strV) - 1
    while l < r:
        if strV[l] == strV[r]:
            l += 1
            r -= 1
        else:
            res1 = isPal(strV, l + 1, r)
            res2 = isPal(strV, l, r - 1)
            if res1 or res2:
                return 1
            else:
                return 2
    return 0


N = int(input())
for _ in range(N):
    word = input().rstrip()
    ans = pal(word)
    print(ans)
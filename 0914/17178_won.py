import sys
# sys.stdin = open("sample_input.txt", "r")
# input = sys.stdin.readline
# from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations

N = int(input())
waiting = []
people = []

for _ in range(N):
    arr = list(input().split())

    for i in range(5):
        alpa, num = arr[i].split('-')
        people.append((alpa, int(num)))
        arr[i] = (alpa, int(num))
    waiting.append(arr)


people.sort()
tmp = []
while waiting:
    cur = waiting.pop(0)

    while cur:
        if cur[0] == people[0]:
            people.pop(0)
            cur.pop(0)
        elif tmp and tmp[-1] == people[0]:
            people.pop(0)
            tmp.pop()
        else:
            if tmp and tmp[-1] < cur[0]:
                print('BAD')
                exit()
            tmp.append(cur.pop(0))
print('GOOD')
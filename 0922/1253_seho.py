# 220922 1253 좋다!~
# 2000개짜리 리스트
# 처음부터 순회하면서 i 번째 수와 i+1번째 수부터 싹더해서.. 2000**2

import sys

input =sys.stdin.readline

n = int(input())
lst = sorted(map(int,input().split()))

answer = 0

for idx in range(n):
    start = 0
    end = n-2
    getLst = lst[:idx] + lst[idx+1:]

    while start < end:
        result = getLst[start]+getLst[end]

        if result == lst[idx]:
            answer += 1
            break
        if result < lst[idx]:
            start += 1
        if result > lst[idx]:
            end -= 1
print(answer)

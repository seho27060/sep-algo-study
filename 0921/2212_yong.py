# 그리드문제
# k가 n보다 크거나 같으면 결국 0
# 아니면 센서 사이 거리를 구한 후 정렬하여 큰 원소부터 제거

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

arr = list(map(int, input().split()))
arr.sort()

if k >= n:
    print(0)
    exit()

dis = []
for i in range(1, n):
    dis.append(arr[i] - arr[i-1])

dis.sort(reverse=True)
for i in range(k-1):
    dis.pop(0)

print(sum(dis))
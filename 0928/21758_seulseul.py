import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
# 누적합용
arr = lst[:]
maxV = 0

for i in range(1, N):
    arr[i] += arr[i-1]

# 왼쪽
for i in range(1, N-1):
    maxV = max(maxV, arr[N-2]+arr[i-1]-lst[i])

# 오른쪽
for i in range(1, N-1):
    maxV = max(maxV, (2*arr[N-1])-lst[0]-lst[i]-arr[i])

# 가운데
for i in range(1, N-1):
    maxV = max(maxV, arr[N-2]-lst[0]+lst[i])

print(maxV)
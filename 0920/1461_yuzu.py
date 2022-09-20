N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = []
arr.sort()
max_res = 0
if abs(arr[0]) > arr[-1]:
    max_res = arr[0]
else:
    max_res = arr[-1]

k = N
for i in range(N):
    if arr[i] > 0:
        arr2 += arr[i:]
        arr = arr[:i]
        k = i
        break

arr2.sort(reverse=True)
res = 0

if arr2:
    for x in range(0, N-k, M):
        if arr2[x] != max_res:
            res += arr2[x]

if arr:
    for y in range(0, k, M):
        if arr[y] != max_res:
            res += abs(arr[y])

res *= 2
res += abs(max_res)

print(res)
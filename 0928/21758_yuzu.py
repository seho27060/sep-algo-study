N = int(input())
arr = list(map(int, input().split()))
arrsum = [arr[0]]

for i in range(1, N):
    arrsum.append(arrsum[i-1]+arr[i])

ans = 0
for i in range(1, N-1):
    ans = max(ans, arrsum[-2] + arrsum[i-1] - arr[i])

for i in range(1, N-1):
    ans = max(ans, arrsum[-1]*2 - arrsum[i] - arr[i] - arr[0])

for i in range(1, N-1):
    ans = max(ans, arrsum[-2] + arr[i] - arr[0])

print(ans)
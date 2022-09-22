N = int(input())
A = list(map(int, input().split()))
A.sort()

ans = 0
for i in range(N):
    arr = A[:i] + A[i+1:]
    l, r = 0, N-2
    while l < r:
        if arr[l] + arr[r] == A[i]:
            ans += 1
            break
        elif arr[l] + arr[r] < A[i]:
            l += 1
        else:
            r -= 1

print(ans)

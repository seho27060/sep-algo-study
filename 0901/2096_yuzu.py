N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def solve(N):
    dp1 = [[0]*3 for _ in range(2)]
    dp2 = [[0]*3 for _ in range(2)]

    dp1[0][0] = arr[0][0]
    dp2[0][0] = arr[0][0]
    dp1[0][1] = arr[0][1]
    dp2[0][1] = arr[0][1]
    dp1[0][2] = arr[0][2]
    dp2[0][2] = arr[0][2]

    if N == 1:
        return max(dp1[0]), min(dp2[0])

    else:
        for i in range(1, N):
            dp1[1][0] = arr[i][0] + max(dp1[0][0], dp1[0][1])
            dp2[1][0] = arr[i][0] + min(dp2[0][0], dp2[0][1])
            dp1[1][1] = arr[i][1] + max(dp1[0][0], dp1[0][1], dp1[0][2])
            dp2[1][1] = arr[i][1] + min(dp2[0][0], dp2[0][1], dp2[0][2])
            dp1[1][2] = arr[i][2] + max(dp1[0][1], dp1[0][2])
            dp2[1][2] = arr[i][2] + min(dp2[0][1], dp2[0][2])

            dp1[0][0] = dp1[1][0]
            dp2[0][0] = dp2[1][0]
            dp1[0][1] = dp1[1][1]
            dp2[0][1] = dp2[1][1]
            dp1[0][2] = dp1[1][2]
            dp2[0][2] = dp2[1][2]

        return max(dp1[1]), min(dp2[1])

a, b = solve(N)
print(a, b)
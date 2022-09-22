N = int(input())
ARR = list(map(int,input().split()))

ARR.sort()
maxN = ARR[-1]

result = 0
for i in range(N):
    L = 0
    R = N-1
    I = ARR[i]
    while L<R:
        if L == i:
            L += 1
            continue
        if R == i:
            R -= 1
            continue

        A = ARR[L] + ARR[R]

        if A == I:
            result += 1
            break
        else:
            if A < I:
                L += 1

            elif A > I:
                R -= 1


print(result)
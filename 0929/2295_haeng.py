N = int(input())
ARR = []
for _ in range(N):
    ARR.append(int(input()))
ARR.sort()


A = []
for i in ARR:
    for j in ARR:
        if i+j < ARR[-1]:
            A.append(i+j)

result = 0
for i in reversed(range(N)):
    B = ARR[i]
    for j in ARR:
        for k in A:
            if ARR[i] == j+k:
                print(ARR[i])
                exit()
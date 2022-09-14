# 백준 17178 줄서기

from collections import deque

N = int(input())
arr = [deque(input().split()) for _ in range(N)]

print(arr)
tickett = []
for i in range(len(arr)):
    for x in arr[i]:
        tickett.append(x)

ticket = sorted(tickett, key=lambda x: (x[0], int(x[2:])))  # 모든 사람 오름차순 정렬
print(ticket)
stack = []

i = 0
for _ in range(N * 5):  # 모든 티켓 조사
    while True:
        check = True
        for j in range(N):
            if arr[j] and ticket[i] == arr[j][0]:
                arr[j].popleft()
                i += 1
                check = False
                break

        if stack and ticket[i] == stack[-1]:
            stack.pop()
            i += 1
            check = False
        if check:
            break

    max_v = ''
    idx = 0
    for k in range(N):
        if arr[k] and max_v < arr[k][0]:
            idx = k
            max_v = arr[k][0]

    if max_v:
        arr[idx].popleft()
        stack.append(max_v)
    print(stack)
#
# print(arr)
# print(stack)
if stack:
    print('BAD')
else:
    print('GOOD')
# 안풀리는데여;; 스택에 쌓고 티켓 비교까지는 이해 ok 왜 안되지??

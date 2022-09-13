from collections import deque
import sys, math

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]


def bfs(s, f):
    v = [0] * (n + 1)
    cnt = 0
    q = deque()
    q.append(s)

    while q:
        if cnt > k:
            return False

        for _ in range(len(q)):
            c = q.popleft()

            if not v[c]:
                v[c] = 1

                for i in range(1, n + 1):
                    distance = math.sqrt(
                        pow(arr[c][0] - arr[i][0], 2) + pow(arr[c][1] - arr[i][1], 2))

                    if distance <= f:
                        ddist = math.sqrt(
                            pow(10000 - arr[i][0], 2) + pow(10000 - arr[i][1], 2))

                        if ddist <= f:
                            return True

                        q.append(i)

        cnt += 1

    return False


left = 0
right = 10000
result = 0

while left <= right:
    mid = (left + right) // 2

    if bfs(0, mid * 10):
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)

N = int(input())
places = list(map(int, input().split()))

leftToRight = [0] * N
rightToLeft = [0] * N
leftToRight[0] = places[0]
rightToLeft[N - 1] = places[N - 1]

for i in range(1, N):
    leftToRight[i] = leftToRight[i - 1] + places[i]
    rightToLeft[N - 1 - i] = rightToLeft[N - i] + places[N - 1 - i]

maxHoney = 0

for hive in range(1, N - 1):
    tmpHoney = (leftToRight[hive] + rightToLeft[hive] - places[0] - places[N - 1])
    maxHoney = max(maxHoney, tmpHoney)

for bee in range(1, N - 1):
    tmpHoney = leftToRight[N - 2] - places[bee] + leftToRight[bee - 1]
    maxHoney = max(maxHoney, tmpHoney)

for bee in range(1, N - 1):
    tmpHoney = leftToRight[N - 1] - places[0] - places[bee] + rightToLeft[bee + 1]
    maxHoney = max(maxHoney, tmpHoney)

print(maxHoney)

# for hive in range(1, N - 1):
#     tmpHoney = 0
#     # left
#     for left in range(1, hive + 1):
#         tmpHoney += places[left]
#     # right
#     for right in range(hive, N - 1):
#         tmpHoney += places[right]
#
#     maxHoney = max(maxHoney, tmpHoney)

# _tmpHoney = 0
# for honey in range(N - 1):
#     _tmpHoney += places[honey]
#
# for bee in range(1, N - 1):
#     tmpHoney = _tmpHoney - places[bee]
#     for left in range(bee):
#         tmpHoney += places[left]
#     maxHoney = max(maxHoney, tmpHoney)

# _tmpHoney2 = 0
# for honey in range(1, N):
#     _tmpHoney2 += places[honey]
#
# for bee in range(1, N - 1):
#     tmpHoney = _tmpHoney2 - places[bee]
#     for right in range(bee + 1, N):
#         tmpHoney += places[right]
#     maxHoney = max(maxHoney, tmpHoney)
#
# print(maxHoney)

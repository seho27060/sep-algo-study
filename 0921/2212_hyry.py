def setTower():
    if N <= K:
        return 0

    pos = [1e10] * (N - 1)
    total = 0
    for i in range(N - 1):
        pos[i] = sensors[i + 1] - sensors[i]
        total += pos[i]

    pos.sort(reverse=True)

    emptyArea = sum(pos[:K - 1])
    return total - emptyArea


_ = input()
K = int(input())
sensors = list(set(map(int, input().split())))
sensors.sort()
N = len(sensors)
print(setTower())

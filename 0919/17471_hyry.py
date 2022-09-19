'''
N [2, 10]
'''

# from itertools import combinations as comb

def isConnected(area):
    _area = list(area)
    ST = [_area[0]]
    visit = set()
    visit.add(_area[0])

    while ST:
        curV = ST.pop()
        for neiV in adj[curV]:
            if neiV not in visit and neiV in area:
                ST.append(neiV)
                visit.add(neiV)

    return area == visit


def combi(num, k):
    arr = [-1] * k
    ans = []

    def makeCombi(depth, minV, ans):
        if depth == k:
            first = set(arr)
            second = set(range(1, N + 1)) - first

            if isConnected(first) and isConnected(second):
                firstSum = secondSum = 0
                for f in first:
                    firstSum += population[f]
                for s in second:
                    secondSum += population[s]
                ans.append(abs(firstSum - secondSum))
            return

        for i in range(minV, num + 1):
            arr[depth] = i
            makeCombi(depth + 1, i + 1, ans)

    makeCombi(0, 1, ans)

    return ans


N = int(input())
population = [0] + list(map(int, input().split()))

adj = [set() for _ in range(N + 1)]
for idx in range(N):
    cnt, *nums = list(map(int, input().split()))
    for num in nums:
        adj[idx + 1].add(num)
        adj[num].add(idx + 1)

res = 1e10
for i in range(1, N // 2 + 1):
    tmp = combi(N, i)
    if tmp:
        res = min(res, min(tmp))

print(res if res != 1e10 else -1)

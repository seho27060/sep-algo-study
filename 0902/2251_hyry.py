
def bfs():
    Q = [(0, 0, C)]
    visit = {(0, 0, C)}

    while Q:
        curA, curB, curC = Q.pop(0)

        # 2 -> 0
        if curA < A and curC:
            if curC >= A - curA:
                tmp = (A, curB, curC - (A - curA))
            else:
                tmp = (curA + curC, curB, 0)

            if tmp not in visit:
                Q.append(tmp)
                visit.add(tmp)
        # 2 -> 1
        if curB < B and curC:
            if curC >= B - curB:
                tmp = (curA, B, curC - (B - curB))
            else:
                tmp = (curA, curB + curC, 0)

            if tmp not in visit:
                Q.append(tmp)
                visit.add(tmp)
        # 0 -> 1
        if curB < B and curA:
            if curA >= B - curB:
                tmp = (curA - (B - curB), B, curC)
            else:
                tmp = (0, curA + curB, curC)
            if tmp not in visit:
                Q.append(tmp)
                visit.add(tmp)
        # 1 -> 2
        if curC < C and curB:
            if curB >= C - curC:
                tmp = (curA, curB - (C - curC), C)
            else:
                tmp = (curA, 0, curB + curC)
            if tmp not in visit:
                Q.append(tmp)
                visit.add(tmp)
        # 0 -> 2
        if curC < C and curA:
            if curA >= C - curC:
                tmp = (curA - (C - curC), curB, C)
            else:
                tmp = (0, curB, curA + curC)
            if tmp not in visit:
                Q.append(tmp)
                visit.add(tmp)
        # 1 -> 0
        if curA < A and curB:
            if curB >= A - curA:
                tmp = (A, curB - (A - curA), curC)
            else:
                tmp = (curA + curB, 0, curC)
            if tmp not in visit:
                Q.append(tmp)
                visit.add(tmp)

    return visit


A, B, C = map(int, input().split())
cases = bfs()

ans = set()
for a, _, c in cases:
    if a == 0:
        ans.add(c)

print(*sorted(ans))
n = int(input())
lst = list(map(int, input().split()))

lst.sort()
cnt = 0
for i in range(n-1, -1, -1):
    s = 0
    e = n-1
    goal = lst[i]
    while s < e:
        if s == i:
            s += 1
            if s == e:
                break
        elif e == i:
            e -= 1
            if s == e:
                break
        if lst[s] + lst[e] > goal:
            e-=1
        elif lst[s] + lst[e] < goal:
            s += 1
        else:

            cnt += 1
            break
print(cnt)
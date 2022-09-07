import copy

T = int(input())
for _ in range(T):
    s = list(input())
    l = 0
    r = len(s)-1
    ans = 0
    idx = [-1, -1]
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            ans = -1
            idx = [l, r]
            break

    if ans == -1:
        s1 = copy.deepcopy(s)
        del s1[idx[0]]
        l = 0
        r = len(s)-2
        while l < r:
            if s1[l] == s1[r]:
                l += 1
                r -= 1
            else:
                ans = -2
                break
        if ans != -2:
            ans = 1
        if ans == -2:
            s2 = copy.deepcopy(s)
            del s2[idx[1]]
            l = 0
            r = len(s)-2
            while l < r:
                if s2[l] == s2[r]:
                    l += 1
                    r -= 1
                else:
                    ans = -3
                    break
            if ans == -3:
                ans = 2
            else:
                ans = 1
    print(ans)
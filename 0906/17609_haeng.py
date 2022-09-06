def check(r,l):
    while r > l:
        if word[l] == word[r]:
            l += 1
            r -= 1
        else:
            return 0
    return 1


T = int(input())
for t in range(T):
    word = list(input())
    delete = 0

    R=len(word)-1
    L=0
    while R > L:
        if word[L] == word[R]:
            R -= 1
            L += 1
        else:
            if word[L] == word[R-1]:
                if check(R-1,L):
                    delete = 1
                    break
            if word[L+1] == word[R]:
                if check(R,L+1):
                    delete = 1
                    break
            delete = 2
            break

    print(delete)
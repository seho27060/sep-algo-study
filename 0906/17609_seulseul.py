import sys
input = sys.stdin.readline

def func(S, E, depth):
    while S < E:
        if word[S]!=word[E]:
            if depth==1:
                return 2
            else:
                left_delete = func(S+1, E, depth+1)
                right_delete = func(S, E-1, depth+1)
            if left_delete != 2 or right_delete != 2:
                return 1
            else:
                return 2
        else:
            S += 1
            E -= 1
    return 1

T = int(input().rstrip())

for _ in range(T):
    ans = 0
    word = input().rstrip()
    if word == word[::-1]:
        print(ans)
        continue
    start, end = 0, len(word)-1
    ans = func(start, end, 0)
    print(ans)
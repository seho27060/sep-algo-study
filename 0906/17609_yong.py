# 포인터를 활용한 문제
# 단어가 회문인 경우와 아닌경우를 먼저 구분
# 회문이 아니라면 포인터를 활용해 단어가 다를 때 유사회문인지를 판단

import sys
input = sys.stdin.readline

def nextCheck(word, l, r):
    while l < r:
        if word[l] == word[r]:
            l += 1
            r -= 1
        else:
            return False
    return True

def check(word, l, r):
    if word == word[::-1]:
        return 0
    while l < r:
        if word[l] != word[r]:
            leftCheck = nextCheck(word, l+1, r)
            rightCheck = nextCheck(word, l, r-1)

            if leftCheck or rightCheck:
                return 1
            else:
                return 2
        else:
            l += 1
            r -= 1

T = int(input())

for _ in range(T):
    word = input().rstrip()
    l, r = 0, len(word)-1
    ans = check(word, l, r)
    print(ans)
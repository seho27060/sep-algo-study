import sys
input = sys.stdin.readline


def iterateWord(w, l, r):
    while l < r:
        if w[l] != w[r]: return (l, r)
        l += 1
        r -= 1
    return (1e10, 1e10)  # 맞는 경우


def isPseudoPalindrome(word, left, right):
    left1, right1 = left + 1, right
    left2, right2 = left, right - 1

    leftCase = iterateWord(word, left1, right1)
    rightCase = iterateWord(word, left2, right2)

    if leftCase == (1e10, 1e10) or rightCase == (1e10, 1e10): return 1

    return 2


def isPalindrome(word):
    N = len(word)
    left, right = 0, N - 1

    resLeft, resRight = iterateWord(word, left, right)
    if (resLeft, resRight) != (1e10, 1e10):
        return isPseudoPalindrome(word, resLeft, resRight)

    return 0


T = int(input())

for _ in range(T):
    word = input().strip()
    print(isPalindrome(word))

# import sys
# input = sys.stdin.readline
#
#
# def isPseudoPalindrome(left, right, word):
#     # 왼쪽이 다른 경우
#     leftCase = rightCase = True
#     left1, right1 = left + 1, right
#     while left1 < right1:
#         if word[left1] == word[right1]:
#             left1 += 1
#             right1 -= 1
#             break
#         leftCase = False
#         break
#
#     # 오른쪽이 다른 경우
#     left2, right2 = left, right - 1
#     while left2 < right2:
#         if word[left2] == word[right2]:
#             left2 += 1
#             right2 -= 1
#             continue
#         rightCase = False
#         break
#
#         # if word[left2] != word[right2]:
#         #     rightCase = False
#         #     break
#         # left2 += 1
#         # right2 -= 1
#
#     if leftCase or rightCase: return 1
#
#     return 2
#
#
# def isPalindrome(word):
#     N = len(word)
#     left, right = 0, N - 1
#
#     while left < right:
#         if word[left] == word[right]:
#             left += 1
#             right -= 1
#             continue
#         return isPseudoPalindrome(left, right, word)
#     else:
#         return 0
#
#
# T = int(input())
#
# for _ in range(T):
#     word = input().strip()
#     print(isPalindrome(word))
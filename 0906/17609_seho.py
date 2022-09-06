# 220906 17609 회문

import sys

input = sys.stdin.readline

def isPseudo(a,b):
    result = True
    for idx in range(len(a)//2):
        if a[idx] != a[-idx-1]:
            result = False
    if result:
        # print(a)
        return 1

    result = True
    # print(b)
    for idx in range(len(a)//2):
        if b[idx] != b[-idx-1]:
            return 2
    if result:
        return 1

def isPalindrome(inStr):
    for findIdx in range(len(inStr) // 2):
        # print(inStr[findIdx],inStr[-findIdx-1],findIdx)
        if inStr[findIdx] != inStr[-findIdx-1]:
            if findIdx == 0:
                aStr, bStr = inStr[1:], inStr[:-1]
            else:
                aStr, bStr = inStr[:findIdx]+inStr[findIdx+1:], inStr[:-findIdx-1]+inStr[-findIdx:]
            return isPseudo(aStr,bStr)
    # print(inStr)
    return 0

n = int(input())

for _ in range(n):
    getStr = input().rstrip()
    # print(getStr, len(getStr))
    answer = isPalindrome(getStr)
    print(answer)

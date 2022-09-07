def check(word,left,right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def back(word,left,right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            left_check = check(word,left+1,right)
            right_check = check(word,left,right-1)
            if left_check or right_check:
                return 1
            else:
                return 2
    return 0

n = int(input())
for _ in range(n):
    word = list(input())
    left=0
    right=len(word)-1
    ans = back(word,left,right)
    print(ans)